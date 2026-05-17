# Zacisze Website Rebuild Agent Instructions

## ⛔ MANDATORY FIRST CHECK — DO THIS BEFORE ANYTHING ELSE

**Working directory:** `/Users/macbookpro/Documents/Claude/Projects/Claude Code/zaciszeturawa-pl/`
**GitHub repo:** `https://github.com/brand-mind-ai/claude-code/`
**Branch:** `main` — always work on main. Never create new branches or worktrees.

Run `git status` as the very first command. If the output does not show `On branch main` inside the folder above — STOP. Do not read files. Do not run any other commands. Tell Martin: "Wrong directory — please close this session and reopen it from `/Users/macbookpro/Documents/Claude/Projects/Claude Code/zaciszeturawa-pl/`."

## Startup

Then read in this order:

1. `CLAUDE.md`
2. `_HANDOVER.md`
3. `PLAN.md`
4. `Session Brief Template.md`


## Project Scope

This project is now about rebuilding `zaciszeturawa.pl`.

Create and edit files only inside this mounted project folder unless Martin explicitly gives a different mounted folder.

## Hard Rules

1. Verify before asserting.
2. Do not invent website text, offers, sections, room details, prices, booking IDs, design details, or images.
3. Preserve current content before rewriting anything.
4. Preserve current image/page pairing in the first production version.
5. Preserve the existing URL structure for search traffic.
6. Polish MVP is built and polished first. No language picker in MVP. EN/DE URLs are preserved in the route contract and can remain dead for about one week before the follow-up rebuild.
7. Initial deployment goes to temporary `.com`; final canonical domain is `.pl`.
8. Do not edit or overwrite existing files without checking them first.
9. Do not delete files without explicit approval.
10. Use `_HANDOVER.md` as the session continuity file and preserve its structure.
11. Use Capital Case With Spaces for user-facing planning artifacts unless a tool or convention requires otherwise.

## Source Of Truth

Planning:

```text
PLAN.md
```

Session continuity:

```text
_HANDOVER.md
```

Booking integration:

```text
guestsage-be-docs.md
```

Brand assets:

```text
Brand assets/Colors+Fonts.txt
Brand assets/zacisze-favicon.svg
Brand assets/zacisze-logo-ogg.svg
```

Current image baseline:

```text
assets/photos/
```

## Build Strategy

Chosen stack:

```text
Astro + TypeScript + Pages CMS + GitHub content + Cloudflare Pages
```

Use CSS for the baseline experience. Use Lenis for smooth scroll and GSAP ScrollTrigger for reveal/parallax, loaded only through Astro islands on pages that actually use motion. Use React only for isolated interactive islands when plain Astro/CSS is not enough.

Prefer:

- static pages
- Pages CMS-backed repository content
- reusable page layouts
- one booking URL builder
- one route inventory
- one image mapping source
- progressive animation
- browser verification after visual changes

Avoid:

- random redesigns
- invented content
- unnecessary backend services
- client-side secrets
- heavy JavaScript on every page
- component-level hardcoded page copy

## Content Rules

All visible page text should come from Pages CMS-backed Markdown or JSON files in the GitHub repository.

Initial content must be extracted from the current live site and preserved as-is. Improvements happen only after Martin approves that stage.

Do not hardcode long text inside Astro, React, or JavaScript components.

Pages CMS does not use a separate content database. It edits files directly in the GitHub repository. Local files are only a working copy of the repository source of truth.

Each content page should have:

```text
locale
translationKey
canonicalPath
sourceUrl
pageType
title
seoTitle
description
heroImage
gallery
body content
booking metadata when verified
```

## URL Rules

Treat URL preservation as a contract.

Preserve the entire existing URL structure in `url-map.json`, including EN/DE paths. The MVP may launch without EN/DE pages and without a language picker, but those URLs must remain tracked for the follow-up rebuild.

Domain policy:

```text
temporary launch domain: https://zaciszeturawa.com/
final canonical domain: https://www.zaciszeturawa.pl/
```

Use relative internal links wherever possible. Canonicals, sitemap URLs, robots behavior, and redirects must be environment-aware so the temporary `.com` launch does not become the long-term SEO canonical by accident.

Before changing routing:

1. Check `PLAN.md` URL inventory.
2. Check the latest route inventory file if one exists.
3. Check temporary `.com` vs final `.pl` domain policy.
4. Verify changed routes locally.
5. Preserve redirects for stale or legacy URLs.

Known issue:

```text
/strefa_spa currently returns 404
/spa currently returns 200 and appears in homepage navigation
```

Do not remove either from the migration map until final redirect decisions are made.

## Booking Rules

GuestSage base URL from local docs:

```text
https://be.guestsage.com/pl/0bf0dc4c-089f-42f4-8bf0-3ea22a76ad8a
```

When passing parameters, include at minimum:

```text
arrivalDate
departureDate
personsCount
```

Do not invent:

```text
featuredRoomTypeId
featuredRatePlanId
ageCategoryId
discountCodeName
filterCategoryId
```

Ask Martin for missing IDs.

The website must not process or store payment data. Payment stays inside the GuestSage iframe.

## Design Rules

- use Martin's brand kit

Hero:

- photo or video first, no massive H1, no tagline
- minimal bottom-center date picker
- header includes social icons, phone, and Google Maps link
- no heavy text overlay
- no language picker in MVP

Images:

- use current images first
- keep image/page pairing
- ask for required aspect ratios
- do not improvise substitutions

Interactions:

- smooth in-page scrolling
- room and offer sideways sliders
- section reveal from bottom
- footer parallax only if performant

## Security Rules

This site handles around USD 10K monthly in payments through an iframe, so treat security as critical.

Requirements:

- HTTPS-only deployment
- no secrets in repository or client bundles
- no custom payment handling
- strict but tested Content Security Policy
- `frame-src` allows GuestSage
- dependency audit before deployment
- preview checkout test after headers are applied

If security headers break booking, test in report-only mode before enforcing.

## Verification

Before claiming work is done:

```text
npm run build
npm run lint
npm run typecheck
route/status check for changed URLs
browser check for changed pages
booking check if booking was touched
filesystem readback for created/edited files
```

If a command does not exist yet, say so and create it during scaffold if appropriate.

## Handover

At session end, update `_HANDOVER.md` surgically.

Preserve existing frontmatter, headings, heading order, checklist style, and extra sections.

Record:

- current focus
- completed artifacts
- decisions made
- blockers
- exact next steps
- files changed
- verification performed

Use the handover skill when available.
