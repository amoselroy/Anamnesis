# WORLD PATTERN 2026-06-24 — Render free-tier cold-start timeout manifesting as mi

*ID: passage-69560bc5-8cc5-44a2-b32c-32ccf5dbc96e*
*Created: 2026-06-24*

---

WORLD PATTERN 2026-06-24 — Render free-tier cold-start timeout manifesting as misleading API error codes — 2026-06-24

PRINCIPLE: When a serverless platform (like Render free tier) spins down during inactivity and takes 20+ seconds to wake up, the resulting timeout can be caught and misreported by downstream error handlers as a permanent failure (404), obscuring the true root cause (transient unavailability).

NARRATIVE: The Braindexer platform on Render free tier exhibited cold-start behavior: after inactivity, the next request would hang for 25 seconds while the service spun up. If the timeout occurred before startup completed, the API would fail with a timeout error. The frontend's generic error handler caught this and displayed "Therapy not found," making it appear as a code bug or missing data rather than a service-wake-up delay. The solution wasn't upgrading Render ($7/mo) but improving frontend error handling to distinguish transient errors and retry automatically while displaying "Service is starting up — please wait..." This pattern generalizes: cloud platforms with free/low-cost tiers often have spin-down behavior that causes initial timeouts. These should be handled at the client level with retry logic and appropriate messaging, rather than assuming they indicate permanent failures. The pattern also suggests that external cron-job keep-alives (pinging every 14 minutes) are more cost-effective than infrastructure upgrades for development/demo environments.
