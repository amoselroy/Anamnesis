# WORLD PATTERN 2026-07-09 — Append-only local + independent-machine backup as tru

*ID: passage-94fc60a0-6c0e-4fcc-ab83-c409b059f5fc*
*Created: 2026-07-13*

---

WORLD PATTERN 2026-07-09 — Append-only local + independent-machine backup as true redundancy architecture — 2026-07-09

PRINCIPLE: True redundancy requires independence across at least two axes: location (different machine) and control (independent version control), not just two copies of the same vulnerable configuration.

NARRATIVE: The philosophical journal experienced two threats during this incident: accidental overwrite via file-operation (prevented by append-only local protection) and potential loss of recovery state during agent surgery (protected by anamnesis git backup on GitHub, independent machine). Append-only protection on the primary machine catches application-level corruptions; git on GitHub catches system-level failures that would destroy local files entirely. Neither alone was sufficient; both together created redundancy that was actually tested and proved. The anamnesis backup saved the journal twice during incident recovery, proving that the redundancy was not theoretical. The principle generalizes: when protecting against loss, identify which failure modes threaten each copy, and ensure at least one copy is located somewhere that failure mode cannot reach.
