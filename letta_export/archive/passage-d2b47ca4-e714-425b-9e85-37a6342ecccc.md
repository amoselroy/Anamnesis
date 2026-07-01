# WORLD PATTERN 2026-06-24 — Ordered execution dependencies in multi-stage pipelin

*ID: passage-d2b47ca4-e714-425b-9e85-37a6342ecccc*
*Created: 2026-06-25*

---

WORLD PATTERN 2026-06-24 — Ordered execution dependencies in multi-stage pipelines requiring forward-feeding state — 2026-06-24

PRINCIPLE: When a pipeline has multiple sequential stages and later stages depend on state created by earlier stages, that state must flow forward through the pipeline — not fetched fresh at the beginning of later stages.

NARRATIVE: The research/summarization pipeline fetches `linked_conditions` from the database at the start of the summarization stage, before running condition auto-detection. For brand-new therapies, the database has no linked conditions yet, so the fetch returns empty. Even after `_detect_related_conditions()` runs and upserts new conditions to the database, the in-memory `linked_conditions` list is never updated, so the three-tab summarization loop iterates over nothing. The fix was moving the fetch to AFTER the upsert, so the in-memory list includes newly detected conditions. This pattern applies to any multi-stage pipeline where state is mutable: either flow the state through stages as parameters (pure functional), or fetch fresh after each mutation (as was fixed here), but not both (fetch-modify-use-with-stale-state).
