"""Add a small bar at the top right of a page's content: "Last updated" and "Report a problem".

The home page and the section hubs (every `index.md`) don't get one.

"Last updated" comes from an `updated:` date in the page's front matter:

    ---
    updated: 2026-10-08
    ---

Editors set it when a page's content changes (`scripts/stamp_updated.py` does it for the pages in your branch), so
it means "the information changed", not "someone touched the file". Patch notes and the generated listings have no
`updated:` and show only the report link. "Report a problem" opens the Wiki Errors channel on Discord.
"""
import datetime
import logging

log = logging.getLogger("mkdocs.hooks.page_meta")

REPORT_URL = "https://discord.com/channels/702960460168953946/1456450631584846011"


def on_page_content(html, page, config, files):
    if page.file.src_uri.endswith("index.md"):
        return html
    parts = []
    value = page.meta.get("updated")
    if isinstance(value, str):
        try:
            value = datetime.date.fromisoformat(value)
        except ValueError:
            value = None
    if isinstance(value, datetime.date):
        label = f"{value:%B} {value.day}, {value.year}"
        parts.append(f'<span>Last updated: <time datetime="{value.isoformat()}">{label}</time></span>')
    elif page.meta.get("updated") is not None:
        log.warning("%s: `updated` must be a date like 2026-10-08", page.file.src_uri)
    parts.append(f'<a href="{REPORT_URL}" target="_blank" rel="noopener">Report a problem</a>')
    return f'<p class="uaro-page-meta">{"".join(parts)}</p>\n{html}'
