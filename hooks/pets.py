"""Build the pet tables on docs/pet-system.md from data/pets.yml.

Edit data/pets.yml to add or change a pet; never the generated tables. Each entry looks like:

    - name: Poring
      id: 1002                 # mob ID
      kind: base               # base = tamed as is, evolved = reached by evolving another pet
      icon: 1725.gif           # path under docs/img/
      taming: {id: 619, name: Unripe Apple, icon: 7821.gif, source: "Moonlight Flower with a 9% chance."}
      food: {id: 531, name: Apple Juice, icon: 531.gif}   # leave out for Pet Food (537)
      accessory: {id: 10013, name: Backpack, icon: 10013.gif}
      bonus: LUK +3, CRIT +1   # evolved pets use a map: shy / neutral / cordial / loyal
      capture: 20%
      egg: {id: 9111, name: Phreeoni Egg, icon: 9111.gif, drops: [{mob: Phreeoni, id: 1159, rate: 0.09%}]}
                               # or `source: "NPC Pascal in Old Glast Heim"` when it is not a drop
      evolves_from: Poring     # evolved pets only
      materials: [{id: 610, name: Yggdrasil Leaf, icon: 610.gif, qty: 10}]
      alt_recipes: [{from: Teddy Bear, materials: [...]}]
      draft: true              # kept in the file but not shown

Placeholders replaced at build time:
    <!-- PET_TABLE -->       one block per pet: IDs, bonus, taming item, food, accessory, evolution
"""
import logging
import os
import re

import yaml

log = logging.getLogger("mkdocs.hooks.pets")

PAGE = "pet-system.md"
DATA = os.path.join("data", "pets.yml")
DEFAULT_EGG = "Pet_System/egg-default.png"  # shown when a pet has no egg icon of its own
PET_FOOD = {"id": 537, "name": "Pet Food", "icon": "537.png"}  # default when a pet lists no food
LEVELS = (("loyal", "Loyal"), ("cordial", "Cordial"), ("neutral", "Neutral"), ("shy", "Awkward/Shy"))

_pets = []
_docs = "docs"


def _load(root):
    path = os.path.join(root, DATA)
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return [p for p in data["pets"] if not p.get("draft")]


def on_config(config):
    global _docs
    root = os.path.dirname(config["config_file_path"])
    _docs = config["docs_dir"]
    _pets[:] = _load(root)
    return config


def on_serve(server, config, builder):
    server.watch(os.path.join(os.path.dirname(config["config_file_path"]), DATA))
    return server


def _code(value):
    """An ID in code, click to copy (docs/js/copy.js)."""
    return f"`{value}`{{ .copy }}"


def _section(title, body, area):
    """`area` names the grid cell in custom.css, so a section sits in the same place on every card."""
    return f'<div class="pet-sec pet-sec-{area}" markdown>\n\n<span class="pet-label">{title}</span>\n\n{body}\n\n</div>'


def _slug(name):
    return "pet-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _anchor(p):
    """Evolved pets own the plain name, so evolution links land on them. A tamed pet with the same name gets a suffix."""
    base = _slug(p["name"])
    if p.get("kind") != "evolved" and any(q["name"] == p["name"] and q.get("kind") == "evolved" for q in _pets):
        return base + "-tamed"
    return base


def _where(obj):
    """Where an item comes from: 'Dropped by Name (`ID`) (rate)' per monster, or the plain source text."""
    if not obj:
        return ""
    if obj.get("drops"):
        lines = []
        for d in obj["drops"]:
            name = d["mob"].replace(" ", "&nbsp;").replace("-", "&#8209;")  # no break inside a name
            mob = f"{name}&nbsp;({_code(d['id'])})" if d.get("id") else name
            lines.append(f"Dropped by {mob}&nbsp;·&nbsp;{d['rate']}")
        return "<br>".join(lines)
    return obj.get("source", "")


def _pet_link(name):
    """Link to a pet's block by name. A tamed pet wins over an evolved one of the same name."""
    match = [q for q in _pets if q["name"] == name]
    match.sort(key=lambda q: q.get("kind") == "evolved")
    return f"[{name}](#{_anchor(match[0])})" if match else name


def _ids(p):
    """Egg ID and Mob ID as separate cells; the header grid puts each over the section column it belongs to."""
    ids = " / ".join(_code(i) for i in dict.fromkeys([p.get("id")] + list(p.get("alt_ids") or [])) if i)
    out = []
    egg = p.get("egg")
    if egg:
        out.append(f'<div class="pet-id pet-id-egg" markdown>\n\nEgg ID {_code(egg["id"])}\n\n</div>')
    if ids:
        out.append(f'<div class="pet-id pet-id-mob" markdown>\n\nMob ID {ids}\n\n</div>')
    return "\n\n".join(out)


def _bonus(p):
    b = p.get("bonus")
    if not isinstance(b, dict):
        return b or "None"
    loyal = b.get("loyal") or "None"
    lower = [(label, b[k]) for k, label in LEVELS[1:] if b.get(k)]
    if not lower:
        return loyal
    title = f"{lower[0][0]} bonus" if len(lower) == 1 else "Show all bonuses"
    return (f"{loyal}\n\n"
            f'<details class="pet-more" markdown>\n<summary>{title}</summary>\n\n'
            + "\n\n".join(f"**{label}:** {text}" for label, text in lower) + "\n\n</details>")


def _row(icon, alt, text):
    """One line with an icon beside its text. They are separate blocks so a wrapped name stays clear of the icon."""
    pic = f"![{alt}](img/{icon})\n\n" if icon else ""
    return f'<div class="pet-item" markdown>\n\n{pic}{text}\n\n</div>'


def _line(it):
    """An item (icon, quantity, name, ID) on its own line."""
    text = f"{it['qty']}x " if it.get("qty") else ""
    text += it["name"]
    if it.get("id"):
        text += f"&nbsp;({_code(it['id'])})"
    return _row(it.get("icon"), it["name"], text)


def _egg_icon(p):
    """The egg's own icon, or the default egg when it has none or the file is missing."""
    egg = p.get("egg")
    icon = egg.get("icon") if egg else None
    if not icon or not os.path.exists(os.path.join(_docs, "img", icon)):
        icon = DEFAULT_EGG
    return icon


def _pet_ref(name):
    """A pet by name: its egg icon and a link to its card."""
    match = sorted((q for q in _pets if q["name"] == name), key=lambda q: q.get("kind") == "evolved")
    return _row(_egg_icon(match[0]) if match else None, name, _pet_link(name))


def _materials(mats):
    """Collapsed by default. The text stays in the page, so site search still finds it."""
    n = len(mats)
    return (f'<details class="pet-more" markdown>\n<summary>Requirements ({n} item{"s" if n != 1 else ""})</summary>\n\n'
            + "\n\n".join(_line(m) for m in mats) + "\n\n</details>")


def _evolution(sources, evolves_into):
    """One section for both directions: what it evolves from, and what it evolves into with the cost."""
    parts = []
    if sources:
        parts.append('<div class="pet-sublabel">Evolves from</div>')
        parts += [_pet_ref(n) for n in sources]
    if evolves_into:
        parts.append('<div class="pet-sublabel">Evolves into</div>')
        parts += [f'<div class="pet-evo" markdown>\n\n{_pet_ref(t["name"])}\n\n{_materials(m)}\n\n</div>'
                  for t, m in evolves_into]
    return _section("Evolution", "\n\n".join(parts), "evolution") if parts else ""


def card(p, evolves_into):
    egg = p.get("egg")
    egg_icon = f"![{egg['name'] if egg else 'Egg'}](img/{_egg_icon(p)}) "
    tag = f'<span class="pet-tag">{_stage(p)}</span>'
    evolved = p.get("kind") == "evolved"
    # Three independent columns, so a tall section only lengthens its own column. Evolution is always the right one.
    left = [_section("Loyal bonus", _bonus(p), "bonus")]
    middle, right = [], []
    taming = []
    if p.get("taming"):
        taming.append(_line(p["taming"]))
        if _where(p["taming"]):
            taming.append(_where(p["taming"]))
    elif p.get("taming_text"):
        taming.append(p["taming_text"])
    if not evolved and re.fullmatch(r"[\d.,]+%", str(p.get("capture") or "")):
        taming.append(f"Capture rate: {p['capture']}")  # Event, Exchange and similar are not captured
    sources = [p["evolves_from"]] if p.get("evolves_from") else []
    sources += [a["from"] for a in p.get("alt_recipes") or []]
    if not taming and egg and _where(egg):  # not tamed, but the egg has a known source
        middle.append(_section("Egg", _where(egg), "taming"))
    elif taming or not evolved:  # an evolved pet has nothing to tame, so no empty section
        if taming and egg and _where(egg):  # tamed, but the egg can also be had another way
            taming.append(f"Egg: {_where(egg)}")
        middle.append(_section("Taming item", "\n\n".join(taming) or "None", "taming"))
    unknown = (p.get("food") or {}).get("name") == "Unknown"
    auto = "Unknown" if unknown else "Yes" if evolved or not evolves_into or p.get("autofeed") else "No"
    evo = _evolution(sources, evolves_into)
    if p.get("accessory"):  # sits under the bonus: both are what the pet gives you
        left.append(_section("Accessory", _line(p["accessory"]), "accessory"))
    food = _section("Food", _line(p.get("food") or PET_FOOD) + f"\n\nAuto-feed: {auto}", "food")
    if evo:
        middle.append(food)
        right.append(evo)
    else:  # nothing evolves either way: food takes the right column instead of leaving it blank
        right.append(food)
    cols = "\n\n".join(f'<div class="pet-col" markdown>\n\n' + "\n\n".join(c) + "\n\n</div>"
                        for c in (left, middle, right))
    sprite = f"![{p['name']}](img/{p['icon']})" if p.get("icon") else ""
    # The name is a real heading so the site search indexes each pet and links straight to its card.
    return (f'<div class="pet" markdown>\n\n'
            f'<div class="pet-head" markdown>\n\n<div class="pet-title" markdown>\n\n<h3 class="pet-name" id="{_anchor(p)}" markdown>{egg_icon}{p["name"]}</h3>\n\n{tag}\n\n</div>\n\n<div class="pet-ids" markdown>\n\n{_ids(p)}\n\n</div>\n\n</div>\n\n'
            f'<div class="pet-body" markdown>\n\n<div class="pet-sprite" markdown>\n\n{sprite}\n\n</div>\n\n'
            f'<div class="pet-sections" markdown>\n\n' + cols + "\n\n</div>\n\n</div>\n\n</div>")


def _parent(p):
    """The pet this one evolves from, or None. A tamed pet wins over an evolved one of the same name."""
    name = p.get("evolves_from")
    match = sorted((q for q in _pets if q["name"] == name), key=lambda q: q.get("kind") == "evolved")
    return match[0] if match else None


def _stage(p):
    """Base Form (tamed, evolves), No Evolution (tamed, stands alone), Evolution 1, 2 ... or Final Evolution."""
    if p.get("kind") != "evolved":
        name = p["name"].lower()
        evolves = any(_parent(q) is p or any(a["from"].lower() == name for a in q.get("alt_recipes") or [])
                      for q in _pets)
        return "Base Form" if evolves else "No Evolution"
    if not any(_parent(q) is p for q in _pets):
        return "Final Evolution"
    step, parent, seen = 1, _parent(p), {id(p)}
    while parent is not None and parent.get("kind") == "evolved" and id(parent) not in seen:
        seen.add(id(parent))
        step, parent = step + 1, _parent(parent)
    return f"Evolution {step}"


def _ordered():
    """Weakest to strongest by mob level then HP, each evolution line kept together: Poring, Mastering, Angeling.

    A line sits where its first pet sits. A pet without stats takes its weakest evolution's, else it goes last.
    """
    kids = {}
    for p in _pets:
        parent = _parent(p)
        if parent is not None:
            kids.setdefault(id(parent), []).append(p)
    none = (float("inf"), 0)

    def weight(p, seen=()):
        own = (p["level"], p.get("hp") or 0) if p.get("level") is not None else none
        if own != none or id(p) in seen:
            return own
        return min((weight(k, seen + (id(p),)) for k in kids.get(id(p), [])), default=none)

    def key(p):
        return (weight(p), p["name"].lower())

    out, seen = [], set()

    def walk(p):
        if id(p) in seen:
            return
        seen.add(id(p))
        out.append(p)
        for kid in sorted(kids.get(id(p), []), key=key):
            walk(kid)

    for root in sorted((p for p in _pets if _parent(p) is None), key=key):
        walk(root)
    out += [p for p in _pets if id(p) not in seen]  # a loop in evolves_from, should not happen
    return out


def table():
    into = {}
    for p in _pets:
        if p.get("evolves_from") and p.get("materials"):
            into.setdefault(p["evolves_from"].lower(), []).append((p, p["materials"]))
        for alt in p.get("alt_recipes") or []:
            into.setdefault(alt["from"].lower(), []).append((p, alt["materials"]))
    cards = [card(p, into.get(p["name"].lower())) for p in _ordered()]
    return '<div class="pet-list" markdown>\n\n' + "\n\n".join(cards) + "\n\n</div>"


BLOCKS = {
    "<!-- PET_TABLE -->": table,
}


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != PAGE:
        return markdown
    for marker, build in BLOCKS.items():
        if marker in markdown:
            markdown = markdown.replace(marker, build())
    return markdown
