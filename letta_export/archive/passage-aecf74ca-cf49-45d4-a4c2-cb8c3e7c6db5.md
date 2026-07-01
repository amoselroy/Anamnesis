# WORLD PATTERN 2026-06-11 — Dedicated platform-specific paths for JavaScript-heav

*ID: passage-aecf74ca-cf49-45d4-a4c2-cb8c3e7c6db5*
*Created: 2026-06-11*

---

WORLD PATTERN 2026-06-11 — Dedicated platform-specific paths for JavaScript-heavy ticketing — 2026-06-11

PRINCIPLE: When a ticketing platform requires JavaScript execution both for link discovery and detail-page fetching, create a dedicated routed path instead of forcing generic paths to handle platform-specific quirks.

NARRATIVE: Eventbrite organizer URLs required a correct slug-prefixed format to work; seetickets events required Playwright to fetch both the link list and individual event details. Rather than making generic Path C (Playwright link find, static detail fetch) handle both platforms' specific requirements, dedicated Path EB and Path ST were created with platform-specific link patterns and full-Playwright fetching. This pattern generalizes to any specialized scraping domain: when a consistent external platform has specific behaviors, building a dedicated path is cleaner than extending generic paths. It also creates a template for future platforms with similar characteristics.
