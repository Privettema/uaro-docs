# Class Changes Source Comparison

A record of what each reference says about the Original column on [Class Changes](../class-changes.md), so a later edit can see what was checked and where the references disagree. The ranking of sources is in the [Class Changes Writing Guide](class-changes-guide.md#sources-for-original-values). Checked on October 6, 2026.

How to read it:

- **Page** is what the Class Changes page says now.
- **Hercules / rAthena** is `db/pre-re` for both. They agree unless noted.
- **iRO Wiki** is iRO Wiki Classic, the official-facing reference.
- **Result** is `match`, `differs` (the references disagree with the page or each other), `partial`, `emulator only` (the iRO Wiki was not checked) or `unverified` (no reference found).
- **Open** rows still need a decision from the maintainer.

## Comparison

| Skill | Page | Hercules / rAthena | iRO Wiki | Result |
|-|-|-|-|-|
| Bowling Bash | Knockback 1 cell, range 1 cell | Knockback 1, range is weapon range | Melee range, knockback 1 | match |
| Brandish Spear | (row removed) uaRO is 2 cells | Hercules 3, rAthena 2 | Knockback 2 | resolved: official 2 matches uaRO 2 |
| Berserk | Items and chat blocked | Items blocked, no chat check | Items, chat, skills and equipment blocked | match (iRO) |
| Concentration | Unaffected by Berserk | No interaction | No data | partial |
| Grand Cross | 1-5 hits, shared cells reduce hits | Not tested | Same | match |
| Holy Cross | 2x damage with a two-handed spear (uaRO) | The spear bonus is renewal only | Not mentioned | match |
| Devotion | Party only, icon on the devoted player | rAthena: party only, has an icon; Hercules: no icon | "Sacrifice" icon on the devoted player | match; caster icon verified on uaRO |
| Shield Reflect | Reflect a percentage of damage | Cap exists only in renewal | No cap stated | match |
| Shield Swapping | Swapping a shield cancels skills | No data | No data | unverified |
| Napalm Beat | Damage is split between targets | Split flag set | Page does not say | partial |
| Soul Strike | +5% per level against Undead | Same | Same | match |
| Amplify Magic Power | (row removed) multi-tick not included | Boost lasts until the next cast, so ticks are included | Ticks included | resolved: no change |
| Ice Wall | Can be used on MVP maps | No data | Disabled in WoE only | match |
| Magic Crasher | MATK-based, reduced by DEF | MATK used as base damage | Physical, DEF applies | partial |
| Sightrasher | 7x7, through walls | 7x7 | 7 cells, walls not stated | match |
| Storm Gust | 9x9 | 9x9 | 9x9 | match |
| Abracadabra | Anywhere except WoE | No data | Disabled in WoE only | match |
| Auto Spell | Level 1-3 bolts, Frost Diver at Level 10 | Same | Same | match |
| Create Elemental Converter | One at a time | No quantity | Not stated | unverified |
| Mind Breaker | Soft MDEF 12% per level | 12% per level | Flat 12 per level, MATK +20 | differs (Open) |
| Cart Revolution | Scales with cart weight | By weight over max | Bonus from weight | match |
| Mammonite | 100-1,000z | Same | Same | match |
| Cart Termination | 600-1,500z | Same | Same | match |
| Adrenaline Rush | Mace and Axe | Same | Axes and maces | match |
| Power Thrust, Maximum Power Thrust | 0.1% weapon break | Same | 0.1% | match |
| Melt Down | Cast 0.5-1 second, SP 50-90 | Same | No cast time, SP 50-90 | differs (Open) |
| Weapon Repair | Weapons only | Weapons only | Weapons and armor (Steel) | differs (Open) |
| Forging | Star Crumbs +5, +10, +40 | Not in the databases | +5, +10, +40 | match |
| Bio Cannibalize | 3 Flora, 2 Parasites, 1 Geographer | 6 minus the skill level | 5, 4, 3, 2, 1 by level | match |
| Bioethics | Allows learning the homunculus skills | No data | Passive skill | match |
| Rest | (row removed) stores the homunculus | Vaporize stores it | Stores it, needs 80% HP | resolved: no change |
| Mental Change | (duration removed) cooldown 10, 15, 20 minutes | Hercules duration 1, 2, 3 minutes; rAthena 1, 3, 5 | Duration 1, 3, 5 minutes, cooldown 10, 15, 20 | resolved: official duration matches uaRO |
| Plant Cultivation | Any walkable cell | No data | Blocked in WoE castles only | match |
| Aqua Benedicta | One Holy Water per cast | One | One | match |
| Twilight Alchemy | Three skills, 3 second cast, 10 second delay | Same | Not checked | emulator only |
| Mace Class Weapons | Standard speed | Priest mace ASPD equals book and rod | Same | resolved: uaRO increases it (approved prose) |
| Impositio Manus | +5 ATK per level | Same | +5, no MATK | match |
| Mace Mastery | +3 ATK per level | Same | +3, no critical | match |
| Magnus Exorcismus | Demon race and Undead element, stops while stunned | Same targets | Same, no damage while stunned | match |
| Fury / Critical Explosion | Disables natural SP recovery | Same | SP only, not HP | match |
| Asura Strike | SP not recovered for 5 minutes | Same, not saved on logout | Same, relog not stated | partial |
| Taekwon Mission | SP 10, 1 second cast, 1% reset | Same | Same | match |
| Pick Stone | Not usable while overweight | Needs weight under 50% | Same | match |
| Create Deadly Poison | SP 50, HP loss on failure | SP 50 | SP 50, loses one fifth of max HP | match |
| Enchant Deadly Poison | 60 seconds at Level 5 | Same | Same | match |
| Venom Dust | 1 Red Gemstone | Same | Same | match |
| Backstab | Delay depends on ASPD | 0.5 second after-cast delay | ASPD-based | partial; iRO used as the Original |
| Chase Walk | 10 second delay, 30 second bonus | Same | 30 second bonus, delay not stated | partial |
| Preserve | 10 minutes, not saved on logout | Same | 10 minutes, dispellable | partial |
| Arrow Vulcan | After-cast delay 2.8-3 seconds | Same | Page not found | emulator only |
| Wand of Hermode | Needs a Clown and a Gypsy | Ensemble skill | Solo skill | differs (Open) |
| Loki's Veil | Can be used on MVP maps | No data | No map data | unverified |
| Songs (buff icons) | (row removed) officially no icon | rAthena has song icons; Hercules has none | Not checked | resolved: official has icons |
| Warmth of the Sun, Moon, and Stars | Land Protector prevents damage | No data | Not checked | unverified |
| Monk, Ninja and Gunslinger SP costs and delays | As listed on the page | Hercules and rAthena agree | Not checked | emulator only |
| Teleport | Random spot on the same map | No data | Random spot; portal rule not stated | partial |
| Taekwon, Soul Linker, Star Gladiator values | As listed on the page | Same where available | Not checked | emulator only |

## Open Decisions

1. **Mind Breaker:** is the soft MDEF reduction a flat 12 per level or 12% per level?
2. **Melt Down:** if official has no cast time, "No cast time" is not a change.
3. **Weapon Repair:** if official already repairs armor, the row is not a change.
4. **Wand of Hermode:** if official is solo, "can be performed solo" is not a change.

## Prose Approved Over Numbers

Mace Class Weapons (maces attack faster), Passive Bonuses (passive ASPD for Super Novice), Angel, Help me! (official HP and SP per second), Breakthrough (official bonuses), Bio Cannibalize (new plant counts).
