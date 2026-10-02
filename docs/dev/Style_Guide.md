# Style Guide

How to write and format a wiki page, so pages feel consistent no matter who wrote them. This page is not in the nav — it's for editors, not players.

Run `python3 scripts/lint_style.py` before opening a PR. It checks the mechanical rules below (see [Checking your changes](#checking-your-changes)).

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

- **Title (`#`)**: exactly one H1, matching the page's nav label with the emoji removed. It's the first line of the file, no blank line above it.
- **Intro**: one or two sentences right after the title, separated from it by a single blank line. Say what the page covers before diving into detail — don't repeat the title as a sentence ("This page is about X").
- **Quick Facts** *(optional)*: for an NPC, event or system with a handful of at-a-glance facts (NPC, location, level requirement, cost, duration), use an `info` admonition right after the intro instead of burying them in prose. Skip it for pages that don't have that kind of data (guides, FAQs, command references), and don't use it to explain how a mechanic works — that belongs in How It Works.
- **Sections use `##`, not `###`**: don't start a page's first section at `###` — it has no `##` parent and breaks the page outline. Use `###` only to subdivide an existing `##` section.
- **Section names**: use the same names across similar pages (a quest page has *Requirements*, *Steps*, *Rewards*) so readers know where to look.
- **System pages** follow one order: intro, `## How It Works`, then the reference table or list under its own heading (`## Daily Rewards`, `## Item List`). Write the rules in How It Works as short bullets that lead with the rule in bold ("**Missing a day doesn't reset you.**"), and state the rule rather than walking through a worked example.

## Admonitions

Use the lowercase type with a quoted title, content indented 4 spaces, one blank line before and after:

```markdown
!!! note "Optional Title"
    Content here.
```

Pick the type by what the reader stands to lose or gain:

| Type | Use it for |
|---|---|
| `info` | Quick Facts, or background a reader might want |
| `note` | A caveat or detail that applies to the paragraph above |
| `tip` | An optional shortcut or a better way to do something |
| `important` | A rule or requirement to check before starting |
| `warning` | Something that costs the reader items, Zeny or progress if missed |
| `danger` | Irreversible loss (permanent deletion, non-refundable purchases) |
| `success` | Event announcements and confirmations in patch notes |

Anything a reader can lose by missing it — an expiry, a deadline, a one-time choice — goes in a `warning`, not in a bullet.

One callout makes one point. If a page has more than a few, some of them are ordinary sentences.

Use `??? note "Title"` (collapsible) for a block that's long and mostly reference material a player skips past — a full town-coordinate table, for example — not for anything a first-time reader needs.

## Images

- Page-specific images go in a subfolder: `docs/img/<Page_Name>/`. Shared item/monster/skill sprites stay directly in `docs/img/`.
- A standalone image (screenshot, NPC portrait) gets its own line: `![Alt text](img/filename.webp)`. Write a real alt text, not `""` or the filename.
- Give a standalone screenshot the `.wiki-screenshot` class: `![Alt text](img/filename.webp){ .wiki-screenshot }`. It adds the frame and the spacing above and below. Don't use blank lines or `<br>` to add space.
- An inline icon (an item or skill next to its name in a sentence or table cell) stays inline: `![Item Name](img/1234.gif) Item Name`.
- For a layout markdown can't do alone (floating an image beside text), use `<img src="img/filename.webp" alt="Alt text" align="left" />` — this is the one place raw HTML is expected on a content page.

## Tables

- Standard Markdown pipe tables. Keep every row's cell content on one line — don't rely on trailing double-spaces for a line break; if a cell genuinely needs a forced break, use `<br>` inside it.
- An item/monster column shows the icon and name together: `![Name](img/1234.gif) Name`. Give item IDs in their own column, last (see Names and terms).
- No trailing whitespace on any line, in or out of a table.

## Links

Link to a page by its current filename (`pet-system.md`, not `Pet_System.md`) — see `all-pages.md` for the full list if you're not sure a page exists yet. Old filenames still redirect, but links should use the new one.

New pages use lowercase, hyphen-separated filenames with no underscores or parentheses: `cart-and-falcon-coupons.md`. Don't rename an existing file as part of a routine content edit; renames also need a redirect entry in `mkdocs.yml`.

- From a page in a subfolder (a section hub), go up first: `../pet-system.md`.
- Link text says where the link goes: "Read the full Halloween Event guide", not "click here" or a bare URL.

## Writing

The rules below match what most existing pages already do. Where pages are inconsistent today, the guide picks one form so new edits converge on it.

### Tone

The wiki reads like a friendly veteran player showing you around: warm, practical, and quick to get to the facts. Flavor comes from the game's own world, not from sales talk.

- **Open with a little flavor, then the facts.** One or two sentences at the top can set the scene in the game's language (adventures, journeys, a town, a festival). After that, be plain. Keep flavor out of How It Works, tables and step lists, where readers are looking something up.
- **Show what makes it special.** Say "a 100-wave endgame challenge for a party of 12" rather than "the ultimate, incredible challenge". If you reach for "exclusive", "powerful" or "legendary", name the thing that earns the word.
- **Warm, not pushy.** Use contractions and "you". Use "we" only where the staff are speaking (see Voice). Don't shout, and don't promise excitement ("Get ready for…", "Your chance to win big!").
- **Emoji stay in the structure.** Emoji belong in nav labels and patch-note headings, not in body copy or in front of facts.
- **Exclamation marks are for announcements.** Use a few in event and patch-note announcements, and none on reference pages.
- **Some older pages (Main Office, Lottery NPC, Horror Toy Factory) are more promotional than this.** Don't copy their style into new pages. Tone them down when you're already editing them.

#### Event pages

Event pages get more flavor than any other page. They are temporary, themed and meant to be fun to read.

- Start with a short scene-setting intro in the event's theme: the location, the mood, who's involved. A few sentences is fine here.
- Themed section names and a bit of personality are welcome ("Meet the Summer Merchant"), and so are light emoji in headings on these pages.
- The facts still follow the normal rules: Quick Facts for location, levels and duration, and plain How It Works, steps and reward tables. Keep all of the flavor out of them.
- When an event ends, put a `warning` admonition titled "Event Concluded" at the very top and keep the page for reference. It says the event has ended and may return.

### Voice

- Address the reader as "you" and use the imperative for steps: "Talk to **Ranger Lettie**", not "Players should talk to Ranger Lettie". "Players" is fine when you mean other people ("trade with other players", "all players").
- "We" is for the staff voice on pages where the team is speaking (Donations, Main Office, announcements). Reference and guide pages don't need it.
- Be direct and brief. Lead with what to do or what the thing is, then add detail. Keep exclamation marks and hype for event and patch-note announcements.
- Describe how it works now. Don't use "new", "recently" or "currently" on a permanent page — they go stale. Dated information belongs in patch notes.
- Use US English: color, favor, center, canceled. Official in-game names keep their own spelling.
- Write dates as month day, year: `October 31, 2025`. Don't use `31/10/2025`, `2025-10-31` or `31 October 2025` in text. (The `date:` front matter in patch notes is the exception; it stays ISO.)

### Names and terms

- Use the name exactly as it appears in game (item, skill, monster, NPC, map). If the in-game name is odd, use it anyway and add a note rather than "fixing" it.
- Official game content is Title Case wherever it appears, in prose as well as headings: skills (Heal, Sharp Shooting), items (Old Card Album), monsters (Thief Bug), NPCs, maps and quests. Generic words stay lowercase ("a card", "the quest") unless they are part of the name.
- **Bold** NPC, item and quest names on first mention in a section, and when they're the thing a step tells you to interact with. Don't bold whole sentences for emphasis.
- Commands, chat input and map addresses go in backticks: `@koerank`, `/navi prontera 130/192`. Say what a command does the first time: "Check the server time with `@time`."
- Use `/navi <map> <x>/<y>` for locations so readers can copy it. Add plain `(x, y)` coordinates only when a page needs the number itself.
- Write "Level", never `Lv` or `Lv.`: "Level 50+". Use "Base Level" or "Job Level" when it matters which.
- **Item names are the exception to every wording rule on this page.** An item's in-game name is used exactly as it appears, even if it uses `Lv`, a UK spelling or unusual capitalization: "Lv10 Blessing Scroll" stays as is. The rules apply to the text around the name.
- Give an item's ID the first time a page mentions it, as a bare number in backticks: **Old Card Album** `616`. Do the same for monster IDs when you mention a monster: **Poring** `1002`. Players already know these IDs, and the code style keeps the number from reading as a quantity. In a table, put the ID in its own column instead of repeating it in every name cell.

### Numbers

- Zeny: always the full amount, with thousands separators and a `z` suffix — `5,000z`, `200,000,000z`. Never `5k`, `7k zeny` or `1m Zeny`. Spell out "Zeny" only when the word stands alone ("costs a lot of Zeny").
- Percentages have no space: `7%`. Durations spell the unit out: `30 seconds`, `5 minutes` — abbreviate to `sec`/`min` only where a table column is tight.
- Say what a value applies to when it isn't obvious (per card, per day, per character).
- If a value hasn't been verified in game, say so in a `note` instead of guessing.

### Headings

- Title Case: capitalize the first and last word and every word except short articles, conjunctions and prepositions (a, an, the, and, but, or, of, in, on, to, for, at, by) — "Blacklisted Cards", "Exchanging for Costumes". In-game names keep their official capitalization.
- Nav labels keep their emoji prefix (see `mkdocs.yml`), and each page's emoji is unique. Search the nav for the one you want before assigning it. Headings inside a page don't need one; the emoji headings on patch-note and event pages are fine there, but be consistent within a page.

### Patch notes

- One file per patch: `patch-notes/YYYY/patchesMMDDYYYY.md`. Add it to `all-patch-notes.md` and move the ⭐ to it.
- Use the section headings recent patches use (Gameplay, Quality of Life, Items, NPC, Commands, Skills, Fixes, Cash Shop), with or without the emoji they already carry, and leave out sections that are empty.
- One bullet per change, in past tense: "Fixed X", "Added Y", "Removed Z". Name what changed, not the internals.
- Link to the full guide page for anything bigger than a few lines instead of repeating it.

## Raw HTML

Keep content pages plain Markdown. The only exceptions: a floating image (`align="left"`, see Images above), a forced line break inside a table cell (`<br>`), and the layout containers already used sitewide (`<div class="grid cards" markdown>` and similar) — those aren't something a content page should introduce on its own.

## Line length

Don't hard-wrap prose. Write a paragraph as one line, however long — Markdown collapses it into the same rendered paragraph either way, and wrapping only makes future edits and diffs messier (a one-word change shifts every wrap point after it, so the diff shows the whole paragraph as changed instead of the sentence that actually moved).

Keep the 120-character limit from the root `CLAUDE.md` for **tables, code blocks and YAML** (front matter, `mkdocs.yml`), where a line has real structural meaning and length affects the rendered result, not just the source file.

## Checking your changes

```bash
python3 scripts/lint_style.py
python3 scripts/lint_style.py docs/card-exchange.md
```

The first command checks every page; the second checks only the files you name. The linter flags the rules that can be checked mechanically: title and heading structure, trailing whitespace, `Lv`, abbreviated or unformatted Zeny, spaced percentages, non-US date formats, common UK spellings, "click here" links, images with no alt text, `<br>` outside tables, long table lines and duplicate nav emojis. It can't judge voice, Title Case or missing item IDs — those are for review.

To silence a line that is deliberately different (an official in-game spelling, say), end it with `<!-- style-ignore -->`.

Existing pages predate the guide and will have findings; fix a page's findings when you're already editing it. Repo-wide cleanup is planned separately.
