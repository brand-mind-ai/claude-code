// @ts-check
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

const SITE_COM = "https://zaciszeturawa.com";
const SITE_PL = "https://www.zaciszeturawa.pl";

// Use ASTRO_SITE env var to override (set to PL domain after final cutover).
// Default to .com for temporary launch.
const site = process.env.ASTRO_SITE ?? SITE_COM;

export default defineConfig({
  output: "static",
  site,
  integrations: [
    sitemap({
      // Exclude pages that are redirect targets or placeholder stubs
      filter: (url) => {
        const EXCLUDE = ["/strona_glowna", "/restauracja_", "/ceny_i_rezerwacja"];
        return !EXCLUDE.some((p) => url.includes(p));
      },
    }),
  ],
});
