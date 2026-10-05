#!/usr/bin/env python3
"""Check wiki pages against the mechanical rules in docs/dev/style-guide.md.

Usage:
    python3 scripts/lint_style.py                 # every page under docs/
    python3 scripts/lint_style.py docs/Foo.md ... # only the files named

Exits 1 if anything is flagged. End a line with `<!-- style-ignore -->` to skip it.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
IGNORE = "style-ignore"
MAX_TABLE_LINE = 120

MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
UK_WORDS = ("colour", "armour", "favour", "honour", "behaviour", "centre", "cancelled", "neighbour", "labour",
            "grey", "defence", "catalogue", "recognise", "organise", "customise", "realise", "levelling")

# (rule id, compiled pattern, message). Run against a line with code spans and HTML comments removed.
LINE_RULES = [
    ("lv", re.compile(r"\bLv\b\.?"), 'write "Level", not "Lv"'),
    ("zeny-abbrev", re.compile(r"\b\d+(?:\.\d+)?\s?[kKmM]\s?(?:[zZ]eny|z)\b"), "write the full Zeny amount, e.g. 5,000z"),
    ("zeny-word", re.compile(r"\b\d[\d,]*\s[zZ]eny\b"), "write Zeny amounts as 5,000z"),
    ("zeny-commas", re.compile(r"(?<![\d,.])\d{4,}z\b"), "add thousands separators, e.g. 25,000z"),
    ("percent-space", re.compile(r"\d\s%"), 'no space before "%"'),
    ("date-iso", re.compile(r"(?<![\d-])\d{4}-\d{2}-\d{2}(?![\d-])"), "write dates as October 31, 2025"),
    ("date-slash", re.compile(r"(?<![\d/])\d{1,2}/\d{1,2}/\d{2,4}(?![\d/])"), "write dates as October 31, 2025"),
    ("date-dmy", re.compile(rf"\b\d{{1,2}}(?:st|nd|rd|th)? (?:{MONTHS})\b,? \d{{4}}"), "write dates as October 31, 2025"),
    ("uk-spelling", re.compile(rf"\b(?:{'|'.join(UK_WORDS)})\w*", re.I), "use US spelling"),
    ("empty-alt", re.compile(r"!\[\s*\]\("), "image needs alt text"),
    ("link-text", re.compile(r"\[(?:click )?here\]\(", re.I), 'link text should say where the link goes'),
]


def strip_inline(line):
    line = re.sub(r"<!--.*?-->", "", line)
    return re.sub(r"`[^`]*`", "", line)


def lint_file(path):
    findings = []
    rel = path.relative_to(ROOT)
    lines = path.read_text(encoding="utf-8").split("\n")

    def add(n, rule, msg):
        findings.append((str(rel), n, rule, msg))

    in_front = bool(lines) and lines[0].strip() == "---"
    in_code = False
    in_comment = False
    h1_lines, seen_h2, heading_reported = [], False, False
    body_start = 0
    if in_front:
        body_start = next((i + 1 for i, l in enumerate(lines[1:], 1) if l.strip() == "---"), 0)

    for i, raw in enumerate(lines):
        n = i + 1
        if i < body_start:
            continue
        if IGNORE in raw:
            continue
        if raw != raw.rstrip():
            add(n, "trailing-space", "trailing whitespace")
        if raw.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            if len(raw) > MAX_TABLE_LINE:
                add(n, "long-code", f"code line over {MAX_TABLE_LINE} characters")
            continue
        if in_comment:
            in_comment = "-->" not in raw
            continue
        if raw.lstrip().startswith("<!--") and "-->" not in raw:
            in_comment = True
            continue

        if raw.lstrip().startswith("|") and len(raw) > MAX_TABLE_LINE:
            add(n, "long-table", f"table line over {MAX_TABLE_LINE} characters")

        m = re.match(r"(#{1,6}) ", raw)
        if m:
            level = len(m.group(1))
            if level == 1:
                h1_lines.append(n)
            elif level == 2:
                seen_h2 = True
            elif level == 3 and not seen_h2 and h1_lines and not heading_reported:
                add(n, "heading-level", "first section heading should be ##, not ###")
                heading_reported = True

        text = strip_inline(raw)
        if re.search(r"<br\s*/?>", text) and not raw.lstrip().startswith("|"):
            add(n, "br", "<br> is only for line breaks inside table cells")
        for rule, pattern, msg in LINE_RULES:
            if pattern.search(text):
                add(n, rule, msg)

    if not h1_lines:
        add(1, "h1", "page has no # title")
    else:
        if len(h1_lines) > 1:
            add(h1_lines[1], "h1", "page has more than one # title")
        first = h1_lines[0]
        if first != body_start + 1:
            add(first, "h1", "the # title should be the first line of the page")
        if first < len(lines) and lines[first].strip() != "":
            add(first, "h1-blank", "leave one blank line after the # title")
        elif first + 1 < len(lines) and lines[first + 1].strip() == "":
            add(first + 1, "h1-blank", "only one blank line after the # title")
    return findings


def nav_emoji_findings():
    """Each nav page's leading emoji should be unique."""
    seen = defaultdict(list)
    for n, line in enumerate((ROOT / "mkdocs.yml").read_text(encoding="utf-8").split("\n"), 1):
        m = re.match(r"\s+- (\S+) (.+?):", line)
        if m and not m.group(1)[0].isascii():
            seen[m.group(1)].append((n, m.group(2)))
    out = []
    for emoji, uses in seen.items():
        if len(uses) > 1:
            names = ", ".join(name for _, name in uses)
            out.append(("mkdocs.yml", uses[1][0], "nav-emoji", f"{emoji} is used by more than one page: {names}"))
    return out


def main(argv):
    if argv:
        paths = [Path(a).resolve() for a in argv]
    else:
        paths = sorted(p for p in DOCS.rglob("*.md"))
    findings = []
    for p in paths:
        findings += lint_file(p)
    if not argv:
        findings += nav_emoji_findings()
    for f, n, rule, msg in findings:
        print(f"{f}:{n}: [{rule}] {msg}")
    files = len({f for f, *_ in findings})
    print(f"\n{len(findings)} finding(s) in {files} file(s), {len(paths)} checked.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
