# WORLD PATTERN 2026-07-08 — Content-hashed primary keys as defense against timeou

*ID: passage-a9ced665-279e-463b-a0a4-d6da00ff8b17*
*Created: 2026-07-13*

---

WORLD PATTERN 2026-07-08 — Content-hashed primary keys as defense against timeout-masked operation failures — 2026-07-08

PRINCIPLE: When external APIs mask operation failures as success (reporting timeout as success rather than error), index-based targeting becomes unsafe; content-hash-based primary keys make operations immune to index shifts caused by silent failures.

NARRATIVE: During MemShepherd pin reconciliation, accidental deletions occurred when PATCH timeout exceptions were caught and naively retried. The retry logic operated on indices queried before the initial failure, but Letta's API masks timeouts as HTTP 200 (operation succeeded when it actually didn't). Some pins failed to delete silently, leaving the returned array unchanged, but the retry logic assumed the array had shifted — indices became stale. Rewriting `reconcile_pins.py` to use SHA256 content hashes (first 8 hex chars) as primary keys eliminated index sensitivity. Each operation now targets content directly: "delete the pin with hash abc12345" rather than "delete the 5th item." Mismatches are detected and refused rather than silently hitting the wrong target. This pattern applies universally to CRUD operations against systems with timeout masking, eventual consistency windows, or any failure mode that reports success while changing nothing — content-based addressing decouples correctness from operation sequencing.
