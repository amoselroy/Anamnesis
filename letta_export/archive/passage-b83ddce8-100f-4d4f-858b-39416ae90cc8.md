# SESSION CHUNK 2026-06-17 — Architectural Refactoring — Consolidating Scattered S

*ID: passage-b83ddce8-100f-4d4f-858b-39416ae90cc8*
*Created: 2026-06-17*

---

SESSION CHUNK 2026-06-17 — Architectural Refactoring — Consolidating Scattered Site-Specific Logic into a Registry Pattern

STRUCTURED
Files: C:\Users\Amos\projects\fb-poster\fb_poster.py, C:\Users\Amos\projects\fb-poster\event_scraper.py
Errors: ECONNREFUSED; Was there a typo in the url or port?
Tools used: ToolSearch, Glob, Read, PowerShell, Grep, Edit, WebFetch
URLs: https://hoboken.recdesk.com/Community/Calendar

SUMMARY
The session identified a critical architectural issue: site-specific handling is currently scattered across four locations in the scraper: (1) `extract_event_fields()` with domain-specific extractors; (2) `scrape_source()` with special listing paths and `_PW_LISTING_DOMAINS`; (3) `passes_location()` with `_ALWAYS_ACCEPT_DOMAINS`, venues, and domain checks; (4) inline venue normalization. Amos raised the question of whether there was a clean way to separate universal algorithm from site-specific handling, asking if this could be structured as a universal algorithm with separate site-specific data. The proposed solution is a **`PLATFORM_HANDLERS` registry** — a configuration dict at the top of the file (or in a separate `handlers.py` module) mapping domain patterns to handler config objects. Each handler object would specify: listing mode (static, Playwright, organizer page), listing extractor function, detail extractor function, always-accept flag, venue suffix normalization. The universal algorithm would dispatch to this registry via `_match_handler(domain)` and delegate, eliminating scattered `if "libcal.com" in domain` checks. This refactor (~100 lines moved/restructured) would have no immediate behavior change but would make every future source (like RecDesk) trivial to add by simply adding an entry to the registry and implementing its extractor function. Amos approved moving forward with the refactor while simultaneously adding RecDesk as the first new source under the new architecture. The session ended with me preparing to read the full scraper before beginning the refactoring work.
