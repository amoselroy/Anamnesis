# WORLD PATTERN 2026-06-17 — Registry pattern for consolidating scattered site-spe

*ID: passage-a5b331e8-02ed-499c-919f-dfdb7ef2378f*
*Created: 2026-06-17*

---

WORLD PATTERN 2026-06-17 — Registry pattern for consolidating scattered site-specific handlers — 2026-06-17

PRINCIPLE: When site-specific logic is scattered across multiple dispatch points in a universal algorithm (extractors, listing paths, location filters, normalizers), consolidation via a registry pattern reduces maintenance burden and makes adding new sources trivial.

NARRATIVE: Review of the event scraper revealed site-specific handling in four locations: `extract_event_fields()` with domain-specific extractors, `scrape_source()` with special listing paths (`_PW_LISTING_DOMAINS`), `passes_location()` with domain checks, and inline venue normalization. Each new source (e.g., RecDesk) required changes across multiple functions and conditionals. Amos proposed a `PLATFORM_HANDLERS` registry — a dict mapping domain patterns to handler config objects specifying listing mode, extractors, location acceptance, and venue suffix. The universal algorithm would dispatch via `_match_handler(domain)` once, eliminating scattered `if "libcal.com" in domain` checks. This refactor (~100 lines moved) has no immediate behavior change but makes every future source addition a simple registry entry plus extractor function. The pattern applies broadly to any system accumulating special cases for different data sources.
