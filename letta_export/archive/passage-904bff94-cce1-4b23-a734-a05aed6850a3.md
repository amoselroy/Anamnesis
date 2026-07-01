# WORLD PATTERN 2026-06-07 — SessionEnd hooks cannot act on sleep-time agent outpu

*ID: passage-904bff94-cce1-4b23-a734-a05aed6850a3*
*Created: 2026-06-07*

---

WORLD PATTERN 2026-06-07 — SessionEnd hooks cannot act on sleep-time agent output — 2026-06-07

PRINCIPLE: Operations that depend on output from the sleep-time agent must run at SessionStart of the next session, not at SessionEnd of the current session, because the agent's processing happens between sessions.

NARRATIVE: MemShepherd's architecture intended to trim the world/patterns block (separate one-liners from full narratives) at session end, but investigation revealed a timing gap: the sleep-time agent runs *after* the SessionEnd export (`session_sync.py`), so exported files are always one cycle behind live blocks. The core issue: sessionized systems have a natural handoff point where one session's end precedes the next session's beginning, and asynchronous processing happens in that gap. Operations that depend on asynchronous output must run after that output is first available — at the next SessionStart, not the previous SessionEnd. This generalizes to any architecture combining session hooks with background processing: ensure dependencies run in the correct phase of the cycle, not at the logical phase in the source code.
