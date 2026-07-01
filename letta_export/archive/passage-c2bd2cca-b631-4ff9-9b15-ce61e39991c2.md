# SESSION CHUNK 2026-06-18 — Separating News Management from Research and Implemen

*ID: passage-c2bd2cca-b631-4ff9-9b15-ce61e39991c2*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — Separating News Management from Research and Implementing Soft-Delete

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/models.py, C:/Users/Amos/projects/braindexer/setup_db.py, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/main.py
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Edit, Read, Bash, Grep, Glob
URLs: https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en`

SUMMARY
Amos raised a critical architecture issue: each time Research is run, it re-adds news articles that have been previously deleted via Manage News, because the research pipeline scrapes both scientific sources AND news sources, and deduplication is based only on URL existing in the database. The solution was to separate concerns: (1) Research should scrape and insert scientific sources only (papers, trials, AlzForum), never touching news; (2) Manage News becomes the sole entry point for news fetching and curation; (3) implement soft-delete using a `deleted_at TIMESTAMPTZ` column instead of hard deletion. With soft-delete, when a user deletes an article via Manage News, the row remains in the database with `deleted_at = NOW()` set. The fetch logic checks the full set of news URLs (including soft-deleted rows) for deduplication, preventing re-addition, but the UI only displays rows where `deleted_at IS NULL`. This allows accidental deletions to be recovered by clearing the `deleted_at` timestamp. The architecture ensures that once a user curates out an article, it cannot resurface through subsequent automated runs. Amos approved this plan with the addition that soft-deleted entries should be re-attachable in case of erroneous deletion.
