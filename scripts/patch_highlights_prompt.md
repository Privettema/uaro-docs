# Writing patch highlights

Every patch file starts with front matter. The `highlights` list is what the home page preview shows for the
latest patches, so write it when you add the patch:

```yaml
---
date: 2026-09-22
highlights:
  - "Scaraba Hole is now a Cat Hand destination for 19,000 zeny and joins the @mapexp rotation."
  - "The 10 item cap on monster kill drops is lifted."
---
```

Rules of thumb:
- 3 to 5 bullets, one sentence each (about 100 characters), plain language a player understands.
- Lead with what players notice most: new content, big balance changes, new commands, quality of life.
- Skip fixes, technical changes and "Important"/"Support us" boxes unless a fix is the headline.
- Use the names players use in game (item, skill, NPC and map names), and include the key number when it matters.
- Wrap each bullet in double quotes.

## Asking Claude Code to write them

Paste this after adding the patch file (replace the path):

> Read `docs/patch-notes/2026/patchesMMDDYYYY.md` and add `highlights:` front matter after the `date:` line,
> following `scripts/patch_highlights_prompt.md`. Show me the bullets before saving.

The build logs a note when one of the three newest patches has no `highlights`. In that case the preview falls
back to lines generated from the patch's own sections, which works but reads less well.
