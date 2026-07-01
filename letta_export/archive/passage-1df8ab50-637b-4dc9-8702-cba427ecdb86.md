# SESSION CHUNK 2026-06-20 — Backfill Script Execution and Query Parameter Bug

*ID: passage-1df8ab50-637b-4dc9-8702-cba427ecdb86*
*Created: 2026-06-20*

---

SESSION CHUNK 2026-06-20 — Backfill Script Execution and Query Parameter Bug

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\services\scraper.py, C:\Users\Amos\projects\braindexer\flush_sources.py, C:\Users\Amos\projects\braindexer\diag_ranking.py, C:\Users\Amos\projects\braindexer\verify_sources.py, C:\Users\Amos\projects\braindexer\audit_news.py, C:\Users\Amos\projects\braindexer\backfill_news_dates.py
Errors: <tool_use_error>Found 3 matches of the string to replace, but replace_all is fal; <tool_use_error>InputValidationError: Grep failed due to the following issue:
An
Tools used: Read, Edit, PowerShell, Grep, Write
Dates: 2026-06-20

SUMMARY
During execution of `backfill_news_dates.py` to populate missing publication dates, an IndexError occurred in the parameterized query: `IndexError: list index out of range` at the point where the LIMIT parameter was being appended to the params list. Investigation revealed a mismatch between the number of `%s` placeholders in the SQL query and the number of parameters being passed. The params list was constructed based on dynamic condition filtering (`therapy_name` optional filter, date range filters, etc.), but the SQL string had been modified to append LIMIT without accounting for the variable number of preceding parameters. The script was corrected to properly handle parameter ordering and count. User discovered PowerShell syntax distinction between pipe (`|`, which passes output to a command) and redirect (`>`, which writes to a file), with the `Tee-Object` cmdlet available for simultaneous console display and file capture. The backfill script's default `--limit` was increased from 10 to 20 articles to ensure sufficient test data visibility while remaining conservative for initial runs. Google News aggregator URLs were identified as unsalvageable since they're redirects that don't preserve the original article's publication date from the RSS source.
