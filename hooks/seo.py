"""Give every page its own meta description and lazy-load content images.

The description is the first sentence of the first plain paragraph under the page's H1, so search results and
link previews differ per page. A `description:` in a page's front matter wins; pages with no usable intro
(patch notes, tables-first pages) keep the site-wide description.

Images inside the article get `loading="lazy"`, so sprite-heavy pages don't fetch every image up front. The home
page hero is exempt, since it is above the fold.
"""
import re

MIN_LENGTH = 30
MAX_LENGTH = 160
SKIP_PREFIXES = ("patch-notes/",)

_img_tag = re.compile(r"<img\b(?![^>]*\b(?:loading=|class=\"[^\"]*wiki-hero))", re.IGNORECASE)
_article = re.compile(r"(<article\b.*?</article>)", re.DOTALL | re.IGNORECASE)


def _plain(text):
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\{[^}]*\}", "", text)
    text = re.sub(r"[*_`]+", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _intro(markdown):
    """First prose paragraph after the H1, or None if the page opens with something else."""
    lines = markdown.split("\n")
    start = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if start is None:
        return None
    paragraph = []
    for line in lines[start + 1:]:
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            if paragraph:
                break
            continue
        if stripped[0] in "#!<|>-*`{:" or line[0] in " \t" or stripped[:2].isdigit() or stripped[:3] == "---":
            break
        paragraph.append(stripped)
    return _plain(" ".join(paragraph)) if paragraph else None


def _sentence(text):
    first = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    if len(first) > MAX_LENGTH:
        first = first[:MAX_LENGTH].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return first


def on_page_markdown(markdown, page, config, files):
    if page.meta.get("description") or page.file.src_uri.startswith(SKIP_PREFIXES):
        return markdown
    intro = _intro(markdown)
    if intro:
        description = _sentence(intro)
        if len(description) >= MIN_LENGTH:
            page.meta["description"] = description
    return markdown


def on_post_page(output, page, config):
    return _article.sub(lambda m: _img_tag.sub('<img loading="lazy"', m.group(1)), output)
