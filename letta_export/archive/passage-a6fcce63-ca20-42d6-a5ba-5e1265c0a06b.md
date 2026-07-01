# SESSION CHUNK 2026-06-23 — MemShepherd Block PATCH API Timeout Investigation and

*ID: passage-a6fcce63-ca20-42d6-a5ba-5e1265c0a06b*
*Created: 2026-06-23*

---

SESSION CHUNK 2026-06-23 — MemShepherd Block PATCH API Timeout Investigation and Resolution

STRUCTURED
Files: C:\Users\Amos\.claude\memshepherd\hooks\chunk_archive.py, C:\Users\Amos\projects\fb-poster\run_exhibition_scraper.bat, C:\Users\Amos\projects\fb-poster\fb_poster.py
Errors: Exit code 127
/usr/bin/bash: line 1: Get-Content: command not found; File content (81066 tokens) exceeds maximum allowed tokens (25000). Use offset a; Exit code 1
Invoke-RestMethod : {"trace_id":"","detail":"[{'type': 
'string_pat; <tool_use_error>Blocked: Start-Sleep 30 followed by: $agent_id = "agent-060fb339; Exit code 1; Exit code 1
Get-Member : You must specify an object for the 
Get-Member cmdlet.; Exit code 255
TaskName:                             \Adobe 
Acrobat Update Task; Exit code 1
schtasks : ERROR: The system cannot find the file 
specified.
At l; Exit code 5
schtasks : ERROR: Invalid argument/option - 'C:\User
s\Amos\project; Exit code 1
schtasks : ERROR: Access is denied.
At line:1 char:1
+ schtasks /c; <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Read, Bash, PowerShell, Grep, Edit, Glob
Dates: June 25, 2026

SUMMARY
Session dropped and restarted. Investigation into why orientation and pins blocks weren't loading revealed consistent timeout failures on Letta's block PATCH API. The symptom: every ORIENTATION and WORLD block update times out at startup with "timed out after 15s" errors, yet archival passages insert successfully (they use a 180s timeout). Testing the API directly revealed that actual PATCH operations take approximately 26 seconds (tested with agent block patching), but the `patch_block` function in chunk_archive.py has only a 15-second timeout. The timeline shows this has been happening consistently since at least June 22. Root cause: Letta's block API is slow (26s for operations that move substantial data), but the timeout was too aggressive. Solution implemented: increased `patch_block` timeout from 15s to 60s and `fetch_agent_blocks` timeout from 10s to 30s, providing safe headroom for the actual operation time. The next session start should successfully load orientation and pins blocks without timeout failures.
