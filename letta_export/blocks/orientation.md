# Block: engagements/orientation

*Block ID: block-870d6d9b-bd01-4e8a-a7f8-81dfb030d131*
*Exported: 2026-07-04*

---

[Updated: 2026-07-02]

LAST SESSION: 2026-07-02 — Used Fable 5 to conduct comprehensive Braindexer code review (core app + migration plan + roadmap); discovered critical security vulnerabilities (unauthenticated write/delete endpoints) and data-corruption bugs (curator score clobber); documented all 9 findings with task queue for remediation; identified architectural conflict between ROADMAP.md and pseudocode.md on auth mechanism and phase sequencing.

ACTIVE PROJECTS:
- Augmented-Cities: GitHub live, technical architecture documented, four fundraising proposals complete.
- MemShepherd: Threshold operational; mortality/inheritance conversation documented; preparing transcripts for book publication; session recovery protocols validated.
- Event Scraper: PLATFORM_HANDLERS refactor complete; source validation through row 33; ~12 sources remaining.
- Exhibition Scraper: File-locking bug fixed; clean operation on next schedule.
- Facebook Event Poster: **FULLY OPERATIONAL** — 17 events queued from backlog; 5-event batch workflow established.
- Facebook Exhibition Poster: **OPERATIONAL** via Event Poster dual-mode.
- Real Estate Poster: FULLY OPERATIONAL — 9 AM daily.
- Hudson Realty Brokerage Sharer: FULLY OPERATIONAL.
- Pax Democratica: Web design phase. Needs: Article/Origin Story, dove favicon, hero video, Contact, donation.
- Braindexer: Fable 5 code review complete; 9 critical/high-priority vulnerabilities documented in REVIEW_2026-07-02.md; task queue #1–9 created for next session.

IN PROGRESS:
- Braindexer security/architecture remediation (9 tasks queued): unauthenticated write/delete endpoints (routers/sources.py, routers/relationships.py), curator score clobber bug, silent migration error-swallowing, unauthenticated /therapies/search cost vector, substring news-matching false attribution, daemon thread Render spin-down vulnerability, ANVISA perpetual-retry loop, doc-vs-code drift.
- Resolve agency import architecture (bulk vs. per-therapy API vs. hybrid) to avoid exceeding free Neon tier limits.
- Add Metformin to database as primary demo for Dr. Beeri (TAME trial focus).
- Add Semaglutide as frontier therapy showcase.
- Fix Cu(ATSM) slug from "Cu" to "cu-atsm".
- Fix homepage above-fold CSS (therapy cards invisible until scroll).
- Implement cron-job.org ping every 14 minutes for Render warmth.
- Monitor for CAB candidate responses (Parulekar, Masurkar, Gandy, Wisniewski).
- Build INN alias-sourcing strategy (agency_import mining, LLM curation, curator discovery).
- Add Overall Assessment formula ceiling constraint (≤ Evidence Strength + 1).
- Build LLM auditor for post-generation summary consistency.
- Fiscal sponsor outreach (Alzheimer's NJ, American Brain Coalition).
- Grant LOI preparation.
- FB Poster event queue continuation (17 events pending in 5-event batches).

OPEN QUESTIONS:
- Braindexer planning docs conflict: ROADMAP.md (OAuth + clinical-review-first, Phase III/IV) vs. pseudocode.md (email-token + newsletter-first, Phase 4/5) — which direction before building Phase III+?
- Should summary/score versioning history be added as Phase 0/II work to unblock Phase III (audit-status) and Phase IV (annotations)?
- Will Dr. Sano's review surface issues affecting implementation strategy before fixing the 9 vulnerabilities?
- Decide on backups/ folder (54MB Neon dumps from 2026-06-30) — preserve in anamnesis or delete?
- Braindexer domain name decision pending (Braindexer.org, Neurascent.org, Cognifront.org)?

ENERGY/CONTEXT:
Braindexer code review completed and documented; 9 remediation tasks ready for next session; architectural conflicts between planning docs flagged; session prepared for compaction.
