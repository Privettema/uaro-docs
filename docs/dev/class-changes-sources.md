# Class Changes Source Comparison

A record of what each reference says about the rows on [Class Changes](../class-changes.md), so a later edit can see what was checked, what the page logs, and where the references disagree. The ranking of sources is in the [Class Changes Writing Guide](class-changes-guide.md#sources-for-original-values). Checked on October 6, 2026.

How to read it:

- **Original** and **uaRO change** are short versions of what the page says now.
- **Hercules / rAthena** is `db/pre-re` for both. They agree unless noted.
- **iRO Wiki** is iRO Wiki Classic, the official-facing reference.
- **Result** is `match`, `differs` (the references disagree with the page or each other), `partial`, `emulator only` (iRO Wiki not checked), `unverified` (no reference found) or `new` (nothing official to compare). Caveats explain choices made for readers.

## General / Shared

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Party Buff Animations | Full animation delay for every recipient | Delay removed for party members; caster still sees it | No data | No data | unverified (patch 08182026) |
| Reflected Damage | No limit | Capped at the user's max HP | Cap exists only in renewal | No cap stated | match. Caveat: which reflect sources the cap covers is not confirmed |
| Safety Wall | Players inside can reflect damage | Players inside cannot reflect | No data | No data | unverified |
| Fury / Critical Explosion | SP recovery disabled | HP and SP recover (not Monk/Champion) | Same | SP only, not HP | match |
| Teleport | Random spot on the same map | Cannot land on a map portal | No data | Random spot; portal rule not stated | partial |
| Warp Portal | Can be used on MVP maps | Cannot be used on MVP maps | No data | Not checked | unverified |

## Status Effects

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Dispell | Songs and dances cannot be dispelled | Removable once the target is outside the song area; protected inside | Hercules: songs flagged no-dispel; rAthena: no flag shown | Not checked | emulator only (patch 10062026) |
| Please Don't Forget Me | Not removed on death | Removed on death | Not removed on death | Not checked | emulator only (patch 24112025) |

## Knight / Lord Knight

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Berserk | Items and chat blocked | Fly Wings usable; chat allowed; aura instead of red tint | Items blocked; no chat check | Items, chat, skills, equipment blocked | match (iRO) |
| Concentration | Unaffected by Berserk | Refreshed and 2.6x longer when Berserk is cast; ends with Berserk | No interaction | Not stated | partial |
| Bowling Bash | Knockback 1, range 1 | Knockback 2, range 2 | Knockback 1; range is weapon range | Melee range, knockback 1 | match |

## Crusader / Paladin

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Shield Swapping | Swapping a shield cancels skills | Swapping no longer interrupts; removing still cancels | No data | No data | unverified |
| Devotion | Party only; icon on devoted player; no party list marker | No non-guild members outside BG; icon on caster too; "+" in party list | rAthena: party only, has icon; Hercules: no icon | "Sacrifice" icon on devoted player | match. Caveat: caster icon and "+" marker verified on uaRO only |
| Grand Cross | 1-5 hits; shared cells reduce hits | Shared cells take 100% of every hit; all 3 waves connect | Not tested | Same as Original | match |
| Holy Cross | No bonus with two-handed spear | 2x damage with two-handed spear | Spear bonus is renewal only | Not mentioned | match |
| Shield Reflect | Reflects, including Boss monsters | No longer affects Boss monsters | No boss exception | Not stated | partial (patch 31102025) |

## Mage and Wizard / High Wizard

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Napalm Beat | Damage split between targets | Full damage to each | Split flag set | Page does not say | partial |
| Soul Strike | 5% per level (Undead) | 7% per level (Undead scope unknown) | Same as Original | Same as Original | match. Caveat: whether 7% is Undead-only is unknown |
| Ice Wall | Usable on MVP maps | Not usable on MVP maps | No data | Disabled in WoE only | match |
| Magic Crasher | MATK-based, reduced by DEF | Pierces 75% DEF of non-player monsters, doubled damage | MATK as base damage | Physical, DEF applies | partial |
| Sightrasher | 7x7, goes through walls | Cannot pass walls or obstacles (not Biolabs 3/4) | 7x7 | 7 cells; walls not stated | match |
| Storm Gust | 9x9 | 10x10 | 9x9 | 9x9 | match |

## Sage / Professor

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Abracadabra | Anywhere except WoE | Not usable in towns | No data | Disabled in WoE only | match |
| Auto Spell | Level 1-3 bolts; Frost Diver at Level 10 | Level 5 bolts at skill Level 4+; Earth Spike replaces Frost Diver | Same as Original | Same as Original | match |
| Create Elemental Converter | One at a time | Up to 300 at a time | No quantity | Not stated | unverified |
| Mind Breaker | Lowers soft MDEF; no debuff icon | Lowers hard MDEF outside WoE/GvG castles; debuff icon | 12% per level (Hercules); rAthena has an icon | Flat 12 per level, MATK +20 | match. Caveat: the exact number is left off the page on purpose (flat vs percent unresolved). The "no debuff icon" line conflicts with rAthena and is still under review |

## Merchant

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Cart Revolution | Scales with cart weight | Treats cart as max weight | By weight over max | Bonus from weight | match |
| Change Cart 2 | (blank, new skill) | Platinum skill, second cart level | n/a | n/a | new |
| Mammonite | 100-1,000z | Max 500z with Bag of Gold Coins; free with Avarice | 100-1,000z | 100-1,000z | match |
| Vending | (blank, new) | Summary of sales after closing a shop | n/a | n/a | new |

## Blacksmith / Whitesmith

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Fame System | Fame kept permanently | Decays 5% per month | No decay | Not checked | match (patch 09102025) |
| Forging | Star Crumbs +5, +10, +40 | 1 crumb +20, 2 crumbs +40, 3 crumbs +60 and 10% neutral bonus | Not in the databases | +5, +10, +40 | match |
| Adrenaline Rush | Mace and Axe | One-Handed Swords too | Same | Axes and maces | match |
| Cart Termination | 600-1,500z; cart weight | Max weight; free in BG; 500z with Bag; free with Avarice | 600-1,500z | 600-1,500z | match |
| Maximum Power Thrust | 0.1% weapon break; not saved on logout | No breaking; saved on logout | Same | 0.1% | match |
| Melt Down | Cast 0.5-1 second, SP 50-90, no debuff | No cast time, SP 50, PvE debuff | Same as Original | No cast time, SP 50-90 | differs. Caveat: kept "No cast time" on the maintainer's call; iRO says official has none |
| Power Thrust | 0.1% weapon break | No breaking | Same | 0.1% | match |
| Repair Weapon | Weapons only | Armor too, using Steel | Weapons only | Weapons and armor (Steel) | differs. Caveat: kept because armor repair is not well known to players |

## Alchemist / Creator

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Fame System | Fame kept permanently | Decays 5% per month | No decay | Not checked | match |
| Bio Cannibalize | 3 Flora, 2 Parasites, 1 Geographer | Increased plant counts (no numbers) | 6 minus skill level | 5, 4, 3, 2, 1 by level | match. Caveat: new counts not published; prose approved |
| Bioethics | Allows learning homunculus skills | Active; swaps homunculi for 1 embryo; Rest first | No data | Passive skill | match |
| Call Homunculus | Summons or recalls | Calls the last selected homunculus | No data | Restores a vaporized one | partial |
| Mental Change | Cooldown 10, 15, 20 min; ends on warp, cooldown keeps running | Cooldown 5 min; cooldown resets when it ends from a teleport or map change | rAthena: ends on warp; durations differ (1, 2, 3 vs 1, 3, 5 min) | Duration 1, 3, 5 min, cooldown 10, 15, 20 min | match. Caveat: duration left off because official equals uaRO (patch 10062026 reversed the earlier carry-through line) |
| Plant Cultivation | Any walkable cell | Blocked in town buildings | No data | Blocked in WoE castles only | match |
| Twilight Alchemy | 3 skills; 3 second cast; 10 second delay | One skill; no cast; 2 second cooldown; up to 300 | Same as Original | Not checked | emulator only |

## Priest / High Priest

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Mace Class Weapons | Standard mace speed | Maces attack faster | Mace ASPD equals book and rod | Same | match. Caveat: no value published (maintainer request); prose approved |
| Aqua Benedicta | One per cast | Up to 300 with empty bottles | One | One | match |
| Impositio Manus | +5 ATK per level | Also +1% MATK per level; not on WoE/GvG maps | Same | +5, no MATK | match |
| Mace Mastery | +3 ATK per level | +1 critical per level too | Same | +3, no critical | match |
| Magnus Exorcismus | Demon race and Undead element; stops while stunned | Also Undead race, Shadow, Ghost; continues while stunned | Same targets | Same; no damage while stunned | match |

## Monk / Champion

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Asura Strike | No SP recovery for 5 minutes; relog does not clear | SP recovers after relog | Same; not saved on logout | Same; relog not stated | partial |
| Chain Crush Combo | SP 4-22 | SP 2-11 | Same | Not checked | emulator only |
| Glacier Fist | SP 4/6/8/10/12 | SP 2/3/4/5/6 | Same | Not checked | emulator only |
| Raging Palm Strike | SP 2/4/6/8/10 | SP 1/2/4/6/8 | Same | Not checked | emulator only |
| Raging Quadruple Blow | SP 11-15 | SP 2/4/6/8/10 | Same | Not checked | emulator only |
| Raging Thrust | SP 11-15 | SP 2/4/6/8/10 | Same | Not checked | emulator only |

## Thief, Assassin and Rogue

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Pick Stone | Not usable overweight | Usable overweight | Needs weight under 50% | Same | match |
| Create Deadly Poison | SP 50; HP loss on failure | SP 10; no HP loss; up to 300 | SP 50 | SP 50; loses 1/5 max HP | match |
| Enchant Deadly Poison | 60 seconds; not saved on logout | 90 seconds; saved on logout | Same | 60 seconds | match |
| Venom Dust | 1 Red Gemstone | No gemstone | Same | Same | match |
| Backstab | Behind only, cannot miss, ASPD-based delay | Any direction; 0.333 second cooldown | 0.5 second after-cast delay | ASPD-based | partial. Caveat: iRO ranked above emulators for the Original |
| Chase Walk | 10 second delay, 30 second bonus | 5 second delay | Same | 30 seconds; delay not stated | partial (patch 09032026) |
| Plagiarism | Copy from another player | Tutor NPC for 25,000z; overwrite with higher level | No data | Not checked | unverified |
| Preserve | 10 minutes; not saved on logout | Infinite toggle; saved on logout | Same | 10 minutes, dispellable | partial |

## Archer

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Weapon Swap | Same-type swap keeps songs | Same-type swap cancels songs | No data | Not checked | unverified (patch 30012026) |
| Arrow Vulcan | After-cast delay 2.8 / 3 seconds | 2 seconds | Same | Page not found | emulator only |
| Loki's Veil | Usable on MVP maps | Not usable on MVP maps | No data | No map data | unverified |
| Wand of Hermode | Needs Clown and Gypsy | Can be performed solo | Ensemble skill | Solo skill | differs. Caveat: kept because both emulators treat it as an ensemble |

## Super Novice

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Death Count | +10 stats if no deaths by Job Level 70; no reset | Free reset at Lupita; 10 second Spirit | Not tested | Not checked | unverified |
| Doridori | SP regen only; no icon; stays active standing | HP regen too; icon; ends on standing | State flag only | Not checked | unverified. Caveat: Original assumed on the maintainer's word |
| Passive Bonuses | (blank) | +2000 weight, +10 DEX, passive ASPD | n/a | n/a | new. Caveat: ASPD value not published |
| Removed Skills | Six skills learnable | Six skills removed | Tree lists five (not Transcendence) | Not checked | partial |
| Angel, Help me! | Expanded skill; not for Super Novice | Platinum skill; 500 HP / 100 SP per second | rAthena renewal: 20 second duration, 300 second cooldown | Not checked | partial. Caveat: official HP and SP values unknown; prose approved |
| Breakthrough | Expanded skill, max Level 5 | Platinum skill, Level 1, +50 ATK/MATK etc. | rAthena renewal: max Level 5 | Not checked | partial. Caveat: official bonuses unknown |
| Super Blessing | (blank, new) | Increase AGI and Blessing; no stacking | n/a | n/a | new |

## Taekwon, Star Gladiator and Soul Linker

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Fame (Taekwon) | Kept permanently | Decays 5% per month | No decay | Not checked | match |
| Taekwon Mission | SP 10, 1 second, 1% reset | SP 1, 0.5 second, 5% reset | Same | Same | match |
| Feeling / Hatred | Memorized permanently; cannot be reset | Salvia resets for 500,000z / 250,000z | No data | Not checked | unverified |
| Miracle | 0.02% | 0.1% | Not in the databases | Not checked | unverified (patch 12062024) |
| Warmth | Land Protector prevents damage | Land Protector does not | No data | Not checked | unverified (patch 08042026) |
| Max Job Level (Soul Linker) | 50 | 70 | Not found | Not checked | unverified (patch 12242024) |
| Soul Link Duration (Level 5) | 5 minutes 50 seconds | 10 minutes | 350 seconds for all 16 Spirit skills | Not checked | match |
| Eske | Usable on Boss monsters | Not usable on Boss monsters | No boss check found | Not checked | unverified (patch 31102025) |
| Esma | SP 8-80 | SP 4-40 | 8-80 | Not checked | match |

## Ninja

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Crimson Fire Blossom | SP 30/32/34/36 at Levels 7-10 | SP 30 | Same | Not checked | emulator only |
| Final Strike | SP 55-100 | SP 30-50 | Same | Not checked | emulator only |
| Lightning Spear of Ice | SP 30-42 at Levels 6-10 | SP 30 | Same | Not checked | emulator only |
| Throw Huuma Shuriken | Delay 2 seconds; SP 20-40; range 9 | Delay 1.5; SP 10-30; range 12 | Same | Not checked | emulator only |
| Throw Kunai | Delay 1 second; range 9 | Delay 0.5; range 12 | Same | Not checked | emulator only |
| Throw Shuriken | Range 9 | Range 12 | Same | Not checked | emulator only |
| Throw Zeny | Delay 5 seconds; SP 50; full Zeny | Delay 2; SP 25; half in WoE; none in BG | Same | Not checked | emulator only |

## Gunslinger and Adoptee

| Skill | Original | uaRO change | Hercules / rAthena | iRO Wiki | Result and caveat |
|-|-|-|-|-|-|
| Adjustment | 2 coins; SP 15; 30 seconds | 1 coin; SP 10; 60 seconds | SP 15, 30 seconds | Not checked | emulator only |
| Flip the Coin | 10-30% chance; SP 2 | 100%; SP 1 | SP 2 | Not checked | emulator only |
| Full Buster | Delay 1.2-3 seconds; SP 40-65 | Max delay 2; SP 35 | Same | Not checked | emulator only |
| Increasing Accuracy | 4 coins; SP 30 | 2 coins; SP 15 | SP 30 | Not checked | emulator only |
| Madness Canceller | 4 coins; SP 30 | 2 coins; SP 15 | SP 30 | Not checked | emulator only |
| Madness Break | (blank, new) | Platinum skill cancels the buff | n/a | n/a | new |
| Rapid Shower | Delay 1 second; SP 22-40; 5 bullets | Delay 0.75; SP 12-20; 1-5 bullets | Same | Not checked | emulator only |
| Triple Action | SP 20 | SP 12 | SP 20 | Not checked | emulator only |
| Maximum Stats (Adoptee) | 80 base | 99 | Not tested | Not checked | unverified |

## Removed or Resolved Rows

| Row | Why it is not on the page |
|-|-|
| Brandish Spear | Official knockback is 2 cells (iRO Wiki, rAthena), the same as uaRO. Only Hercules says 3. |
| Amplify Magic Power | Official already boosts every tick of the amplified spell (both emulators, iRO Wiki). |
| Rest | Official Vaporize also stores the homunculus; the uaRO difference belongs to Bioethics. |
| Reject Sword | Its only change was the reflect cap, which is covered by Reflected Damage. |
| Gospel | The status already resets on relog (Hercules). |
| Full Strip | Removed on death officially too (Hercules). |
| Song buff duration and icons | Official songs already linger after leaving the area and show icons (rAthena, maintainer). |
| Resurrect Homunculus | Not a change. |
| Soul Link Equips | A bug fix; the page said "same as the original". |

## Open Decisions

No open decisions. Mind Breaker keeps the number off the page, Melt Down keeps "No cast time", Repair Weapon keeps the armor line and Wand of Hermode keeps "can be performed solo", all on the maintainer's call (see the caveats above).

## Prose Approved Over Numbers

Mace Class Weapons (maces attack faster), Passive Bonuses (passive ASPD for Super Novice), Angel, Help me! (official HP and SP per second), Breakthrough (official bonuses), Bio Cannibalize (new plant counts).
