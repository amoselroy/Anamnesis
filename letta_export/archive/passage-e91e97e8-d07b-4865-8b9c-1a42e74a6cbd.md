# WORLD PATTERN 2026-09-22 — Unattended-action cap with automatic mode demotion fo

*ID: passage-e91e97e8-d07b-4865-8b9c-1a42e74a6cbd*
*Created: 2026-11-12*

---

WORLD PATTERN 2026-09-22 — Unattended-action cap with automatic mode demotion for bounded autonomy — 2026-09-22

PRINCIPLE: Autonomous systems can operate unattended up to a complexity threshold, then require human supervision to prevent drift.

NARRATIVE: In the Telegram scam-baiting bot, `auto` mode (LLM-drafted replies sent without human review) caps at 40 messages unattended; reaching the cap automatically demotes the bot to `bot` mode (supervised, requiring keypress approval per message). This pattern implements bounded autonomy without hard stops: the system is permitted to run independently until complexity or duration reaches a threshold that signals need for human oversight. The demotion is automatic and transparent—no external intervention required—yet transforms the system's capability. The pattern generalizes: any agent operating in adversarial or uncertain environments can be designed to self-limit autonomy at decision points where accumulated risk warrants a shift to supervision. The mechanism differs from hard timeouts or message caps that silently fail; it instead escalates the human's involvement in direct proportion to system activity, preserving functionality while capping unexamined drift.
