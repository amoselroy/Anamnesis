# SESSION CHUNK 2026-05-16 — <channel source="matrix" room_id="!GSOZZxCxJSCyQCaGsP

*ID: passage-31f7133e-0f8e-4d63-a19f-0b27a7aacbcd*
*Created: 2026-05-16*

---

SESSION CHUNK 2026-05-16 — <channel source="matrix" room_id="!GSOZZxCxJSCyQCaGsPh-Eh0DrnnNZeAaRX5Cau-GZJ8" 

STRUCTURED
Files: C:\Users\Amos\.claude\settings.json, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_memshepherd.md, C:\Users\Amos\.claude\memshepherd\hooks\chunk_archive.py
Errors: <tool_use_error>InputValidationError: Grep failed due to the following issue:
An
Tools used: PowerShell, Read, Bash, Edit, mcp__matrix__reply, Grep

SUMMARY
**2026-05-16 Late Evening: Architectural Correction — Semantic Chunking vs. Fixed-Length Splitting**

Session focused on finalizing the MemShepherd chunk archival design after the successful deferred-queue implementation. Amos raised a critical question about whether chunking saves all semantic chunks or just the first one.

**Critical Discovery**: Amos identified a fundamental flaw in my implementation. I had implemented fixed-length chunking (`CHUNK_MAX_TURNS = 15`) that splits sessions arbitrarily at 15-turn intervals regardless of semantic boundaries. Amos immediately recognized this defeats the entire architectural purpose.

**Design Principle Clarification**: The whole MemShepherd redesign is built around context_watch.py's semantic boundary detection — the PostToolUse hook already identifies natural breaking points by scoring context saturation (score 3-4 indicates a true boundary). The chunking strategy should USE those boundaries, not ignore them:

- **Semantic boundaries** detected by context_watch → those are the chunk break points
- **Each semantic chunk** (from one boundary to the next) should be archived individually
- **Multiple chunks per pre-compact** are expected and correct (if context_watch fired multiple boundaries during the session)
- **Multiple chunks before session end** may also exist (remainder of transcript after last PreCompact)

**The Flaw**: Fixed-length 15-turn splits are arbitrary and orthogonal to semantic structure. A 15-turn chunk might span multiple logical boundaries or cut a single coherent narrative in the middle. This violates the principle that archival entries should align with the natural "thought units" that context_watch identified as saturation points.

**Correct Approach** (deferred): The chunking should respect context_watch's boundary scores. Rather than `CHUNK_MAX_TURNS`, the split should occur at context boundaries that context_watch already identified. This requires integrating with the context_watch scoring system or using the PreCompact hook's state to know where boundaries occurred.

**Current Status**: The deferred-queue architecture is sound (queueing at PreCompact/SessionEnd, processing at SessionStart). But the sub-chunking logic needs redesign to use semantic boundaries instead of fixed turn counts.

**Key Insight**: Amos's challenge "Do you see how that defeats our whole design?" identifies the tension between operational simplicity (fixed chunks are easy) and architectural integrity (semantic chunks preserve meaning and context structure). The solution must honor both the boundary detection already in place AND archive each semantic unit separately.
