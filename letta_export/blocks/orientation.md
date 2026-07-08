# Block: engagements/orientation

*Block ID: block-870d6d9b-bd01-4e8a-a7f8-81dfb030d131*
*Exported: 2026-07-08*

---

[Updated: 2026-06-11]

LAST SESSION: 2026-06-11 — Fixed critical Event Scraper infrastructure issue (log file write lock crash on Windows Task Scheduler), added 4 new event sources, removed 3 unsuitable sources, debugged and fixed multiple broken sources (WFMU URL correction, Pilsener Haus rate limiting, Fox & Crow venue closure), and implemented architectural improvements to scraper paths (all_failed fallback for Path B, dedicated Path ST for seetickets ticketing platform, query-string deduplication).

ACTIVE PROJECTS:
- MemShepherd: Concurrency safety deployed. Session gap detection pinned for future implementation.
- Braindexer: **Phase 1 COMPLETE & OPERATIONAL** — Therapy pages fully functional with condition-specific views, active trials display, semantic search (0.87 threshold with aliases), admin console with summaries dates and multiline notes. All 5 therapies have embeddings. Page entrance animation (2-second fade, dark purple header/search band). Ready for clinical testing.
- Augmented-Cities: GitHub live, technical architecture documented, four fundraising proposals complete.
- Event Scraper: **NOW OPERATIONAL** — Infrastructure fix resolved 3-day outage (log file write lock). 49 sources active. Architectural improvements deployed (all_failed Path B fallback, dedicated ticketing paths, query deduplication). Outstanding: Hudson Theatre Works (location scope + LLM JSON errors) needs debugging.
- Exhibition Scraper: File-locking fix integrated; operational with failure monitoring.
- Facebook Event Poster: **FULLY OPERATIONAL** with automated source-failure monitoring.
- Real Estate Poster: **FULLY OPERATIONAL** — 9 AM daily.
- Hudson Realty Brokerage Sharer: **FULLY OPERATIONAL**.
- Pax Democratica: Web design phase ongoing.

IMMEDIATE NEXT STEPS:
- Event Scraper: Continue systematic source testing (rows 18–27+ remaining)
- Continue running 4-source batches on nightly rotation (full rotation = 12 nights for 48 sources)

ENERGY/CONTEXT:
Event infrastructure is now healthy. Scraper reliability restored and architectural patterns refined. Three sources identified and removed (closed/unsuitable), four new sources added and integrated. Ready for stable nightly operation.
