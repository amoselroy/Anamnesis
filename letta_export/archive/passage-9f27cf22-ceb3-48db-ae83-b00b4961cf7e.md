# WORLD PATTERN 2026-07-17 — Centralized auth patterns require explicit propagatio

*ID: passage-9f27cf22-ceb3-48db-ae83-b00b4961cf7e*
*Created: 2026-07-28*

---

WORLD PATTERN 2026-07-17 — Centralized auth patterns require explicit propagation across repo boundaries — 2026-07-17

PRINCIPLE: When authentication requirements change centrally, pre-existing code in separate repositories that predates the centralization won't automatically inherit the new pattern, creating islands of silently-failing API calls.

NARRATIVE: MemShepherd's centralized Letta ops pattern was introduced on 2026-07-15 with letta_ops.py and 12 scripts in the hooks repository were updated to use it. However, session_sync.py in the separate private anamnesis repository predates this centralization and was never retrofitted. When the Letta container was hardened with SECURE=true, all API requests required Authorization headers — a requirement the new letta_ops.py handled automatically for callers that used it. But session_sync.py's fetch_blocks() function still made bare HTTP requests without the header. The hooks ran without raising errors; the actual operation failed silently — exports stopped accumulating on July 14th while the health monitor correctly detected the real problem (export lag) and blocked its own heartbeat. The gap wasn't discovered for 12 days because the symptom (missing exports) didn't produce a loud failure signal — it was detected only by monitoring the gap between last-processed-session and last-exported-commit. The pattern generalizes: when infrastructure changes propagate across a deployed system, code living in separate repositories becomes invisible to automatic updates. The fix requires explicit enumeration and retrofit of all auxiliary services, integration testing that exercises the external API path, and monitoring that detects silent API failures (401, 403 misconfigurations) rather than relying on missing output to surface the problem.
