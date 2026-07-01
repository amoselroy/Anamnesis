# WORLD PATTERN 2026-06-04 — Playwright for progressive scraper fallback — 2026-06

*ID: passage-d4c09cd6-b2d0-4d26-87fd-85168abd8a6a*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Playwright for progressive scraper fallback — 2026-06-04

When building a scraper that needs to handle both static HTML and JavaScript-rendered content across many heterogeneous sources, implement layered extraction paths: (1) static requests with CSS/regex parsing for plain HTML sites; (2) LLM-assisted extraction for listing pages when static parsing yields nothing; (3) Playwright rendering as an automatic fallback when paths 1 and 2 both return 0. The three-path approach balances cost (Playwright is expensive at ~0.75s per page, but only fires for genuinely JS-dependent sites) with reliability (guaranteed extraction across all source types). Implementation: trigger Path C when both A and B yield 0 events from a given source. Use one lazy-initialized browser instance per scraper run, reuse across all sources, close in a `finally` block to ensure cleanup. Detail pages on JS-heavy sites (like Squarespace) may require `networkidle` wait strategy instead of `load` to allow JavaScript to fully execute before scraping; test empirically on problem sites and adjust wait strategy per-source if needed.
