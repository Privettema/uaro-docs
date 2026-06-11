# AGENTS.md

## Project Overview

This repository contains the official uaRO documentation website built with MkDocs.

The documentation is written in English and documents server-specific functionality, mechanics, activities, commands, systems, and gameplay features.

## Primary Objective

When changelog updates are provided:

1. Analyze the changelog.
2. Identify affected documentation pages.
3. Update existing documentation whenever possible.
4. Create new pages only when no suitable page exists.

## Documentation Rules

* Documentation language is English.
* Preserve existing writing style and formatting.
* Keep content concise and practical.
* Prefer updating existing sections over creating duplicate content.
* Keep navigation structure consistent.

## uaRO-Specific Rules

* This documentation is for uaRO only.
* Do not use information from official Ragnarok Online servers.
* Do not use information from other private servers.
* Do not assume Hercules or rAthena behavior unless explicitly confirmed.
* Only document information explicitly confirmed by:

  * changelog
  * existing documentation
  * repository content

## Change Processing

Before editing:

1. Search the repository for related content.
2. Identify all potentially affected pages.
3. Report planned changes.

When editing:

* Update existing tables when possible.
* Preserve internal links.
* Preserve images and media references.
* Preserve Markdown formatting conventions already used in the page.

## Validation

After changes:

Run:

mkdocs build

Report:

* Files modified
* Summary of changes
* Open questions
* Potential documentation gaps

## Forbidden Actions

Do not:

* Modify GitHub workflows
* Modify deployment configuration
* Modify CSS files
* Modify JavaScript files
* Modify mkdocs.yml unless navigation changes are required
* Delete pages without explicit instruction

## Changelog Updates

When a changelog is provided:

1. Analyze the changelog.
2. Map changes to documentation pages.
3. Apply updates.
4. Generate a summary of all modifications.
5. Highlight any ambiguous items requiring human review.