# WORLD PATTERN 2026-08-06 — Default Time Field for Events with Implicit Times — 2

*ID: passage-26e2d63c-b4a1-4aa4-ab47-89c1d6e15d16*
*Created: 2026-08-06*

---

WORLD PATTERN 2026-08-06 — Default Time Field for Events with Implicit Times — 2026-08-06

PRINCIPLE: When a source consistently publishes events without explicit times because the time is always known by convention, declaring a `default_time` field on the SiteHandler allows the scraper to fill missing times automatically rather than dropping timeless events.

NARRATIVE: LSC After Dark events were being silently dropped from the scraper because the `_build_row` function hard-rejects events without extracted times. However, Space Talk events (which are part of After Dark) genuinely have no published time — they're scheduled at 6 PM by convention as part of the series structure. Rather than special-case LSC, Tal implemented a `default_time` field on SiteHandler that allows sources to declare a fallback time, which `_build_row` applies before rejection. This converts implicit knowledge ("Space Talk always runs at 6 PM") into explicit schema (`default_time="06:00"`), making the convention auditable and reusable across any future source with the same pattern. The principle generalizes: when venue event data has implicit attributes that aren't published but are consistently known, encoding them as SiteHandler-level declarations prevents data loss while keeping the discovery explicit.
