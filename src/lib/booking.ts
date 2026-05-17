const GUESTSAGE_HASH = "0bf0dc4c-089f-42f4-8bf0-3ea22a76ad8a";
const GUESTSAGE_BASE = "https://be.guestsage.com";

export type BookingLocale = "pl" | "en" | "de";

export interface BookingParams {
  arrivalDate?: string;   // YYYY-MM-DD
  departureDate?: string; // YYYY-MM-DD
  personsCount?: number;
  locale?: BookingLocale;
  featuredRoomTypeId?: number;
  featuredRatePlanId?: number;
}

// Returns a GuestSage booking URL.
// If dates are missing, returns the base booking page.
// If dates are present, all three required params (arrival, departure, persons) must be set.
export function buildBookingUrl(params: BookingParams = {}): string {
  const { arrivalDate, departureDate, personsCount = 2, locale = "pl" } = params;
  const base = `${GUESTSAGE_BASE}/${locale}/${GUESTSAGE_HASH}`;

  if (!arrivalDate || !departureDate) {
    return base;
  }

  const query = new URLSearchParams({
    arrivalDate,
    departureDate,
    personsCount: String(personsCount),
  });

  if (params.featuredRoomTypeId) query.set("featuredRoomTypeId", String(params.featuredRoomTypeId));
  if (params.featuredRatePlanId) query.set("featuredRatePlanId", String(params.featuredRatePlanId));

  return `${base}/offers?${query.toString()}`;
}
