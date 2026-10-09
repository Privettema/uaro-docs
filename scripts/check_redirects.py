#!/usr/bin/env python3
"""Check that every page URL from an older version of the site still resolves in the current build.

For each Markdown page that existed at the base revision it works out the URL the page had then, and looks in the
built site (default `site/`, from `mkdocs build`) for a page or a redirect there. A redirect's target must exist too.
Paths are matched with their exact letter case, as on the live site (GitHub Pages is case-sensitive), even when the
checkout is on a case-insensitive filesystem such as macOS. An old URL that differs from a current page only in letter
case (`/FAQ/` for `/faq/`) has no file, because it could not exist next to the page on macOS; the 404 page redirects
it instead, and this script counts it as resolved when the built `404.html` has that redirect.

Usage:
    mkdocs build
    python3 scripts/check_redirects.py                   # against the site before the filename rename (PR #82)
    python3 scripts/check_redirects.py --base <rev>      # against any commit or tag
    python3 scripts/check_redirects.py --site path/to/site

Exits 1 if any old URL does not resolve.
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
# Last commit on main before the lowercase-hyphenated filename rename (PR #82).
DEFAULT_BASE = "98c5bdc"
REFRESH = re.compile(r'<meta[^>]+http-equiv="refresh"[^>]+content="[^"]*url=([^"]+)"', re.I)
CANONICAL = re.compile(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', re.I)


def old_pages(base):
    """Markdown pages at `base`, leaving out the editor pages under dev/ (not linked from the site)."""
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", base, "docs/"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout.splitlines()
    return [p[len("docs/"):] for p in out if p.endswith(".md") and not p.lower().startswith("docs/dev/")]


def url_of(md_path):
    """The URL path MkDocs gives a page (use_directory_urls), without a leading slash."""
    path = md_path[:-3]
    if path == "index":
        return ""
    if path.endswith("/index"):
        return path[: -len("/index")] + "/"
    return path + "/"


def exact_file(site, rel):
    """Return the real path of `rel` under `site` if it exists with exactly this letter case, else None."""
    current = site
    for part in [p for p in rel.split("/") if p]:
        try:
            names = os.listdir(current)
        except OSError:
            return None
        if part not in names:
            return None
        current = current / part
    return current


def resolve(site, url, seen=()):
    """Follow a URL to a real page. Returns (kind, detail): kind is page, redirect or missing."""
    rel = url.strip("/")
    target = exact_file(site, (rel + "/index.html") if rel else "index.html")
    if target is None:
        return "missing", "no page or redirect at this URL"
    text = target.read_text(encoding="utf-8", errors="replace")
    m = REFRESH.search(text)
    if not m:
        return "page", ""
    dest = unquote(urlparse(m.group(1).strip()).path)
    if dest.startswith("/"):
        dest_rel = dest.lstrip("/")
    else:
        dest_rel = os.path.normpath(os.path.join(rel, dest)).replace(os.sep, "/")
    if dest_rel in seen:
        return "missing", "redirect loop"
    kind, detail = resolve(site, dest_rel, seen + (rel,))
    if kind == "missing":
        return "missing", f"redirects to /{dest_rel.strip('/')}/ which {detail}"
    return "redirect", f"-> /{dest_rel.strip('/')}/"


def case_twin(site, url):
    """The current page whose URL matches `url` ignoring letter case, if any (found by walking the real names)."""
    current = site
    parts = [p for p in url.strip("/").split("/") if p]
    for part in parts:
        try:
            names = os.listdir(current)
        except OSError:
            return None
        match = next((n for n in names if n.lower() == part.lower()), None)
        if match is None:
            return None
        current = current / match
    return "/".join(current.relative_to(site).parts) + "/" if (current / "index.html").exists() else None


def main(argv):
    ap = argparse.ArgumentParser(description="Check that old page URLs still resolve.")
    ap.add_argument("--base", default=DEFAULT_BASE, help=f"commit to take the old pages from (default {DEFAULT_BASE})")
    ap.add_argument("--site", default="site", help="built site directory (default: site)")
    args = ap.parse_args(argv)

    site = (ROOT / args.site).resolve()
    if not (site / "index.html").exists():
        sys.exit(f"No built site at {site}. Run `mkdocs build` first.")
    pages = old_pages(args.base)
    case_redirect = (site / "404.html").exists() and "uaro-case-redirect" in (site / "404.html").read_text(
        encoding="utf-8", errors="replace")
    counts = {"page": 0, "redirect": 0, "case": 0, "missing": 0}
    missing = []
    for md in sorted(pages):
        url = url_of(md)
        kind, detail = resolve(site, url)
        if kind == "missing" and case_redirect and case_twin(site, url):
            kind = "case"
        counts[kind] += 1
        if kind == "missing":
            missing.append((f"/{url}", md, detail))
    print(f"{len(pages)} pages at {args.base}: {counts['page']} still there, {counts['redirect']} redirected, "
          f"{counts['case']} fixed by the 404 page (letter case), {counts['missing']} not resolving")
    for url, md, detail in missing:
        print(f"  {url}  ({md}): {detail}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
