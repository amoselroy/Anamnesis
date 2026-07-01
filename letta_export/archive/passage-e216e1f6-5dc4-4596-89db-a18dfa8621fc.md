# SESSION CHUNK 2026-06-19 — Critical Discovery - Massive Paper Duplication and De

*ID: passage-e216e1f6-5dc4-4596-89db-a18dfa8621fc*
*Created: 2026-06-20*

---

SESSION CHUNK 2026-06-19 — Critical Discovery - Massive Paper Duplication and Deduplication Failure

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\pseudocode.md, C:\Users\Amos\projects\braindexer\routers\therapies.py, C:\Users\Amos\projects\braindexer\services\scraper.py, C:\Users\Amos\projects\braindexer\diag_ranking.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_braindexer.md
Errors: Exit code 1
Fetching papers for: sauna-therapy

Traceback (most recent call la; Exit code 1
postgresql://neondb_owner:npg_aBDud8x6LCKl@ep-delicate-smoke-aps537e
Tools used: Edit, PowerShell, Grep, Read, Glob, Write
URLs: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
Dates: 2026-06-19, 2026-06-20

SUMMARY
When the diagnostic script was run on Sauna therapy, it revealed a catastrophic data integrity issue: 315 papers total in the database, but only 9 unique papers, with each duplicated approximately 35 times. This massive duplication was invisible to users (UI displays unique papers) but was sent to Haiku during ranking, causing the LLM to receive 315 score requests for essentially the same 9 papers, resulting in completely scrambled tier assignments. The duplicates likely accumulated from multiple research runs on Sauna without proper deduplication. This explained the erratic tier classifications Amos had observed — papers appeared to be randomly assigned to different tiers because Haiku's output (315 scores for a 9-paper set repeated 35 times) was being misaligned with the displayed title list. The discovery revealed a systemic failure in the deduplication logic in `research_therapy()`: the `seen_urls` set-based deduplication was not preventing duplicates from accumulating across multiple research runs. This was identified as the root cause of the ranking inconsistencies and a critical bug requiring immediate investigation of the deduplication implementation.
