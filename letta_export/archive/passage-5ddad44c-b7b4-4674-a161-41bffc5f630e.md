# WORLD PATTERN 2026-06-04 — Cloudflare bot protection is unbypassable via headles

*ID: passage-5ddad44c-b7b4-4674-a161-41bffc5f630e*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Cloudflare bot protection is unbypassable via headless browsers — 2026-06-04

When a website returns 403 Forbidden errors, attempts to bypass via playwright-stealth (hiding automation signals) or changing user-agent headers are ineffective against genuine Cloudflare protection. Playwright with stealth, real Chrome via CDP, or other browser automation will all fail identically. The only proven bypass is controlling a real user's browser session (via MCP tools like Claude-in-Chrome or manual interaction). For unattended scrapers running at 3 AM, Cloudflare-protected sites are not accessible. Practical approach: detect 403 responses and skip the source gracefully (log 0 events, move to next source in ~2 seconds). If a site becomes accessible later, the scraper will automatically start returning results on the next rotation without code changes. This is preferable to investing effort in bypasses that won't work long-term.
