# SESSION CHUNK 2026-06-18 — Production Database Migration Failure and Startup-Tim

*ID: passage-cd042aca-7c59-4fda-b0cc-57d58a670160*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — Production Database Migration Failure and Startup-Time Schema Guarantee

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/models.py, C:/Users/Amos/projects/braindexer/setup_db.py, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/main.py
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Edit, Read, Bash, Grep, Glob
URLs: https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en`

SUMMARY
After deploying the side effects score addition, the condition-specific therapy view failed with "no therapy found." Investigation traced the root cause to the new `side_effects_score` column missing from the production Neon database — the SELECT now included it, but the column didn't exist, causing the query to return 500, which the JS caught as "Therapy not found." Although `preDeployCommand: python setup_db.py` was configured in `render.yaml`, the migration apparently hadn't executed or had failed silently. To make schema changes bulletproof, a `_run_migrations()` function was added to the FastAPI startup lifespan that executes all critical `ALTER TABLE ... ADD COLUMN IF NOT EXISTS` statements before any request is served. Each migration is individually try-excepted, so a single failure (e.g., column already exists) won't block startup. Going forward, adding a new column requires only adding it to the `_MIGRATIONS` list — no dependency on preDeployCommand succeeding or external deployment steps. This pattern ensures that schema and application code never diverge, which had been the source of the silent failure in this case. The fix was deployed and the condition view restored after Render redeployed.
