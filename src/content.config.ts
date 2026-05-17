import { defineCollection, z } from "astro:content";

const ctaSchema = z.object({
  label: z.string(),
  bookingMode: z.enum(["base", "offers", "room", "package"]).default("base"),
});

const guestSageSchema = z.object({
  featuredRoomTypeId: z.number().optional(),
  featuredRatePlanId: z.number().optional(),
});

// Canonical schema — .pages.yml mirrors this manually.
// When adding/removing fields here, update .pages.yml fields section too.
const pageSchema = z.object({
  locale: z.enum(["pl", "en", "de"]),
  translationKey: z.string(),
  canonicalPath: z.string().startsWith("/"),
  sourceUrl: z.string().url().optional(),
  pageType: z.enum([
    "home", "rooms", "room-detail", "packages", "package-detail",
    "spa", "restaurant", "conferences", "gallery", "contact",
    "booking", "vouchers", "attractions", "reviews", "legal", "jobs", "other",
  ]),
  title: z.string(),
  seoTitle: z.string().optional(),
  description: z.string().optional(),
  status: z.enum(["captured", "deferred", "redirect-pending"]),
  heroImage: z.string().optional(),
  gallery: z.array(z.string()).optional(),
  cta: ctaSchema.optional(),
  guestSage: guestSageSchema.optional(),
});

// Collections are named after their src/content/ subdirectory.
export const collections = {
  pl: defineCollection({ type: "content", schema: pageSchema }),
  en: defineCollection({ type: "content", schema: pageSchema }),
  de: defineCollection({ type: "content", schema: pageSchema }),
};
