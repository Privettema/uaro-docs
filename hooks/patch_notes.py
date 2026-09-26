"""Generate the patch note listings from the patch files themselves.

Each patch file lives in docs/patch-notes/YYYY/ and starts with front matter:

    ---
    date: 2026-09-22      # required
    hotfix: true          # optional, marks a hotfix
    summary: One line.    # optional, shown under the latest patch
    ---

Placeholders replaced at build time:
    <!-- PATCH_LATEST -->     latest patch card + the most recent patches (All_Patch_Notes.md)
    <!-- PATCH_YEAR -->       every patch of the year, newest first (docs/patch-notes/YYYY/index.md)

Every patch page also gets Previous / All / Next links appended. Adding a patch is just adding one dated file.
Adding a new year means a new docs/patch-notes/YYYY/index.md (copy the previous one) plus one nav entry.
"""
import datetime
import os
import re

RECENT = 8
SKIP_TAGS = ("we need your support", "important")
TAGS_SHOWN = 4
MAX_TAG = 28  # longer headings are descriptive sentences, not topics
SEASONS = {12: "❄️", 1: "❄️", 2: "❄️", 3: "🌸", 4: "🌸", 5: "🌸", 6: "☀️", 7: "☀️", 8: "☀️", 9: "🍂", 10: "🍂", 11: "🍂"}

_patches = []  # newest first


def _front_matter(text):
    match = re.match(r"---\r?\n(.*?)\r?\n---", text, re.DOTALL)
    data = {}
    if match:
        for line in match.group(1).splitlines():
            key, _, value = line.partition(":")
            if value:
                data[key.strip()] = value.strip().strip("\"'")
    return data


def _tags(text):
    tags = []
    for heading in re.findall(r"^## (.+)$", text, re.MULTILINE):
        name = re.sub(r"^[^A-Za-z0-9]+", "", heading.replace("*", "")).strip()
        name = re.sub(r"[^A-Za-z0-9)]+$", "", name)
        if name and len(name) <= MAX_TAG and not name.lower().startswith(SKIP_TAGS) and name not in tags:
            tags.append(name)
    return tags[:TAGS_SHOWN]


def on_files(files, config):
    _patches.clear()
    for file in files.documentation_pages():
        if not re.match(r"patch-notes/\d{4}/patches[^/]*\.md$", file.src_uri):
            continue
        text = file.content_string
        meta = _front_matter(text)
        if "date" not in meta:
            continue
        date = datetime.date.fromisoformat(meta["date"])
        _patches.append({
            "uri": file.src_uri,
            "date": date,
            "hotfix": meta.get("hotfix", "").lower() == "true",
            "summary": meta.get("summary", ""),
            "tags": _tags(text),
        })
    _patches.sort(key=lambda p: (p["date"], p["uri"]), reverse=True)
    return files


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


def _year(year, from_uri):
    items = [_item(p, from_uri) for p in _patches if p["date"].year == year]
    return "\n".join(items)


def on_page_markdown(markdown, page, config, files):
    uri = page.file.src_uri
    if "<!-- PATCH_LATEST -->" in markdown:
        markdown = markdown.replace("<!-- PATCH_LATEST -->", _latest(uri))
    if "<!-- PATCH_YEAR -->" in markdown:
        year = int(re.search(r"patch-notes/(\d{4})/", uri).group(1))
        markdown = markdown.replace("<!-- PATCH_YEAR -->", _year(year, uri))

    for i, patch in enumerate(_patches):
        if patch["uri"] == uri:
            newer = _patches[i - 1] if i > 0 else None
            older = _patches[i + 1] if i + 1 < len(_patches) else None
            parts = []
            if older:
                parts.append(f"[← {_label(older)[2:]}]({_link(older, uri)})")
            parts.append(f"[All patch notes]({os.path.relpath('All_Patch_Notes.md', os.path.dirname(uri))})")
            if newer:
                parts.append(f"[{_label(newer)[2:]} →]({_link(newer, uri)})")
            markdown = markdown.rstrip() + "\n\n---\n\n" + " · ".join(parts) + "\n"
            break
    return markdown
