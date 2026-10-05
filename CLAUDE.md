# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation site for **uaRO World of Your Dream**, a private MMORPG game server. The site is built with **MkDocs** using the Material theme and is published at https://wiki.uaro.net.

All documentation source files are located in the `docs/` directory. The site includes:
- Server information, rules, and features
- Patch notes organized by year (`docs/patch-notes/2024/`, `docs/patch-notes/2025/`)
- Game guides (dungeons, quests, systems, events)
- Custom styling in `docs/css/custom.css` (uses REMs for accessibility, CSS variables for theme support)

## Build and Development Commands

### Build the site
```bash
mkdocs build
```
This validates the configuration and builds the static site. The build must complete without warnings or errors before submitting PRs.

### Serve locally (if needed)
```bash
scripts/serve.sh
```
This starts a local development server on a port unique to the checkout (8100-8999, printed on start), so several
worktrees can serve at once. Plain `mkdocs serve` uses `http://127.0.0.1:8000/`, which only one checkout can hold.

### Check git status
```bash
git status
```
The working tree should be clean before creating PRs.

## Documentation Standards

Follow `docs/dev/style-guide.md` for page structure, formatting, wording and tone. It is the single source of truth, so
this file doesn't repeat it. Before opening a PR, run the linter on the pages you changed:

```bash
python3 scripts/lint_style.py docs/some-page.md
```

Existing pages predate the guide, so only fix findings on pages you are already editing, and don't restyle text that
has nothing to do with your change.

### Patch Notes Structure
- Individual patch files live in `docs/patch-notes/YYYY/patchesMMDDYYYY.md`
- Each patch starts with front matter: `date: YYYY-MM-DD`, optional `hotfix: true`, and `highlights:` (3 to 5 short,
  player-facing bullets, see `scripts/patch_highlights_prompt.md`)
- `docs/all-patch-notes.md`, the per-year pages, the sidebar Archive and the home page preview are generated from the
  patch files by `hooks/patch_notes.py`. Do not edit them by hand; a new patch is just a new dated file
- A new year needs a copy of `docs/patch-notes/YYYY/index.md`
- Section headings and bullet wording are covered in the style guide

### Where Content Goes
Content pages carry one tag (see `docs/whats-different.md`): **Changed** (official content uaRO altered),
**Renewal** (renewal content added; it is rebalanced where needed) or **uaRO** (made for uaRO).

- **Changes pages** (`class-changes.md`, `item-changes.md`, `monster-changes.md`, `map-changes.md`, `quest-changes.md`) list only things
  that differ from the official game, as Original vs uaRO. Original is the pre-renewal value (Hercules `db/pre-re`); if there is no
  pre-re version it is the renewal value (Hercules `db/re`, then rAthena) and the row says so.
- Items that uaRO added also go in `item-changes.md`, with a blank Original and no tag. `whats-different.md` lists the areas and
  instances that uaRO added, by episode. Unchanged cards from renewal monsters belong on the page for the area where they drop.
- **Quality of Life** (`improvements.md`) is for game-wide rules and mechanics that are not about one item, skill, monster or map:
  inventory and trade rules, buff stacking, teleport behavior, storage limits. Add a one-line row to the Optimized Mechanics
  table (or the section that fits); longer features get their own page. A change to one item goes in `item-changes.md`, one
  skill in `class-changes.md`.
- **Content pages** (`biolab4.md`, `el-dicastes.md`, `horror-toy-factory.md`, ...) say how to get things. Put an item's stats in `item-changes.md` once and
  link to its row (anchor `<a id="..."></a>`); do not copy the stats onto the content page.
- Add the content-type line (`**Content type:** [Renewal](whats-different.md#content-tags)`) under the title of each content page.
- Item rows: unslotted by default (write `[n]` only when slotted), list monsters as `Name (`ID`)`, and leave Original blank when there
  is nothing official to compare against.

## Repository Architecture

### Navigation (`mkdocs.yml`)
The navigation structure is defined in the `nav:` section of `mkdocs.yml`. When adding new pages:
1. Create the markdown file in `docs/`
2. Add the entry to the appropriate section in `nav:`
3. Use an emoji prefix (e.g., `🎉`, `🧵`, `⚔️`) that no other nav entry uses; the linter flags duplicates

### Custom Styling
`docs/css/custom.css` contains page-specific styles:
- `.class-changes-table` for `class-changes.md`
- `#main-features-cards` for feature cards
- All styles use REM units (based on 16px) and CSS variables from the Material theme

### Theme Configuration
The site uses Material for MkDocs with:
- Dark/light mode toggle
- Navigation features: sections, expand, footer, table of contents integration
- Search with suggestions and highlighting
- Code blocks with syntax highlighting and copy buttons
- Multiple markdown extensions (see `markdown_extensions:` in `mkdocs.yml`)

## Pull Request Workflow

When creating PRs:
1. Run `mkdocs build` to validate changes
2. Verify no warnings or errors in build output
3. Ensure `git status` shows a clean working tree
4. Summarize changes and note whether `mkdocs build` succeeded
5. If MkDocs is not installed, note this in the PR description
