# SESSION CHUNK 2026-05-30 — fb_poster False-Positive Posts and Spreadsheet State 

*ID: passage-670734c6-b8ca-4f30-8ecf-5bb1b0fe28d5*
*Created: 2026-06-02*

---

SESSION CHUNK 2026-05-30 — fb_poster False-Positive Posts and Spreadsheet State Management

STRUCTURED
Files: C:\Users\Amos\projects\re-poster\brokerage_sharer.py, C:\Users\Amos\projects\fb-poster\fb_poster.py, C:\Users\Amos\projects\fb-poster\clear_false_posted.py
Errors: Exit code 127
/usr/bin/bash: line 1: Get-Content: command not found; <tool_use_error>Cancelled: parallel tool call Bash(Get-Content "$env:TEMP\fb_pos; <tool_use_error>String to replace not found in file.
String:     # Scroll the ac
Tools used: Read, Edit, Glob, Bash, PowerShell, Write
URLs: https://static.xx.fbcdn.net/rsrc.php/yp/r/twpm7Tz4xLN.webp&quot, https://www.facebook.com/ExitOnTheHudsonRealty/, https://www.facebook.com/HobokenNJRealEstate/
Dates: May 30, 2026, 2026-05-30, 2026-05-31, 2026-06-01

SUMMARY
During the session, Amos discovered that many events were being marked as "posted" in the spreadsheet but were not actually appearing on the Hoboken Connection group feed. Investigation revealed this was a false-positive issue: the `fb_post()` function was returning True (successfully submitted) when the post button was clicked, but Facebook either silently rejected the group post (because the script was acting as a Page, not personal account) or the post landed somewhere other than the group feed.

A cleanup script (`clear_false_posted.py`) was written to identify and clear "Posted At" timestamps for events from today (or future dates) so they would be retried on the next run. However, the script's timestamp format detection required debugging — the spreadsheet stores values as `datetime.datetime` objects, not strings. After the session file separation fixed the underlying contamination, events began posting correctly and the false positives were resolved naturally.

The deeper lesson: the script's `mark_posted()` logic was sound, but the marking was premature — it occurred before validating that the post actually landed on the intended destination. The session contamination made this vulnerability visible, and separating session files removed the contamination source.
