# WORLD PATTERN 2026-06-09 — Curator override authority with AI inference — 2026-0

*ID: passage-7c4ec496-aa73-4a71-af5d-b60abbc932f2*
*Created: 2026-06-09*

---

WORLD PATTERN 2026-06-09 — Curator override authority with AI inference — 2026-06-09

PRINCIPLE: When AI auto-infers structured fields, use conditional logic to allow AI to promote values but never demote human edits, and only fill optional fields if currently empty, preserving curator authority.

NARRATIVE: When implementing AI assessment scoring for the Rosemary therapy, the system correctly inferred therapeutic properties but failed to set the `self_administrable` flag despite clear evidence in sources. Rather than simply letting AI overwrite all fields on each Research & Summarize run, the architecture needed to respect that if a curator had deliberately set `self_administrable = true`, subsequent AI runs should never demote it back to false. This led to using CASE expressions in SQL UPDATE statements: `self_administrable = CASE WHEN assess_result['self_administrable'] THEN true ELSE COALESCE(current_value, false) END`. Similarly, optional notes fields like `self_admin_notes` are only populated by AI if currently null, preserving curator-written explanations. This pattern generalizes beyond Braindexer: any system combining AI inference with human editorial control needs asymmetric permission — AI can suggest and promote values, but human edits remain authoritative and sticky across multiple AI runs.
