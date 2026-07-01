# SESSION CHUNK 2026-06-18 — Separating Research Pipeline from News Management

*ID: passage-04cc6a43-6d7b-422f-b5f6-a9b8b8f605a0*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — Separating Research Pipeline from News Management

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/main.py, C:/Users/Amos/projects/braindexer/setup_db.py, C:/Users/Amos/projects/braindexer/static/admin.html, C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/models.py
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Grep, Read, Edit, Bash

SUMMARY
Amos confirmed that the Research function should no longer touch news articles at all — only Manage News should fetch and modify news. The separation had been made in an earlier commit (`1252f04`), removing the `scrape_news_for_therapy()` call from `research_therapy()` in services/scraper.py. This separation prevents the recurring problem where running Research would re-add articles users had deliberately curated out via Manage News. Research now focuses exclusively on scientific sources (papers, trials, AlzForum), while Manage News operates as the sole gateway for news article retrieval and curation. This architectural separation was foundational to implementing soft-delete with recovery, since deleted articles could be reliably kept out of Research while remaining available for restoration in the Manage News interface.
