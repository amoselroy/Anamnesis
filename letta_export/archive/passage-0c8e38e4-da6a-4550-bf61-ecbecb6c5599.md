# SESSION CHUNK 2026-05-28 — Implementing Two-Dimensional Engagement Scoring

*ID: passage-0c8e38e4-da6a-4550-bf61-ecbecb6c5599*
*Created: 2026-05-29*

---

SESSION CHUNK 2026-05-28 — Implementing Two-Dimensional Engagement Scoring

STRUCTURED
Files: C:\Users\Amos\projects\fb-poster\_remove_inman.py, C:\Users\Amos\projects\fb-poster\re_poster.py, C:\Users\Amos\projects\fb-poster\adaptive_terms.json, C:\Users\Amos\.claude\projects\C--WINDOWS-system32\memory\project_fb_poster.md
Errors: Exit code 127
/usr/bin/bash: line 1: del: command not found
Tools used: Read, Write, Bash, PowerShell, Edit, Agent
URLs: https://www.facebook.com/profile.php?id=61586443622077", https://www.housingwire.com/articles/fidelity-data-shows-record-retirement-savings-rising-roth-adoption/, https://www.housingwire.com/articles/new-home-sales-april-2026/, https://www.housingwire.com/articles/warren-bilt-payment-disruptions/, https://www.zillow.com/research/april-2026-new-home-sales-36365/, https://www.zillow.com/research/mortgage-rates-18722/, https://www.zillow.com/research/dual-agency-sale-price-36325/, https://www.housingwire.com/articles/fha-zero-down-loans-risk/, https://www.zillow.com/research/april-2026-rent-report-36354/
Dates: May 30, 2026, 2026-05-28

SUMMARY
The filtering system was enhanced from a single `score` dimension to a two-dimensional model: `local` (relevance to Hoboken/Hudson County consumers, 1-10) and `engagement` (likelihood to generate comments and shares, 1-10). A weighted composite was calculated as `0.4 × local + 0.6 × engagement`, prioritizing engagement since Facebook's reach depends on comment activity. This was accomplished within the same single Haiku API call by requesting both scores in the JSON response.

The log output was updated to show per-article breakdowns (e.g., "SELECTED [8.2] local=7 engage=9") giving visibility into why each article passed the selection threshold. This enabled future tuning of the weights if engagement emphasis needed adjustment. The scoring worked efficiently — the system fetched 24 candidates from 5 feeds, filtered to 21 after keyword blacklist, and Claude scored those down to 3 final selections per run.
