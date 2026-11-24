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

When a change alters what a page says (not formatting, typos, links or renames), set its `updated:` date before opening the
PR: `python3 scripts/stamp_updated.py` stamps every page changed on the branch (see "Last updated" in the guide).

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
- **Changes pages** (`class-changes.md`, `item-changes.md`, `monster-changes.md`, `map-changes.md`, `quest-changes.md`) list everything
  that is added, removed or modified compared with the official game. The baseline is iRO as players see it: uaRO is pre-renewal with
  renewal content added, so a thing that existed before renewal is compared with its pre-renewal version, and renewal-only content with
  its renewal version. The class, monster, map and quest pages show Original vs uaRO; `item-changes.md` gives each item's uaRO description.
- We can't see how iRO or uaRO work internally, so every source is an approximation of "official". Check, in order: the client item
  text (game-data-tools), Hercules (`db/pre-re` or `db/re`, matching the ruleset above), then rAthena. Where they disagree, or an item
  is missing from one, say the value is unconfirmed. Hercules is what uaRO's server runs, so a Hercules/official gap still counts as a
  change for players; flag it as unconfirmed until the maintainer says it is intended.
- Items that uaRO added also go in `item-changes.md`. `whats-different.md` lists the areas and
  instances that uaRO added, by episode. Unchanged cards from renewal monsters belong on the page for the area where they drop.
- **Quality of Life** (`improvements.md`) is for game-wide rules and mechanics that are not about one item, skill, monster or map:
  inventory and trade rules, buff stacking, teleport behavior, storage limits. Add a one-line row to the Optimized Mechanics
  table (or the section that fits); longer features get their own page. A change to one item goes in `item-changes.md`, one
  skill in `class-changes.md`.
- **Content pages** (`biolab4.md`, `el-dicastes.md`, `horror-toy-factory.md`, ...) say how to get things. Put an item's stats in `item-changes.md` once and
  link to its row (anchor `<a id="..."></a>`); do not copy the stats onto the content page.
- Item rows: icon (`img/item<ID>.gif`) and name, then the copyable Item ID (unslotted ID first, then the slotted one), then the
  uaRO description. Unslotted by default (write `[n]` only when slotted). List monsters as `Name `ID`{ .copy }`, with no parentheses.
  General rules that aren't one item (such as a weapon type) go at the top of their table.

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
