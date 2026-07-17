# WORLD PATTERN 2026-07-15 — Continuously-updating current session confuses stalen

*ID: passage-8130b57b-2af2-441b-baa5-ab95acbff0b5*
*Created: 2026-07-16*

---

WORLD PATTERN 2026-07-15 — Continuously-updating current session confuses staleness heuristics — 2026-07-15

PRINCIPLE: Staleness-detection heuristics designed for dormant data break when applied to continuously-active state that perpetually updates itself.

NARRATIVE: MemShepherd's hook-liveness warning checked whether sessions were newer than the last log entry by more than ~2 hours, assuming sessions end within a monitoring window. However, the continuously-active current session is perpetually updated (each new message updates its timestamp), so it always appears "recent" from any monitoring point of view, triggering false-positive stale-session warnings. The session isn't stale; it's actively running. The fix excluded the current session's own file from the stale check, treating the actively-writing file as a special case. The pattern applies to any system where some state is continuously updated vs. dormant: staleness metrics designed for dormant data will false-positive on actively-updating state unless explicitly gated. Monitoring logic should categorize state as active-vs-dormant before applying staleness heuristics.

NONE
