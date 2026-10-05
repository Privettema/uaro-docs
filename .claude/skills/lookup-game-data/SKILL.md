---
name: lookup-game-data
description: Look up game data (which class learns a skill, skill/item/monster stats, drops, shop prices, uaRO-specific values) before writing or correcting wiki content. Use when a doc claim needs checking, when placing a change under the right class, or when a patch note names a skill, item or monster and you need its official data.
---

# Look up game data

Read this before you assign a skill to a class, quote an official value in an
"Original" column, or check an item ID. Don't rely on memory or on a single
web page. The steps below come from the `uaro-loot-sheet` project, which
uses the same sources every day.

## Where data comes from (most reliable first)

1. **In-game screenshots or values from the maintainer.** They beat
   everything else. Take them as given.
2. **The uaRO wiki (wiki.uaro.net)** is the authority for what uaRO changed.
   It is this repo, so use the Markdown in `docs/` and the patch notes in
   `docs/patch-notes/`. Old pages can be stale: when a page and a newer patch
   note disagree, the newer patch note wins. Flag the stale page.
3. **Hercules, pre-renewal** (`HerculesWS/Hercules`, branch `stable`). This is
   the default for "Official" behavior, because uaRO is pre-renewal.
   Files: `db/pre-re/skill_db.conf`, `db/pre-re/skill_tree.conf`,
   `db/pre-re/item_db.conf`, `db/pre-re/mob_db.conf`.
4. **Hercules, renewal** (same repo, `db/re/` with the same file names). If an item
   or skill has no pre-re entry, it is renewal content: check here next and write
   the renewal values in the "Original" column. Not every renewal item is in it.
5. **rAthena** (`rathena/rathena`, branch `master`). Use it for renewal
   content missing from Hercules `db/re/` and as a second opinion. It has
   `db/pre-re/` and `db/re/` folders (YAML, `item_db_equip.yml`, `item_db_etc.yml`).
   Hercules and rAthena renewal values sometimes differ (for example Cannon
   Spear, Old Parasol, Celine's Ribbon). Prefer Hercules and say when they differ.
6. **Classic wiki** (irowiki.org/classic, already linked from Class Changes)
   for human-readable skill descriptions. Its URLs often redirect to older
   names and 404 on guesses, so treat a fetched summary as provisional and
   confirm against Hercules.

Hercules and rAthena show the **Official** value (renewal values count as official when pre-re has no entry). They never show what uaRO
changed. Values in "uaRO Changed Behavior" come from the patch notes.

## Fetching emulator files

Download with `curl` from `raw.githubusercontent.com` into a temp folder (the
session scratchpad), never into the repo:

```bash
D=<scratchpad>; B=https://raw.githubusercontent.com/HerculesWS/Hercules/stable/db/pre-re
for f in skill_db skill_tree item_db mob_db; do curl -s $B/$f.conf -o $D/$f.conf; done
```

The wiki at wiki.uaro.net blocks plain `curl`, and WebFetch only returns a lossy
summary that can drop or change table rows. That does not matter here (the
docs are local), but if you must read the live site, use the browser pane and
extract the table with JavaScript (`document.querySelectorAll('table')`).

## Recipes

### Which class learns a skill?

The skill tree file lists every job with its skills at two tabs of
indentation. A job may `inherit` another job's tree, so a skill listed under
`Swordsman` is also usable by Knight and Crusader.

```python
import re
job, res = None, {}
for l in open('skill_tree.conf').read().split('\n'):
    m = re.match(r'^([A-Za-z_0-9]+):\s*\{', l)
    if m: job = m.group(1)
    m = re.match(r'^\t\t([A-Z]{2,3}_[A-Z0-9_]+):', l)
    if m and job: res.setdefault(m.group(1), []).append(job)
print(res.get('MO_ABSORBSPIRITS'))   # ['Monk', 'Expanded_Super_Novice']
```

Job names in the file are the first-class names (`Magician` = Mage,
`Swordsman`, `Monk`, `Assassin`, ...) and `Expanded_Super_Novice` shows up
for skills the Expanded Super Novice can use. Look up the constant name first
(next recipe).

Skills that are **not** in the tree (for example potion or converter creation,
Fury, Maximum Over-Thrust) are granted by quests, statuses or scripts. Find the
skill's page in the classic wiki or check who the wiki already lists it under.
Say so instead of guessing.

### Find a skill's constant name and data

```bash
grep -n -B1 -A14 'Description: "Absorb Spirit Sphere"' skill_db.conf
```

Each entry has `Id`, `Name` (the constant, like `MO_ABSORBSPIRITS`),
`Description`, `MaxLevel`, and, further down, SP cost, cast time and delay
tables. Compare with the patch note to write the "Original" column.

### Items and monsters

Search `item_db.conf` / `mob_db.conf` by `Name:` for IDs, stats, drops
and NPC buy or sell prices. uaRO changes monster drops and stats: for a monster
uaRO edited, the patch notes or `@mi` screenshots beat the emulator.

## Rules learned the hard way

- Use uaRO's in-game item and skill names in the docs, even when the emulators
  name them differently.
- Item IDs on old wiki pages sometimes have typos. Check each against
  Hercules and fix or flag it.
- Emulator **trade flags** were wrong for uaRO every time they were checked.
  Don't document "tradeable" or "not tradeable" from the emulators.
- A behavior that already matches the pre-renewal default is **not** a change.
  Don't list it (for example, a trap skill reverted to pre-renewal).
- A bug fix, animation fix or status icon is not a change unless it alters
  what players can do. Skip those.
- Never invent a number. If a value isn't in the patch notes, the maintainer's
  screenshot, or the emulator, write "unknown" and ask.

## Reporting

When you use this to check content, say which source each answer came from,
and list anything you could not confirm so the maintainer can decide.
