# WORLD PATTERN 2026-06-09 — Transient socket errors during streaming API response

*ID: passage-7c9bfd68-17b8-4c1f-bc2b-ee9f455df801*
*Created: 2026-06-10*

---

WORLD PATTERN 2026-06-09 — Transient socket errors during streaming API responses — 2026-06-10

PRINCIPLE: When a streaming API response is interrupted by transient socket disconnection, verify all local state changes were persisted, then resume from the exact point of interruption rather than restarting the entire operation.

NARRATIVE: During implementation of the condition-specific data architecture, the Anthropic API socket connection closed unexpectedly mid-response while rewriting `therapy.html`. Rather than assume all work was lost, the recovery involved: (1) confirming that all previously written files (`setup_db.py`, `models.py`, `services/summarizer.py`, `routers/therapies.py`, `services/scraper.py`) were safely persisted to disk, (2) identifying that only `therapy.html` had been in progress and not yet written, (3) continuing from that exact point with the `therapy.html` rewrite without losing any prior work. This pattern generalizes: streaming responses from language models that are interrupted do not cause loss of file state — only loss of the current in-flight response. The recovery strategy is to verify persistence of prior work, identify the exact resumption point, and continue without re-executing completed steps. This is distinct from general error handling because streaming responses have the property that context before the interruption is already written and safe.
