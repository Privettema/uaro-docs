"""Generate the A-Z page list (docs/all-pages.md) from the nav, so it never goes stale.

Pages in the nav are listed with the section they live in. Pages that exist but are not in the nav
(for example sub-pages linked from other pages) are listed too, so removing something from the sidebar
never makes it unfindable. Individual patch notes and Dev pages are skipped.

Also writes page-index.json to the built site, a small {title, url} list of the same pages, so the
404 page (overrides/404.html) can suggest nearby pages for a mistyped or moved URL without shipping
the full search index.
"""
import json
import os
import re
from collections import defaultdict

PLACEHOLDER = "<!-- ALL_PAGES -->"
SKIP_PREFIXES = ("dev/",)
SKIP_FILES = {"all-pages.md"}

_nav_titles = {}
_page_index = []


def _is_patch(file):
    """The individual patch notes have their own listing under Patch Notes."""
    return re.match(r"patch-notes/\d{4}/(patches|index)", file.src_uri) is not None


def _is_hub(file):
    """Section landing pages (folder/index.md) only repeat what the sidebar shows."""
    return file.src_uri.endswith("/index.md")


def on_nav(nav, config, files):
    _nav_titles.clear()
    for page in nav.pages:
        section = page.ancestors[-1].title if page.ancestors else ""
        title = page.title or _h1(page.file)
        if title:
            _nav_titles[page.file.src_uri] = (title, section)
    return nav


def _sort_key(title):
    """Sort and group by the first letter or digit, ignoring any leading emoji or symbols."""
    return re.sub(r"^[^A-Za-z0-9]+", "", title).lower()


def _h1(file):
    match = re.search(r"^# (.+)$", file.content_string, re.MULTILINE)
    return match.group(1).strip() if match else None


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "all-pages.md":
        return markdown

    entries = []
    _page_index.clear()
    for file in files.documentation_pages():
        uri = file.src_uri
        if uri in SKIP_FILES or uri.startswith(SKIP_PREFIXES) or _is_hub(file) or _is_patch(file):
            continue
        if uri in _nav_titles:
            title, section = _nav_titles[uri]
        else:
            title, section = _h1(file), ""
            if not title:
                continue
        entries.append((title, section, uri))
        _page_index.append({"title": title, "url": file.url})

    groups = defaultdict(list)
    for title, section, uri in sorted(entries, key=lambda e: _sort_key(e[0])):
        key = _sort_key(title)
        letter = key[:1].upper() if key[:1].isalpha() else "#"
        groups[letter].append((title, section, uri))

    lines = []
    for letter in sorted(groups):
        lines.append(f"## {letter}\n")
        for title, section, uri in groups[letter]:
            suffix = f" *({section})*" if section else ""
            lines.append(f"- [{title}]({uri}){suffix}")
        lines.append("")
    return markdown.replace(PLACEHOLDER, "\n".join(lines))


def on_post_build(config):
    out = os.path.join(config["site_dir"], "page-index.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(_page_index, f, ensure_ascii=False)
