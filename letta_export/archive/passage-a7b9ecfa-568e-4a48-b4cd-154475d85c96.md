# SESSION CHUNK 2026-06-16 — FB Poster and Exhibition Scraper Silent Failures — Ta

*ID: passage-a7b9ecfa-568e-4a48-b4cd-154475d85c96*
*Created: 2026-06-17*

---

SESSION CHUNK 2026-06-16 — FB Poster and Exhibition Scraper Silent Failures — Task Disablement and Log File Conflict Bugs

STRUCTURED
Files: none
Errors: Exit code 2
EXIT:1; Exit code 1
   Id ProcessName StartTime             RunTime     
   -- --------
Tools used: Bash, Glob, Read, PowerShell, AskUserQuestion, Grep, ToolSearch, mcp__claude-in-chrome__tabs_context_mcp, mcp__claude-in-chrome__computer, mcp__claude-in-chrome__navigate, WebSearch
Dates: 2026-06-16

SUMMARY
Amos reported that FB-poster and promo bot have not posted anything in the last few days. Investigation revealed multiple distinct failure modes across the FB posting infrastructure. Task Scheduler showed that both **FB Event Poster** (daily 7am) and **FB Exhibition Poster** (weekly Monday 8am) tasks are in **Disabled** status, with last run dates of 6/8/2026 — matching the gap Amos observed. This mirrors a prior incident from 2026-06-02 where these tasks were silently disabled with no clear cause. In contrast, the FB Promo Poster task remains enabled and healthy (weekly Friday cadence, last ran 6/12 as expected). The investigation then uncovered a more serious underlying bug: both the `run_event_scraper.bat` and `run_exhibition_scraper.bat` files have a **double-write file-locking conflict**. The batch files redirect all stdout/stderr to a log file via shell redirection (`>> exhibition_scraper.log 2>&1`), while the Python scripts' own `log()` functions independently try to open the same file for writing. On Windows, this creates competing file handles racing for the same resource, resulting in `PermissionError: [Errno 13] Permission denied` on the very first log call, before any actual scraping occurs. The exhibition scraper has been **losing this race 100% of the time since 6/9**, causing zero new exhibition candidates to be collected for 8 days. The event scraper has the same latent bug but began winning the race consistently from 6/12 onward (currently healthy, finding 4-129 new events per day). Amos clarified that "duplicate tasks" referenced in memory were actually mischaracterized — there are genuinely distinct pipeline stages: scrapers (source collection into spreadsheet) and posters (spreadsheet-to-Facebook publication). The root causes identified are: (1) two poster tasks mysteriously disabled (requires re-enabling and investigation into *why* they flipped), and (2) redundant log-file writing from shell redirect plus Python function, causing predictable lock conflicts (fix: remove the batch redirect, rely on Python's own logging). No fix was applied during this session as Amos pivoted to investigating a separate Facebook account issue.
