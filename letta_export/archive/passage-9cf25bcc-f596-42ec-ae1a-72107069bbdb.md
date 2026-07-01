# SESSION CHUNK 2026-06-20 — Environment Variable Management and Multi-Database Su

*ID: passage-9cf25bcc-f596-42ec-ae1a-72107069bbdb*
*Created: 2026-06-20*

---

SESSION CHUNK 2026-06-20 — Environment Variable Management and Multi-Database Support

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\services\scraper.py, C:\Users\Amos\projects\braindexer\flush_sources.py, C:\Users\Amos\projects\braindexer\diag_ranking.py, C:\Users\Amos\projects\braindexer\verify_sources.py, C:\Users\Amos\projects\braindexer\audit_news.py, C:\Users\Amos\projects\braindexer\backfill_news_dates.py
Errors: <tool_use_error>Found 3 matches of the string to replace, but replace_all is fal; <tool_use_error>InputValidationError: Grep failed due to the following issue:
An
Tools used: Read, Edit, PowerShell, Grep, Write
Dates: 2026-06-20

SUMMARY
To improve developer experience and reduce security risk when switching between local development and production databases, a systematic approach to environment variable management was implemented. Rather than hardcoding production credentials or requiring manual URI edits, all diagnostic and utility scripts were updated to support a `--prod` flag that reads from `BRAINDEXER_PROD_DB_URI` (separate from the local `BRAINDEXER_DB_URI`). This allows a user to set the production URI once per terminal session without ever exposing it in code or files: `$env:BRAINDEXER_PROD_DB_URI = "..."` then use `--prod` on any script. The scripts `diag_ranking.py`, `audit_news.py`, `verify_sources.py`, `flush_sources.py`, and `backfill_news_dates.py` were all updated with this pattern. Default behavior uses the existing local environment variable unless `--prod` is explicitly specified, making the feature opt-in and safer against accidental production modifications. This approach balances security (credentials stay in terminal session memory, never in scripts) with convenience (single flag to switch databases).
