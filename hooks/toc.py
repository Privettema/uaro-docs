"""Hide the table of contents on pages that have only one heading (or none): a TOC with a single entry is noise."""


def _count(items):
    return sum(1 + _count(item.children) for item in items)


def on_page_content(html, page, config, files):
    if _count(page.toc.items) <= 1:
        hide = list(page.meta.get("hide") or [])
        if "toc" not in hide:
            page.meta["hide"] = hide + ["toc"]
    return html
