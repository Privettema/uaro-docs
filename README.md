# uaro-docs

Documentation wiki for **uaRO: World of Your Dream**, published at https://wiki.uaro.net. It is built with
[MkDocs](https://www.mkdocs.org/) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).

## Spotted a mistake?

Tell us in the **Wiki Errors** channel on the uaRO Discord, or open an issue or pull request here. For a small fix
(a typo, a wrong number), you can edit the file directly on GitHub and open a pull request from there.

## What is in this repo

| Path | What it holds |
|---|---|
| `docs/` | Every page, written in Markdown. `docs/img/` holds the images |
| `docs/patch-notes/YYYY/` | One file per patch. The listings and the home page preview are generated from these |
| `mkdocs.yml` | Site settings, the navigation (`nav:`) and the page redirects |
| `docs/dev/` | Editor pages, including the [style guide](docs/dev/style-guide.md) |
| `hooks/` | Build-time Python hooks (A-Z page list, patch notes, 404 suggestions, descriptions, dates, lazy images) |
| `overrides/` | Theme template overrides, such as the 404 page |
| `scripts/` | Helper scripts: `serve.sh`, `lint_style.py`, `stamp_updated.py`, `link_health.py` |

## Run the site locally

You need Python 3. From the repository root:

```bash
python3 -m venv mkdocs-venv
source mkdocs-venv/bin/activate
pip install -r requirements.txt
```

Start a local server, which rebuilds when you save a page:

```bash
scripts/serve.sh
```

It prints the address to open (the port depends on the checkout, so several copies can run side by side). Plain
`mkdocs serve` also works and uses http://127.0.0.1:8000/. The server only watches `docs/` and `mkdocs.yml`, so restart
it after changing `hooks/` or `overrides/`.

Before opening a pull request, run a strict build. It must finish with no warnings or errors:

```bash
mkdocs build --strict
```

## Making changes

- **Follow the [style guide](docs/dev/style-guide.md)** for page structure, admonitions, images, tables, links and
  writing conventions. Edit an existing page rather than creating a duplicate, and keep its tone and formatting.
- **Check your page:** `python3 scripts/lint_style.py docs/your-page-name.md` flags style-guide problems. Older pages
  still have findings, so you only need to clear the ones on lines you touched.
- **Mark the page as updated:** if you changed what a page says, run `python3 scripts/stamp_updated.py` to set its
  `updated:` date, shown as "Last updated" under the title. Skip it for typo, formatting or link-only changes.
- **Check links and images:** after changing links or images, run `python3 scripts/link_health.py` to find missing alt
  text, orphaned pages and unreferenced images. Add `--check external` to test outside links too (slower).
- **Add a page:** create `docs/your-page-name.md` (lowercase, words joined with hyphens), start it with a single
  `# Title`, and add it to `nav:` in `mkdocs.yml`. The first sentence under the title becomes the page's search and
  link-preview description (or set `description:` in the front matter).
- **Rename or move a page:** fix every link to it, and add an entry under `redirect_maps` in `mkdocs.yml` so the old
  address keeps working. Changing only the letter case of a name needs no redirect.
- **Images:** put them in `docs/img/` and give each one alt text, for example `![Poring](img/1002.gif)`.
- **Callouts:** use admonitions (`!!! note "Title"`, followed by an indented body).
- **Patch notes:** add one new file under `docs/patch-notes/YYYY/` with front matter that starts with `date: YYYY-MM-DD`
  (add `hotfix: true` for hotfixes) and a `highlights:` list of 3 to 5 short, player-facing bullets. See
  `scripts/patch_highlights_prompt.md`. Do not edit `docs/All_Patch_Notes.md` or the yearly pages by hand; they are
  generated. A new year needs a copy of `docs/patch-notes/YYYY/index.md`.
- **Only write confirmed information:** from a changelog, the existing documentation or this repository. Do not copy
  details from official servers or other private servers.

## Pull requests

Small pull requests are easier to review and merge. Aim for one topic per pull request, such as one page, one patch
note or one fix. Describe what changed and why in the pull request, and confirm that `mkdocs build --strict` passes.
The pull request template has a short checklist.

Merging into `main` publishes the site automatically.
