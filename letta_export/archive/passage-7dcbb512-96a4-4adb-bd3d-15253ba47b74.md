# WORLD PATTERN 2026-06-10 — Consolidating multiple outputs in single API call — 2

*ID: passage-7dcbb512-96a4-4adb-bd3d-15253ba47b74*
*Created: 2026-06-10*

---

WORLD PATTERN 2026-06-10 — Consolidating multiple outputs in single API call — 2026-06-10

PRINCIPLE: When extending an existing API call to return additional fields, structure the response as a single JSON object with all fields rather than making parallel calls, preserving request efficiency while expanding information richness.

NARRATIVE: The `assess_therapy` function was extended to return not just the original four score fields (therapeutic_action, effectiveness_score, evidence_score, safety_score) but also pathway_tags — without increasing the number of API calls or the token cost, because all five outputs come from a single Claude API invocation returning structured JSON. This is distinct from "batch multiple requests" because it leverages the fact that a single reasoning process can output multiple structured fields. The pattern generalizes: when a model is already analyzing content for one output, adding related outputs to the same response is nearly free. This applies across summarization (return summary + extracted entities in one call), assessment (return multiple scores together), and any other structured extraction task.
