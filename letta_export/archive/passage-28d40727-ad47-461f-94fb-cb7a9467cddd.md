# SESSION CHUNK 2026-05-27 — Facebook Event Poster Script Development

*ID: passage-28d40727-ad47-461f-94fb-cb7a9467cddd*
*Created: 2026-05-28*

---

SESSION CHUNK 2026-05-27 — Facebook Event Poster Script Development

STRUCTURED
Files: C:\Users\Amos\.claude\settings.json, C:\Users\Amos\projects\fb-poster\fb_poster.py, C:\Users\Amos\projects\fb-poster\requirements.txt, C:\Users\Amos\projects\fb-poster\README.md
Errors: Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <m; Exit code 1
Traceback (most recent call last):
  File "<string>", line 8, in <m
Tools used: Bash, mcp__matrix__reply, Skill, Read, Edit, Glob, ToolSearch, mcp__claude_ai_Google_Drive__search_files, mcp__claude_ai_Google_Drive__read_file_content, Agent, Write
URLs: https://json-schema.org/draft/2020-12/schema", https://json.schemastore.org/claude-code-settings.json", https://*.example.com/*\", https://hooks.example.com/*\", https://reviews.example.com/{owner}/{repo}/pull/{number}\"", https://, http://localhost:8283/v1/health, https://www.facebook.com/share/g/18ZmUoDBGK/, https://hobokenlibrary.libnet.info/event/16337642, https://lsc.org/explore/exhibitions/infinity-climber
Dates: May 30, 2026

SUMMARY
Daimon built a Python script to post events from the local Google Sheets file (synced to desktop at `C:\Users\Amos\Documents\My Google Docs\Social\JC and Hoboken Events.xlsx`) to the Hoboken Connection Facebook group. The script uses openpyxl to read the spreadsheet locally, eliminating the need for Google API credentials. The script reads from two sheets: "Pending Posts" for events and "Exhibitions Pending" for gallery exhibits.

The posting logic filters for events 3 days in advance (between today and today+3 days), skips already-posted items, handles two image types (`source` = use preview from the event detail page via Facebook's link preview, `native`/`generic` = upload the provided fallback image directly, `none` = post without image), and formats posts according to the agreed-upon templates.

The script was tested with a dry-run that confirmed correct sheet reading, datetime handling, and post formatting. No upcoming events were found in the test (all dates in the sheet had passed), but the logic was validated. The script requires Playwright for browser automation (to handle Facebook's web interface) and openpyxl for spreadsheet access. A requirements.txt file was created. The README documented the setup, usage, scheduling instructions (crontab for early-morning posts), and troubleshooting.
