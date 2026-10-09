"""Add "Last updated" under a page's title and a "Spotted a mistake?" note at the end of its content.

"Last updated" comes from an `updated:` date in the page's front matter:

    ---
    updated: 2026-10-08
    ---

Editors set it when a page's content changes (`scripts/stamp_updated.py` does it for the pages in your branch), so
it means "the information changed", not "someone touched the file". Patch notes have no `updated:` and get only the
note at the end. The note links to the Wiki Errors channel on Discord.

The home page, the section hubs (every `index.md`) and the generated listings get neither.
"""
import datetime
import logging

log = logging.getLogger("mkdocs.hooks.page_meta")

NO_META = ("all-pages.md", "all-patch-notes.md")  # generated listings
REPORT_URL = "https://discord.com/channels/702960460168953946/1456450631584846011"


def on_page_content(html, page, config, files):
    if page.file.src_uri.endswith(("index.md", *NO_META)):
        return html
    value = page.meta.get("updated")
    if isinstance(value, str):
        try:
            value = datetime.date.fromisoformat(value)
        except ValueError:
            value = None
    if isinstance(value, datetime.date):
        label = f"{value:%B} {value.day}, {value.year}"
        updated = f'<p class="uaro-updated">Last updated: <time datetime="{value.isoformat()}">{label}</time></p>'
        html = html.replace("</h1>", f"</h1>\n{updated}", 1) if "</h1>" in html else updated + html
    elif page.meta.get("updated") is not None:
        log.warning("%s: `updated` must be a date like 2026-10-08", page.file.src_uri)
    report = (f'<p class="uaro-report">Spotted a mistake? Tell us in '
              f'<a href="{REPORT_URL}" target="_blank" rel="noopener">#wiki-errors on Discord</a>.</p>')
    return f"{html}\n{report}"
