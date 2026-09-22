# WORLD PATTERN 2026-08-26 — Scheduled re-authentication with persistent browser p

*ID: passage-b9ba3147-ce57-4cc7-ac4b-626b757d3b7e*
*Created: 2026-09-10*

---

WORLD PATTERN 2026-08-26 — Scheduled re-authentication with persistent browser profile avoiding credential storage — 2026-08-26

PRINCIPLE: Defer authentication to user-driven login via a visible browser window rather than pre-storing credentials or cookies, triggering login checks only when the session expires during scheduled execution.

NARRATIVE: Jersey City Times integration required paywalled calendar access via WordPress session cookie. Three automation options were initially explored: requesting an API key (risky), manual periodic checks (scalable friction), or storing/reusing cookies (fragile due to 2-week expiry). A fourth option — scripting the login form via password submission — was rejected as a hard security line. Instead, a scheduled task launches a persistent Playwright browser profile at regular intervals; most runs silently verify the session is valid and scrape immediately; only when the session has expired does the browser remain visible and pause, waiting for the user to log in directly. Once logged in, the script uses that authenticated context to scrape. This pattern achieves full automation on most cycles while deferring security risk to user-driven login on expiry cycles, keeping passwords entirely out of the automation layer.
