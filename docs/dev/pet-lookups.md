# Pet Lookups

Open questions and confirmed values for the data in `data/pets.yml`. Not in the nav; it's for editors of the pet page.

## Egg images
- [x] Done: 104 egg icons downloaded from Divine Pride (`static.divine-pride.net/images/items/item/<id>.png`)
      into `docs/img/Pet_System/<egg id>.png` and `data/pets.yml`, and into `game-data-tools/images/items/`.
      Only the pets with no egg ID (Valkyrie Randgris) have no egg icon. Wrong egg IDs below would mean wrong icons.

## Egg IDs to confirm in game
- [x] Wild Rose `9141`, Eddga `9142`, Fire Golem `9131`, Kiel D-01 `9126`, Chaotic Bapho Jr `9130`: confirmed.
- [x] Wild Rose and Eddga egg icons downloaded.
- [x] Valkyrie Randgris egg is `9185`. The name "Valkyrie Randgris Egg" is a guess (not in the client file).
- [x] White Knight (evolved) may not be a real mob, so it has no mob ID. Egg `9134` and Mutating White Knight's `9133` match the client file.
- [x] Baphomet egg `9137`: confirmed.

## Mob and item IDs
- [x] Evil Nymph: egg `9047` and bonus match your screenshot. Mob ID is `1416` (Wicked Nymph); its drop-source
      entry and old sprite use `1564`.
- [x] 12 custom pets had their mob ID taken from the sprite filename on the old page, not a database:
      Green Petite, Knife Goblin, Flail Goblin, Hammer Goblin, Wandering Duck Doll, Mutating White Knight,
      Yao Jun, Chaotic Bapho Jr, Blue Moon Loli Ruri, Contaminated Wanderer, Abysmal Knight, Fire Golem.
- [x] Poring's taming item is Unripe Apple (`619`); icon fixed.
- [x] Hornet's taming item is Beehive (`102723`, the client says Hornets like it), dropped by Hornet at 1%.
- [x] Names: Imp, Civil Servant, Chung E.

## Pets from the game database
- [x] Resolved: uaRO has New Year Doll and Blue Unicorn (added). The other 20 are not present.

## Drop sources: which monster ID is the one that drops it
The pet page now says "Dropped by Name (ID) (rate)". The drop rates are from the old page, unchanged. Several of
these monsters exist under more than one ID in the database; I used the original spawn. Please confirm in game.
- [x] Vagabond Wolf is mob `1092`.
- [x] Evil Nymph `1564` (also `1416`, `2004`, `2214`)
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
