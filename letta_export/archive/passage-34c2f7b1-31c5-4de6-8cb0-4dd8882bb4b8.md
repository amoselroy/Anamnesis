# WORLD PATTERN 2026-06-17 — External endpoint-based scheduling decouples executio

*ID: passage-34c2f7b1-31c5-4de6-8cb0-4dd8882bb4b8*
*Created: 2026-06-18*

---

WORLD PATTERN 2026-06-17 — External endpoint-based scheduling decouples execution from server uptime — 2026-06-18

PRINCIPLE: Replacing in-process schedulers that depend on server uptime with external HTTP-triggered endpoints makes scheduled tasks reliably independent of infrastructure lifecycle.

NARRATIVE: Braindexer's therapy discovery wasn't firing because it relied on APScheduler running inside the FastAPI process scheduled for Sunday 3 AM. On Render's free tier, the server spins down on inactivity. When cron-job.org pings awakened it, the scheduler restarted with a fresh clock and missed its window every week. The solution: add HTTP endpoints secured with a curator key, let cron-job.org call them on an explicit schedule. This decouples the triggering from server uptime — the server can sleep normally, waking only when an external request arrives. The pattern generalizes: in-process schedulers are fragile when infrastructure is ephemeral; external triggers via HTTP endpoints are more reliable for operations that should survive infrastructure restart cycles. The trade-off is explicitness (cron-job.org owns the schedule, not buried in app config) versus coupling to an external service, but the trade usually favors reliability.
