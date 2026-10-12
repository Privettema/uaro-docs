# Cute Pet System

Tame a cute pet, keep it fed and it follows you through every adventure with a bonus in tow. Some pets can even evolve into stronger forms.

## How It Works

- **Tame it with its taming item.** Use the taming item on the monster. Every pet's taming item, and where it comes from, is on its card in [All Pets](#all-pets).
- **Keep it fed.** A hungry pet loses intimacy, and a pet that starves returns to its egg at Awkward intimacy instead of running away.
- **Its bonus depends on intimacy.** Each card lists the Loyal bonus, and the lower levels where a pet has them.
- **Evolve it at Loyal.** A pet must be at Loyal intimacy to evolve. The materials are on the pet it evolves from, under "Evolves into".
- **Switch or restyle it.** Swap to another egg with a [**Pet Incubator**](#pet-switch) (`643`), or turn a loyal pet into a permanent skin at the [Pet Stylist](#pet-stylist).

## Taming

Most taming items drop from monsters, using the official drop tables you can look up on [RateMyServer](https://ratemyserver.net/), or come from the ![Taming Gift Set](img/12105.gif) [**Taming Gift Set**](taming-gift-set.md) (`12105`). The exceptions on our server are listed on each pet's card in [All Pets](#all-pets), under "Taming item".

- **Taming items check for a valid target.** They are only used up when the target is valid.
- **Lower HP means a better chance.** The success rate doubles when the monster is under 1% HP.
- **Non-evolved pets are all in the Taming Gift Set.** Their taming items can come from it.
- **Abracadabra has the same chance as the item.** A non-evolved pet tamed with the skill has the same chance of success as its taming item. An evolved pet has a 0.01% chance through Abracadabra.

!!! warning "Bacsojin Tamed With Abracadabra"
    The **Bacsojin** you get from the Abracadabra skill **does not have any bonuses**. It is used as a costume. Evolve an **Evil Nymph** into a **Bacsojin** and the pet has all of its bonuses.

    Check that a Bacsojin comes with a bonus before you buy one.

## Feeding

Auto-feed is available for evolved pets and for pets without an evolution. The **Auto-feed** line under Food on each card in [All Pets](#all-pets) says whether a pet can be auto-fed.

To turn it on:

1. Open your pet window (`ALT+J` or right click).
2. Select the checkbox next to "Automatic feeding" at the bottom of the window. If you don't see it, that pet can't be auto-fed.

![Auto-feed option in the pet window](img/Pet_System/autofeed.png){ .wiki-screenshot }

!!! warning "Enable Auto-Feed Before You Leave"
    A pet that starves returns to its egg with intimacy at Awkward. Turn on auto-feed before you leave a pet unattended.

### Intimacy

Intimacy is how much your pet likes you. It sets which bonus you get, and a pet must reach Loyal to evolve. The maximum is 1,000.

| Level | Intimacy needed |
|---|---|
| Awkward | 1 |
| Shy | 100 |
| Neutral | 250 |
| Cordial | 750 |
| Loyal | 900 |

Every feeding raises intimacy, and the amount depends on the pet:

| Pet | Intimacy per feeding |
|---|---|
| Evolved, first tier | 40 |
| Evolved, second or final | 30 |
| Non-evolvable | 30 |
| Phreeoni (MVP, final) | 20 |
| Incubus and Succubus | 20 |

### Reaching Loyal

- **A new pet starts at Neutral.** You need 650 more intimacy to reach Loyal, about 22 feedings for a pet that gains 30 each time.
- **Feed it when it is hungry.** A pet that is already full loses intimacy when you feed it, and one that is only a little hungry gains less.
- **Hunger drops by 3 points every 60 seconds,** for all pets. Turn on [auto-feed](#feeding) and the pet feeds itself.
- **Dying costs intimacy.** Your pet loses 5 intimacy each time you die.
- **Starving returns it to its egg.** Keep it fed so it never gets there.

## Pet Switch

Use a **Pet Incubator** while a pet is out to swap directly to another pet egg.

- **Your current pet returns to its egg.** This needs 1 free inventory slot.
- **The Pet Incubator is only used when you pick an egg.** Closing the list doesn't waste it.
- **Your [Pet Stylist](#pet-stylist) skin is kept** when you switch pets.

## Pet Stylist

Talk to the **Pet Stylist** in Prontera (`/navi prontera 218/224`), directly north of the Pet Groomer, to permanently swap your pet's skin.

- **Your pet must be loyal.** Talk to the Pet Stylist with the pet out to exchange it for a skin.
- **The cost is the pet.** It returns to its egg and the egg is consumed. It is not turned back into an egg afterwards.
- **The skin is account wide.** You can apply it to any pet, and it persists through logout.
- **A Pet Incubator switch keeps the skin.** See [Pet Switch](#pet-switch).

!!! warning "Reverting to Egg"
    Returning a pet to its egg reverts it to the default appearance when it is rehatched, regardless of the skin applied. A Pet Incubator switch keeps your skin (see [Pet Switch](#pet-switch)).

## Hiding Pets

- **Mute pets.** The **Mute Pets** option in `@settings` hides all pet talk and emotes for you only. Pets still function normally and other players are unaffected.
- **Bombring event.** During the [Bombring event](auto-events.md#bombring-event), pets hide automatically and are not stored to their egg.

## All Pets

Every pet in one list, from the weakest mob to the strongest, with each evolution line kept together. **Egg ID** is the egg item you get and **Mob ID** is the monster you tame, so pets that can't be tamed show only an Egg ID. Click an ID to copy it.

<!-- PET_TABLE -->
