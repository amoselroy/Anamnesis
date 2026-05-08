# context_watch.py â€” boundary detection architecture (2026-05-08)

*ID: passage-f55a5d4d-de51-49ce-898e-be02a250f507*
*Created: 2026-05-08*

---

context_watch.py â€” boundary detection architecture (2026-05-08)

PostToolUse hook monitoring session transcript size. File: C:\Users\Amos\.claude\memshepherd\hooks\context_watch.py

Trigger: JSONL > 320KB (THRESHOLD_BYTES). Re-evaluation every +150KB (RECHECK_BYTES), or +320KB after a strong boundary fires (post-compact breathing room). State tracked in TEMP/memshepherd_ctx_{session_id}.json as {next_check_at: bytes}.

4-point boundary scorer (last 30 JSONL entries):
  +1 recent user message is confirmatory
  +1 last 5 tool calls are read-only (no Edit/Write)
  +1 no tool errors in recent turns
  +1 3+ turns since last write mutation (or no writes in window)

Score routing:
  0-1: LIKELY MID-TASK â€” silent exit (no Letta call)
  2: POSSIBLE BOUNDARY â€” calls Letta primary agent for semantic YES/NO evaluation
  3-4: STRONG BOUNDARY â€” fires advisory directly

--verbose flag (enabled in settings.json): includes size, %, signals, Letta assessment. Brief mode: one-liner.

Replay validation against real sessions: would have caught cc332f66 at 316KB and 632KB (both STRONG BOUNDARY). Mid-session implementation work (1095-1554KB) correctly suppressed.
