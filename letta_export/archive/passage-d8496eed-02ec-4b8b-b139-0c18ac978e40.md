# Session wrap-up design principle â€” what to do at clear session end (2026-05-08

*ID: passage-d8496eed-02ec-4b8b-b139-0c18ac978e40*
*Created: 2026-05-08*

---

Session wrap-up design principle â€” what to do at clear session end (2026-05-08)

When a clear session-end signal appears (good night, explicit close):

DO: Let sleep-time Letta handle synthesis automatically. session_end.py delivers transcript; sleep-time companion fires within ~1 min; updates persona, patterns, world knowledge blocks. No trigger needed.

DO: Manual archival_insert.py calls for specific facts worth searching later â€” design decisions, verified fixes, technical discoveries. Sleep-time updates memory blocks, not the archival search index.

DON'T: Run /compact â€” pointless at true session end. Session is closing; there is no context window to free for continuation.

DON'T: Trigger the full context_watch boundary logic manually â€” it will fire automatically if threshold is crossed, and at true session end the JSONL growth stops anyway.

The gap sleep-time doesn't cover: searchable archival memory. If the session produced something specific and retrievable-later, insert it manually before closing.
