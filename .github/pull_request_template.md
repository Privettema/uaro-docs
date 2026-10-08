## What changed and why

<!-- A sentence or two. Link the changelog, issue or Discord message if there is one. -->

## Checklist

- [ ] `mkdocs build --strict` finishes with no warnings or errors
- [ ] Only information confirmed by a changelog, the existing docs or this repo (nothing from other servers)
- [ ] Follows `docs/dev/style-guide.md`; `python3 scripts/lint_style.py` shows nothing new on the lines you changed
- [ ] New pages are in `nav:` in `mkdocs.yml`; renamed or moved pages have a `redirect_maps` entry
- [ ] Images are in `docs/img/` and have alt text; `python3 scripts/link_health.py` is clean if you changed links or images
- [ ] Patch notes: new dated file with `date:` and `highlights:`; generated pages are not edited by hand
- [ ] Kept to one topic, so it is quick to review
