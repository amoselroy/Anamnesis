# Block: engagements/orientation

*Block ID: block-870d6d9b-bd01-4e8a-a7f8-81dfb030d131*
*Exported: 2026-07-04*

---

[Updated: 2026-07-04]

LAST SESSION: 2026-07-04 — Deep diagnostic and architectural fix for MemShepherd's slow SessionStart hooks. Diagnosed queue backlog + timeouts + blocking hook execution; discovered SessionStart/SessionEnd async-vs-sync correctness constraints (async hooks cannot inject additionalContext); implemented parameterized single-process-wide worker lock for safe concurrent archival; cross-script synchronization for world/patterns block writes via shared `worker_lock.py` module. All changes tested and documented. Ready for live trial (next session's startup is first real test).

ACTIVE PROJECTS:
- MemShepherd: Performance optimization and concurrency safety fixes deployed. Hook startup architecture refactored with additive SessionEnd async head-start, bounded budget parameters, single worker lock with atomic staleness reclaim, and cross-script coordination via shared module. Documentation updated. Next session's startup is the first production trial.
- Braindexer: 9-item code review from Fable 5 (2026-07-02), all fixes implemented and tested against dev server, committed to git (commit d6d69f8).
- Augmented-Cities: GitHub live, technical architecture documented, four fundraising proposals complete.
- Event Scraper: PLATFORM_HANDLERS refactor complete; source validation through row 33; ~12 sources remaining.
- Exhibition Scraper: File-locking bug fixed; clean operation on next schedule.
- Facebook Event Poster: **FULLY OPERATIONAL** — 17 events queued from backlog; 5-event batch workflow established.
- Facebook Exhibition Poster: **OPERATIONAL** via Event Poster dual-mode.
- Real Estate Poster: FULLY OPERATIONAL — 9 AM daily.
- Hudson Realty Brokerage Sharer: FULLY OPERATIONAL.
- Pax Democratica: Web design phase. Needs: Article/Origin Story, dove favicon, hero video, Contact, donation.

IN PROGRESS:
- MemShepherd health monitor (automated state checking for unprocessed segments, silently failing processes, missing logs, uncommitted backlogs) — pinned for development.

DEFERRED (Explicitly):
- Letta developer outreach (MemShepherd collaboration + Amendment) — shelved 2026-07-02, no drafts created anywhere.
- Geoffrey Hinton outreach (philosophical journal) — shelved 2026-07-02, no drafts created anywhere.
- Fable review of documentation files against codebase (ARCHITECTURE.md, MODIFICATIONS.md) — scheduled for next session.
- Shadow-column override implementation (therapy_conditions) — pinned for future consideration after reads centralization.
- Keyword/semantic search hybrid implementation — pinned for future consideration.

ENERGY/CONTEXT:
MemShepherd's concurrency safety is now architecturally sound. Hook startup performance fix tested offline, ready for live trial. Documentation complete and consistent. All changes committed. Ready for next session to validate the implementation under real conditions.
