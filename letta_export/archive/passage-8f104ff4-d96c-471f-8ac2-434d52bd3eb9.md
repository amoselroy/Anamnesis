# SESSION CHUNK 2026-06-11 — Scraper Infrastructure Fix — Log File Write Lock Cras

*ID: passage-8f104ff4-d96c-471f-8ac2-434d52bd3eb9*
*Created: 2026-06-11*

---

SESSION CHUNK 2026-06-11 — Scraper Infrastructure Fix — Log File Write Lock Crash

STRUCTURED
Files: C:\Users\Amos\projects\fb-poster\event_scraper.py
Errors: Exit code 1
/usr/bin/bash: line 1: type: C:\Users\Amos\projects\fb-poster\event_; Permission denied by user; Exit code 1
Traceback (most recent call last):
  File "<string>", line 14, in <; Exit code 1
<string>:15: SyntaxWarning: "\." is an invalid escape sequence. Such
Tools used: Glob, Grep, ToolSearch, Read, Bash, Edit, mcp__claude-in-chrome__tabs_context_mcp, mcp__claude-in-chrome__navigate
URLs: https://www.bikejc.org/events, https://segundaquimbamba.org/upcoming-events/, https://jerseycityculture.org/events/, https://www.thestatuaryofjerseycity.com/event-details/the-statuary-presents-jason-marshall

SUMMARY
Discovered that the Event Scraper had been failing on every nightly run for 3 days (June 9–11 at 3:11 AM UTC) with a `PermissionError` on `event_scraper.log`. Root cause identified: the batch file redirect (`>> event_scraper.log 2>&1`) holds an exclusive write lock on the log file, preventing the Python `log()` function from opening the same file for writing. Both approaches had existed since the initial commit, but the conflict only triggered when running via Windows Task Scheduler (batch redirect active) — manual terminal runs worked because there was no redirect competing for the file lock. Zero sources had ever been successfully scraped on the scheduled task. Fixed by removing the file-writing logic from `log()` and allowing `print()` output to flow through the batch redirect. Also removed the now-unused `LOG_FILE` constant. The fix restored full operational capability for nightly scheduled runs.
