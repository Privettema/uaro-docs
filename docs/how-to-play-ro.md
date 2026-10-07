# How to Play RO

The basics of playing Ragnarok Online, from your first character to your first job change. Read this if the game is new to you. The [Beginner Guide](beginner-guide.md) covers what is special about uaRO.

## Creating a Character

Every adventure begins at the character select screen. You choose a name, a hairstyle and starting stats, and then step into the world as a **Novice**, a blank slate with no class yet. Nothing you pick here decides what you become.

- **Stats:** STR, AGI, VIT, INT, DEX and LUK. Look up what your planned class needs before you spend points, and don't worry about a few messy stats at the start.
- **Slots:** one account holds several characters, so you can try different classes on separate characters.
- **Training Ground:** new characters begin in the [Novice Training Ground](remastered-novice-location.md), which teaches the controls and gives your first levels.

## Controls

Ragnarok Online is played mostly with the mouse, and you will pick it up within minutes. The keyboard fills in the rest: hotkeys for skills and items, and shortcuts for the main windows.

| Action | How |
|---|---|
| Move | Left-click the ground |
| Attack | Left-click a monster and your character keeps attacking until it dies |
| Pick up loot | Left-click the item on the ground |
| Talk to an NPC | Left-click the NPC |
| Use a skill or item | Press the hotkey you set in the shortcut bar (`F1`-`F9`) |
| Stats, skills, equipment | `Alt+A`, `Alt+S`, `Alt+Q` |
| Chat | Type in the chat box, or use `/` commands such as `/where` |

!!! tip
    Drag skills and consumables onto the shortcut bar so you can use them with one key press.

### Chat Channels

Besides party and guild chat, uaRO has server-wide channels that everyone can read from any map. Use them to ask for help, trade, or find a group.

- **Channels:** `#main` for general talk, `#trade` for buying and selling, and `#party` for finding or filling parties.
- **Talking:** whisper the channel as if it were a player. Type `#main` in the small whisper box on the left of the chat bar and your message in the larger box on the right, then press Enter. Everyone in the channel sees it.
- **Managing:** type `@channel` to open the channel settings, or `@channel list` to see the public ones. See [Commands](commands.md#channel-commands).

!!! note
    The `#trade` and `#party` channels have a 180 second delay between messages, so post once and wait.

## Levels and Jobs

Progress in RO is measured by two separate levels that rise as you fight. Together they decide how tough you are, how many skills you can learn and when you can change class.

- **Base level** raises your HP and SP and gives stat points to spend on STR, AGI, VIT, INT, DEX and LUK.
- **Job level** gives skill points, and is how you qualify for a job change.

Killing monsters gives both Base EXP and Job EXP. At job level 10 a Novice can become a First Class (Swordman, Mage, Archer, Acolyte, Merchant or Thief), and every later class builds on that choice. See the [Beginner Guide](beginner-guide.md#choosing-your-first-class) for first class picks, the [External Classic Wiki](https://irowiki.org/classic/Main_Page) for builds, and [Class Changes](class-changes.md) for what uaRO changed.

!!! important
    uaRO has no job changer NPC. Every job change has to be earned by completing that class's job quest, and a character's class can never be changed once chosen. Since you can always make another character, try a class out and read about it first, and ask on the [Discord](https://discord.gg/uaro-the-world-of-your-dream-702960460168953946) if you are unsure.

## The World

The world of Rune-Midgarts is split into areas of rising danger. You start in the safety of town and work outward as you grow stronger.

- **Towns** are safe. Monsters cannot enter, and you will find shops, storage and your save point there.
- **Fields** surround the towns and hold easy and medium monsters.
- **Dungeons** are harder, with stronger monsters and better drops.

Use `/where` to see your map and coordinates, `/navi <map> <x>/<y>` to be guided to a place, and `Ctrl+Tab` to open the world map.

### Traveling

You will cross the map constantly, so learn the shortcuts early. There are several ways to get around, and each suits a different situation.

- **Kafra:** save your point, store items, and teleport between major towns for a fee.
- **Warper:** [Warpra](warper-system.md) takes you to places you have unlocked.
- **Fly Wing:** teleports you to a random spot on the current map.
- **Butterfly Wing:** returns you to your save point.

## Fighting

Combat is where most of your time goes. Every monster has strengths and weaknesses, and a little knowledge goes a long way.

- Monsters have a **level**, **element** and **race**. Some skills and cards are strong against specific ones.
- **HP** is your health and **SP** pays for skills. If your HP reaches 0 you die, lose a little EXP and return to your save point.
- Sit down with `Insert` to recover HP and SP faster. On uaRO, sitting restores 3% of your maximum HP and SP every 1.5 seconds when you haven't been hit, see [Increased Natural Recovery](improvements.md#increased-natural-recovery).
- Keep potions on your hotkeys and check your weight: over 50% you stop recovering naturally, and over 90% you can't attack or use skills.

!!! warning
    Some monsters are **aggressive** and attack you when you walk close, while others only fight back. Check a new map before you wander in at a low level.

## Items and Money

Loot is the heart of the game. Monsters drop items that you sell, use, or keep to make your character stronger, and Zeny is how it all gets paid for.

- **Zeny** is the currency. Sell loot to NPCs, or to other players through vending and trading.
- **Equipment** has slots for cards. A card adds a bonus to the item it is socketed into, and cards drop from monsters at a very low rate.
- **Storage:** Kafra storage is shared by all characters on your account.
- **Consumables:** carry healing potions, Fly Wings and Butterfly Wings, and restock when you return to town.

## Parties and Guilds

RO is at its best with company. Playing with others levels you faster, lets you tackle harder content and makes the world feel alive.

- **Party:** up to 12 players who share EXP and loot, and each extra member raises the EXP everyone earns (see the [Beginner Guide](beginner-guide.md#party-exp-bonus)). Use `/organize` to create one.
- **Guild:** a long-term group with its own chat, storage and emblem. Guilds also take part in [War of Emperium](woe.md).
- **PvP:** fight other players in the [PvP Arena](pvp-arena.md), or join team matches in [Battlegrounds](battlegrounds.md) to earn Valor Badges. Use `@bg` to join the queue from anywhere.
- **Trading:** right-click a player and choose trade, or open a vending shop with a Merchant.

## uaRO Essentials

uaRO is a classic pre-renewal server at x5 base rates (x7.5 on weekends), with a handful of custom systems that make the long road to max level friendlier. The [Beginner Guide](beginner-guide.md) goes into the rest, but these are the ones to know on day one.

- **Autoloot:** turn on `@autoloot` and set what to pick up with `@lootconfig`. You no longer walk to every drop, which saves time on every kill. See [Commands](commands.md#lootconfig-advanced-autoloot-system).
- **Poring Coins:** most monsters have a 5% chance to drop one. They sell well to players and buy useful things such as Field Manual 100%, a Gym Pass for more carry weight, and quest headgears. See [Poring Coin System](poring-coins-system.md).
- **Main Office:** the hub for Poring Coin exchanges, costumes and stat and skill resets. See [Main Office](main-office.md).
- **Rodex mail:** send tradeable items to your other characters from anywhere, so you can restock or offload loot without walking back to town. See [Quality of Life](improvements.md#rodex-mail-system).
- **Server time:** type `@time` to see the server's clock and whether it is day or night. Events and weekend rates run on server time, so it is the quickest way to know what is active. `@rates` shows the current rates and `@commands` lists everything else. See [Commands](commands.md#system-commands).

## Things to Do

Once you have a few levels, there is plenty to try.

- **Instances:** party dungeons with their own rewards. See the [Instance Guide](instance-guide.md).
- **Events:** automatic events run through the day. See [Auto Events](auto-events.md).
- **Pets:** tame monsters and keep them at your side. See the [Cute Pet System](pet-system.md).
- **Mini games:** try your luck at the [Comodo Casino](comodo-casino.md) or [Hugel Mini Games](hugel-mini-game.md).
- **War of Emperium:** join a guild and fight for castles. See [War of Emperium](woe.md).

## Tips for Your First Day

The first few hours decide how comfortable the rest of the game feels. These habits will save you time and Zeny.

- Finish the Novice Training Ground quests for free supplies and EXP.
- Do your [Repeatable Quests](repeatable-quests.md) and [Hunting Missions](hunting-mission.md), which are among the quickest ways to level early on.
- Don't sell items you don't recognize before you look them up.
- Don't worry about builds yet. The Reset Girl in the [Main Office](main-office.md) resets your stats, skills, or both, and the first reset of each type is free, so you can learn the game first and plan later.
- Rest at an [inn](inns.md): for 10,000z it fully restores HP and SP and gives Blessing and Increase AGI for 10 minutes.
- Ask in Discord when you're stuck.

## Where to Go Next

- [Beginner Guide](beginner-guide.md): uaRO's features, a short class overview and a quick route to level 60.
- [Commands](commands.md): every in-game command.
- [QOL Improvements](improvements.md): what uaRO changed.
- [FAQ](faq.md) and [Troubleshooting](troubleshooting.md).

## Resources

These sites are mostly accurate for uaRO, so use them to look things up and plan.

- [uaRO Discord](https://discord.gg/uaro-the-world-of-your-dream-702960460168953946): ask questions, find player-made guides, and reach staff.
- [RateMyServer](https://ratemyserver.net/): a database of items, monsters, skills and quests.
- [Rocalc](https://rocalc.com/): a calculator for comparing builds and equipment.
- [Skillsim](https://skills.irowiki.org): plan your skill tree.
- [External Classic Wiki](https://irowiki.org/classic/Main_Page): game mechanics, quests and builds for every class. Use the "classic" pages, since the regular version of that wiki covers Renewal.
