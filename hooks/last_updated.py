"""Show "Last updated" under the title of a page that has an `updated:` date in its front matter.

    ---
    updated: 2026-10-08
    ---

Editors set the date when a page's content changes (`scripts/stamp_updated.py` does it for the pages in your branch),
so it means "the information changed", not "someone touched the file". The hook turns the ISO date into the wiki's
date style and inserts it right after the page's H1. Pages without `updated:` show nothing.
"""
import datetime
import logging

log = logging.getLogger("mkdocs.hooks.last_updated")


def on_page_content(html, page, config, files):
    value = page.meta.get("updated")
    if value is None:
        return html
    if isinstance(value, str):
        try:
            value = datetime.date.fromisoformat(value)
        except ValueError:
            value = None
    if not isinstance(value, datetime.date):
        log.warning("%s: `updated` must be a date like 2026-10-08", page.file.src_uri)
        return html
    label = f"{value:%B} {value.day}, {value.year}"
    tag = f'<p class="uaro-updated">Last updated: <time datetime="{value.isoformat()}">{label}</time></p>'
    if "</h1>" in html:
        return html.replace("</h1>", f"</h1>\n{tag}", 1)
    return tag + html
