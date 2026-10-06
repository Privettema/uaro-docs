# Class Changes

uaRO uses the pre-renewal class system, with selected adjustments to skills and mechanics for balance and smoother gameplay. These changes preserve the classic feel while improving the overall experience.

In the tables below, Original is the official pre-renewal behavior and uaRO Changes is how uaRO differs from it.

For full reference on unmodified pre-renewal skills, you can [visit the external classic wiki](https://irowiki.org/classic/Main_Page).

<!-- Dev Note: Skill icons in the converted tables use the skill name as alt text, as the style guide requires. Screen readers may announce the name twice, so this is to be revisited. Tables not yet converted still use a blank alt="" so the decorative image is skipped. -->

## General / Shared

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Party Buff Animations | Buffs from party members play their full animation delay on every recipient. | Delay removed for party members, so the buff lands instantly with the effect and a floating skill name. The caster still sees the full animation.<br>Covers Angelus, Magnificat, Gloria, Wind Walk, Adrenaline Rush, Full Adrenaline Rush, Weapon Perfection, Over Thrust, Help Angel, and the Blessing, Increase AGI and Assumptio scrolls. |
| Reflected Damage (skills and equipment effects) | Reflects the listed percentage of damage taken, with no limit. | Reflected damage cannot exceed the max HP of the skill's user. For example, with 5,000 max HP, an attack for 10,000 reflects at most 5,000. |
| Safety Wall | Players inside can reflect damage with reflect skills. | Players inside cannot reflect damage with reflect skills. |
| ![Fury / Critical Explosion](img/skill_270.png) Fury / Critical Explosion | Natural SP recovery is disabled while in Fury. | Natural HP and SP recovery work while in Fury.<br>Does not apply to Monk or Champion. Other characters, such as those who get Fury from an item, benefit from the change. |
| ![Teleport](img/Class_Changes/al_teleport.gif) Teleport | Teleports to a random spot on the same map. | Cannot land on a map portal. |
| ![Warp Portal](img/Class_Changes/al_warp.gif) Warp Portal | Cannot be used in GvG maps or Battleground maps. | Also cannot be used on MVP maps. |

</div>



<!---------------------------------------------------------------------------->

## Status Effects
Status effects that behave differently from the official game.

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Song Buff Icons | No status icon for songs. | Song buff icons are added with the other player buffs. |
| ![Please Don't Forget Me](img/Class_Changes/dc_dontforgetme.png) Please Don't Forget Me | Not removed on death. | Removed on death. |

</div>



<!---------------------------------------------------------------------------->

## Swordsman

### Knight / Lord Knight

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Berserk](img/Class_Changes/lk_berserk.png) Berserk | No items can be used while Berserked.<br>Red body tint while active. | Fly Wing, Novice Fly Wing, and Infinite Fly Wing can be used while Berserked (all other items remain blocked).<br>The red body tint is replaced with an aura effect and a cast sound (the aura can be hidden via the Status Color Effect setting). |
| ![Concentration](img/skill_357.png) Concentration | Runs for its normal duration, unaffected by Berserk. | If active when you cast Berserk, it is refreshed and extended to 2.6x its normal duration (Level 5: 45 seconds to 117 seconds), and it ends when Berserk ends. |
| ![Bowling Bash](img/Class_Changes/kn_bowlingbash.gif) Bowling Bash | Knockback distance of 1 cell.<br>Skill range of 1 cell. | Knockback distance of 2 cells.<br>Skill range increased to 2 cells. |
| ![Brandish Spear](img/Class_Changes/kn_brandishspear.gif) Brandish Spear | Knockback distance of 3 cells. | Knockback decreased to 2 cells. |

</div>


### Crusader / Paladin

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Shield Swapping | Swapping a shield while a skill is active cancels the skill. | Swapping shields no longer interrupts the skill. Removing the shield still cancels the skill. |
| ![Devotion](img/Class_Changes/cr_devotion.gif) Devotion | Skill is usable on party members, including non-guild members.<br>No buff icon. | Cannot be placed on non-guild members outside of Battlegrounds.<br>Adds a buff icon for both the caster and the receiver while the skill is active. |
| ![Grand Cross](img/Class_Changes/cr_grandcross.gif) Grand Cross | Hits 1-5 times, depending on the position and movement of the enemy. Each monster on a single cell reduces the number of hits by 1 (to a minimum of one hit to one monster). | Mobs on the same cell take 100% of the damage from every hit. All 3 waves connect with any target in range. |
| ![Shield Reflect](img/Class_Changes/cr_reflectshield.gif) Shield Reflect | Returns a percentage of the damage dealt to you back to the enemy, including Boss-type monsters (MVPs). | Reflect damage no longer affects Boss-type monsters (MVPs). |

</div>



<!---------------------------------------------------------------------------->

## Mage

### Mage

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Napalm Beat](img/Class_Changes/mg_napalmbeat.gif) Napalm Beat | Damage is split between the targets it hits. | Full damage applies to each monster hit. |
| ![Soul Strike](img/Class_Changes/mg_soulstrike.gif) Soul Strike | 5% MATK per level. | 7% MATK per level. |

</div>



### Wizard / High Wizard

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Amplify Magic Power](img/Class_Changes/hw_magicpower.gif) Amplify Magic Power | Increases MATK for the next instance of magical damage dealt. Does not include multiple ticks. | Increases MATK for each tick of the AoE spells Meteor Storm, Storm Gust, and Lord of Vermilion. |
| ![Ice Wall](img/Class_Changes/wz_icewall.gif) Ice Wall | Cannot be used in GvG, Battlegrounds, Endless Tower, or Nidhoggur's Nest. | Additionally cannot be used on MVP maps. |
| ![Magic Crasher](img/Class_Changes/hw_magiccrasher.png) Magic Crasher | Physical attack that deals damage based on MATK instead of ATK, reduced by the target's DEF. Uses the weapon's element. | Pierces 75% of the DEF of non-player monsters and damage is doubled. Cards still apply, as does the active element on the weapon (converters/scrolls). |
| ![Sightrasher](img/Class_Changes/wz_sightrasher.gif) Sightrasher | Damages targets through obstacles and walls. | Cannot go through obstacles or walls (exception: Biolabs 3/4). |
| ![Storm Gust](img/Class_Changes/wz_stormgust.png) Storm Gust | 9x9 cell area. | 10x10 cell area. |

</div>



### Sage / Professor

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Abracadabra](img/Class_Changes/sa_abracadabra.gif) Abracadabra | Can be used anywhere excluding WoE: SE. | Can no longer be used in towns. |
| ![Auto Spell](img/Class_Changes/sa_autospell.gif) Auto Spell | Maximum Level of the spell varies from 1-3 based on the skill Level. Cast chance varies by level used. | Casts up to Level 5 bolts of all elements at skill Level 4 or higher.<br>When a bolt triggers, it casts the maximum Level you have learned, up to Level 5 (non-Linked).<br>Offers Earth Spike instead of Frost Diver: Level 1 from Auto Spell Level 2, Level 2 at Level 3, and Level 5 from Level 4 onward (always Level 5 under Sage Spirit). Frost Diver is removed from the list. |
| ![Create Elemental Converter](img/Class_Changes/sa_createcon.png) Create Elemental Converter | Crafts one converter at a time. | Mass production of up to 300 at a time. |
| ![Mind Breaker](img/Class_Changes/pf_mindbreaker.gif) Mind Breaker | Lowers the target's soft MDEF (the flat reduction from INT) by 12% per level.<br>No debuff icon. | Reduces the target's hard MDEF (the percentage reduction from equipment) everywhere except WoE and GvG castles, where it keeps reducing soft MDEF (the flat reduction from INT).<br>Adds a debuff icon for the receiver and updates stats to show the impact. |

</div>



<!---------------------------------------------------------------------------->

## Merchant

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Cart Revolution](img/Class_Changes/mc_cartrevolution.gif) Cart Revolution | Damage increases by up to 100% with cart weight (1% per 80 weight, 8,000 maximum). | Cart assumes max weight regardless of actual cart weight. |
| ![Change Cart 2](img/Class_Changes/mc_changecart.png) Change Cart 2 | | Platinum skill that adds a second level to support additional cart styles. The Platinum Skill NPC re-grants it after a skill reset, so unlocked cart styles are not lost. |
| ![Mammonite](img/Class_Changes/mc_mammonite.gif) Mammonite | Costs 100z per skill level (100-1,000z). | Maximum cost reduced to 500z while you carry a [Bag of Gold Coins](#bag-of-gold-coins).<br>Cost removed entirely once the [Avarice](#bag-of-gold-coins) platinum skill is learned. |
| ![Vending](img/Class_Changes/mc_vending.gif) Vending | | After closing your shop, you get a summary showing what sold, how much zeny you earned, and what's left in your cart. |

</div>

### Blacksmith / Whitesmith

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Fame System | Fame points are kept permanently. | Fame points decay by 5% per month. |
| Forging System | 1, 2 or 3 Star Crumbs add +5, +10 or +40 Mastery ATK to all of the weapon's attacks. | 1 Star Crumb: +20 ATK.<br>2 Star Crumbs: +40 ATK (+60 total).<br>2 Star Crumbs and an element: +60 ATK and +10% bonus damage (element).<br>3 Star Crumbs: +60 ATK and +10% neutral damage bonus.<br>Weapons forged by top-ranked smiths get an additional +10 ATK. |
| ![Adrenaline Rush](img/Class_Changes/bs_adrenaline.gif) Adrenaline Rush | Increases attack speed with Mace and Axe weapons. | One-Handed Swords can also be used. |
| ![Cart Termination](img/Class_Changes/ws_carttermination.gif) Cart Termination | Costs 600z to 1,500z. Damage depends on cart weight. | Cart assumes max weight regardless of cart weight.<br>Cost is 0z in Battlegrounds.<br>Cost reduced to 500z while you carry a [Bag of Gold Coins](#bag-of-gold-coins).<br>Cost removed entirely once the [Avarice](#bag-of-gold-coins) platinum skill is learned. |
| ![Maximum Power Thrust](img/Class_Changes/ws_overthrustmax.gif) Maximum Power Thrust | 0.1% chance to break your weapon with each hit.<br>Does not persist through logout. | No longer breaks weapons.<br>Persists through logout. |
| ![Melt Down](img/Class_Changes/ws_meltdown.gif) Melt Down | No debuff on the target.<br>Cast time of 0.5 seconds to 1 second by Level. Duration of 15 seconds to 60 seconds. SP cost of 50 to 90. Chance to break the target's weapon and armor. | No cast time. SP cost capped at 50 at any Level.<br>Duration of 25 seconds at Level 1, scaling up to 150 seconds at Level 10 to match Adrenaline Rush.<br>On hit, applies a 5 second debuff (100% rate) to PvE targets, reducing the target's DEF and the monster's ATK by 35%. Hitting again within the 5 seconds refreshes it. It procs on normal attacks and skills, and works with Cart Termination.<br>Does not work on MVPs, but affects mini-boss monsters.<br>Equipment breaking in PvP is unchanged. |
| ![Power Thrust](img/Class_Changes/bs_overthrust.gif) Power Thrust | 0.1% chance to break your weapon with each hit. | No longer breaks weapons. |
| ![Repair Weapon](img/Class_Changes/bs_repairweapon.png) Repair Weapon | Repairs broken weapons. | Also repairs broken armor, using Steel. |

</div>


### Alchemist / Creator

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Fame System | Fame points are kept permanently. | Fame points decay by 5% per month. |
| ![Bio Cannibalize](img/Class_Changes/am_cannibalize.gif) Bio Cannibalize | At most 3 Flora, 2 Parasites or 1 Geographer can be out at once (6 minus the skill level). | Increased plant count of Flora, Parasite and Geographer on non-PvP maps. |
| ![Bioethics](img/Class_Changes/am_bioethics.gif) Bioethics | Allows the Alchemist to begin learning the Homunculus skill tree. | Now an active skill, used as the interface to swap between your stored homunculi (costs 1 embryo to swap). |
| ![Call Homunculus](img/Class_Changes/am_callhomun.gif) Call Homunculus | Summons or recalls an already created Homunculus. | Calls your most recently selected homunculus. Your active choice won't show on your Bioethics storage list. |
| ![Mental Change (Lif)](img/Class_Changes/hlif_change.png) Mental Change (Lif) | Duration of 1, 2 and 3 minutes for Levels 1-3.<br>Cooldown of 10, 15 and 20 minutes. | Duration of 1, 3 and 5 minutes for Levels 1-3.<br>Cooldown of 5 minutes at every Level.<br>Effects carry through Fly Wing and Teleport for the full duration. |
| ![Plant Cultivation](img/Class_Changes/cr_cultivation.png) Plant Cultivation | Can be used on any walkable cell. | Blocked in all town buildings (inns, shops, guild halls, etc.). |
| ![Rest](img/Class_Changes/am_rest.gif) Rest | Destroys a currently created Homunculus. | Stores your active homunculus instead of destroying it. Required before you can open Bioethics to swap. |
| ![Twilight Alchemy](img/Class_Changes/am_twilight3.gif) Twilight Alchemy | Three separate skills (Twilight Alchemy 1, 2 and 3). 1 makes 200 White Potions, 2 makes 200 Slim White Potions, and 3 makes 100 Alcohol, 50 Acid Bottles and 50 Flame Bottles.<br>Cast time of 3 seconds.<br>Cooldown of 10 seconds. | One skill that brews up to 300 of any create-potion item, based on resources in your inventory.<br>Auto-crafts if only one potion type is available (no ingredient selection screen).<br>No cast time.<br>Cooldown of 2 seconds. |

</div>


### Bag of Gold Coins

Bag of Gold Coins (`#670`) lowers the Zeny cost of Mammonite and Cart Termination while it is in your inventory.
Mammonite costs at most 500z, and Cart Termination costs 500z.

- **Where to get it:** the Blacksmith Guild in Geffen (`/navi geffen_in 100/174`), for 50,000,000z.
- **Weight:** 500.
- **Restrictions:** limited to one per character. It cannot be dropped, put in your cart, traded, mailed, sold or put in guild storage. It can be kept in your personal storage.

**Avarice (Platinum Skill):** Whitesmiths can permanently trade in the bag to learn the Avarice platinum skill for an additional 200,000,000z. Avarice removes the Zeny cost of Mammonite and Cart Termination entirely for that character, with no weight penalty. It survives skill resets: the Platinum Skill NPC re-grants it automatically.


<!---------------------------------------------------------------------------->

## Acolyte
Blue Gems are sold at our [Inn Tool Dealers](dealers.md#enhanced-tool-dealer) in addition to typical locations.

### Priest / High Priest

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Mace Class Weapons | Priests suffer an ASPD penalty when using mace type weapons. | The ASPD penalty with mace type weapons is reduced. |
| ![Aqua Benedicta](img/Class_Changes/al_holywater.png) Aqua Benedicta | Crafts one Holy Water at a time. | Holy Water can be mass produced, up to 300 at a time, if you have the empty bottles. |
| ![Impositio Manus](img/Class_Changes/pr_impositio.png) Impositio Manus | Increases weapon ATK by 5 per skill level. | Also grants 1% MATK per skill level, up to 5% at Level 5.<br>No effect on WoE and GvG castle maps. |
| ![Mace Mastery](img/Class_Changes/pr_macemastery.gif) Mace Mastery | +3 ATK per level with mace type weapons. | Also gives +1 critical per level. |
| ![Magnus Exorcismus](img/Class_Changes/pr_magnus.gif) Magnus Exorcismus | Damages Demon race and Undead element monsters entering the area with Holy damage per wave. | Also damages Undead race monsters and Shadow and Ghost element monsters. |

</div>

### Monk / Champion

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Asura Strike](img/Class_Changes/mo_extremityfist.gif) Asura Strike | Natural SP recovery is disabled for 5 minutes after use, and relogging does not clear it. | SP regenerates normally after relogging. |
| ![Chain Crush Combo](img/Class_Changes/ch_chaincrushcombo.png) Chain Crush Combo | SP cost 4-22. | SP cost reduced to 2-11 (spirit sphere cost unchanged). |
| ![Glacier Fist](img/Class_Changes/ch_tigerfist.png) Glacier Fist | SP cost 4/6/8/10/12. | SP cost reduced to 2/3/4/5/6. |
| ![Raging Palm Strike](img/Class_Changes/ch_palmstrike.png) Raging Palm Strike | SP cost 2/4/6/8/10. | SP cost reduced to 1/2/4/6/8. |
| ![Raging Quadruple Blow](img/Class_Changes/mo_chaincombo.png) Raging Quadruple Blow | SP cost 11/12/13/14/15. | SP cost reduced to 2/4/6/8/10. |
| ![Raging Thrust](img/Class_Changes/mo_combofinish.png) Raging Thrust | SP cost 11/12/13/14/15. | SP cost reduced to 2/4/6/8/10. |

</div>



<!---------------------------------------------------------------------------->

## Thief
A selection of arrows can be found at [Inn Tool Dealers](dealers.md#enhanced-tool-dealer). Additional specialty arrows must be crafted.

### Thief
<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Pick Stone](img/Class_Changes/tf_pickstone.png) Pick Stone | Cannot be used while overweight. | Can be used while overweight. |

</div>


### Assassin / Assassin Cross
Venom Knife can be found at our [Inn Tool Dealers](dealers.md#enhanced-tool-dealer) in addition to typical locations.

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Create Deadly Poison](img/Class_Changes/asc_cdp.gif) Create Deadly Poison | SP cost 50.<br>Lose HP on failure. | SP cost 10.<br>You no longer lose HP on failure.<br>Mass production of up to 300 at a time. |
| ![Enchant Deadly Poison](img/Class_Changes/asc_edp.gif) Enchant Deadly Poison | Duration is 60 seconds.<br>Does not persist through logout. | Duration increased to 90 seconds.<br>Persists through logout. |
| ![Venom Dust](img/Class_Changes/as_venomdust.png) Venom Dust | Consumes 1 Red Gemstone. | No longer consumes a Red Gemstone. |

</div>



### Rogue / Stalker

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Backstab](img/Class_Changes/rg_backstab.gif) Backstab | Can only be used from behind the enemy. Cannot miss, and turns the target to face the caster, which prevents repeated use.<br>Cooldown of 0.5 seconds. | Can be performed like most attack skills.<br>Cooldown of 0.333 seconds. |
| ![Chase Walk](img/Class_Changes/st_chasewalk.gif) Chase Walk | After a delay of 10 seconds, it increases STR for 30 seconds. | Delay reduced to 5 seconds. |
| ![Plagiarism](img/Class_Changes/rg_plagiarism.gif) Plagiarism | Skills must be copied from another player. | The [Plagiarism Tutor](custom-npc.md#skills) lets Rogues and Stalkers copy skills for 25,000z, and refuses the trade while Preserve is active.<br>A skill you already know can be overwritten when a higher Level is offered, including with normal in-combat Plagiarism. |
| ![Preserve](img/Class_Changes/st_preserve.gif) Preserve | Duration of 10 minutes.<br>Does not persist through logout. | Infinite duration. Becomes an on/off toggle.<br>Persists through logout. |

</div>



<!---------------------------------------------------------------------------->

## Archer
A selection of arrows can be found at [Inn Tool Dealers](dealers.md#enhanced-tool-dealer). Additional specialty arrows must be crafted.

### Hunter / Sniper
Traps are sold at our [Inn Tool Dealers](dealers.md#enhanced-tool-dealer) in addition to typical locations.

No other changes to Hunter skills.

### Dancer / Gypsy & Bard / Clown (Minstrel)

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Weapon Swap | Swapping to a weapon of the same type does not cancel songs. | Swapping to a weapon of the same type cancels songs. |
| ![Arrow Vulcan](img/Class_Changes/cg_arrowvulcan.gif) Arrow Vulcan | After-cast delay of 2.8 seconds at Levels 1-5 and 3 seconds at Levels 6-10. | After-cast delay of 2 seconds. |
| ![Loki's Veil](img/Class_Changes/bd_rokisweil.gif) Loki's Veil | Can be used on MVP maps. | Cannot be used on MVP maps. |
| ![Wand of Hermode](img/Class_Changes/cg_hermode.gif) Wand of Hermode | Requires both a Clown and a Gypsy to perform. | Can be performed solo. |

</div>



<!---------------------------------------------------------------------------->
## Super Novice

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Death Count | Reaching Job Level 70 without dying gives +10 to all stats. Dying afterwards removes the bonus for good, and the death count cannot be reset. | The death count can be reset for free at [Lupita](custom-npc.md#other), south of Prontera.<br>The reset also grants a 10 second Super Novice Spirit (Super Novice and Super Baby only), long enough to swap into gear unlocked by the link. |
| Doridori | Increases SP regeneration only.<br>No status icon.<br>Stays active when you stand up. | Also increases HP regeneration.<br>Shows a status icon while active.<br>Ends when you stand up. |
| Passive Bonuses | | +2000 weight limit.<br>+10 DEX in total, granted over Job Levels 1-50.<br>Passive ASPD increase. |
| Removed Skills | Super Novices can learn Increase Agility, Blessing, Enlarge Weight Limit, Identify, Transcendence and Owl's Eye. | These six skills are removed from the skill tree. Blessing and Increase Agility are replaced by the Super Blessing platinum skill. |
| ![Angel, Help me!](img/Class_Changes/nv_helpangel.png) Angel, Help me! | Expanded Super Novice skill, not available to Super Novice. | Available as a platinum skill from the Platinum Skill NPC in the Main Office.<br>Restores HP and SP for you and your party members in a 15x15 area around you: 500 HP and 100 SP per second for 20 seconds. Cooldown of 300 seconds. |
| ![Breakthrough](img/Class_Changes/nv_breakthrough.png) Breakthrough | Expanded Super Novice skill with a maximum Level of 5. | Available as a platinum skill from the Platinum Skill NPC in the Main Office. Combines Breakthrough and Transcendence, with a maximum Level of 1.<br>ATK +50, MATK +50, Max HP +2000, Max SP +200, healing received +20%. |
| ![Super Blessing](img/Class_Changes/nv_transcendence.png) Super Blessing | | Grants the Increase AGI and Blessing statuses.<br>Does not stack with other Increase AGI or Blessing skills or scrolls. |

</div>



---

## Extended Classes
Many previously unequippable items are now accessible to Extended Classes: [see the full list](item-changes.md#extended-classes).


<!---------------------------------------------------------------------------->
### Taekwon

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Fame System | Fame points are kept permanently. | Fame points decay by 5% per month. |
| ![Taekwon Mission](img/Class_Changes/tk_mission.gif) Taekwon Mission | SP cost 10.<br>Reset chance 1%.<br>Cast time of 1 second. | SP cost 1.<br>Reset chance 5%.<br>Cast time of 0.5 seconds. |

</div>



<!---------------------------------------------------------------------------->

#### Star Gladiator

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Feeling of the Sun, Moon, and Stars](img/Class_Changes/sg_feel.gif) Feeling of the Sun, Moon, and Stars | Memorizes a map permanently for the Place of the Sun, Moon and Stars bonuses. It cannot be reset. | [Salvia](custom-npc.md#skills) resets Feeling for 500,000z. |
| ![Hatred of the Sun, Moon, and Stars](img/Class_Changes/sg_hate.gif) Hatred of the Sun, Moon, and Stars | Memorizes a monster permanently for the Target of the Sun, Moon and Stars bonuses. It cannot be reset. | [Salvia](custom-npc.md#skills) resets Hatred for 250,000z. |
| ![Miracle of the Sun, Moon, and Stars](img/Class_Changes/sj_document.gif) Miracle of the Sun, Moon, and Stars | Success rate of 0.02%. | Success rate of 0.1%. |
| ![Warmth of the Sun, Moon, and Stars](img/Class_Changes/sg_warmth.png) Warmth of the Sun, Moon, and Stars | Land Protector prevents the damage. | Land Protector does not prevent the damage. |

</div>



<!---------------------------------------------------------------------------->

#### Soul Linker

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| Max Job Level | 50 | 70. HP and SP pools stay the same as at Job Level 50. |
| Soul Link Duration (Level 5) | 5 minutes 50 seconds | 10 minutes |
| ![Eske](img/Class_Changes/sl_ske.gif) Eske | Can be used on Boss-type monsters. | Cannot be used on Boss-type monsters. |
| ![Esma](img/Class_Changes/sl_sma.gif) Esma | SP cost 8-80 for Levels 1-10. | SP cost 4-40 for Levels 1-10. |

</div>



<!---------------------------------------------------------------------------->

### Ninja 
Ninja's skill materials and ammo can are sold by our [Enhanced NPC Dealers](dealers.md#ninja-materials) in addition to their typical locations. Weapons and other gear are not sold at this NPC.

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Crimson Fire Blossom](img/Class_Changes/nj_kouenka.png) Crimson Fire Blossom | SP cost for Levels 7-10 is 30, 32, 34, 36. | SP cost for Levels 7-10 is 30. |
| ![Final Strike](img/Class_Changes/nj_issen.gif) Final Strike | SP cost for Levels 1-10 is 55-100. | SP cost for Levels 1-10 is 30-50. |
| ![Lightning Spear of Ice](img/Class_Changes/nj_hyousensou.png) Lightning Spear of Ice | SP cost for Levels 6-10 is 30, 33, 36, 39, 42. | SP cost for Levels 6-10 is 30. |
| ![Throw Huuma Shuriken](img/Class_Changes/nj_huuma.gif) Throw Huuma Shuriken | After-cast delay of 2 seconds.<br>SP cost for Levels 1-5 is 20, 25, 30, 35, 40.<br>Range of 9 cells. | After-cast delay of 1.5 seconds.<br>SP cost for Levels 1-5 is 10, 15, 20, 25, 30.<br>Range of 12 cells. |
| ![Throw Kunai](img/Class_Changes/nj_kunai.gif) Throw Kunai | After-cast delay of 1 second.<br>Range of 9 cells. | After-cast delay of 0.5 seconds.<br>Range of 12 cells. |
| ![Throw Shuriken](img/Class_Changes/nj_syuriken.gif) Throw Shuriken | Range of 9 cells. | Range of 12 cells. |
| ![Throw Zeny](img/Class_Changes/nj_zenynage.gif) Throw Zeny | After-cast delay of 5 seconds.<br>SP cost 50.<br>Full Zeny cost in WoE and Battlegrounds. | After-cast delay of 2 seconds.<br>SP cost 25.<br>Half the Zeny cost in WoE.<br>No Zeny cost in Battlegrounds. |

</div>



<!---------------------------------------------------------------------------->

### Gunslinger
Gunslinger's skill materials and ammo can are sold by our [Enhanced NPC Dealers](dealers.md#gunslinger-materials) in addition to their typical locations. Weapons and other gear are not sold at this NPC.

<div class="class-changes-table" markdown>

| Skill | Original | uaRO Changes |
|-|-|-|
| ![Adjustment](img/Class_Changes/gs_adjustment.gif) Adjustment | Cost of 2 coins.<br>SP cost 15.<br>Duration of 30 seconds. | Cost of 1 coin.<br>SP cost 10.<br>Duration of 60 seconds. |
| ![Flip the Coin](img/Class_Changes/gs_glittering.gif) Flip the Coin | Success chance of 10-30% at Levels 1-5.<br>SP cost 2. | Success chance of 100%.<br>SP cost 1. |
| ![Full Buster](img/Class_Changes/gs_fullbuster.gif) Full Buster | After-cast delay of 1.2-3 seconds at Levels 1-10.<br>SP cost of 40-65 at Levels 5-10. | Maximum after-cast delay of 2 seconds.<br>SP cost of 35 at Levels 5-10. |
| ![Increasing Accuracy](img/Class_Changes/gs_increasing.png) Increasing Accuracy | Cost of 4 coins.<br>SP cost 30. | Cost of 2 coins.<br>SP cost 15. |
| ![Madness Canceller](img/skill_504.png) Madness Canceller | Costs 4 coins and 30 SP. | Costs 2 coins and 15 SP. |
| Madness Break | | New platinum skill that cancels the Madness Canceller buff. |
| ![Rapid Shower](img/Class_Changes/gs_rapidshower.gif) Rapid Shower | After-cast delay of 1 second.<br>SP cost of 22-40 at Levels 1-10.<br>Consumes 5 bullets. | After-cast delay of 0.75 seconds.<br>SP cost of 12-20 at Levels 1-10.<br>Consumes 1 bullet at Levels 1-2, 2 at 3-4, 3 at 5-6, 4 at 7-8 and 5 at 9-10. |
| ![Triple Action](img/Class_Changes/gs_tripleaction.gif) Triple Action | SP cost 20. | SP cost 12. |

</div>



<!---------------------------------------------------------------------------->

## Adoptee

<div class="class-changes-table">
    <table>
        <thead>
            <tr>
                <th>Topic</th>
                <th>Original Behavior</th>
                <th>uaRO Changed Behavior</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Maximum Stats</td>
                <td>Adopted characters cannot increase a stat past 80 base.</td>
                <td>Increased maximum stat to 99.</td>
            </tr>
        </tbody>
    </table>
</div>

## Reporting Issues
Find an error or some item not mentioned here? Report it in [#wiki-errors on Discord](https://discord.com/channels/702960460168953946/1456450631584846011).