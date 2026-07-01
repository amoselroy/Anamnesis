# SESSION CHUNK 2026-06-18 — Comparative Experiment — Google News vs. Direct Publi

*ID: passage-ef506fc1-e480-4ecf-9bcc-73defde43c64*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — Comparative Experiment — Google News vs. Direct Publication Scraping Approaches

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/static/admin.html, C:/Users/Amos/projects/braindexer/services/scraper.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_braindexer.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md, C:\Users\Amos\projects\braindexer\news_experiment.py, C:\Users\Amos\projects\braindexer\news_sniff.py, C:\Users\Amos\projects\braindexer\news_sniff2.py, C:\Users\Amos\projects\braindexer\news_sniff3.py, C:\Users\Amos\projects\braindexer\news_sniff4.py, C:\Users\Amos\projects\braindexer\news_experiment2.py, C:\Users\Amos\projects\braindexer\news_sniff5.py, C:\Users\Amos\projects\braindexer\smoke_test.py, C:/Users/Amos/projects/braindexer/setup_db.py, C:/Users/Amos/projects/braindexer/models.py
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<; Exit code 1
Traceback (most recent call last):
  File "<string>", line 18, in <; Exit code 1
  File "<string>", line 16
    print(f'  [{i+1}] {" OK \
         ; <tool_use_error>Found 4 matches of the string to replace, but replace_all is fal; File does not exist. Note: your current working directory is C:\Users\Amos\proje; Exit code 1
Running approach A (Google News, therapy+condition)�
Traceback (mos; Exit code 1
Running approach A (Google News, therapy+condition)�
  -> 15 articl; Exit code 1
python :   File "<string>", line 14
At line:1 char:39
+ cd C:\User; The user doesn't want to proceed with this tool use. The tool use was rejected (
Tools used: Edit, Read, Bash, PowerShell, Grep, Glob, Write
URLs: https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en`, https://www.alzforum.org/therapeutics/search/"`

SUMMARY
Amos questioned whether the architecture should use direct scraping of whitelisted publications instead of Google News as a gateway, noting that custom per-publication searches would be a heavy lift but might be worth the quality difference. Rather than commit to one approach, a comparative experiment was designed to test three strategies: (A) current (Google News RSS, condition+therapy query), (B) Google News with `site:` operators targeting the whitelist, (C) direct per-publication HTML scraping of select outlets. Testing on Lecanemab revealed decisive results: Approach A found 15 highly relevant articles all directly about Lecanemab; Approach B, by removing the therapy filter and only searching Alzheimer's across selected sites, drowned in noise (donanemab, vitamin K, genetic research, etc.) with only 2 overlapping articles; Approach C had implementation issues (selectors were wrong for EurekAlert and Being Patient). However, a second, more focused experiment comparing direct scraping of three readily-scrapable publications (The Conversation, Being Patient, Alzheimer's News Today) against the same query via Google News revealed a more nuanced story: The Conversation showed 9/10 overlap with Google News but direct scrape had zero extra articles; Being Patient was most interesting — direct scrape found 8 older articles from 2022–2023 that Google News had de-indexed, while Google found 59 current articles; Alzheimer's News Today had implementation issues in the experiment. The data suggested that while Google News dominates for current coverage (4–6x more articles), direct scraping provides archival depth for older articles. Amos concluded that upfront investment in direct publication scraping was worth the long-term quality implications as the corpus grew, valuing the archival completeness and signal-to-noise ratio over maintenance burden.
