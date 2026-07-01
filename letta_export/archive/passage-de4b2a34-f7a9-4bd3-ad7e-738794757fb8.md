# SESSION CHUNK 2026-06-20 — Diagnostic Query Bug — 315 Paper "Duplication" Was a 

*ID: passage-de4b2a34-f7a9-4bd3-ad7e-738794757fb8*
*Created: 2026-06-20*

---

SESSION CHUNK 2026-06-20 — Diagnostic Query Bug — 315 Paper "Duplication" Was a Cross-Join Artifact

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\services\scraper.py, C:\Users\Amos\projects\braindexer\flush_sources.py, C:\Users\Amos\projects\braindexer\diag_ranking.py, C:\Users\Amos\projects\braindexer\verify_sources.py, C:\Users\Amos\projects\braindexer\audit_news.py, C:\Users\Amos\projects\braindexer\backfill_news_dates.py
Errors: <tool_use_error>Found 3 matches of the string to replace, but replace_all is fal; <tool_use_error>InputValidationError: Grep failed due to the following issue:
An
Tools used: Read, Edit, PowerShell, Grep, Write
Dates: 2026-06-20

SUMMARY
While investigating the massive paper duplication on Sauna therapy, a critical discovery revealed that the diagnostic script `diag_ranking.py` was itself producing the inflated count through a query design flaw. The original query performed a cross-join between sources and conditions (via therapy_conditions), multiplying the 9 actual papers by 35 linked conditions: 9 × 35 = 315 rows. This explained why Haiku was receiving 315 entries when only 9 unique papers existed — the diagnostic was querying the same papers repeated once per condition. The actual source count was 133 rows (9 visible plus 124 soft-deleted papers that Amos had manually hidden through the admin panel). The flush operation deleted these 133 rows, leaving zero papers for all therapies. The diagnostic query was corrected to remove the unnecessary condition join and properly deduplicate at the SQL level. This discovery clarified that the original NULL-URL deduplication issue was real, but the scale and origin of the problem had been misdiagnosed as massive data duplication when it was actually a diagnostic methodology error.
