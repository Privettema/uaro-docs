# Class Changes Writing Guide

Conventions for [Class Changes](../class-changes.md), so every section reads the same.

Follow the [Style Guide](style-guide.md) first. This guide only adds rules that are specific to the Class Changes tables. Where the two overlap (Zeny, durations, "Level", Title Case names, no hard-wrapped prose, no raw HTML), the style guide wins and the rule is not repeated here.

## Goals

### Reader Goals

Readers are players with average familiarity with Ragnarok Online. They come to this page to:

- Find out whether a skill they use or plan to use behaves differently on uaRO.
- See exactly what changed, in numbers, without having to compare against the official game themselves.
- Judge a class or build before committing to it.
- Scan quickly: find their class, then their skill, without reading the whole page.

### Writer Goals

- Make every row answer "what is different, and by how much" in one glance.
- Keep Original and uaRO Changes comparable, so a reader can line the two cells up property by property.
- Be accurate. A wrong Original misleads more than a missing row does.
- Stay consistent, so the page reads as if one person wrote it.

## Tone and Voice

- Follow Tone and Voice in the style guide. Table cells are reference text, so they carry no flavor: plain, neutral and factual. Describe the change; do not sell it or apologize for it.
- Direct and present tense: "Cooldown reduced to 5 seconds", not "The cooldown has been reduced".
- Address the player as "you" only when the skill is about them ("You can chat while Berserked"); otherwise name the subject ("Mobs on the same cell").
- No hype, opinions or balance arguments ("much better", "finally", "to support better game balance").
- Use the game's own terms. Explain a term only when a player with average knowledge would not know it.

## Do and Don't

| Do | Don't |
|-|-|
| List only what differs from the official game. | Repeat unchanged official stats. |
| Write the Original as the official value. | Copy a skill's full description or leave "N/A". |
| Give the number: "Cooldown of 0.5 seconds" to "0.333 seconds". | Write "faster" or "reduced" with no values, unless the maintainer approved prose for that row. |
| Compare the same property in both columns. | Mention something in uaRO Changes that Original never states. |
| Put an NPC, icon or related rule in the skill's own row. | Give each side detail its own row. |
| State a shared rule once, in General / Shared. | Repeat it in every skill it affects. |
| Say "unverified" in the pull request when a value could not be checked. | Guess a number or a source. |
| Use short cells with one point per line. | Write paragraphs or lists inside a cell. |

## Table Layout

- One table per heading, wrapped in `<div class="class-changes-table" markdown>` so the column widths from `docs/css/custom.css` apply.
- Columns are `Skill | Original | uaRO Changes`, with the separator row `|-|-|-|`.
- Put each skill icon in the first cell as an inline icon, `![Skill name](img/Class_Changes/file.png) Skill name`, with real alt text as the style guide requires. Rows without an icon (general mechanics) start with the plain name.
- Use `<br>` for a new line inside a cell, one point per line. Do not use lists inside cells.
- Link with Markdown (`[Bag of Gold Coins](#bag-of-gold-coins)`), not HTML anchors.

## What Belongs in a Row

- List only what differs from the official pre-renewal game. Bug fixes, cosmetics and normal drop-rate scaling are not changes.
- One row per skill or mechanic. Fold related NPCs and icons into the skill's row instead of giving them their own.
- The Original column holds only what the uaRO column compares against, rewritten as the official value. Do not copy a skill's full description.
- Leave Original blank when uaRO added something with no official counterpart. Do not write "N/A".
- If a patch note and the page disagree, the newer patch note wins. Never invent numbers; ask the maintainer.
- State a rule once. If a mechanic applies to many skills (for example, reflected damage cannot exceed the user's HP), keep it in General / Shared and leave only the skill-specific part in each skill's row.
- The uaRO column may only state something the Original column also states, so the two can be compared. If the Original is silent (for example, whether a status had an icon), add that fact to the Original.

### Numbers and Prose

Give the number whenever one exists. Sometimes the patch notes and databases do not have it ("ASPD penalty is reduced", "increased plant count"). In that case, prose is allowed only when the maintainer has approved it for that row. List every approved prose row in the pull request description under "Prose approved over numbers", with the row name, so reviewers can see the gap is known and can fill it in later.

## Sources for Original Values

In order: maintainer screenshots or in-game checks, uaRO patch notes, Hercules `db/pre-re`, Hercules `db/re`, rAthena, iRO Wiki Classic. Values that could not be checked go in the pull request description as unverified. Do not name the source inside the table.

## Wording

- Write skill names as they appear in game ("Lord of Vermilion", "Mental Change (Lif)").
- Write "Level 3" when naming a skill Level, and lowercase "level" for a generic one ("per skill level"). Use "Base Level" and "Job Level" as in the style guide.
- Write cooldowns as "Cooldown of 5 seconds". Use "delay" only when the skill itself calls it a delay (Chase Walk).
- Compare the same property in both columns: "Delay of 10 seconds" is answered by "Delay reduced to 5 seconds".
- Use "homunculus", not "homc". WoE, GvG and "WoE: SE" are known terms and need no explanation.
- Start each cell with a capital letter and end it with a full stop. Keep sentences short and in the present tense.

## Checks

Recheck every row against its sources twice: before pushing commits, and again before opening the pull request. Sources and patch notes change, and a row that was right when drafted may not be later.

1. Recheck each Original and uaRO value against the sources above.
2. `mkdocs build` finishes with no new warnings.
3. `python3 scripts/lint_style.py docs/class-changes.md` has no findings on the new lines (long table rows and `<br>` findings in tables not yet converted are ignored for now).
4. Open the page with `scripts/serve.sh` and check the table widths and icons.
5. Commit each class section separately.
6. In the pull request description, list unverified values and the prose-over-numbers rows.
