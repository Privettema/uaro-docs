# Class Changes Writing Guide

Conventions for [Class Changes](../class-changes.md), so every section reads the same. For wiki-wide rules, see the style guide when it lands.

## Table Layout

- One table per heading, wrapped in `<div class="class-changes-table" markdown>` so the column widths from `docs/css/custom.css` apply.
- Columns are `Skill | Original | uaRO Changes`, with the separator row `|-|-|-|`.
- Put each skill icon in the first cell as `![Skill name](img/Class_Changes/file.png)Skill name`. Rows without an icon (general mechanics) start with the plain name.
- Use `<br>` for a new line inside a cell, one point per line. Do not use lists inside cells.
- Link with Markdown (`[Bag of Gold Coins](#bag-of-gold-coins)`), not HTML anchors.

## What Belongs in a Row

- List only what differs from the official pre-renewal game. Bug fixes, cosmetics and normal drop-rate scaling are not changes.
- One row per skill or mechanic. Fold related NPCs and icons into the skill's row instead of giving them their own.
- The Original column holds only what the uaRO column compares against, rewritten as the official value. Do not copy a skill's full description.
- Leave Original blank when uaRO added something with no official counterpart. Do not write "N/A".
- If a patch note and the page disagree, the newer patch note wins. Never invent numbers; ask the maintainer.

## Sources for Original Values

In order: maintainer screenshots or in-game checks, uaRO patch notes, Hercules `db/pre-re`, Hercules `db/re`, rAthena, iRO Wiki Classic. Values that could not be checked go in the pull request description as unverified. Do not name the source inside the table.

## Wording

- Write skill names as they appear in game ("Lord of Vermilion", "Mental Change (Lif)").
- Use "Level 3" when naming a skill Level. Use lowercase "level" for everything else ("per skill level", "base level").
- Write durations in words: "5 seconds", "0.5 seconds", "5 minutes". Write cooldowns as "Cooldown of 5 seconds". Use "delay" only when the skill itself calls it a delay (Chase Walk).
- Compare the same property in both columns: "Delay of 10 seconds" is answered by "Delay reduced to 5 seconds".
- Zeny amounts are `500z` and `50,000,000z`.
- Use "homunculus", not "homc". WoE, GvG and "WoE: SE" are known terms and need no explanation.
- Start each cell with a capital letter and end it with a full stop. Keep sentences short and in the present tense.
- No hard-wrapped prose.

## Checks Before a Pull Request

1. `mkdocs build` finishes with no new warnings.
2. The style linter has no findings on the new lines (long table rows are ignored for now).
3. Open the page with `scripts/serve.sh` and check the table widths and icons.
4. Commit each class section separately.
