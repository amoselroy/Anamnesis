# SESSION CHUNK 2026-06-18 — Side Effects Severity as a Distinct Indicator and Com

*ID: passage-f739ae11-0d64-4bc0-8fff-e8bd6959b6de*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — Side Effects Severity as a Distinct Indicator and Comprehensive Tooltip Infrastructure

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/models.py, C:/Users/Amos/projects/braindexer/setup_db.py, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/main.py
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Edit, Read, Bash, Grep, Glob
URLs: https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en`

SUMMARY
Building on the literature signals foundation, Amos requested a dedicated side effects severity indicator, emphasizing that side effects (discomfort, fatigue, nausea) are distinct from safety (cardiac events, mortality, loss of function). This prompted a planning conversation to ensure coherence across all indicators before building. The final plan established clear distinctions: Safety (1–5 curator) covers serious outcomes; Side Effects (1–5 AI-derived) covers non-life-threatening adverse effects; Overall Assessment (1–5 AI-derived) synthesizes effectiveness + safety + side effects equally. A new `side_effects_score` column was added to `therapy_conditions`, and `assess_therapy_signals()` was extended to return four outputs from one Haiku call: `effectiveness`, `safety`, `side_effects_score`, and `overall_score`. Simultaneously, hover tooltips were added to every dashboard card with the ⓘ icon. Each tooltip showed the full 1–5 scale with human-readable labels (e.g., Effectiveness: 1 = No evidence → 5 = Strong evidence; Safety: 1 = Significant risk → 5 = Excellent safety). AI-derived cards included the disclosure "AI-assessed from indexed source titles — not a clinical evaluation." The LLM prompt was refined to distinguish side effects from safety explicitly and to describe the overall_score as equal-weighted synthesis. All changes (schema, prompt, DB writes across both scraper and routers, models, dashboard CSS and labels) were deployed in one pass. The result: six indicators covering curator judgment (Effectiveness, Evidence, Safety), AI-derived signals (two qualitative signals, side effects score, overall score), with full transparency via tooltips.
