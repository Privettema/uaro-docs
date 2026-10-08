"""Show "Last updated" at the bottom of a page that has an `updated:` date in its front matter.

    ---
    updated: 2026-10-08
    ---

Editors set the date when a page's content changes (`scripts/stamp_updated.py` does it for the pages in your branch),
so it means "the information changed", not "someone touched the file". Material renders `page.meta.revision_date`
on its own; this hook only turns the ISO date into the wiki's date style. Pages without `updated:` show nothing.
"""
import datetime
import logging

log = logging.getLogger("mkdocs.hooks.last_updated")


def on_page_markdown(markdown, page, config, files):
    value = page.meta.get("updated")
    if value is None:
        return markdown
    if isinstance(value, str):
        try:
            value = datetime.date.fromisoformat(value)
        except ValueError:
            value = None
    if not isinstance(value, datetime.date):
        log.warning("%s: `updated` must be a date like 2026-10-08", page.file.src_uri)
        return markdown
    page.meta["revision_date"] = f"{value:%B} {value.day}, {value.year}"
    return markdown
