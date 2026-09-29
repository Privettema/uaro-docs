# Style Guide

How to write and format a wiki page, so pages feel consistent no matter who wrote them. This page is
not in the nav — it's for editors, not players.

## Page structure

```markdown
# Page Title

One or two sentences that say what this page is and who needs it.

!!! info "Quick Facts"
    - **Location:** ...
    - **Level Required:** ...
    - **Cost:** ...

## First Section

Content.

## Second Section

Content.
```

- **Title (`#`)**: exactly one H1, matching the page's nav label with the emoji removed. It's the
  first line of the file, no blank line above it.
- **Intro**: one or two sentences right after the title, separated from it by a single blank line.
  Say what the page covers before diving into detail — don't repeat the title as a sentence
  ("This page is about X").
- **Quick Facts** *(optional)*: for a system, event or NPC with a handful of at-a-glance stats
  (location, level requirement, cost, duration), use an `info` admonition right after the intro
  instead of burying those facts in prose. Skip it for pages that don't have that kind of data
  (guides, FAQs, command references).
- **Sections use `##`, not `###`**: don't start a page's first section at `###` — it has no `##`
  parent and breaks the page outline. Use `###` only to subdivide an existing `##` section.

## Admonitions

Use the lowercase type with a quoted title, content indented 4 spaces, one blank line before and
after:

```markdown
!!! note "Optional Title"
    Content here.

!!! warning "Optional Title"
    Content here.

!!! important "Optional Title"
    Content here.

!!! tip "Optional Title"
    Content here.
```

Use `??? note "Title"` (collapsible) for a block that's long and mostly reference material a player
skips past — a full town-coordinate table, for example — not for anything a first-time reader needs.

## Images

- Page-specific images go in a subfolder: `docs/img/<Page_Name>/`. Shared item/monster/skill sprites
  stay directly in `docs/img/`.
- A standalone image (screenshot, NPC portrait) gets its own line: `![Alt text](img/filename.webp)`.
  Write a real alt text, not `""` or the filename.
- An inline icon (an item or skill next to its name in a sentence or table cell) stays inline:
  `![Item Name](img/1234.gif) Item Name`.
- For a layout markdown can't do alone (floating an image beside text), use
  `<img src="img/filename.webp" alt="Alt text" align="left" />` — this is the one place raw HTML is
  expected on a content page.

## Tables

- Standard Markdown pipe tables. Keep every row's cell content on one line — don't rely on trailing
  double-spaces for a line break; if a cell genuinely needs a forced break, use `<br>` inside it.
- An item/monster column shows the icon and name together: `![Name](img/1234.gif) Name`.
- No trailing whitespace on any line, in or out of a table.

## Links

<!--
  DISABLED (temporarily): a repo-wide page-filename rename (lowercase-hyphenated, no underscores or
  parentheses) is planned but not merged yet. Once it lands, replace the paragraph below with:
  "Link to a page by its current filename (`pet-system.md`, not `Pet_System.md`) — see
  `all-pages.md` for the full list if you're not sure a page exists yet." Until then, link using
  whatever filename the target page actually has today; don't rename or re-target links yourself as
  part of routine content edits — that's handled by the rename effort, not by this guide.
-->

Link to a page by its current filename, whatever that is today — see `all-pages.md` for the full
list if you're not sure a page exists. Renaming a page's file is a separate, repo-wide effort; don't
rename a file or change how it's linked to as part of a routine content edit.

- From a page in a subfolder (a section hub), go up first: `../Pet_System.md`.

## Raw HTML

Keep content pages plain Markdown. The only exceptions: a floating image (`align="left"`, see
Images above), a forced table-cell line break (`<br>`), and the layout containers already used
sitewide (`<div class="grid cards" markdown>` and similar) — those aren't something a content page
should introduce on its own.

## Line length

Don't hard-wrap prose. Write a paragraph as one line, however long — Markdown collapses it into the
same rendered paragraph either way, and wrapping only makes future edits and diffs messier (a
one-word change shifts every wrap point after it, so the diff shows the whole paragraph as changed
instead of the sentence that actually moved).

Keep the 120-character limit from the root `CLAUDE.md` for **tables, code blocks and YAML** (front
matter, `mkdocs.yml`), where a line has real structural meaning and length affects the rendered
result, not just the source file.
