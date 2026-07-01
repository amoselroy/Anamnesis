# WORLD PATTERN 2026-06-22 — Static HTTP agency URLs migrating to JavaScript-rende

*ID: passage-540fc15e-f851-4ffd-9bc1-1c9de90be657*
*Created: 2026-06-23*

---

WORLD PATTERN 2026-06-22 — Static HTTP agency URLs migrating to JavaScript-rendered sites breaks HTTP-based automation — 2026-06-23

PRINCIPLE: Government and regulatory agencies migrating from static document URLs to JavaScript-rendered SPAs break HTTP-based scraping without providing equivalent programmatic access, requiring either browser automation, local processing, or accepting stale data.

NARRATIVE: EMA's medicines data was initially accessible via static Excel download URL (`/en/documents/report/medicines-output-medicines-report_en.xlsx`). Between January and June 2026, EMA completely migrated their website to a Drupal-based SPA. The old URL now returns 404. Investigation via Wayback Machine confirmed the path no longer exists; their new download interface is JavaScript-rendered, not accessible via plain HTTP requests. Three options: (1) Wayback archive (7 months stale, won't capture changes), (2) Playwright browser automation (adds 150-350MB memory, risky on 512MB Render free tier), (3) run EMA download locally as separate process, then import file. The root cause: as government agencies modernize web infrastructure, they're moving toward SPA/JS rendering for all content, which breaks the assumption that data is available at stable HTTP URLs. This pattern will likely recur as more agencies modernize. Mitigation: identify agency data sources early, document their exact access model (static URL vs. API vs. JS-rendered), and have contingency for URL breakage (local backup, Wayback fallback, or scheduled testing to detect 404s).
