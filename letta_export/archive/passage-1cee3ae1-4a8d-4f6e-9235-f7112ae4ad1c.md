# SESSION CHUNK 2026-06-18 — Opt-Out vs Opt-In Visibility Model Decision for Multi

*ID: passage-1cee3ae1-4a8d-4f6e-9235-f7112ae4ad1c*
*Created: 2026-06-19*

---

SESSION CHUNK 2026-06-18 — Opt-Out vs Opt-In Visibility Model Decision for Multi-Condition Article Associations

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/main.py, C:/Users/Amos/projects/braindexer/setup_db.py, C:/Users/Amos/projects/braindexer/models.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/static/admin.html
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Read, Grep, Edit, Bash

SUMMARY
The critical realization emerged during the design discussion: the choice between opt-out (articles visible everywhere by default, curator hides from specific conditions) and opt-in (articles invisible everywhere by default, curator explicitly includes for specific conditions) had enormous implications for curation workflow. Under opt-out, adding a new condition (e.g., Parkinson's) tomorrow would instantly flood the new condition view with hundreds of Alzheimer's-specific articles that had never been intended for that condition — curators would face an immediate burden of removing hundreds of incorrect associations. Under opt-in, adding a new condition creates a clean slate; curators fetch and build the pool at their own pace. Amos articulated this perfectly: "I would have to instantly clean out hundreds of therapy records in the opt-out scenario... I think it is better to opt-in over time than be suddenly inundated by a mass of items that need to be removed." The decision was made definitively in favor of opt-in, which required a dual-array design: `shown_condition_ids INTEGER[]` (conditions where the article is explicitly visible) and `excluded_condition_ids INTEGER[]` (conditions where it's been explicitly removed). This design also required adding a unique constraint on `(therapy_id, url)` to support UPSERT logic — when fetching an article that already exists but for a different condition, the new condition is appended to the existing row's shown array rather than creating a duplicate row.
