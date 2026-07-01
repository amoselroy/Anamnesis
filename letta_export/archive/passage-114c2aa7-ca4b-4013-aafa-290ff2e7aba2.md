# WORLD PATTERN 2026-06-11 — Query string deduplication in event link collection —

*ID: passage-114c2aa7-ca4b-4013-aafa-290ff2e7aba2*
*Created: 2026-06-11*

---

WORLD PATTERN 2026-06-11 — Query string deduplication in event link collection — 2026-06-11

PRINCIPLE: Event venues often generate multiple links to the same event (differing only by query parameters like `?format=ical`), which creates redundant detail page fetches that can trigger rate limiting unnecessarily.

NARRATIVE: Pilsener Haus's Squarespace calendar generated 60 event links, but analysis revealed they were actually 30 unique URLs with 30 duplicates that differed only by `?format=ical` query parameters. When the scraper fetched all 60 in rapid succession, every venue link timed out due to rate limiting. Deduplicating links by stripping query parameters before storage reduced the request volume to 30, which the server could handle. The pattern generalizes to any scraping scenario where URL generators create intentional or accidental query-parameter variants of the same resource. Deduplication is especially critical when scraping JavaScript-generated link lists that may naturally produce redundant variants.
