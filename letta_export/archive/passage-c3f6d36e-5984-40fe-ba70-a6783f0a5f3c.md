# WORLD PATTERN 2026-06-10 — Configuration gaps in batch export lists silently bre

*ID: passage-c3f6d36e-5984-40fe-ba70-a6783f0a5f3c*
*Created: 2026-06-11*

---

WORLD PATTERN 2026-06-10 — Configuration gaps in batch export lists silently break data synchronization — 2026-06-11

PRINCIPLE: Missing entries in a batch export configuration list will silently prevent those data types from being backed up, and this gap won't be detected unless explicitly verified.

NARRATIVE: The session_sync.py file had a `BLOCK_FILES` list that controlled which Letta memory blocks were exported to anamnesis for backup. The orientation and pins blocks (created on May 18) were never added to this list, so they never got exported despite being updated regularly in the live system. The gap went undetected for months because the blocks still functioned normally — only the backup was missing. When system crashes broke the SessionEnd hook chain, the live blocks became the source of truth but had no backup to restore from. This pattern affects any system with batch export or bulk synchronization: configuration lists must be explicitly audited when new data types are introduced, because omissions don't produce errors — they produce silent data loss in the backup layer.
