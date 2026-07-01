# WORLD PATTERN 2026-06-07 — Documented architecture without runtime enforcement c

*ID: passage-f9b31bdf-2ada-4bd1-aa34-7c5ab5497218*
*Created: 2026-06-07*

---

WORLD PATTERN 2026-06-07 — Documented architecture without runtime enforcement creates feature debt — 2026-06-07

PRINCIPLE: When a design pattern is documented in source code or configuration but has no active enforcement mechanism, the pattern will drift and debt will accumulate silently.

NARRATIVE: The world/patterns block itself documents the principle that it should contain "compact one-liner principles only" with "full three-level narratives stored in Neon archival memory." This design intent was clear. But no hook existed to enforce the split. The result: the live block grew to 20,720 characters with full narratives intact, the spillover archive existed but was never populated, and the documented architecture became historical record rather than enforced practice. The fix required building the actual mechanism (a SessionStart hook that reads the block, splits content, and queues archival). The lesson: documentation without enforcement is a future maintenance burden. Either enforce the pattern with automation, or accept that the pattern won't hold.
