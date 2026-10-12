"""Rank real pages above patch-note mentions in the site search.

A search for "commands" or "pets" returns the patch notes that mention the word, often many times each, ahead of the
page that is actually about it. Material's search worker reads a per-document `boost` from the search index, but
MkDocs' built-in search plugin does not write one, so this hook adds it after the build: patch-note sections get a
lower weight, and everything else keeps the default of 1.
"""
import json
from pathlib import Path

PATCH_NOTE_BOOST = 0.3


def on_post_build(config):
    index = Path(config["site_dir"]) / "search" / "search_index.json"
    if not index.exists():
        return
    data = json.loads(index.read_text(encoding="utf-8"))
    for doc in data.get("docs", []):
        if doc["location"].startswith("patch-notes/"):
            doc["boost"] = PATCH_NOTE_BOOST
    index.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
