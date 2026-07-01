# SESSION CHUNK 2026-06-19 — Migration Transaction Failures and Savepoint-Based Re

*ID: passage-50822d85-c05e-4c6d-ab92-2b0ded34e0ce*
*Created: 2026-06-19*

---

SESSION CHUNK 2026-06-19 — Migration Transaction Failures and Savepoint-Based Recovery

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/main.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/static/admin.html, C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/pseudocode.md, C:/Users/Amos/.claude/journal_entry_tmp.md, C:/Users/Amos/.claude/projects/C--Users-Amos/memory/feedback_journal_append_only.md
Errors: Exit code 2
C:\Users\Amos\AppData\Local\Python\pythoncore-3.14-64\python.exe: ca; The user doesn't want to proceed with this tool use. The tool use was rejected (
Tools used: Bash, Read, Edit, Grep, Glob, Write, PowerShell

SUMMARY
After pushing the opt-in schema changes, deployment to Render resulted in HTTP 500 errors when accessing Manage News and selecting conditions. Root cause diagnosis revealed that `_run_migrations()` in `main.py` was executing all ALTER TABLE statements in a single PostgreSQL transaction. When any statement failed (e.g., column already exists, unique index conflict), PostgreSQL marked the entire transaction as aborted. All subsequent statements silently skipped without error, meaning the new `shown_condition_ids` and `excluded_condition_ids` columns were never actually created. Any code attempting to read or write these columns threw a 500. The fix applied the same savepoint pattern already used elsewhere in the codebase: each migration statement gets wrapped in its own savepoint, so a pre-existing column or index failure doesn't cascade to subsequent statements. After this fix was deployed, migrations ran cleanly and the columns were created successfully, resolving both 500 errors.
