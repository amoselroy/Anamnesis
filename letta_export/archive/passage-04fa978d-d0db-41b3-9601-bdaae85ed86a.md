# SESSION CHUNK 2026-06-18 — AlzForum Page Redesign, Scraper Rewrite, and Readable

*ID: passage-04fa978d-d0db-41b3-9601-bdaae85ed86a*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — AlzForum Page Redesign, Scraper Rewrite, and Readable Name Extraction

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
AlzForum completely redesigned their therapeutics page structure from a traditional drug table to a pivot table showing target types × trial phases (counts only). The old scraper returned zero candidates. Investigation revealed the therapy listing moved to `/therapeutics/search/` with a clean 7-column structure (Name, Synonyms, FDA Status, Company, Target Type, Therapy Type, ApprovedFor). The scraper was rewritten to parse this new URL, yielding 366 real candidates. A separate issue emerged: therapy names on AlzForum are pharmaceutical codes (`AV-GAD2.NLX-P101`, `PF-05236812`) rather than readable names, which is unsuitable for a layperson interface. Solution implemented in two parts: (1) parse comma-separated synonym values from AlzForum's Synonyms column, apply heuristics to identify and prefer non-code names (`AV-GAD2,NLX-P101` → display name=`NLX-P101`, alias=`AV-GAD2`); (2) LLM fallback via Haiku for remaining code-only entries, asking Claude to identify common names (though discontinued compounds like `PF-05236812` correctly returned None rather than hallucinating). The implementation stores pharmaceutical codes as aliases so they remain queryable while display names become human-readable. Testing confirmed clean results: `Acetyl-L-carnitine` with alias `ALCAR`, `Alicapistat` (no alias needed), etc. This work required understanding the data transformation pipeline and making careful decisions about when to apply heuristics vs. LLM assistance.
