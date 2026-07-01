# WORLD PATTERN 2026-06-10 — Broken SessionEnd hook chains cause silent memory syn

*ID: passage-02e05d9b-521e-4daf-9e99-f4dfc1fb9545*
*Created: 2026-06-11*

---

WORLD PATTERN 2026-06-10 — Broken SessionEnd hook chains cause silent memory synchronization drift — 2026-06-11

PRINCIPLE: When system crashes interrupt the SessionEnd hook chain, pending work queued for processing never gets executed, causing memory exports to fall out of sync with live state indefinitely.

NARRATIVE: Forced PC restarts and session compactions broke the chain of SessionEnd hooks that were supposed to queue `.pending.json` files for the worker process to consume. Even though blocks like orientation and pins were being updated in Letta, the background worker had nothing to process and silently left the anamnesis backup unchanged. This drift wasn't detected because the blocks remained functional in the live system — they just weren't being exported. Investigation revealed the memory export had a known gap since May 18 where orientation and pins weren't even in the batch export list. The combination of two failures (broken hook chain + incomplete export configuration) created a silently diverging system. This pattern recurs whenever a system has asynchronous background processing: a broken queue or pending job mechanism combined with incomplete batch export configuration can cause persistent synchronization drift without warnings.
