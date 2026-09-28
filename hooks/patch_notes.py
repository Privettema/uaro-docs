"""Generate the patch note listings from the patch files themselves.

Each patch file lives in docs/patch-notes/YYYY/ and starts with front matter:

    ---
    date: 2026-09-22      # required
    hotfix: true          # optional, marks a hotfix
    summary: One line.    # optional, shown under the latest patch on the Patch Notes page
    highlights:           # optional, 3 to 6 player-facing bullets shown in the home page preview
      - "Scaraba Hole is now a Cat Hand destination for 19,000 zeny."
      - "The 10 item cap on monster kill drops is lifted."
    ---

If `highlights` is missing, the preview is generated from the patch's own sections instead (less polished).

Placeholders replaced at build time:
    <!-- PATCH_LATEST -->     latest patch card + the most recent patches (All_Patch_Notes.md)
    <!-- PATCH_HOME -->       the latest patch on one line, for the home page (index.md)
    <!-- PATCH_YEAR -->       every patch of the year, newest first (docs/patch-notes/YYYY/index.md)

Every patch page also gets Previous / All / Next links appended. Adding a patch is just adding one dated file.
Adding a new year means a new docs/patch-notes/YYYY/index.md (copy the previous one) plus one nav entry.
"""
import datetime
import logging
import os
import re

log = logging.getLogger("mkdocs.hooks.patch_notes")

RECENT = 8
SKIP_TAGS = ("we need your support", "important")
TAGS_SHOWN = 4
MAX_TAG = 28  # longer headings are descriptive sentences, not topics
SEASONS = {12: "❄️", 1: "❄️", 2: "❄️", 3: "🌸", 4: "🌸", 5: "🌸", 6: "☀️", 7: "☀️", 8: "☀️", 9: "🍂", 10: "🍂", 11: "🍂"}

_patches = []  # newest first, filled by _scan() when the config loads


def _unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1].replace('\\"', '"')
    return value


def _front_matter(text):
    """Read the simple front matter we use: `key: value` lines and `key:` followed by `- item` lines."""
    match = re.match(r"---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    data = {}
    key = None
    if match:
        for line in match.group(1).splitlines():
            item = re.match(r"^\s+-\s+(.*)$", line)
            if item and key and isinstance(data.get(key), list):
                data[key].append(_unquote(item.group(1)))
                continue
            name, _, value = line.partition(":")
            if not name.strip() or name.startswith((" ", "#")):
                continue
            key = name.strip()
            data[key] = _unquote(value) if value.strip() else []
    return data


def _tags(text):
    tags = []
    for heading in re.findall(r"^## (.+)$", text, re.MULTILINE):
        name = re.sub(r"^[^A-Za-z0-9]+", "", heading.replace("*", "")).strip()
        name = re.sub(r"[^A-Za-z0-9)]+$", "", name)
        if name and len(name) <= MAX_TAG and not name.lower().startswith(SKIP_TAGS) and name not in tags:
            tags.append(name)
    return tags[:TAGS_SHOWN]


PRIORITY = ("gameplay", "items", "skills", "npc", "instances", "monsters", "commands", "wo", "battlegrounds", "pvp")


def _clean(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # links
    return re.sub(r"[`*]", "", text).strip()


def _sentence(text, limit=110):
    text = _clean(text)
    first = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0].rstrip(".")
    return first if len(first) <= limit else first[:limit].rsplit(" ", 1)[0] + "..."


def _auto_highlights(text, per_section=2, total=5):
    """Fallback preview when a patch has no `highlights`: one short line per item from the most player-facing sections."""
    body = re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", "", text, flags=re.DOTALL)
    sections = []
    for order, section in enumerate(re.split(r"^## ", body, flags=re.MULTILINE)[1:]):
        heading, _, rest = section.partition("\n")
        name = re.sub(r"^[^A-Za-z0-9]+", "", heading.replace("*", "")).strip()
        name = re.sub(r"^\d+\.\s*", "", name)
        if not name or name.lower().startswith(SKIP_TAGS + ("fixes", "technical")):
            continue
        items = []
        for line in rest.split("\n"):
            row = re.match(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|?\s*$", line)
            bullet = re.match(r"^\s*[-*]\s+\*\*(.+?)\*\*:?\s*(.*)$", line)
            match = row or bullet
            if match:
                title, detail = _clean(match.group(1)).rstrip(":"), match.group(2)
                items.append(f"{title}: {_sentence(detail)}" if detail.strip() else title)
            if len(items) >= per_section:
                break
        rank = next((i for i, key in enumerate(PRIORITY) if name.lower().startswith(key)), len(PRIORITY))
        if items:
            sections.append((rank, order, items))
    lines = []
    for _, _, items in sorted(sections):
        lines += items
    return lines[:total]


def _scan(docs_dir):
    _patches.clear()
    root = os.path.join(docs_dir, "patch-notes")
    for year in sorted(os.listdir(root)) if os.path.isdir(root) else []:
        folder = os.path.join(root, year)
        if not (year.isdigit() and os.path.isdir(folder)):
            continue
        for name in os.listdir(folder):
            if not (name.startswith("patches") and name.endswith(".md")):
                continue
            with open(os.path.join(folder, name), encoding="utf-8") as handle:
                text = handle.read()
            meta = _front_matter(text)
            if "date" not in meta:
                continue
            _patches.append({
                "uri": f"patch-notes/{year}/{name}",
                "date": datetime.date.fromisoformat(meta["date"]),
                "hotfix": meta.get("hotfix", "").lower() == "true",
                "summary": meta.get("summary", ""),
                "tags": _tags(text),
                "highlights": meta.get("highlights") or _auto_highlights(text),
                "curated": bool(meta.get("highlights")),
            })
    _patches.sort(key=lambda p: (p["date"], p["uri"]), reverse=True)
    for patch in _patches[:HOME_PREVIEW]:
        if not patch["curated"]:
            log.info("%s has no `highlights:` front matter; the home preview is auto-generated. "
                     "See scripts/patch_highlights_prompt.md.", patch["uri"])


def _nav_label(patch):
    date = patch["date"]
    emoji = "🔧" if patch["hotfix"] else SEASONS[date.month]
    return f"{emoji} {date.strftime('%b')} {date.day}" + (" (Hotfix)" if patch["hotfix"] else "")


def on_config(config):
    """Build the sidebar for the Patch Notes tab from the files: Latest Patches, then an Archive of years.

    The year holding the page you are reading is expanded; the other years stay collapsed but clickable.
    """
    _scan(config["docs_dir"])
    for item in config["nav"]:
        if isinstance(item, dict) and "Patch Notes" in item:
            years = []
            for year in sorted({p["date"].year for p in _patches}, reverse=True):
                pages = [f"patch-notes/{year}/index.md"]
                pages += [{_nav_label(p): p["uri"]} for p in _patches if p["date"].year == year]
                years.append({str(year): pages})
            item["Patch Notes"] = [{"Latest Patches": "All_Patch_Notes.md"}, {"Archive": years}]
    return config


def _label(patch):
    date = patch["date"]
    emoji = "🔧" if patch["hotfix"] else SEASONS[date.month]
    text = f"{date.strftime('%B')} {date.day}, {date.year}"
    return f"{emoji} {text}" + (" (Hotfix)" if patch["hotfix"] else "")


def _link(patch, from_uri):
    rel = os.path.relpath(patch["uri"], os.path.dirname(from_uri) or ".")
    return rel.replace(os.sep, "/")


def _item(patch, from_uri):
    tags = f" · {' · '.join(patch['tags'])}" if patch["tags"] else ""
    return f"- [{_label(patch)}]({_link(patch, from_uri)}){tags}"


def _latest(from_uri):
    if not _patches:
        return ""
    latest = _patches[0]
    lines = [
        '<div class="grid cards" markdown>\n',
        f"- **[⭐ Latest patch: {_label(latest)[2:]}]({_link(latest, from_uri)})**\n",
        f"    {latest['summary'] or ' · '.join(latest['tags'])}\n",
        "</div>\n",
        "## Recent patches\n",
    ]
    lines += [_item(p, from_uri) for p in _patches[1:RECENT + 1]]
    lines += ["", "Older patches are grouped by year in the menu."]
    return "\n".join(lines)


HOME_PREVIEW = 5


def _home(from_uri):
    """The home page preview: tabs for the latest patches, each with a few highlights and buttons to the notes."""
    all_notes = os.path.relpath("All_Patch_Notes.md", os.path.dirname(from_uri) or ".")
    lines = []
    for patch in _patches[:HOME_PREVIEW]:
        date = patch["date"]
        lines.append(f'=== "{date.strftime("%B")} {date.day}"\n')
        lines.append(f"    **{_label(patch)}**\n")
        for highlight in patch["highlights"]:
            lines.append(f"    - {highlight}")
        lines.append("")
        lines.append(f"    [Read full patch notes]({_link(patch, from_uri)}){{ .md-button .md-button--primary }}")
        lines.append(f"    [View all patch notes]({all_notes}){{ .md-button }}\n")
    return "\n".join(lines)


def _year(year, from_uri):
    items = [_item(p, from_uri) for p in _patches if p["date"].year == year]
    return "\n".join(items)


def on_page_markdown(markdown, page, config, files):
    uri = page.file.src_uri
    if "<!-- PATCH_LATEST -->" in markdown:
        markdown = markdown.replace("<!-- PATCH_LATEST -->", _latest(uri))
    if "<!-- PATCH_HOME -->" in markdown:
        markdown = markdown.replace("<!-- PATCH_HOME -->", _home(uri))
    if "<!-- PATCH_YEAR -->" in markdown:
        year = int(re.search(r"patch-notes/(\d{4})/", uri).group(1))
        markdown = markdown.replace("<!-- PATCH_YEAR -->", _year(year, uri))

    for i, patch in enumerate(_patches):
        if patch["uri"] == uri:
            newer = _patches[i - 1] if i > 0 else None
            older = _patches[i + 1] if i + 1 < len(_patches) else None
            # The nav label is a short "Sep 22"; keep the full date as the browser/page title.
            long_date = _label(patch)[2:].replace(" (Hotfix)", "")
            page.meta["title"] = f"{'Hotfix' if patch['hotfix'] else 'Patch Notes'} - {long_date}"
            parts = []
            if older:
                parts.append(f"[← {_label(older)[2:]}]({_link(older, uri)})")
            parts.append(f"[All patch notes]({os.path.relpath('All_Patch_Notes.md', os.path.dirname(uri))})")
            if newer:
                parts.append(f"[{_label(newer)[2:]} →]({_link(newer, uri)})")
            markdown = markdown.rstrip() + "\n\n---\n\n" + " · ".join(parts) + "\n"
            break
    return markdown
