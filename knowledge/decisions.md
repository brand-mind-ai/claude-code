# Zacisze — Decisions log (append-only)

Format: `- YYYY-MM-DD HH:MM [session_id]: <decision text>`

---

- 2026-04-25 14:00 [local_42be8162]: HotelSystems.pl migration target locked = **GuestSage LITE + KWHotel**

- 2026-04-22 12:00 [local_8c799f08]: Claude Design (research preview, launched 2026-04-17) is a mockup/prototype tool only — NOT for production deployment. For Zacisze self-build path: Claude Design (mockup) → Claude Code / Codex (production code). Recommended stack = Astro + Cloudflare Pages

- 2026-04-22 13:00 [local_4c971d14]: Pricing Math: at +15% price / -25% volume scenario, break-even direct recapture = 48.4% (need to convert ~half of "lost" Booking.com customers to direct). Worst-case "30/30" (30% volume loss + 30% recapture) = ~6.2% net revenue drop (~29K PLN/yr loss). Direct funnel quality (website conversion, SEO, booking widget UX) is the prerequisite, not a parallel workstream.

- 2026-05-17 21:37 [repo-foundation-2026-05-17]: Zacisze website rebuild
  repo foundation started at
  `/Users/macbookpro/Documents/Claude/Projects/Hotel/zacisze-turawa`,
  cloned from `https://github.com/brand-mind-ai/zacisze-turawa.git`.
  Current committed direction: Astro + TypeScript + Pages CMS + GitHub
  content + Cloudflare Pages.

- 2026-05-17 21:37 [repo-foundation-2026-05-17]: Animation stack locked
  by Martin: Lenis for smooth scroll + GSAP ScrollTrigger for
  reveal/parallax. Both must load only as Astro islands on pages that
  use motion. Reduced-motion preference disables Lenis and all GSAP
  triggers.

- 2026-05-17 21:37 [repo-foundation-2026-05-17]: Temporary `.com` domain
  is only short-term parking/preview. Long-term search optimization,
  route preservation, canonical planning, and final launch target are
  for `zaciszeturawa.pl`.

- 2026-05-17 20:37: Martin reset the Hotel project scope to the
  `zaciszeturawa.pl` website rebuild only. Current build rules:
  preserve existing URL structure, current content, and current
  image/page pairings first; build Polish first; use GuestSage booking
  engine, Pages CMS, GitHub repo
  `https://github.com/brand-mind-ai/zacisze-turawa/tree/main`, and a
  lean Astro + TypeScript + Cloudflare Pages plan unless changed later.

- 2026-05-17 21:11: Stack decision locked for the Codex-owned Zacisze
  rebuild: Astro + TypeScript + Pages CMS-backed GitHub content +
  Cloudflare Pages. Use CSS/Astro View Transitions first, GSAP only for
  advanced scroll choreography, and React only for isolated islands if
  needed. MVP is Polish-only with no language picker; EN/DE URLs remain
  in the route contract and may be dead for about one week before the
  follow-up rebuild.

- 2026-05-17 21:11: Domain plan clarified. Initial public deployment
  goes to temporary parking domain `https://zaciszeturawa.com/`; final
  canonical migration target remains `https://www.zaciszeturawa.pl/`.
  Preserve paths as relative route contracts, keep internal links
  relative where possible, and make canonical tags, sitemap generation,
  robots behavior, and `.com` to `.pl` redirects environment-aware.
