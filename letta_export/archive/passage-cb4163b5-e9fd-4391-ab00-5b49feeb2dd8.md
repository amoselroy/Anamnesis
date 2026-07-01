# WORLD PATTERN 2026-06-17 — LLM JSON extraction returning empty arrays with trail

*ID: passage-cb4163b5-e9fd-4391-ab00-5b49feeb2dd8*
*Created: 2026-06-17*

---

WORLD PATTERN 2026-06-17 — LLM JSON extraction returning empty arrays with trailing explanation text — 2026-06-17

PRINCIPLE: LLM listing extraction sometimes returns valid JSON (empty array `[]`) followed by explanation text, which breaks `json.loads()` parsing despite the JSON being structurally correct.

NARRATIVE: When investigating Hoboken Recreation's zero-yield result, the LLM fallback was returning `"Extra data: line 2 column 1"` error. This occurs when the LLM returns a legitimate JSON array but appends explanation or reasoning text after it (e.g., `[]` followed by "No events found because..." or similar). The `json.loads()` parser reads the closing `]` successfully but then encounters unparseable trailing text. A one-line fix was identified: strip any text after the closing bracket before parsing. This pattern affects any LLM-based listing extraction that returns JSON, not just event scrapers, and is worth defensive handling globally.
