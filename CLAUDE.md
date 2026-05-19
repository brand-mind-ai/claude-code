# Zacisze Website Rebuild Agent Instructions

## ⛔ MANDATORY FIRST CHECK — DO THIS BEFORE ANYTHING ELSE

**Working directory:** `/Users/macbookpro/CLAUDE CODE/Zacisze-CC/`
**GitHub repo:** `https://github.com/brand-mind-ai/claude-code/`
**Branch:** `main` — always work on main. The `zacisze-alternative` branch is an archived snapshot — do not touch it.

Run `git status` as the very first command. If the output does not show `On branch main` inside the folder above — STOP. Do not read files. Do not run any other commands. Tell Martin: "Wrong directory — please close this session and reopen it from `/Users/macbookpro/CLAUDE CODE/Zacisze-CC/`."

## Startup

Read in this order:

1. `CLAUDE.md` (this file)
2. `_HANDOVER.md`
3. `PLAN.md`

## What Went Wrong in Previous Sessions — Read This First

An earlier agent ignored the Non-Negotiables and invented:
- Entirely custom page designs with no basis in the live site
- Sections, features, and offers that do not exist on zaciszeturawa.pl
- Image pairings that replaced the original ones
- Rewritten marketing copy instead of preserving the crawled text
- Schema markup, FAQs, and CTAs that were invented, not sourced

The alternative design is parked in `zacisze-alternative` branch for reference only.

**Main is now reset to the content-crawl baseline (9d5833c).** The task is to build a faithful HTML/CSS copy of the live site using the already-crawled content.

## Non-Negotiables

1. **Do not rewrite copy.** Use the text already in `src/content/pl/pages/*.md` exactly as crawled. Fix typos only if they are clearly transcription errors.
2. **Do not invent sections, features, offers, claims, or design details.** If it is not on `zaciszeturawa.pl`, it does not go on the new site.
3. **Preserve image/page pairing.** Each page's hero and gallery images must match what the live site shows for that page. Check `sourceUrl` in the frontmatter and cross-reference.
4. **Mirror the live site's structure first.** Same sections in the same order. Redesign comes later, with Martin's explicit approval.
5. **No invented UI components.** Build the carousel, room slider, newsletter form, and date picker to match the live site's behaviour — not a reimagined version of it.

## What to Build — Version 0.1

The goal is a **faithful functional copy** of `zaciszeturawa.pl`, not a redesign:

- **Homepage**: hero with overlay date picker (arrival / departure / guests → GuestSage), USP bar, intro text, offer carousel (exactly like live), room slider (exactly like live), newsletter signup form (exactly like live), footer
- **Interior pages**: same sections as live site, same text order, same images
- **Navigation**: same items as live site header — logo, nav links, phone, book button
- **Room slider**: sideways scroll, same rooms as live site
- **Offer carousel**: same packages as live site
- **Newsletter form**: same fields as live site (email + submit, or email + name if live has that)
- **Date picker**: minimal, bottom-center on hero, passes arrivalDate + departureDate + personsCount to GuestSage

Do **not** build anything that does not exist on the live site in version 0.1.

## Stack

```
Astro 5 (static) + plain CSS + Cloudflare Pages
```

- Plain CSS only for v0.1 — no Tailwind, no GSAP, no Lenis yet
- Vanilla JS for interactive islands (slider, date picker, mobile nav)
- No React for v0.1
- No heavy animation for v0.1

## Source of Truth

| Asset | Location |
|---|---|
| Crawled content | `src/content/pl/pages/*.md` |
| URL contract | `src/data/url-map.json` |
| Contact info / nav | `src/data/site.json`, `src/data/navigation.json` |
| Booking URL builder | `src/lib/booking.ts` |
| Brand fonts/colors | `Brand assets/Colors+Fonts.txt` |
| Logo SVG | `public/zacisze-logo.svg` (create from brand kit) |
| Favicon | `public/zacisze-favicon.svg` |
| Images | `public/assets/current/hotel/` (37 files already committed) |
| Live site | `https://www.zaciszeturawa.pl/` — reference for layout, section order, image pairing |

## Image Rules

- 37 images are committed at `public/assets/current/hotel/`
- Before assigning an image to a page, verify the live site uses that image for that page (`sourceUrl` in frontmatter)
- Do not substitute images — if the correct image is not in the 37, leave a `<!-- TODO: image needed -->` comment and note it in `_HANDOVER.md`
- Do not reference images that are not in `public/assets/current/hotel/`

## Booking Rules

GuestSage base URL:
```
https://be.guestsage.com/pl/0bf0dc4c-089f-42f4-8bf0-3ea22a76ad8a
```

Minimum parameters: `arrivalDate`, `departureDate`, `personsCount`

Do not invent: `featuredRoomTypeId`, `featuredRatePlanId`, `ageCategoryId`, `discountCodeName`, `filterCategoryId` — ask Martin for these.

Payment stays inside GuestSage. The site must not process or store payment data.

## URL Rules

- Preserve all URLs in `src/data/url-map.json`
- Use relative internal links
- Deployment domain: `https://pl.zaciszeturawa.com` (temporary); final: `https://www.zaciszeturawa.pl`
- Set `ASTRO_SITE` env var in Cloudflare Pages to match the live domain

## Security

- HTTPS-only, no secrets in repo or client bundles
- CSP must allow `frame-src` for GuestSage
- Test security headers in report-only mode before enforcing

## Verification Before Claiming Done

```
npm run build       — must pass 0 errors
npm run typecheck   — must pass 0 errors
visual check in browser for every changed page
booking flow check if date picker or booking link was touched
```

## Handover

At session end, update `_HANDOVER.md` surgically. Record: focus, completed artifacts, decisions, blockers, exact next steps, files changed.
