#!/usr/bin/env python3
"""Report link and image problems that `mkdocs build --strict` does not catch.

Checks (all but `external` run by default; `external` needs the network and takes a while):
  alt       Images with no alt text: Markdown `![](x.png)` and HTML `<img>` with no alt attribute.
            HTML `alt=""` is treated as decorative on purpose (the event pages use it for inline icons).
  orphans   Pages that are not in the nav and that no other page links to.
  images    Files under docs/img that nothing references. A name match is crude: confirm a file is really
            unused before deleting it, since the script cannot see references built at runtime.
  external  http(s) links that fail to load. 403 and 429 are listed separately as "unsure" (sites that block bots).

Usage: scripts/link_health.py [--check alt,orphans,images,external] [--timeout 10]
Exits 1 if anything is reported, so it can run as a pre-commit hook later.
"""
import argparse
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
IMAGE_EXTENSIONS = {".png", ".gif", ".jpg", ".jpeg", ".webp", ".svg", ".ico"}
SOURCE_SUFFIXES = {".md", ".yml", ".css", ".py", ".html", ".js"}
DEFAULT_CHECKS = ("alt", "orphans", "images")
ALL_CHECKS = DEFAULT_CHECKS + ("external",)

MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)")
HTML_IMG = re.compile(r"<img\s[^>]*>", re.IGNORECASE)
MD_LINK = re.compile(r"\]\(([^)\s#]+\.md)(?:#[^)\s]*)?\)")
HREF_MD = re.compile(r'href="([^"#]+\.md)')
URL = re.compile(r"""https?://(?:[^\s<>"'()\]]|\([^\s<>"'()]*\))+""")


def pages():
    return sorted(p for p in DOCS.rglob("*.md"))


def rel(path):
    return path.relative_to(ROOT).as_posix()


def strip_code(text):
    """Drop fenced code blocks so example snippets are not mistaken for real links or images."""
    return re.sub(r"^(```|~~~).*?^\1", "", text, flags=re.MULTILINE | re.DOTALL)


def check_alt():
    findings = []
    for page in pages():
        text = strip_code(page.read_text(encoding="utf-8", errors="replace"))
        for number, line in enumerate(text.splitlines(), 1):
            for match in MD_IMAGE.finditer(line):
                if not match.group(1).strip():
                    findings.append(f"{rel(page)}: image with empty alt text: {match.group(2)} (near line {number})")
            for tag in HTML_IMG.findall(line):
                if not re.search(r"\balt\s*=", tag, re.IGNORECASE):
                    findings.append(f"{rel(page)}: <img> with no alt attribute (near line {number})")
    return findings


def nav_files():
    """Markdown files named anywhere in mkdocs.yml (the nav, redirect targets and so on)."""
    text = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    return set(re.findall(r"[\w./'()-]+\.md", text))


def check_orphans():
    in_nav = nav_files()
    linked = set()
    for page in pages():
        text = page.read_text(encoding="utf-8", errors="replace")
        for target in MD_LINK.findall(text) + HREF_MD.findall(text):
            resolved = (page.parent / unquote(target)).resolve()
            if resolved.is_file():
                linked.add(resolved)
    findings = []
    for page in pages():
        relative = page.relative_to(DOCS).as_posix()
        if relative in in_nav or page.resolve() in linked or relative.startswith("patch-notes/"):
            continue
        findings.append(f"{rel(page)}: not in the nav and not linked from any page")
    return findings


def source_text():
    """Every file that could reference an image, joined into one string for a cheap name search."""
    chunks = []
    for folder in (DOCS, ROOT / "overrides", ROOT / "hooks", ROOT / "scripts"):
        if not folder.is_dir():
            continue
        for path in folder.rglob("*"):
            if path.is_file() and path.suffix in SOURCE_SUFFIXES:
                chunks.append(path.read_text(encoding="utf-8", errors="replace"))
    chunks.append((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    return unquote("\n".join(chunks))


def check_images():
    text = source_text()
    findings = []
    for path in sorted((DOCS / "img").rglob("*")):
        if path.suffix.lower() not in IMAGE_EXTENSIONS or not path.is_file():
            continue
        if path.name not in text:
            size = path.stat().st_size / 1024
            findings.append(f"{rel(path)}: not referenced anywhere ({size:,.0f} KB)")
    return findings


def external_urls():
    urls = {}
    for page in pages():
        text = strip_code(page.read_text(encoding="utf-8", errors="replace"))
        for url in URL.findall(text):
            urls.setdefault(url.rstrip(".,;:"), rel(page))
    return urls


def ssl_context():
    """Python on macOS ships without a CA bundle; certifi (installed with mkdocs-material) fills the gap."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def probe(url, timeout, context):
    headers = {"User-Agent": "Mozilla/5.0 (uaro-docs link check)"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
                return response.status
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in (400, 403, 405, 501):
                continue  # some servers refuse HEAD; retry with GET
            return error.code
        except Exception as error:  # DNS failure, timeout, TLS error
            return str(error)
    return None


def check_external(timeout):
    urls = external_urls()
    print(f"Checking {len(urls)} external links...", file=sys.stderr)
    context = ssl_context()
    with ThreadPoolExecutor(max_workers=16) as pool:
        results = list(pool.map(lambda url: probe(url, timeout, context), urls))
    findings = []
    for (url, page), status in zip(urls.items(), results):
        if status == 200 or (isinstance(status, int) and status < 400):
            continue
        label = "unsure" if status in (403, 429) else "broken"
        findings.append(f"{page}: {label} ({status}) {url}")
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", default=",".join(DEFAULT_CHECKS), help="comma-separated: " + ", ".join(ALL_CHECKS))
    parser.add_argument("--timeout", type=int, default=10, help="seconds per external request")
    args = parser.parse_args()

    checks = [name.strip() for name in args.check.split(",") if name.strip()]
    unknown = [name for name in checks if name not in ALL_CHECKS]
    if unknown:
        parser.error(f"unknown check(s): {', '.join(unknown)}")

    total = 0
    for name in checks:
        findings = check_external(args.timeout) if name == "external" else globals()[f"check_{name}"]()
        print(f"\n== {name}: {len(findings)} finding(s)")
        for finding in findings:
            print(f"  {finding}")
        total += len(findings)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
