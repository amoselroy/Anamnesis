# SESSION CHUNK 2026-06-18 — Opt-In Implementation with Dual Arrays and UI Languag

*ID: passage-6ef468cd-77bc-4fb4-a068-feb41477e405*
*Created: 2026-06-19*

---

SESSION CHUNK 2026-06-18 — Opt-In Implementation with Dual Arrays and UI Language Alignment

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/main.py, C:/Users/Amos/projects/braindexer/setup_db.py, C:/Users/Amos/projects/braindexer/models.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/static/admin.html
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Read, Grep, Edit, Bash

SUMMARY
The opt-in visibility model was fully implemented across the database schema (migrations adding `shown_condition_ids` and `excluded_condition_ids` arrays, dropping the incorrect `condition_id` column), the six critical router endpoints (`get_therapy` display filtering, `update_news` UPSERT logic, `delete_news` moving conditions between arrays, `restore_news` reversing that move, `deleted-news` display, `backfill-sentiment`), and the admin.html Manage News modal. The UPSERT logic in `update_news` was carefully designed to handle three cases: new article (INSERT with shown array), existing article/new condition (append to shown), existing article/already-shown condition (no-op, silently skip). The modal vocabulary was updated to reflect the semantic shift from deletion/restoration to visibility management: "Hide" button for active articles (moves condition to excluded_condition_ids), "Include" button for hidden articles (moves condition back to shown_condition_ids), empty state text changed from "No removed articles" to "No hidden articles", and toasts changed from "Article removed/restored" to "Article hidden from/included in this condition". This language alignment ensures curators understand they're managing condition-scoped visibility, not performing permanent deletions. The solution scales cleanly: adding Parkinson's condition tomorrow results in zero articles appearing; curators fetch and include articles at their own pace. An article fetched for both Alzheimer's and Parkinson's exists as one row with both condition IDs in shown_condition_ids, conserving storage and dedup checking — the same URL fetched again for the same therapy/condition combination is silently skipped by the UPSERT WHERE clause.
