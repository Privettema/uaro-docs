---
updated: 2026-10-11
---

# Pet Lookups

Open questions and confirmed values for the data in `data/pets.yml`. Not in the nav; it's for editors of the pet page.

## Egg images
- [x] Done: 104 egg icons downloaded from Divine Pride (`static.divine-pride.net/images/items/item/<id>.png`)
      into `docs/img/Pet_System/<egg id>.png` and `data/pets.yml`, and into `game-data-tools/images/items/`.
      Only the pets with no egg ID (Valkyrie Randgris) have no egg icon. Wrong egg IDs below would mean wrong icons.

## Egg IDs to confirm in game
- [x] Wild Rose `9141`, Eddga `9142`, Fire Golem `9131`, Kiel D-01 `9126`, Chaotic Bapho Jr `9130`: confirmed.
- [x] Wild Rose and Eddga egg icons downloaded.
- [x] Valkyrie Randgris egg is `9185`. The name is "Randgris Egg", from `monster-changes.md`.
- [x] White Knight (evolved) may not be a real mob, so it has no mob ID. Egg `9134` and Mutating White Knight's `9133` match the client file.
- [x] Baphomet egg `9137`: confirmed.

## Mob and item IDs
- [x] Evil Nymph: egg `9047` and bonus match your screenshot. Mob ID is `1416` (Wicked Nymph); the drop source uses it too (`1564` is the no-EXP copy)
- [x] 12 custom pets had their mob ID taken from the sprite filename on the old page, not a database:
      Green Petite, Knife Goblin, Flail Goblin, Hammer Goblin, Wandering Duck Doll, Mutating White Knight,
      Yao Jun, Chaotic Bapho Jr, Blue Moon Loli Ruri, Contaminated Wanderer, Abysmal Knight, Fire Golem.
- [x] Poring's taming item is Unripe Apple (`619`); icon fixed.
- [x] Hornet's taming item is Beehive (`102723`, the client says Hornets like it), dropped by Hornet at 1%.
- [x] Names: Imp, Civil Servant, Chung E.

## Pets from the game database
- [x] Resolved: uaRO has New Year Doll and Blue Unicorn (added). The other 20 are not present.

## Drop sources: which monster ID is the one that drops it
The 17 uaRO-added taming item drops moved from the pet cards to `monster-changes.md` (none exist in Hercules). The pet
page points players to `@whodrops` and `@ii` instead. The drop rates are from the old page, unchanged. Several of
these monsters exist under more than one ID in the database; I used the original spawn. Please confirm in game.
- [x] Vagabond Wolf is mob `1092`.
- [x] Evil Nymph `1416` (also `1564`, `2004`, `2214`; `1564` is the no-EXP copy)
- [x] Moonlight Flower `1150` (also `20424`, which looks like the pet version)
- [x] Gloom Under Night `1768` (also `2108`, `20619`)
- [x] Galion `1783` (also `1791`)
- [x] Nightmare Terror `1379` (also `1554`)
- [x] Dracula `1389`; Dark Lord `1272`; Dark Illusion `1302`; Evil Druid `1117` (also `1435`); Golem `1040`
      (also `1540`); Medusa `1148` (also `1749`); Ghostring `1120`; Phreeoni `1159`; Hornet `1004`
- [x] Typo fixed: "Loli Rur" on the old page is Loli Ruri (`1505`). Say if it was meant to be someone else.

## Event pets (from your in-game screenshots)
- [x] Violet: no mob ID, no bonus, Pet Food.
- [x] Tai-Zi (egg `9184`): rotating event shop item. The price stays unknown; no mob ID, Pet Food, no bonus.
- [x] Event Token is item `7866`, sold by Marley in Main Office. Blue Unicorn is 3 tokens.
- [x] Mochi icon added.
- [x] Rice Cake: mob `1815` and diet Green Herb come from Hercules and the client file. Confirm.

## Values taken from the emulators (not checked against uaRO)
- [x] Loyal intimacy is 900 (confirmed).
- [x] Hunger drops 3 points every 60 seconds: 3 is from the old page, the 60 seconds is the Hercules default.
- [x] Intimacy per feeding (40 / 30 / 20): from the old page; the emulators have no per-tier values.

## Food and accessory review against Hercules
- [x] Gremlin food Cheap Lubricant (`25232`), Willow Fine-grained Trunk (`1066`), Roween Rotten Meat (`7564`): taken from Hercules.
- [x] Wanderer, Whisper, Diabolic and Rigid Nightmare Terror use Pet Food in game; Domovoi uses Luxurious Pet Food.
- [x] Incubus food is Vital Flower (Yellow) (`6110`) and Succubus is Vital Flower (Blue) (`6113`).
- [x] Skelion food `11616` is Delicious Meat in game (Hercules calls it Yummy Meat).
- [ ] Bug to report: Teddy Bear's food shows as Cotton Wads in game, but item `25233` is named Cotton Tufts.
- [x] Whisper accessory is Pet Soul Ring (`10027`). Scatleton's Red Bell Necklace (`10040`) has no description, so it is not listed.

- [x] NPC-crafted taming items (Monster Tamer in Alberta and Izlude, Munak's Grandma in Comodo): Orc Trophy `635`, No Recipient `636`, Book of the Devil `642` and Her Heart `659`. Singing Flower `629` and Monster Juice `626` are also crafted there but drop from monsters, so the page does not list the recipe. Recipes from the Hercules scripts (`monstertamers.txt`) and [Tame Ingredients](https://irowiki.org/wiki/Tame_Ingredients).
- [x] Knife, Flail and Hammer Goblin rings and the Goblin Leader Staff Of Leader are event only.

## To do
Left open after the data review. Come back to these.

### Confirm in game
- [x] Gremlin taming item `23188` is "Broken Part" (renamed from "Airship Part" in the data, the Hodremlin material, `taming-gift-set.md` and `monster-changes.md`). The icon file is still `231800_1.png`.
- [ ] Evil Nymph drop source was changed to mob `1416` (the real spawn). Confirm that is what was meant.
- [x] Valkyrie Randgris egg drops from her at 0.15%, taken from `monster-changes.md` (Hercules has no egg in her drops).
- [ ] Valkyrie Randgris accessory: the old page listed "Randgris's Accessory" with no item ID or icon, and it is not in Hercules. Removed from the page until the real name and ID are known.
- [ ] Tai-Zi event shop price is unknown.
- [ ] Rice Cake mob `1815` and Green Herb diet come from Hercules, not the game.
- [ ] Hunger 3 per 60 seconds, death penalty 5 and feeding tiers (40, 30 and 20) are kept as uaRO values with no source (Hercules defaults are 1, 20 and 10 to 50 per pet).
- [ ] About 22 capture rates differ from Hercules `db/re` and were kept from the old page. Evil Nymph (10%) and Goblin Leader (5%) differ from pre-re and are kept as custom.

### Report
- [ ] Bug: Teddy Bear's food shows as Cotton Wads in game, but item `25233` is named Cotton Tufts.

### Before a PR
- [ ] No PR is open. Do not open one without a yes.
- [x] `lint_style.py` is clean on `pet-system.md`, `taming-gift-set.md` (now a table) and this page.

### Page review follow-ups
- [ ] Decide on a name index or filter for All Pets (115 cards, no way to jump to one).
- [ ] "Reaching Loyal" on the page assumes a new pet starts at Neutral (250) and that over-feeding loses intimacy. Both come from the rAthena source, not from uaRO.
- [x] The content-type rule was removed from `CLAUDE.md` and the `**Content type:**` line from the six pages that carried it. `whats-different.md` still has the Content Tags table, so it can be cleaned up separately.
