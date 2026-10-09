#!/usr/bin/env python3
"""Set `updated:` in the front matter of the pages whose content you changed.

The wiki shows "Last updated" under a page's title from this field (see hooks/page_meta.py). Run it once
before you open a pull request, after your edits are done. Skip it for changes that don't alter what a page says
(formatting, link or typo cleanup, renames).

Usage:
    scripts/stamp_updated.py                 # every page changed on this branch (committed or not) vs main
    scripts/stamp_updated.py docs/pets.md    # only the pages named
    scripts/stamp_updated.py --date 2026-10-08 --dry-run

Patch notes (they carry their own `date:`), the generated listings, the home page and the section hubs
(every index.md) are never stamped.
"""
import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SKIP_PREFIXES = ("patch-notes/",)
SKIP_FILES = {"all-patch-notes.md", "all-pages.md"}  # generated listings; every index.md (home, hubs) is skipped too
BASES = ("upstream/main", "origin/main", "main")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout


def changed_pages():
    base = next((b for b in BASES if git("rev-parse", "--verify", "-q", b).strip()), None)
    if base is None:
        sys.exit("No main branch found to compare against; name the pages instead.")
    fork = git("merge-base", base, "HEAD").strip()
    names = set(git("diff", "--name-only", "--diff-filter=AMR", fork).split())
    names |= set(git("ls-files", "--others", "--exclude-standard").split())
    return sorted(ROOT / n for n in names if n.startswith("docs/") and n.endswith(".md"))


def stampable(path):
    try:
        rel = path.resolve().relative_to(DOCS).as_posix()
    except ValueError:
        return False
    return (path.exists() and not rel.startswith(SKIP_PREFIXES) and rel not in SKIP_FILES
            and not rel.endswith("index.md"))


def stamp(text, date):
    """Return text with `updated: date` set in its front matter (created if the page has none)."""
    nl = "\r\n" if "\r\n" in text else "\n"
    line = f"updated: {date}"
    if text.startswith(f"---{nl}"):
        end = text.find(f"{nl}---", 3)
        if end != -1:
            front = text[3 + len(nl):end]
            if re.search(r"^updated:.*$", front, re.M):
                front = re.sub(r"^updated:.*$", line, front, flags=re.M)
            else:
                front = front + nl + line if front else line
            return f"---{nl}{front}{text[end:]}"
    return f"---{nl}{line}{nl}---{nl}{nl}{text}"


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*", help="pages to stamp (default: pages changed on this branch)")
    ap.add_argument("--date", default=datetime.date.today().isoformat(), help="YYYY-MM-DD (default: today)")
    ap.add_argument("--dry-run", action="store_true", help="list what would change without writing")
    args = ap.parse_args(argv)
    try:
        datetime.date.fromisoformat(args.date)
    except ValueError:
        sys.exit("--date must look like 2026-10-08")

    paths = [Path(f).resolve() for f in args.files] if args.files else changed_pages()
    done = 0
    for path in paths:
        if not stampable(path):
            continue
        # Read and write bytes so Windows line endings survive.
        text = path.read_bytes().decode("utf-8")
        new = stamp(text, args.date)
        if new == text:
            continue
        print(("would stamp " if args.dry_run else "stamped ") + str(path.relative_to(ROOT)))
        if not args.dry_run:
            path.write_bytes(new.encode("utf-8"))
        done += 1
    print(f"{done} page(s) {'would be ' if args.dry_run else ''}stamped with {args.date}")


if __name__ == "__main__":
    main(sys.argv[1:])
