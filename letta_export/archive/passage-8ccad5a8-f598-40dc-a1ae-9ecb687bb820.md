# WORLD PATTERN 2026-06-04 — Augmented-Cities AR architecture — 2026-05-22

*ID: passage-8ccad5a8-f598-40dc-a1ae-9ecb687bb820*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Augmented-Cities AR architecture — 2026-05-22

GPS-triggered AR experiences require careful technology choice with cascading implications: WebAR (AR.js, 8th Wall, Zappar) enables zero-install but carries latency/perspective-correction tradeoffs; native (ARKit/ARCore) solves latency but requires app distribution. World-anchoring (character moves/scales with phone rotation and approach) is critical to immersion and highly sensitive to perspective correction—roll axis especially exposes failures because it's the least natural phone rotation for viewers. Alpha-channel transparency in video is the most technically consequential early decision. Two-phase strategy (Phase 1: WebAR explanatory videos at historic landmarks; Phase 2: native apps + ghost overlays with temporal perspective correction) defers complex features while validating core architecture via empirical MVP testing.
