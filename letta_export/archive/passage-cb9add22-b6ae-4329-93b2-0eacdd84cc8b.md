# SESSION CHUNK 2026-07-13 — MemShepherd 422 Error Root Cause — SessionEnd Async R

*ID: passage-cb9add22-b6ae-4329-93b2-0eacdd84cc8b*
*Created: 2026-07-13*

---

SESSION CHUNK 2026-07-13 — MemShepherd 422 Error Root Cause — SessionEnd Async Race Condition

STRUCTURED
Files: none
Errors: none
Tools used: Read, Bash

SUMMARY
Amos arrived for a new session but encountered a 422 error on MemShepherd's orientation call, with Letta container and memory system appearing unavailable. Initial investigation suggested a restart might be needed. However, Assistant verified that the container was actually healthy (10 days uptime, port 8283 responsive), meaning the 422 was not a service-down issue but something more subtle.

Amos then clarified the actual problem: he had exited the previous session and immediately started a new one without letting the async session-end process complete. This revealed the architectural timing issue. The MemShepherd SessionStart hook triggers `chunk_archive.py --process-queue` asynchronously to drain the prior session's queued memory writes (pins, world, orientation data) before the new session's orientation load attempts to fetch a consistent snapshot. When sessions start back-to-back without adequate spacing, the new session's orientation call fires while the previous session's async worker is still mid-drain or holds a lock, causing the request to fail with a 422 (bad request). This is a race condition on shared state between the SessionEnd async worker and SessionStart's synchronous orientation load.

The solution is straightforward: introduce a real time gap between session exit and session restart to allow the async queue processor to complete its work cleanly before the next session attempts to load state. This is a pattern worth remembering — the system is working as designed, but the human-controlled timing between sessions must respect the worker lifecycle.
