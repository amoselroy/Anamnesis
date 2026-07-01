# WORLD PATTERN 2026-06-07 — Async operations require pending-file queuing when se

*ID: passage-4ddf1e96-3d89-4a22-b8b4-b54fbf76fb39*
*Created: 2026-06-07*

---

WORLD PATTERN 2026-06-07 — Async operations require pending-file queuing when session hooks must complete synchronously — 2026-06-07

PRINCIPLE: When a SessionStart hook needs to queue asynchronous work (database operations, external API calls), use a pending-file pattern rather than blocking on the async operation, so the hook can complete and injection can proceed without delay.

NARRATIVE: The world/patterns trimming operation needed to (1) split content (fast, synchronous), (2) patch the live block (fast, synchronous), and (3) insert full narratives to Neon (slow, asynchronous). If the hook blocked on the Neon insert, SessionStart would hang and injection would be delayed. The solution: write full narratives to a pending-file queue (synchronous), then have a separate async job process the queue. This is the same pattern used by `chunk_archive.py` for session data — the hook completes fast, async processing happens independently. The pattern generalizes: whenever a synchronous hook depends on async work, decouple them via a queue rather than blocking.
