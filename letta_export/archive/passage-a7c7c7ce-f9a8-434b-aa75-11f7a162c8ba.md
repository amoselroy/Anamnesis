# WORLD PATTERN 2026-09-22 — Trusted-entity whitelist protecting legitimate contac

*ID: passage-a7c7c7ce-f9a8-434b-aa75-11f7a162c8ba*
*Created: 2026-11-12*

---

WORLD PATTERN 2026-09-22 — Trusted-entity whitelist protecting legitimate contacts in adversarial-input systems — 2026-09-22

PRINCIPLE: When a system must distinguish between adversarial and legitimate inputs arriving through the same channel, an explicit whitelist exempts known-legitimate sources from triggering adversarial-mode logic.

NARRATIVE: The Telegram scam-baiting bot monitors all incoming DMs for money-request phrases (gift card mentions, wire transfers, payment apps). However, Amos's legitimate Telegram friends should never be engaged as if they were scammers. The trusted_contacts.txt whitelist holds chat IDs of known friends, and messages from whitelisted contacts bypass both auto-trigger detection (they don't activate the LLM scam-baiting) and manual forcing into bot/auto modes (they cannot be accidentally or deliberately engaged as scam targets). The whitelist is verified by chat ID (printed to console on each message, allowing Amos to collect and curate the list). The pattern applies broadly: any system that must process inputs from mixed legitimate and adversarial sources benefits from an explicit whitelist that carves out protected entities, preventing the system from treating legitimate participants as threats merely because they share the same input channel as actual threats. The whitelist is an architectural boundary, not a performance optimization.
