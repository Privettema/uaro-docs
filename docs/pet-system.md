# Cute Pet System

<!--TODO: Add intro flavor text -->

!!! tip "Mute Pets"
    A **Mute Pets** option in `@settings` hides all pet talk and emotes for you only.
    Pets still function normally and other players are unaffected.

!!! warning "Remember to enable auto-feed before leaving your pet unattended!"

!!! tip "Bombring Event"
    During the [Bombring event](auto-events.md#bombring-event), pets hide automatically
    and are not stored to their egg.

## Feeding
Automatic feeding (Auto-feed) is available for evolved pets or pets without an evolution. Pets that starve will return to their egg with intimacy at Awkward, instead of running away.

To enable auto-feed:

1. Open your pet window (`ALT+J` or right click)
2. At the bottom of the window, select the checkbox next to "Automatic feeding". If you don't see the auto-feed option, this pet cannot be auto-fed.

![Autofeed Hyegun](img/Pet_System/autofeed.png)

| Type | Feeding |
|---|---|
| Evolvable Pet | Only manual. Example: Poring evolves into Mastering, so it does not have auto-feed. |
| Evolved Pet | Can be auto-fed. Example: Angeling is an evolved pet, so it can use auto-feed. |
| Pet without Evolution | Can be auto-fed. Example: Incubus does not have an evolution tree, so it can use auto-feed. |



### Exceptions
| Pet | Type | Feeding |
|---|---|---|
| Leaf Cat | Evolvable | Auto-feed Available |
| Miyabi Doll | Evolvable | Auto-feed Available |
| Civil Servant | Evolvable | Auto-feed Available |



!!! Intimacy
    - HungerDecrement: 3 (all)
    - OwnerDeathDecrement: 5 (all)

    FeedIncrements:

    - Evolved (1st tier)         = 40
    - Evolved (2nd or final)     = 30
    - Evolved (3rd and final)    = 20
    - Non-evolvable              = 30

    Exceptions:

    - Phreeoni (MVP, final)      = 20
    - Incubus / Succubus         = 20

!!! note
    Pet Capture Rates

    - Lower HP of the mob, higher chance of success (2x success rate @ <1% HP).
    - All Non-evolved pet taming items are within Taming Gift Set.
    - Taming Non-evolved pet via AbraCadabra skill have same chance of success as taming items.
    - All Evolved pets have a 0.01% chance of being taming via AbraCadabra skill.

!!! warning
    The pet **Bacsojin**, which was tamed using the skill Abracadabra, **does not have any bonuses**.

    This pet is used as a costume.If you evolve the pet **Evil Nymph** into a **Bacsojin**, the pet **will have all the bonuses.**

    **Please be mindful when buying this pet. Check if it comes with a bonus!**


---

## Taming Items

The vast majority of taming items drop from monsters according to the RMS database or from
![Taming Gift Set](img/12105.gif) [**Taming Gift Set**](taming-gift-set.md). The exceptions for our server are
listed on each pet's entry in [All Pets](#all-pets), under "Taming item".

!!! note
    Taming items now check for use on a valid target before disappearing.

---

## Pet Switch

Use a **Pet Incubator** while a pet is out to swap directly to another pet egg.

!!! info "How It Works"
    - Your current pet returns to its egg. This requires **1 free inventory slot**.
    - The Pet Incubator is only consumed when you select an egg. Closing the list does not waste it.
    - Your [Pet Stylist](#pet-stylist) skin is kept when switching pets.

---

## Pet Stylist

Talk to the **Pet Stylist** NPC, located in **Prontera** `/navi prontera 218/224` — directly north of the Pet Groomer — to permanently swap your pet's skin.

!!! info "How It Works"
    - Requires a fully **loyal** pet.
    - With the pet out, talk to the **Pet Stylist** to exchange your loyal pet in for a permanent skin swap.
      The only cost is the pet itself — it is returned to its egg and the egg is consumed. It will not be
      turned back into egg form at any time afterwards.
    - The unlocked skin is permanently available **account wide** and can be applied to any pet.
    - The skin persists through logout.
    - The applied skin is kept when you switch pets with a Pet Incubator (see [Pet Switch](#pet-switch)).

!!! warning "Reverting to Egg"
    Returning a pet to egg form — regardless of the skin applied — will revert it to the default
    appearance when the pet is rehatched. Switching pets with a Pet Incubator keeps your applied skin
    (see [Pet Switch](#pet-switch)).

---

## Pet Evolution

A pet must be at Loyal intimacy to evolve. The materials for each evolution are on the evolved pet's entry in
[All Pets](#all-pets), under "Evolves from".

---

## All Pets

Every pet in one list. **Mob ID** is the monster you tame; **Egg ID** is the egg item you get. Pets without a food
listed eat Pet Food (`537`{ .copy }). Evolved pets list the bonus at each intimacy level.

<!-- PET_TABLE -->
