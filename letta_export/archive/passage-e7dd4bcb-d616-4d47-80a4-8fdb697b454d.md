# WORLD PATTERN 2026-08-12 — Recovery-sequence detection preventing monitor false-

*ID: passage-e7dd4bcb-d616-4d47-80a4-8fdb697b454d*
*Created: 2026-08-12*

---

WORLD PATTERN 2026-08-12 — Recovery-sequence detection preventing monitor false-positives — 2026-08-12

PRINCIPLE: Monitoring systems flagging transient failures as permanent can be corrected by detecting when successful recovery immediately follows the failure marker.

NARRATIVE: Monitor.py was reporting Hoboken Now as permanently failed (5-for-5) despite the scraper having successfully bypassed a bot challenge on 2026-08-08 with returning results. The failure flag never reset because the code detected "Bot challenge page detected" and marked the source failed without checking whether a subsequent success/recovery line followed. The fix was detecting the pattern "failure marker followed by recovery/success line" and resetting the failure state when found. This transforms monitoring from a one-way ratchet (once flagged, always flagged) to a state machine accounting for transient events and recovery. The pattern applies wherever monitoring systems aggregate signals across time without checking whether those signals have been resolved.
