# SESSION CHUNK 2026-06-18 — Braindexer Discovery 503/500 Errors and Schema Migrat

*ID: passage-eb5074fa-8a3a-47e8-97c7-8c916bb69c6f*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — Braindexer Discovery 503/500 Errors and Schema Migration Fix

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/render.yaml, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/scheduler.py
Errors: Exit code 1
<string>:18: SyntaxWarning: "\]" is an invalid escape sequence. Such; Exit code 1
INFO:services.scraper:Discovery: fetching AlzForum therapeutics list; Exit code 1
Invoke-WebRequest : Cannot bind parameter 'Headers'. 
Cannot conver; <tool_use_error>String to replace not found in file.
String:         if name.low; <tool_use_error>Blocked: Start-Sleep 30 followed by: Invoke-RestMethod -Method P; Exit code 1
  File "<string>", line 7
    print(f'  [{r[" authors\]}]
        ; Exit code 1
Traceback (most recent call last):
  File "<string>", line 9, in <m; Exit code 1
Invoke-RestMethod : The remote server returned an 
error: (500) Int; Exit code 1
python : Traceback (most recent call last):
At line:1 char:39
+ cd; Exit code 1
Invoke-WebRequest : The remote server returned an 
error: (500) Int
Tools used: Glob, Read, Grep, Edit, PowerShell, Bash
Dates: 2026-06-17

SUMMARY
Amos reported a 503 error on initial cron-job.org discovery run (expected due to Render cold-start) followed by HTTP 500 on the Drafts page. Investigation revealed the root cause: the production Neon database was missing columns (`therapeutic_action`, `effectiveness_score`, `evidence_score`, `safety_score`) that were added via `ALTER TABLE` statements in `setup_db.py`, which was never called on Render startup. The `list_drafts` endpoint queries these columns, causing every query to fail with a PostgreSQL error. The live Render configuration only runs `uvicorn` on startup with no database migration step. The solution was two-fold: (1) add `preDeployCommand: python setup_db.py` to `render.yaml` so all future schema changes auto-migrate on deploy, making the system idempotent; (2) manually run `python setup_db.py` locally against production Neon to apply the missing columns immediately. This fixed the 500 and revealed a secondary problem: the scraper had captured a UI element ("View Timeline", a table action button) instead of actual therapy entries, with mechanism stored as bare integer "18". The integer mechanism was added as a guard heuristic but Amos correctly pushed back that numeric mechanisms could be legitimate and the guard would silently drop real data. The guard was removed and replaced with targeted UI keyword filtering on names instead. This episode demonstrated the importance of making schema migrations automatic and the risk of heuristic guards that could inadvertently filter valid data.
