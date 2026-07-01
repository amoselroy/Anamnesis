# SESSION CHUNK 2026-05-27 — Event Date Parsing Bug Discovery and Fix

*ID: passage-0b29ccef-feca-4dd7-9011-dcbb57d3720d*
*Created: 2026-05-28*

---

SESSION CHUNK 2026-05-27 — Event Date Parsing Bug Discovery and Fix

STRUCTURED
Files: C:\Users\Amos\projects\fb-poster\fb_poster.py, C:\Users\Amos\.claude\projects\C--WINDOWS-system32\memory\project_fb_poster.md, C:\Users\Amos\.claude\projects\C--WINDOWS-system32\memory\MEMORY.md
Errors: none
Tools used: ToolSearch, mcp__matrix__reply, Edit, Read, Write
URLs: http://localhost:8283, https://www.facebook.com/share/g/18ZmUoDBGK/", https://lsc.org/explore/exhibitions/universe-revealed, https://lsc.org/explore/exhibitions/making-mammoths, https://lsc.org/explore/exhibitions/great-train-set, https://lsc.org/explore/exhibitions/microbes-rule, https://lsc.org/explore/exhibitions/daniel-tiger, https://lsc.org/explore/exhibitions/touch-tunnel, https://lsc.org/explore/exhibitions/infinity-climber, https://lsc.org/explore/exhibitions/wobbly-world, https://lsc.org/explore/exhibitions/wild-about-animals, https://lsc.org/explore/exhibitions/dino-dig-adventure, https://lsc.org/explore/exhibitions/our-hudson-home, https://lsc.org/explore/exhibitions/bees-to-bots, https://lsc.org/explore/exhibitions/brain-games, https://www.manacontemporary.com/exhibition/mana-contemporary-presents-mana-highlights/
Dates: May 31, June 1, May 31, 2026, 2026-05-27, June 30, 2026

SUMMARY
A dry-run test revealed that while 14 exhibitions formatted correctly, zero events were being picked up for posting even though Amos confirmed upcoming events existed in the spreadsheet. Investigation identified that `Event Date` cells come back from openpyxl as `datetime` objects, not strings. When the code attempted `strptime()` on a datetime object it failed silently, and the fallback `str()` conversion produced timestamps like `"2026-05-28 00:00:00"` which didn't parse. The fix was to use the existing `_to_date()` helper function (already created for exhibitions) in `get_pending_events()`, which correctly handles datetime, date, string, and special value types. This single change restored event visibility.
