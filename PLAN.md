# Zacisze Website Rebuild Plan

Updated: 2026-05-17  
Scope: planning only. No production site code in this session.

## TLDR

Rebuild `zaciszeturawa.pl` as a lean static hotel website with Pages CMS-backed content, preserved URL structure, verified current content, current images first, GuestSage booking integration, and strict QA before cutover.

Stack decision: Astro + TypeScript + Pages CMS + GitHub + Cloudflare Pages. Use CSS for the baseline experience. Use Lenis for smooth scroll and GSAP ScrollTrigger for reveal/parallax, loaded only through Astro islands on pages that actually use motion. Reduced-motion preference disables Lenis and all GSAP triggers. Use React only for isolated interactive islands if a component genuinely needs it.

Why Astro: this is a content-heavy hotel site with many preserved URLs, high image weight, strict speed requirements, and a booking iframe rather than an application backend. Astro gives static output, component reuse, content collections, low JavaScript by default, and enough animation capability to match the references without turning the whole site into a heavy single-page app.

Domain plan: initial public deployment goes to `zaciszeturawa.com` as a temporary parking/preview domain. Final canonical migration target remains `zaciszeturawa.pl`. SEO, internal linking, sitemap, canonical tags, and redirects must be planned around the later `.com` to `.pl` move.

## Non-Negotiables

1. Preserve existing content first. Do not rewrite copy during the initial build.
2. Preserve current image/page pairing in version 0.1. Do not replace images without explicit approval.
3. Preserve existing URL structure for search traffic. Missing or stale URLs must be captured and mapped.
4. Polish site first. English and German URL preservation is tracked from day one, but EN/DE rebuild can follow after the Polish launch. Martin explicitly accepted old EN/DE URLs being dead for about a week.
5. Do not invent sections, features, offers, claims, or design details.
6. The MVP hero is photo-first: small navigation/header, social links, phone/maps links, and a minimal date picker at bottom center. No language picker in the MVP.
7. Booking flow opens the embedded GuestSage booking page with date parameters.
8. Build for fast load, clean code, repeated agent handoff, and controlled iteration.
9. Payment stays inside the GuestSage iframe. The Zacisze site must not process, store, log, or proxy card data.
10. Every external URL mentioned in build docs or user-facing answers must be checked before use.
11. Initial deployment domain is temporary `.com`; final canonical domain is `.pl`.

## Verified Inputs

Local project folder:

```text
/Users/macbookpro/Documents/Claude/Projects/Claude Code/zaciszeturawa-pl
```

Verified local files:

```text
_HANDOVER.md
guestsage-be-docs.md
Brand assets/Colors+Fonts.txt
Brand assets/zacisze-favicon.svg
Brand assets/zacisze-logo-ogg.svg
assets/hotel/    # 37 current image files
knowledge/decisions.md
knowledge/domain.md
knowledge/contacts.md
codex-zacisze redesign.html
Claude Code zacisze-turawa.html
Claude Code Zacisze-Redesign-Mockup-2026-04-24.html
```

Brand kit currently available:

```text
Main background: #F6F1EA
Body text: #131210
Secondary colors: #FAFAFA, #CDC0B1, #231C1A, #3c3121
Header font: Libre Baskerville
Body font: Host Grotesk
```

Booking engine currently documented:

```text
https://be.guestsage.com/pl/0bf0dc4c-089f-42f4-8bf0-3ea22a76ad8a
```

GuestSage URL parameters documented locally:

```text
arrivalDate=YYYY-MM-DD
departureDate=YYYY-MM-DD
personsCount=number
featuredRatePlanId=number
featuredRoomTypeId=number
discountCodeName=string
filterCategoryId=number/string
ageCategoryCounts=JSON-like array
```

Important rule from `guestsage-be-docs.md`: if extra booking parameters are used, include at least arrival date, departure date, and people count.

## Verified External URLs

Checked on 2026-05-17.

| URL | Status | Use |
| --- | ---: | --- |
| https://www.zaciszeturawa.pl/ | 200 | Current live site |
| https://zaciszeturawa.com/ | 200 | Temporary launch/parking domain |
| https://www.zaciszeturawa.pl/sitemap.xml | 200 | Starting URL inventory |
| https://book.zaciszeturawa.com/ | 200 | Current booking host mentioned by Martin |
| https://be.guestsage.com/pl/0bf0dc4c-089f-42f4-8bf0-3ea22a76ad8a | 200 | New booking engine |
| https://github.com/brand-mind-ai/claude-code | 200 | Target GitHub repo (confirmed 2026-05-17) |
| https://pagescms.org | 200 | Pages CMS |
| https://pagescms.org/docs/ | 200 | Pages CMS docs |
| https://pagescms.org/docs/configuration/ | 200 | `.pages.yml` configuration docs |
| https://pagescms.org/docs/configuration/content/ | 200 | Pages CMS content model docs |
| https://pagescms.org/docs/configuration/media/ | 200 | Pages CMS media docs |
| https://docs.astro.build/en/guides/content-collections/ | 200 | Astro content collections |
| https://docs.astro.build/en/guides/images/ | 200 | Astro images |
| https://docs.astro.build/en/guides/view-transitions/ | 200 | Astro view transitions |
| https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/ | 200 | Astro on Cloudflare Pages |
| https://www.lenis.dev/ | 200 | Lenis smooth-scroll docs |
| https://gsap.com/docs/v3/Plugins/ScrollTrigger/ | 200 | GSAP ScrollTrigger option |
| https://www.dangleterre.com/en | 200 | Design reference |
| https://www.odins-crow.com/ | 200 | Design reference |
| https://farmform.be/ | 200 | Design reference |
| https://hutstuf.com/ | 200 | Design reference |

## URL Inventory V0.1

Source checks:

1. `https://www.zaciszeturawa.pl/sitemap.xml` returned 67 URLs.
2. A status check over those sitemap URLs found 66 returning 200 and 1 returning 404.
3. A homepage link crawl found additional live URLs not present in the sitemap.
4. `/link?role=booking` currently redirects to `/ceny_i_rezerwacja`.

### Sitemap URLs Returning 200

Polish core and utility:

```text
/
/vouchery
/strona_glowna
/pakiety_pobytowe
/pokoje
/restauracja_
/oferta_dla_firm
/galeria
/kontakt
/ceny_i_rezerwacja
/restauracja
/konferencje
/regulamin
/praca
/polityka-prywatnosci-cookies-zaciszeturawa.pdf
```

Polish package and room detail pages:

```text
/lejdis
/wspanialy-weekend
/zawsze_mlodzi_
/rocznica_slubu
/pokoj_2os_classic
/pokoj_2os_lux
/apartament_w_domku_wolnostojacym
/pokoj_classic_z_dostawka
/pokoj_na_poddaszu
```

English:

```text
/en
/about_us
/offer
/rooms
/spa_en
/restaurant
/conferences
/gallery
/contact
/prices_and_booking
/ladies_night
/romantic_weekend
/forever_young_55
/wedding_anniversary_
/classic-room
/deluxe-room
/garden-apartment
/classic-room-extra-bed
/room-attic
/rodo
/statute
/job
```

German:

```text
/de
/uber_uns
/pakete
/raume
/spa_de
/restaurant_de
/konferenzen
/galerie
/kontakt_de
/preise_und_buchung
/ladies_de
/tolles_wochenende
/fur_immer_jung_55
/classic_zimmer
/deluxe_zimmer
/garten_apartment
/classic_zimmer_mit_extrabett
/raum_auf_dem_dachboden
/satzung
/arbeiten
```

### Sitemap URL Returning 404

```text
/strefa_spa
```

Do not delete this from the migration map. Treat it as a legacy URL that needs a redirect decision. `/spa` returns 200 and appears in current homepage navigation, so `/spa` should be treated as the likely active Polish SPA URL unless a deeper crawl proves otherwise.

### Additional Live Homepage URLs Missing From Sitemap

These returned 200 and must be included in the route audit:

```text
/spa
/atrakcje
/boze_cialo_w_zaciszu_
/opinie
/pokoj_lux_dbl
/wakacje-4-dni
/wakacje_6_dni_nad_jeziorem_turawskim_2021
/wakacje_nad_jeziorem_turawskim_2021
```

### Booking Redirect To Preserve

```text
/link?role=booking -> /ceny_i_rezerwacja
```

The new site should preserve or intentionally replace this behavior with a tested GuestSage route.

## Stack Decision

Final stack for this Codex-owned project:

```text
Astro
TypeScript
Pages CMS
GitHub repository content
Cloudflare Pages
CSS design tokens
Lenis for smooth scroll, only where loaded by Astro islands
GSAP ScrollTrigger for reveal/parallax sections, only where loaded by Astro islands
React only for isolated islands if needed
```

Rationale:

1. Astro is built for fast, content-focused sites and can output static pages with minimal client JavaScript.
2. The site has many legacy URLs and mostly editorial/marketing content, not application state.
3. Pages CMS edits files in the GitHub repository, which fits Astro content collections and JSON data cleanly.
4. The design references need high-end motion, but not a full React/Next.js runtime on every page.
5. Cloudflare Pages has a direct Astro deployment path and preview deployments.
6. GuestSage owns the payment/booking transaction inside an iframe, so a custom backend is unnecessary for MVP.

Important Pages CMS clarification:

Pages CMS does not store content in a separate database. It edits files directly in the GitHub repository. So "Pages CMS end to end" means:

```text
content source of truth = GitHub repo files edited through Pages CMS
local clone = working copy only
visible site content = rendered from CMS-managed files
components = layout and behavior only, no page body copy hardcoded
```

## Domain And SEO Plan

Temporary launch domain:

```text
https://zaciszeturawa.com/
```

Final canonical domain:

```text
https://www.zaciszeturawa.pl/
```

Verified on 2026-05-17:

```text
https://zaciszeturawa.com/ returns 200 and is Cloudflare-served.
https://www.zaciszeturawa.pl/ returns 200 and is still HotelSystems-backed.
```

Rules:

1. Build and preview publicly on `.com` first.
2. Treat `.com` as temporary, not the long-term SEO canonical.
3. Preserve all old `.pl` paths as path-only routes in `url-map.json`, for example `/pokoje`, `/spa`, `/ceny_i_rezerwacja`.
4. Internal links should be relative paths wherever possible, not hardcoded `.com` or `.pl` absolute URLs.
5. Canonical URL behavior must be environment-aware:
   - On `.com` temporary launch, either use self-canonical `.com` while `.pl` is not live, or noindex `.com` if Martin wants to avoid search indexing the temporary domain.
   - After `.pl` cutover, canonical URLs must point to `.pl`.
6. Sitemap generation must be environment-aware:
   - Temporary `.com` sitemap only if we want `.com` indexed.
   - Final `.pl` sitemap after cutover.
7. When `.pl` goes live, add permanent redirects from `.com` paths to matching `.pl` paths unless Martin wants `.com` to remain a separate brand/domain.
8. Do not publish dead EN/DE routes in the active sitemap until rebuilt.
9. The final `.pl` cutover checklist must include canonical tags, sitemap domain, robots.txt, redirects, and internal link crawl.

## Four-Day Build Plan

Assumption: 4 calendar days, multiple focused sessions per day, with user checkpoints. The build should optimize for a working Polish production site first. EN/DE URLs are captured and preserved in the route contract from day one, but their content rebuild can follow after launch.

### Day 1 - Inventory, Structure, Scaffold

Session 1: project setup and guardrails

- Confirm repo access for https://github.com/brand-mind-ai/claude-code.
- Create or verify branch naming and deployment expectations.
- Configure deployment assumptions: `.com` temporary launch first, `.pl` final canonical later.
- Add project `AGENTS.md`, `PLAN.md`, session brief template, and `_HANDOVER.md` update discipline.
- Lock stack: Astro, TypeScript, Pages CMS, GitHub content, Cloudflare Pages, CSS tokens, Lenis, GSAP ScrollTrigger, reduced-motion fallback.
- Confirm no current-code edits beyond scaffold until URL/content inventory is complete.

Session 2: full crawl and CMS-backed content extraction

- Crawl all sitemap URLs plus discovered homepage URLs.
- Extract current visible page content into structured Pages CMS-backed Markdown/JSON files in the repository.
- Preserve PL content for MVP build. Capture EN/DE URL and content inventory for the follow-up rebuild.
- Capture title, meta description, headings, body copy, buttons, internal links, and page images.
- Export a crawl report with status, canonical path, language, page type, source URL, and missing assets.

Session 3: Pages CMS model and asset inventory

- Map current page images to local asset files where possible.
- Define image naming convention without randomly replacing images.
- Identify missing, low-quality, duplicate, or unknown images.
- Add `.pages.yml` early so the content structure is Pages CMS-native from the beginning.
- Define page, room, offer, gallery, navigation, booking, and site-settings fields.
- Test Pages CMS assumptions against its documented `media` and `content` configuration model before building templates.

Day 1 exit criteria:

- Complete URL map exists.
- Current PL content exists in Pages CMS-backed Markdown/JSON.
- EN/DE URL inventory exists and is marked deferred, not forgotten.
- Asset mapping exists.
- `.pages.yml` exists and reflects the content model.
- Astro scaffold is ready or clearly queued.
- No page is redesigned before its source content is captured.

### Day 2 - Polish Site Build

Session 4: base layout and system components

- Implement global layout, header, footer, social links, phone link, maps link, SEO head, cookie/legal links.
- Implement brand fonts and colors from `Brand assets/Colors+Fonts.txt`.
- Build responsive navigation and mobile header.
- Implement smooth in-page scrolling.

Session 5: booking UX and core Polish routes

- Build minimal hero date picker at bottom center.
- Generate GuestSage URLs with `arrivalDate`, `departureDate`, and `personsCount`.
- Build `/ceny_i_rezerwacja` with GuestSage iframe.
- Add fallback direct booking link if iframe fails.
- Build Polish home, rooms, packages, SPA, restaurant, conferences, gallery, contact.

Session 6: Polish detail pages

- Build room pages.
- Build package/offer pages.
- Build legal pages and PDF links.
- Preserve current URL paths exactly.
- Add placeholder-free content only from Pages CMS-backed content files.

Day 2 exit criteria:

- Polish route set builds locally.
- Booking date picker opens the correct GuestSage URL.
- Header/footer/social/phone/maps links are present.
- No invented copy or image substitutions.

### Day 3 - Motion, CMS Editing, Polish QA

Session 7: motion layer

- Add reveal-from-bottom section animation.
- Add sideways sliders for rooms and offers.
- Add footer parallax.
- Respect reduced-motion preferences.
- Keep animations progressive: content must remain readable if JavaScript fails.

Session 8: Pages CMS editing validation

- Validate `.pages.yml` against the actual content files.
- Confirm Pages CMS can edit pages, rooms, offers, gallery, navigation, booking settings, and global settings.
- Keep canonical paths locked by default.
- Confirm uploaded media writes to the intended repository folder and public path.
- Use clear labels so Martin can edit without touching code.

Session 9: Polish QA and hardening pass

- Check all PL routes for status, broken links, missing images, layout overflow, mobile header, sliders, smooth scroll, booking URL formation, iframe behavior.
- Run build, lint, type checks, and browser QA.
- Check Lighthouse-style basics: image weight, unused JavaScript, font loading, cumulative layout shift, first viewport.

Day 3 exit criteria:

- Polish site is content-complete and visually coherent.
- Pages CMS content structure is usable and already backing the rendered site.
- Critical booking flow works.
- Known issues are listed, not hidden.

### Day 4 - SEO, Security, Deployment, EN/DE Contract

Session 10: EN/DE route contract

- Preserve all current EN/DE URL paths in `url-map.json`.
- Mark EN/DE content rebuild as post-MVP, accepted dead-window up to about one week.
- Do not add a language picker in the Polish MVP.
- Do not include dead EN/DE routes in the new sitemap until rebuilt.
- Prepare the future `translationKey` mapping so EN/DE can be added cleanly.

Session 11: SEO and redirects

- Generate sitemap.xml from route inventory.
- Add robots.txt.
- Add environment-aware canonical URLs and, later, hreflang links.
- Keep internal links relative so `.com` launch and later `.pl` move do not require content rewrites.
- Decide whether temporary `.com` should be indexed or noindexed before public launch.
- Preserve legacy URLs and redirect stale paths where needed.
- Specifically decide `/strefa_spa` to `/spa`.
- Preserve `/link?role=booking` or replace with tested equivalent.
- Prepare `.com` to `.pl` redirect plan for final domain move.

Session 12: security and performance

- Enforce HTTPS-only deployment.
- Add strict security headers suitable for static hosting and GuestSage iframe.
- Content Security Policy must explicitly allow the GuestSage frame host.
- No secrets in repo or client bundles.
- Dependency audit and update check before deploy.
- Verify no card data can be submitted to Zacisze infrastructure.
- Confirm iframe checkout works after headers are applied.

Session 13: deployment and cutover buffer

- Deploy preview from GitHub.
- Run route/status checks on preview.
- Compare preview against current URL inventory.
- Launch first on `zaciszeturawa.com`.
- Keep current `.pl` site untouched until `.com` preview/launch passes.
- Prepare rollback path: keep old vendor DNS/hosting info until final switch is confirmed.
- Cut `.pl` over only after Martin approval.
- After `.pl` cutover, verify `.com` to `.pl` redirects or noindex behavior, depending on final domain policy.

Day 4 exit criteria:

- Polish route coverage is complete.
- EN/DE route inventory and rebuild plan are complete.
- Booking flow works on deployed preview.
- SEO preservation checklist passes.
- Temporary `.com` launch behavior and final `.pl` canonical behavior are documented and tested.
- Security headers do not break GuestSage.
- Rollback path exists before DNS/domain changes.

## Proposed Repo File Structure

```text
/
  AGENTS.md
  PLAN.md
  Session Brief Template.md
  _HANDOVER.md
  .pages.yml
  package.json
  astro.config.mjs
  tsconfig.json
  public/
    assets/
      current/
        hotel/
      generated/
      icons/
      logos/
    documents/
      polityka-prywatnosci-cookies-zaciszeturawa.pdf
  src/
    content/
      pl/
        pages/
        rooms/
        offers/
      en/
        pages/
        rooms/
        offers/
      de/
        pages/
        rooms/
        offers/
    data/
      navigation.json
      socials.json
      site.json
      domains.json
      url-map.json
      redirects.json
      booking.json
      gallery.json
    layouts/
      BaseLayout.astro
      PageLayout.astro
      RoomLayout.astro
      OfferLayout.astro
      BookingLayout.astro
    components/
      booking/
        BookingDatePicker.*
        BookingIframe.astro
        BookingLink.astro
      global/
        Header.astro
        Footer.astro
        SocialLinks.astro
        SEOHead.astro
      media/
        HeroMedia.astro
        ResponsiveImage.astro
        GalleryGrid.astro
      sections/
        PageIntro.astro
        RichTextSection.astro
        ImageTextSection.astro
        RoomSlider.*
        OfferSlider.*
        RevealSection.astro
      utilities/
        SmoothAnchor.*
        MapsLink.astro
        PhoneLink.astro
    pages/
      [...slug].astro
      ceny_i_rezerwacja.astro
```

Notes:

- `public/assets/current/` stores the initial source images that match the current site.
- `public/assets/generated/` stores optimized derivatives if used.
- `src/content/{locale}/...` is the Pages CMS-backed editable content source in the GitHub repository.
- `src/data/url-map.json` is the route preservation contract.
- `src/data/domains.json` records temporary `.com` and final `.pl` domain policy.
- `src/data/redirects.json` records redirects and legacy URLs.
- `.pages.yml` exposes only safe content/media fields for Pages CMS.
- `LanguageSwitcher.astro` is deferred until EN/DE rebuild.

## Content File Contract

Each page Markdown file should use frontmatter similar to:

```yaml
locale: pl
translationKey: rooms-classic
canonicalPath: /pokoj_2os_classic
sourceUrl: https://www.zaciszeturawa.pl/pokoj_2os_classic
pageType: room
title: ""
seoTitle: ""
description: ""
status: captured
heroImage: /assets/current/hotel/example.jpg
gallery:
  - /assets/current/hotel/example.jpg
cta:
  label: REZERWUJ
  bookingMode: room
guestSage:
  featuredRoomTypeId:
  featuredRatePlanId:
```

The body content should contain the current page text exactly as extracted. Editing happens through Pages CMS, which writes to repository files. Components must not contain page body copy.

## Component Reuse Strategy

1. One route renderer for all content pages, with layout chosen by `pageType`.
2. Separate presentational components from content data.
3. Use shared `RoomSlider` and `OfferSlider` for homepage modules and listing pages.
4. Use one booking URL builder across hero date picker, room CTAs, offer CTAs, and booking page.
5. Defer `LanguageSwitcher` until EN/DE rebuild; when added, drive it by `translationKey`, not hardcoded links.
6. Use one `ResponsiveImage` or equivalent media component to avoid inconsistent image handling.
7. Animation should be component-level and opt-in, not scattered across page templates.

## Booking Engine Plan

Base:

```text
https://be.guestsage.com/{locale}/0bf0dc4c-089f-42f4-8bf0-3ea22a76ad8a
```

Offer search with dates:

```text
https://be.guestsage.com/pl/0bf0dc4c-089f-42f4-8bf0-3ea22a76ad8a/offers?arrivalDate=YYYY-MM-DD&departureDate=YYYY-MM-DD&personsCount=2
```

Implementation rules:

- Hero date picker collects check-in, check-out, and adults.
- If dates are missing, send the user to the base booking page.
- If dates are present, send to `/offers` with required parameters.
- Room and package CTAs may add `featuredRoomTypeId` or `featuredRatePlanId` only after Martin or GuestSage provides verified IDs.
- Do not invent room IDs, rate plan IDs, child age IDs, discount codes, or filters.
- Iframe page must include a direct external booking fallback link.
- Test language-specific GuestSage paths before using EN/DE booking links.

## Pages CMS Plan

Pages CMS is the editing layer from day one. It edits repository files and media directly in GitHub; there is no separate CMS database.

Planned `.pages.yml` groups:

```text
Site settings
Navigation
Polish pages
Polish rooms
Polish offers
Gallery
Redirects
Booking settings
English pages - deferred
English rooms - deferred
English offers - deferred
German pages - deferred
German rooms - deferred
German offers - deferred
```

Media plan:

```text
public/assets/current/hotel      # current site images, protected baseline
public/assets/uploads            # user-uploaded CMS images
public/documents                 # PDFs and legal documents
```

CMS safety rules:

- Current baseline images should not be renamed casually.
- New uploads go into `public/assets/uploads`.
- Page slugs/canonical paths are locked fields unless an explicit SEO task unlocks them.
- Room and offer IDs from GuestSage are editable only when verified.
- Content extraction should populate CMS-backed files immediately, before visual components are built on top.

## Security Plan

The site cannot be literally "100% secure", but the rebuild can avoid custom payment risk and use a hardened static architecture.

Security controls:

1. Static frontend only. No custom payment backend.
2. GuestSage iframe handles payment flow.
3. No card data in Zacisze forms, logs, analytics, query collectors, or APIs.
4. HTTPS-only deploy.
5. Security headers:
   - `Content-Security-Policy`
   - `X-Content-Type-Options: nosniff`
   - `Referrer-Policy`
   - `Permissions-Policy`
   - `Strict-Transport-Security` after HTTPS is confirmed
6. CSP must allow only required script, style, image, font, connect, and frame sources.
7. `frame-src` must include `https://be.guestsage.com`.
8. No unsafe inline scripts unless justified and documented.
9. Dependency audit before deployment.
10. Check generated client bundle for secrets before deployment.

Security verification:

- Booking iframe loads on preview.
- Payment step is reachable inside iframe.
- CSP report-only test before enforcing if checkout breaks.
- External links use safe attributes where needed.
- Forms, if any, are scoped and do not collect payment data.

## Performance Plan

Targets:

- Static pages.
- Minimal JavaScript by default.
- Images sized and lazy-loaded.
- Hero image/video optimized separately from galleries.
- Fonts loaded with clear fallback strategy.
- Sliders and animation libraries loaded only where used.
- Reduced-motion support.
- No heavy tracking scripts during launch unless explicitly approved.

Checks:

- Build size report.
- Lighthouse-style pass on homepage, room page, offer page, gallery, booking page.
- Mobile viewport screenshot QA.
- Slow network spot check.

## Design Implementation Rules

Use the brand kit Martin provided, not the previous mockup palette.

Hero:

- Photo/video first.
- No massive H1.
- No heavy text overlay.
- Bottom-center minimal date picker.
- Header includes social icons, phone, and Google Maps link. No language picker in MVP.

Images:

- Current image/page pairing first.
- No random substitutions.
- No 60 percent overlays.
- Ask for square/aspect-ratio-specific content before designing around missing assets.

Sections:

- No invented sections.
- Current content first.
- More photos allowed on homepage, but gallery remains its own page.
- Smooth reveal from bottom.
- Sideways sliders for rooms and offers.
- Footer parallax only if it stays performant.

## Risk Register

| Risk | Mitigation |
| --- | --- |
| Current vendor disruption | Crawl/export content early; preserve old URLs; avoid touching DNS until preview passes |
| Temporary `.com` gets treated as permanent | Use relative internal links, environment-aware canonicals/sitemaps, and final `.com` to `.pl` redirect plan |
| Sitemap incomplete | Combine sitemap, homepage links, full internal crawl, and manual checks |
| Existing sitemap has stale `/strefa_spa` | Map to `/spa` only after final crawl confirms |
| Random content drift | All visible copy comes from Markdown/JSON, not components |
| Random image drift | Page image mapping file controls image use |
| Booking URL breaks | One URL builder, direct fallback link, preview tests |
| Iframe blocked by security headers | Test CSP in report-only mode before enforcement |
| Animations hurt speed | Progressive enhancement, reduced-motion support, route-level loading |
| CMS edits break routes | Lock canonical path fields, validate route map in build |
| EN/DE URLs temporarily dead | Explicitly accepted for about one week; keep route inventory and rebuild plan so they are not forgotten |
| Four-day timeline slips | Polish production site first; EN/DE copy migration after PL acceptance |

## Verification Checklist Per Session

Every build session must finish with:

```text
npm run build
npm run lint
npm run typecheck
route/status check for changed URLs
browser screenshot check for changed templates
booking link/iframe check if booking touched
git diff review
_HANDOVER.md update
```

If a command does not exist yet, add it during scaffold or state clearly that it is not available.

## Useful Codex Skills

Use these installed skills when relevant:

```text
build-web-apps:frontend-app-builder       # actual UI/build sessions
build-web-apps:frontend-testing-debugging # rendered QA, browser checks, responsive bugs
build-web-apps:react-best-practices       # only if React islands are used
browser:browser                           # local preview and screenshot checks
handover                                  # session-end handover update
```

No extra GitHub skill is required before starting. If a later session needs one, use `skill-installer` to inspect the candidate first and install only after the benefit is concrete.

## Immediate Next Session Brief

Goal: connect the repo, create the Pages CMS-backed content structure, and run full route/content inventory without redesigning pages.

Tasks:

1. Open target GitHub repo locally or clone it into the mounted workspace.
2. Confirm existing repo contents before editing.
3. Add or verify `.pages.yml` and the intended Pages CMS content/media folders.
4. Add `domains.json` or equivalent config for temporary `.com` and final `.pl` behavior.
5. Create route inventory from sitemap, homepage links, and a full internal crawl.
6. Extract current Polish page content into Pages CMS-backed files.
7. Capture EN/DE URL/content inventory as deferred rebuild scope.
8. Map current page images to repository media paths.
9. Create first `url-map.json`, `redirects.json`, and content schema draft.
10. Do not build visual design until content and URL preservation are done.
