# SESSION CHUNK 2026-05-18 — Documenting the Orientation/Pins Async Injection Desi

*ID: passage-baed5bf5-fc1d-49e7-9114-8e4953bfa39e*
*Created: 2026-05-20*

---

SESSION CHUNK 2026-05-18 — Documenting the Orientation/Pins Async Injection Design Rationale

STRUCTURED
Files: C:\Users\Amos\.claude\memshepherd\hooks\_patch_pins.py, C:\Users\Amos\.claude\memshepherd\MODIFICATIONS.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_memshepherd.md, C:\Users\Amos\.claude\memshepherd\hooks\_patch_world.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\feedback_search_before_concluding.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md
Errors: Exit code 2
/usr/bin/bash: eval: line 1: unexpected EOF while looking for matchi; Exit code 1
Error: HTTP Error 400: Bad Request; Exit code 1
Traceback (most recent call last):
  File "<string>", line 9, in <m; <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Glob, Read, Bash, Grep, Write, Edit, ToolSearch, mcp__matrix__reply
Dates: june 1

SUMMARY
Amos pointed out that the rationale for the async hook injection design—why `output_orientation_pins()` was meant to fire at the end of the worker process rather than load synchronously in `session_start.py`—had not survived in the archival narratives. Through investigation, Daimon found the reasoning in MODIFICATIONS.md and project memory: loading orientation/pins synchronously in session_start.py would give stale blocks (one session behind), because the worker that updates them runs after session_start.py. The async injection defers loading to the worker so fresh blocks—reflecting the immediately previous session rather than two sessions back—get injected.

This led to a broader realization about gaps in the archival system: the archive narratives capture high-level intent but often lose specific design tradeoffs and rationales. The new blocks (orientation and pins) hadn't been added to the anamnesis export list in session_sync.py, and the design decisions behind them weren't preserved with enough depth. Daimon updated MODIFICATIONS.md with a full incident log, appended a pin to the pins block to revisit the design post-June 1, and updated project_memshepherd.md so the investigation and known gaps would be discoverable from multiple entry points in memory.
