# SESSION CHUNK 2026-05-16 — Semantic Chunking Design — Rejecting Mechanical Split

*ID: passage-9236d21c-3f1a-4ed0-bbb7-ee310d9ed77e*
*Created: 2026-05-17*

---

SESSION CHUNK 2026-05-16 — Semantic Chunking Design — Rejecting Mechanical Splits, Implementing LLM-Driven Boundaries

STRUCTURED
Files: C:\Users\Amos\.claude\memshepherd\hooks\chunk_archive.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_memshepherd.md, C:\Users\Amos\.claude\memshepherd\MODIFICATIONS.md
Errors: Exit code 128
fatal: not a git repository (or any of the parent directories): .g; Exit code 127
/usr/bin/bash: line 1: Get-Item: command not found
/usr/bin/bash: ; Exit code 2
/usr/bin/bash: eval: line 1: unexpected EOF while looking for matchi
Tools used: Read, Write, ToolSearch, mcp__matrix__reply, Edit, Bash, Glob, PowerShell
URLs: http://localhost:8283"
Dates: 2026-05-16

SUMMARY
NARRATIVE SUMMARY:

With the timeout problem solved, focus shifts to how large session blocks should be split for archival. Initial implementation used a fixed-count approach: `CHUNK_MAX_TURNS=15`, cutting the transcript into chunks regardless of where semantic boundaries actually occur.

**Amos's Critical Objection**: "Do you see how that defeats our whole design?" — pointing out that imposing mechanical boundaries (15-turn chunks) obliterates the semantic structure. A session might have three distinct topics that happen to span 18 turns, or one coherent narrative that spans 25 turns. Cutting at turn 15 creates fragmented archives that don't reflect the actual shape of the conversation.

**Design Correction**: Remove all splitting from the hook. Instead, the hook writes ONE pending file with the full block. The worker (which already calls Letta for narrative generation) asks Letta in a single call to identify genuine topic boundaries and generate a separate narrative for each semantic section. The prompt explicitly instructs Letta to look for "genuine topic shifts" not mechanical turn counts.

**Implementation**: New `segment_and_narrate()` function replaces the old `generate_narrative()`. Letta returns sections delimited by `
