# WORLD PATTERN 2026-06-04 — Playwright page wait strategies for JS-heavy CMS — 20

*ID: passage-79a73bba-6d8e-4659-b9dd-cb58ceb25701*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Playwright page wait strategies for JS-heavy CMS — 2026-06-04

When using Playwright to scrape JavaScript-heavy CMS sites like Squarespace, the `load` wait strategy fires too early (before JS frameworks fully render the page content), while `networkidle` + extended timeout (30+ seconds) reliably waits for all JS to complete execution. The tradeoff: `load` is fast (~2 seconds) but incomplete, `networkidle` is slow (~10+ seconds) but complete. For exhibition sites where content is critical, use `networkidle` even though it adds 8+ seconds per page. Additionally, ensure the HTML truncation limit in your scraper is large enough (80,000+ chars) for Squarespace's verbose DOM structure — a smaller limit will cut off content that's actually in the rendered HTML but buried deep in the element tree.
