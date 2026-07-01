# SESSION CHUNK 2026-06-18 — Mainstream Health Articles Feature for Layperson View

*ID: passage-7d8d63cc-f965-4df2-bcb2-fab781eed13e*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — Mainstream Health Articles Feature for Layperson View

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/render.yaml, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/scheduler.py
Errors: Exit code 1
<string>:18: SyntaxWarning: "\]" is an invalid escape sequence. Such; Exit code 1
INFO:services.scraper:Discovery: fetching AlzForum therapeutics list; Exit code 1
Invoke-WebRequest : Cannot bind parameter 'Headers'. 
Cannot conver; <tool_use_error>String to replace not found in file.
String:         if name.low; <tool_use_error>Blocked: Start-Sleep 30 followed by: Invoke-RestMethod -Method P; Exit code 1
  File "<string>", line 7
    print(f'  [{r[" authors\]}]
        ; Exit code 1
Traceback (most recent call last):
  File "<string>", line 9, in <m; Exit code 1
Invoke-RestMethod : The remote server returned an 
error: (500) Int; Exit code 1
python : Traceback (most recent call last):
At line:1 char:39
+ cd; Exit code 1
Invoke-WebRequest : The remote server returned an 
error: (500) Int
Tools used: Glob, Read, Grep, Edit, PowerShell, Bash
Dates: 2026-06-17

SUMMARY
Amos requested a mainstream health articles feature specifically for the layperson view as a replacement for scientific literature links. The feature was designed with clear principles: (1) in layperson tab, display mainstream health articles instead of scientific papers; (2) do not feed articles into summary generation, keeping it grounded in primary evidence; (3) filter by Alzheimer's + specific therapy name, including synonyms. Initial implementation used Google News RSS feed with outlet whitelist (WebMD, Healthline, Harvard Health, Medical News Today, Mayo Clinic, etc.). The frontend was modified to split sources into `news` and `scientific` sections, toggling visibility based on tab selection. However, Amos identified a fundamental architectural flaw: RSS is a push mechanism, not a static archive, and should drive background updates rather than be queried at research time. This led to a major architecture redesign (documented in next section). During implementation, Amos also flagged important quality concerns: Frontiers is peer-reviewed but pay-to-publish and belongs in scientific articles, not layperson news; Nature has a paywall and should be removed. These corrections were made by adjusting the outlet whitelist. The feature also exposed the need for future work on non-peer-reviewed sections (medRxiv, preprints) with explicit tagging, pinned for future implementation.
