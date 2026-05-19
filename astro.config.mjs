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
      filter: (url) => !url.includes("/strona_glowna"),
    }),
  ],
});
