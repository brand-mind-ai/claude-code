---
session_id: infra-rollout-2026-04-20
updated: 2026-04-20
source: migrated from Cowork auto-memory (reference_hotel_zacisze.md)
---

# Zacisze — Domain Facts

Stable facts about Hotel Zacisze. Two contexts share this file:
- **Hotel sale** (selling for 12M PLN — see `_HANDOVER.md`)
- **Brand Mind case study** (first client, agent KB source — see
  `Projects/Agency/`)

## Location

- Northern shore of Lake Turawa (Duże Jezioro Turawskie), near Opole,
  Opolszczyzna region, Poland
- ~150m from beach, surrounded by pine-oak forest
- Website: www.zaciszeturawa.pl
- Primary email: biuro@zaciszeturawa.pl
- Main phone: +48 77 402 90 30
- Secondary phone: +48 882 111 394

## Facility

| Item | Value |
|---|---|
| Category | 3-star hotel |
| Beds | 75 (rooms + garden apartments) |
| Check-in | 15:00 |
| Check-out | 11:00 |
| Parking | ~40 monitored spots, 10 PLN/day |
| SPA hours | 16:00-22:00 daily |
| External SPA access | 65 PLN/person (3 hrs) |
| Breakfast weekday | 07:30-09:30 |
| Breakfast weekend | 08:30-10:30 |
| Restaurant Sunday | Open from 13:00 (weekdays 15:00) |
| Conference capacity | Up to 150 people |
| Banquet hall | 100 people, air-conditioned |

## Room types

| Type | Rate (from) | Notes |
|---|---|---|
| Classic | 220 PLN/person | Standard |
| Lux DBL | 240 PLN/person | Double bed |
| Lux TWIN | 240 PLN/person | Two singles — separate SKU |
| Garden Apartment | 270 PLN/person | |

## SPA

Jacuzzi, sauna, salt grotto, gym. Free for hotel guests. CERAGEM
massage included in SPA.

## Voucher / gift card system

Supported (per hotel website). Likely hotelsystems.pl-driven.

## Reviews (April 2026)

- Booking.com: 8.3/10
- Google: 4.3/5
- TripAdvisor: 8.8/10
- Praise focus: food, staff, cleanliness, surroundings

## Current offers (April 2026)

- Majówka 2026 — 4 days from 815 PLN/person
- Weekend relaxation — 3 days from 460 PLN/person
- Long June weekend — 3 days from 620 PLN/person

## Tech stack (operational)

- **PMS:** KWHotel (Booking Engine API v0.47 at dev.kwhotel.com)
- **Website / booking widget:** hotelsystems.pl (Integrator API = JS embed
  only; PHP API read-only; no transactional external API; no webhooks)
- **Email server:** HotelSystems (NOT Gmail → Gmail API can't directly
  access biuro@zaciszeturawa.pl)
- **Online bookings flow:** email to reception → manual entry into
  KWHotel (the gap Brand Mind would automate)

### HotelSystems investigation findings (2026-04-06)

- No external transactional API.
- Integrator API (JS embed) is booking widget on website only.
- PHP API returns HTML/XML for pakiety / pokoje_list / opinie — read-only.
- Admin panel (zaciszeturawa.hotelsystems.pl/admin): full management,
  but no API keys, webhooks, or developer settings exposed.
- PMS integration with KWHotel exists but is paid + managed by
  HotelSystems, not self-serve.

## AI automation opportunities (for Brand Mind case study)

- Guest chatbot / inquiry handling
- Automated booking confirmations
- Review response automation
- Email marketing sequences
- Conference / event inquiry handling
- Voucher management
- Email interception for booking auto-entry (Booking.com + HotelSystems
  → auto-create reservations in KWHotel) — highest-value automation, does
  NOT require n8n
- Reception notifications: email + shared Google Sheet (live booking
  ledger), not n8n

## Open questions

- Does HotelSystems email panel support forwarding rules? (Needed for
  the email interception automation — forward to dedicated Gmail, then
  process via Google Apps Script.)
- KWHotel ↔ HotelSystems sync: currently manual by reception, no
  complaints. **Parked**, not worth automating yet.
- Booking.com availability updates: same reasoning. **Parked**.

---

## Ownership + legal (sale-critical)

**Registered owners:** BOGDAN SZYDŁOWSKI + WERONIKA SZYDŁOWSKA
(wspólność ustawowa majątkowa małżeńska — marital joint property).

Marcin is NOT the registered owner — he acts on their behalf. **Power
of attorney (pełnomocnictwo) may be required** for any binding
signature in the sale process. Confirm status before LOI / NDA /
contract stages.

**Property legal IDs:**
- Działki 68/11, 68/204 (0.4414 ha), KW `OP1O/00109298/4`
- Działka 68/198 (0.2431 ha), KW `OP1O/00115173/7`
- Total land: ~0.68 ha
- Obręb Rzędów, km 4, Turawa

## Appraisal (WYCENA HOTEL_dochodowa.pdf)

| Item | Value |
|---|---|
| Method | Income approach (podejście dochodowe) |
| Appraised value | **14,012,000 PLN** (~€3.3M) |
| Appraiser | mgr Patrycja Piszczan, Kancelaria "RENOMA", Wodzisław Śl. |
| Appraiser tel | 691 512 300 |
| Date | 2024-11-14 |
| 12-month validity expired | **2025-11-14** — EXPIRED. Art. 156 ust. 3-4 renewal required before serious investor discussions. |

**Asking price vs appraisal:** 12M PLN asking / 14M PLN appraised.
2M PLN gap positioned as "motivated seller / quick transaction"
discount in investor deck.

### Building data per appraisal (reconcile with marketing copy)

| Metric | Value |
|---|---|
| Main building usable | 1,279.44 m² |
| Main building footprint | 605.45 m² |
| Main building volume | 5,809.40 m³, 3-story |
| Cottage segments | 3 × 62.39 m² usable, 2-story, independent units |
| **Total usable** | **1,466.61 m²** |
| Total footprint | 746.57 m² |
| Total volume | 6,526.01 m³ |
| Rooms per appraisal | 35 (incl. disability-accessible room) |
| Modernized | 2011 |
| Construction | Traditional masonry, elevated standard, good technical condition |
| Heating | Oil central (C.O. olejowe) |
| Other | Rooftop solar (fotowoltaika), SPA w/ sauna + salt cave + massage, conference hall, restaurant, heated outdoor pool |

### Room-count discrepancy (unresolved)

Three different room counts in play — pick one canonical number
before sending anything to brokers:

| Source | Count | Notes |
|---|---|---|
| Appraisal (Nov 2024) | 35 rooms | "incl. disability-accessible" |
| Marketing / operations | 24 rooms + 6 two-room apartments = 30 units | "30 units total" framing in outreach |
| Reviews / `_HANDOVER.md` earlier estimate | 29 rooms, 75 beds | Per facility table above |

Most likely cause: appraisal counts bedrooms (apartments = 2 each),
ops counts SKUs. **Do NOT quote inconsistent numbers to a buyer.**
Lock one representation; update investor deck accordingly.

## Sale process rules (load-bearing)

- **100% remote.** No in-person meetings with brokers or buyers.
  Entire process executed via email / phone / video. Discovery calls
  via Calendar link, VDR for document sharing.
- **Seller financing pre-approved.** Indicative structure: 70% upfront,
  30% over 3–5 years. Open to negotiation inside that envelope.
- **Marcin's commission on success:** ~1M PLN upon finalized sale.
- **Investment memorandum is in-house** (not outsourced to broker).
  Financial model + deck + extended PDF all built here.
- **Gatekeeper problem:** direct email/phone for decision-makers is the
  constraint. LinkedIn Sales Navigator + targeted outreach is the
  workaround.

## Email + infrastructure separation (HARD RULE)

Hotel Zacisze business NEVER touches Reaktion.com infrastructure.

| Resource | Belongs to | OK for hotel? |
|---|---|---|
| `szydlowski001@gmail.com` | Martin personal | YES — primary for now |
| `biuro@zaciszeturawa.pl` | Hotel reception | YES — ops, not sale |
| Future `@zaciszeturawa.pl` alias on Marcin's personal Google Workspace | To be set up | YES — target state for sale correspondence |
| `marcin@reaktion.com` | Past employer Reaktion.com (Martin laid off April 2026) | **NO** — never send hotel mail from this |
| Close CRM | Reaktion-owned, read-only for Martin | **NO** — never store hotel leads here |
| Reaktion Google Workspace | Employer | **NO** — no hotel aliases or domain setup on this |

If a workflow suggests using Reaktion infrastructure for hotel
purposes, stop and re-route to personal Gmail / personal Workspace.

