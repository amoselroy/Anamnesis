# SESSION CHUNK 2026-06-20 — News Article Date Backfilling and Inventory Discovery

*ID: passage-06ecbb38-7f4f-4cf9-9dba-45541138bd10*
*Created: 2026-06-21*

---

SESSION CHUNK 2026-06-20 — News Article Date Backfilling and Inventory Discovery

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\backfill_news_dates.py, C:\Users\Amos\projects\braindexer\audit_news.py, C:\Users\Amos\projects\braindexer\_count_news.py, C:\Users\Amos\projects\braindexer\_link_condition.py, C:\Users\Amos\projects\braindexer\_list_therapies.py, C:\Users\Amos\projects\braindexer\_find_therapy.py, C:\Users\Amos\projects\braindexer\services\scraper.py, C:\Users\Amos\projects\braindexer\static\admin.html
Errors: Exit code 1
At line:10 char:5
+     FROM braindexer.sources
+     ~~~~
The 'f; Exit code 1
Traceback (most recent call last):
  File "C:\Users\Amos\projects\b; Exit code 1
Therapy 'cu' not found; Exit code 1
  File "<string>", line 5
    cur.execute(" SELECT slug name FROM b
Tools used: Edit, PowerShell, Read, Grep, Write, Glob

SUMMARY
After fixing the encoding issues, the `backfill_news_dates.py` script was executed to recover missing publication dates for existing news articles. A `_count_news.py` utility was created to query the database directly and discover that 235 total news articles exist in production, with only 59 needing date backfilling (the remaining 176 were Google News aggregator URLs, which are unrecoverable because they redirect to target articles without preserving the original publication date). The script successfully backfilled dates for almost all 59 articles using a 5-method extraction strategy (Open Graph meta tags, standard meta tags, JSON-LD, `<time datetime>`, `<time>` text). This demonstrated that the `_nearby_date()` helper implementation is effective for real-world news sources. The conclusion: news articles scraped via direct publication scrapers now have dates captured at scrape time going forward due to the `_nearby_date()` integration, and the backfill handled the legacy articles that lacked dates. The distinction between transient aggregator sources (Google News) and recoverable direct sources was validated operationally.
