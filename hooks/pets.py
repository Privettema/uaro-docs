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


def _item(it, ids=True):
    """Icon, quantity, name and ID of an item, in that order, for a table cell."""
    if not it:
        return ""
    out = f"![{it['name']}](img/{it['icon']}) " if it.get("icon") else ""
    if it.get("qty"):
        out += f"{it['qty']}x "
    out += it["name"]
    if ids and it.get("id"):
        out += f"&nbsp;({_code(it['id'])})"
    return out


def _pet(p):
    out = f"![{p['name']}](img/{p['icon']}) " if p.get("icon") else ""
    return out + p["name"]


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
            mob = f"{d['mob']}&nbsp;({_code(d['id'])})" if d.get("id") else d["mob"]
            lines.append(f"Dropped by {mob}&nbsp;({d['rate']})")
        return "<br>".join(lines)
    return obj.get("source", "")


def _pet_link(name):
    """Link to a pet's block by name. A tamed pet wins over an evolved one of the same name."""
    match = [q for q in _pets if q["name"] == name]
    match.sort(key=lambda q: q.get("kind") == "evolved")
    return f"[{name}](#{_anchor(match[0])})" if match else name


def _ids(p):
    """Mob ID and Egg ID as separate lines; the header lays them out side by side."""
    ids = " / ".join(_code(i) for i in dict.fromkeys([p.get("id")] + list(p.get("alt_ids") or [])) if i)
    out = [f"Mob ID {ids}"] if ids else []
    egg = p.get("egg")
    if egg:
        out.append(f"Egg ID {_code(egg['id'])}")
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


def _line(it):
    """One item on its own line, with the icon vertically centred on the text."""
    return f'<div class="pet-item" markdown>\n\n{_item(it)}\n\n</div>'


def _materials(mats):
    return "\n\n".join(_line(m) for m in mats)


def card(p, evolves_into):
    egg = p.get("egg")
    icon = egg.get("icon") if egg else None
    if not icon or not os.path.exists(os.path.join(_docs, "img", icon)):
        icon = DEFAULT_EGG
    egg_icon = f"![{egg['name'] if egg else 'Egg'}](img/{icon}) "
    tag = f' <span class="pet-tag">{_stage(p)}</span>'
    evolved = p.get("kind") == "evolved"
    # Three independent columns, so a tall section only lengthens its own column.
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
    sources_md = "\n\n".join(_pet_link(n) for n in sources)
    from_in_taming = bool(sources) and not taming  # nothing to tame: "Evolves from" takes the taming item's place
    if from_in_taming:
        middle.append(_section("Evolves from", sources_md, "taming"))
    elif not taming and egg and _where(egg):  # not tamed, but the egg has a known source
        middle.append(_section("Egg", _where(egg), "taming"))
    else:
        if taming and egg and _where(egg):  # tamed, but the egg can also be had another way
            taming.append(f"Egg: {_where(egg)}")
        middle.append(_section("Taming item", "\n\n".join(taming) or "None", "taming"))
    auto = evolved or not evolves_into or p.get("autofeed")
    food = _line(p.get("food") or PET_FOOD) + f"\n\nAuto-feed: {'Yes' if auto else 'No'}"
    left.append(_section("Food", food, "food"))
    if not from_in_taming:
        middle.append(_section("Evolves from", sources_md or "None", "from"))
    blocks = [f'<div class="pet-evo" markdown>\n\n{_pet_link(target["name"])}\n\n{_materials(mats)}\n\n</div>'
              for target, mats in evolves_into or []]
    right.append(_section("Evolves into", "\n\n".join(blocks) or "None", "into"))
    if p.get("accessory"):
        right.append(_section("Accessory", _line(p["accessory"]), "accessory"))
    cols = "\n\n".join(f'<div class="pet-col" markdown>\n\n' + "\n\n".join(c) + "\n\n</div>"
                        for c in (left, middle, right))
    sprite = f"![{p['name']}](img/{p['icon']})" if p.get("icon") else ""
    return (f'<div class="pet" id="{_anchor(p)}" markdown>\n\n'
            f'<div class="pet-head" markdown>\n\n{egg_icon}**{p["name"]}**{tag}\n\n<div class="pet-ids" markdown>\n\n{_ids(p)}\n\n</div>\n\n</div>\n\n'
            f'<div class="pet-body" markdown>\n\n<div class="pet-sprite" markdown>\n\n{sprite}\n\n</div>\n\n'
            f'<div class="pet-sections" markdown>\n\n' + cols + "\n\n</div>\n\n</div>\n\n</div>")


def _parent(p):
    """The pet this one evolves from, or None. A tamed pet wins over an evolved one of the same name."""
    name = p.get("evolves_from")
    match = sorted((q for q in _pets if q["name"] == name), key=lambda q: q.get("kind") == "evolved")
    return match[0] if match else None


def _stage(p):
    """Non-Evolved, Evolved (1), Evolved (2) ... or Evolved (Final) when nothing evolves from it."""
    if p.get("kind") != "evolved":
        return "Non-Evolved"
    if not any(_parent(q) is p for q in _pets):
        return "Evolved (Final)"
    step, parent, seen = 1, _parent(p), {id(p)}
    while parent is not None and parent.get("kind") == "evolved" and id(parent) not in seen:
        seen.add(id(parent))
        step, parent = step + 1, _parent(parent)
    return f"Evolved ({step})"


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
