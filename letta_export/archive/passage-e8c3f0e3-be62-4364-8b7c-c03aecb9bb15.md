# WORLD PATTERN 2026-07-04 — Rebuild vs. debug under infrastructure opacity — 2026

*ID: passage-e8c3f0e3-be62-4364-8b7c-c03aecb9bb15*
*Created: 2026-07-08*

---

WORLD PATTERN 2026-07-04 — Rebuild vs. debug under infrastructure opacity — 2026-07-04

PRINCIPLE: When a system's state is opaque to inspection and fails silently, the cost-benefit calculation inverts: rebuilding from scratch can be faster than debugging something you cannot reliably observe.

NARRATIVE: FB_Poster tasks displayed as active in Task Scheduler UI but produced no posts. Investigation revealed the tasks were visible in the MMC snap-in but invisible to all query tools—PowerShell, schtasks.exe, raw COM enumeration all returned different counts. The divergence between what the UI claimed and what the tools could find meant the debugging surface itself was corrupted. Rather than continue chasing phantom tasks, the user deleted the broken registration and recreated it fresh. The new tasks worked immediately. The decision wasn't resolving the underlying corruption; it was recognizing that opacity made debugging untrustworthy. Under those conditions, the cost of rebuilding (delete + recreate) is lower than the cost of debugging (investigating caches, registry corruption, orphaned references). This pattern applies anywhere the system's observability is compromised: corrupted caches, missing audit trails, UI-state divergence. When you cannot reliably see what the system is doing, rebuilding becomes the pragmatic path forward.
