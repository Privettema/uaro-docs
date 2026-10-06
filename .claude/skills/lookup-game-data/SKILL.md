---
name: lookup-game-data
description: Look up game data (which class learns a skill, skill/item/monster stats, drops, descriptions, sprite IDs, uaRO-specific values) before writing or correcting wiki content. Use when a doc claim needs checking, when placing a change under the right class, or when a patch note names a skill, item or monster and you need its official data.
---

# Look up game data

Read this before you assign a skill to a class, quote an official value in an "Original" column, or check an item ID. Don't rely on memory or on a single web page.

## Use the tools first

The lookups are done by [game-data-tools](https://github.com/rhya-games/game-data-tools), which keeps local copies of the emulator databases and saved pages in `~/game-data` (set `GAME_DATA` to move it). If `~/game-data` is missing, clone that repo there and run `setup.sh`; its README has the steps.

Run the compare tools from the root of this repo, so they can also search `docs/` and the patch notes for mentions. Each one lines up Hercules pre-re and renewal and rAthena pre-re and renewal, and lists the fields where they disagree:

| Question | Command |
|---|---|
| Is this item value right? | `~/game-data/bin/compare_item.py <id or name>` (also shows a saved irowiki page and the client description) |
| Is this monster value right? | `~/game-data/bin/compare_mob.py <id or name>` |
| Is this skill value right, and which class learns it? | `~/game-data/bin/compare_skill.py <constant, name or id>` |
| Which monsters drop an item, or what does a monster drop? | `~/game-data/bin/drops.py <item>` or `drops.py --mob <monster>` |
| Item description, slots, view ID | `~/game-data/bin/parse_iteminfo.py <id or name>`, or `--view N` for the items using a headgear view ID |
| Sprite or headgear view ID | `~/game-data/bin/parse_sprites.py <id or name>`, or `--gaps` for view IDs missing from the list |

A disagreement between sources is a question for the maintainer, not something to settle by picking one. Hercules and rAthena renewal values sometimes differ from each other, so say so when they do.

### Saving what you read

- Save any page you rely on with `~/game-data/bin/save_page.sh <url>`, so it is read from disk next time. It keeps the page unmodified, with a `.meta` file for the URL and date. For a page you could only read through the browser pane, save its HTML to a file and run `save_page.sh <url> --file <path>`. Never edit a saved page.
- Write what you learn about a page in `~/game-data/notes/<host>/<slug>.md`, kept apart from the raw copy.
- Append confirmed facts to `~/game-data/notes/learnings.md` with the date and source. The notes folder is its own private repo (`rhya-games/game-data-notes`): commit and push it after adding notes.

## Where data comes from (most reliable first)

1. **In-game screenshots or values from the maintainer.** They beat everything else. Take them as given.
2. **The uaRO wiki (wiki.uaro.net)** is the authority for what uaRO changed. It is this repo, so use the Markdown in `docs/` and the patch notes in `docs/patch-notes/`. Old pages can be stale: when a page and a newer patch note disagree, the newer patch note wins. Flag the stale page.
3. **Hercules, pre-renewal** (`db/pre-re`). This is the default for "Official" behavior, because uaRO is pre-renewal.
4. **Hercules, renewal** (`db/re`). If an item or skill has no pre-re entry, it is renewal content: write the renewal values in the "Original" column. Not every renewal item is in it.
5. **rAthena** (`db/pre-re`, `db/re`). Use it for renewal content missing from Hercules and as a second opinion.
6. **Client item file** (`parse_iteminfo.py`). Descriptions, slots and view IDs. It follows the current client, so its numbers are usually renewal values and it can disagree with pre-re for items renewal changed.
7. **Public wikis and databases**, for human-readable descriptions and guides. curl works on all of these with `-A 'Mozilla/5.0'`:

| Source | Use it for | URL pattern |
|---|---|---|
| db.irowiki.org | Item descriptions, drops (iRO values) | `/db/item-info/<id>/` |
| skills.irowiki.org | Skill descriptions | site search |
| irowiki.org, irowiki.org/classic | Guides, quests (classic = pre-renewal) | `/classic/<Page>` |
| ratemyserver.net | Item, monster, skill pages | site search |
| renewal.playragnarok.com | Renewal database | site search |
| nn.ai4rei.net/dev/npclist/, `/viewlist/` | NPC sprite IDs, headgear view IDs | `?qq=<page>`, anchor `id<N>` |
| dotalux.com/ro/npclist/ | NPC sprite list | single page |

Reading lists, not data: the Warp Portal guide master list, Ragnarok Research Lab community projects, and the `ragnarok-online` GitHub topic.

Hercules and rAthena show the **Official** value (renewal values count as official when pre-re has no entry). They never show what uaRO changed. Values in "uaRO Changed Behavior" come from the patch notes.

## Rules learned the hard way

- Use uaRO's in-game item and skill names in the docs, even when the emulators name them differently.
- Item IDs on old wiki pages sometimes have typos. Check each against Hercules and fix or flag it.
- Emulator **trade flags** were wrong for uaRO every time they were checked. Don't document "tradeable" or "not tradeable" from the emulators.
- A behavior that already matches the pre-renewal default is **not** a change. Don't list it (for example, a trap skill reverted to pre-renewal).
- A bug fix, animation fix or status icon is not a change unless it alters what players can do. Skip those.
- uaRO changes monster drops and stats. For a monster uaRO edited, the patch notes or `@mi` screenshots beat the emulator.
- `compare_skill.py` has a Quest column from the databases' own quest-skill flag (Hercules `SkillInfo.Quest`, rAthena `IsQuest`). Both flag the same 40 pre-renewal skills, including the platinum skills such as Making Arrow, Charge Arrow, Change Cart and Holy Light. A quest skill is learned through a quest, not skill points, so name the quest requirement in the docs. The tree still lists these under the first class, so Quest = yes is the only sign. Fury, Maximum Over-Thrust, Potion Creation and Converter Creation are normal skills (Monk, Whitesmith, Alchemist).
- Never invent a number. If a value isn't in the patch notes, the maintainer's screenshot, or the emulator, write "unknown" and ask.

## Reporting

When you use this to check content, say which source each answer came from, and list anything you could not confirm so the maintainer can decide.

## Reading the database files directly

The emulator files are in `~/game-data/hercules/db/` and `~/game-data/rathena/db/`. If they are missing, run `~/game-data/setup.sh` (clone the repo first if the folder doesn't exist). To find a skill's constant and data, `grep -n -B1 -A14 'Description: "Absorb Spirit Sphere"' ~/game-data/hercules/db/pre-re/skill_db.conf`. The skill tree (`skill_tree.conf`) lists each job's skills at two tabs of indentation, and a job may `inherit` another job's tree, so a skill under `Swordsman` is also usable by Knight and Crusader. Job names are the first-class names (`Magician` = Mage).

WebFetch only returns a lossy summary that can drop table rows. To read a live page, use the browser pane and extract the table with JavaScript (`document.querySelectorAll('table')`).
