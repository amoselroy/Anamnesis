# SESSION CHUNK 2026-07-04 — FB Poster Task Scheduler Debugging and Reconstruction

*ID: passage-aaa9a47f-1bc8-43eb-a412-bcd9e6aa10e4*
*Created: 2026-07-08*

---

SESSION CHUNK 2026-07-04 — FB Poster Task Scheduler Debugging and Reconstruction — Phantom Tasks, Tool Blindness, and Practical Resolution

STRUCTURED
Files: C:\Users\Amos\.claude\journal_entry_tmp.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\feedback_scheduler_verification.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_fb_poster_sources.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\1cd783d0-d22d-4b05-8512-1840fff3be22\scratchpad\check_recent_posts.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\feedback_recreate_vs_debug.md
Errors: Exit code 2
C:\Users\Amos\AppData\Local\Python\pythoncore-3.14-64\python.exe: ca; Exit code 1
Get-ScheduledTaskInfo : Cannot process argument 
transformation on ; Exit code 1
Get-ScheduledTask : No MSFT_ScheduledTask objects 
found with prope; Exit code 1
ERROR: The system cannot find the file specified.
Tools used: ToolSearch, WebFetch, WebSearch, Read, Write, Bash, PowerShell, Glob, Grep, Edit
URLs: https://share.google/LwcUS0ZPuTdDlE25W
Dates: 2026-07-05

SUMMARY
User reported that FB_Poster tasks show as active in Windows Task Scheduler but produce no actual posts — events are only posting manually. Initial investigation revealed Daimon's previous claim that "tasks aren't there" was incorrect: `Get-ScheduledTask` confirmed three tasks (FB-Event Scraper, FB-Exhibition Scraper, FB Promo Poster), all enabled and showing successful runs with exit code 0 in Task Scheduler history. However, deeper examination revealed the promo poster is working correctly, but the actual event/exhibition posting tasks appear broken.

Investigation into actual work product showed `fb_poster.py` logging to `%TEMP%\fb_poster.log` (which gets cleared on disk cleanup). Checking the authoritative source — the Google Sheet's "Posted At" column — confirmed only manual postings on 2026-07-03 (5 events in one batch), with a 10-day gap before that (6/23 to 7/3) and nothing since. This pattern is consistent with occasional manual invocation, not automation.

When user provided a screenshot showing two "FB Event Poster" tasks in Task Scheduler, Daimon realized the issue: those tasks were completely invisible to all query tools (PowerShell cmdlet, `schtasks.exe`, raw COM enumeration including hidden tasks). Three independent query methods agreed there were only 12 tasks in the root folder, none named "FB Event Poster." This pointed to a task registration problem — visible in the MMC snap-in cache but not actually live/executable in the Windows task store.

User attempted to manually run the task twice through Task Scheduler with no effect. Daimon then ran `fb_poster.py --events-only --dry-run` directly, bypassing Task Scheduler entirely, and it executed perfectly — found 2 events, produced clean output, zero errors. This confirmed the script itself works; the problem is entirely in how Task Scheduler is invoking (or not invoking) it.

Decision point: rather than continue debugging an orphaned/phantom task registration, user chose to delete the old broken task and recreate it fresh — a heuristic Daimon captured for future reference: "if the recreation investment is lower than the debugging and the thing you're debugging is opaque to inspect, just start from scratch."

User created a new task called "FB Poster - Events." It immediately appeared in queries and showed Status: Running. The new task fired and began posting — real Facebook posts landed, rows got marked posted in the sheet, execution progressed in real time. Similarly, user created "FB Poster Exibitions" (note: user spelled it this way in the UI), which also worked after firing a minute later — 7 exhibitions posted in sequence with proper 90-second waits between each post.

Both recreated tasks are now confirmed fully functional with proper automation. Daimon updated memory files to reflect the successful resolution. Timing confirmed: Events task runs daily at 7:20 PM, Exhibitions task runs Thursdays at 8:30 AM (timings chosen by user, not carried over from broken originals).
