# SESSION CHUNK 2026-06-11 — Institutional and Aggregator Source Testing — Rows 15

*ID: passage-935b03c3-0e7b-4b5e-ada4-f0147f89ab7f*
*Created: 2026-06-11*

---

SESSION CHUNK 2026-06-11 — Institutional and Aggregator Source Testing — Rows 15–17 and Library of Congress Content

STRUCTURED
Files: C:\Users\Amos\projects\fb-poster\event_scraper.py, C:\Users\Amos\projects\fb-poster\fix_hudson_theatre_url.py, C:\Users\Amos\projects\fb-poster\check_hudson_row.py, C:\Users\Amos\projects\fb-poster\test_hudson_theatre.py, C:\Users\Amos\projects\fb-poster\check_eb_page.py, C:\Users\Amos\projects\fb-poster\check_eb_detail.py, C:\Users\Amos\projects\fb-poster\check_eb_organizer.py, C:\Users\Amos\projects\fb-poster\check_eb_organizer2.py, C:\Users\Amos\projects\fb-poster\list_sources.py, C:\Users\Amos\projects\fb-poster\probe_sources.py, C:\Users\Amos\projects\fb-poster\probe_sources2.py, C:\Users\Amos\projects\fb-poster\probe_sources3.py, C:\Users\Amos\projects\fb-poster\probe_museum.py, C:\Users\Amos\projects\fb-poster\probe_museum2.py, C:\Users\Amos\projects\fb-poster\probe_museum3.py, C:\Users\Amos\projects\fb-poster\probe_museum4.py, C:\Users\Amos\projects\fb-poster\fix_museum_url.py, C:\Users\Amos\projects\fb-poster\test_mana.py, C:\Users\Amos\projects\fb-poster\probe_11_12.py, C:\Users\Amos\projects\fb-poster\probe_11_12b.py, C:\Users\Amos\projects\fb-poster\probe_11_12c.py, C:\Users\Amos\projects\fb-poster\probe_barsky.py, C:\Users\Amos\projects\fb-poster\probe_barsky2.py, C:\Users\Amos\projects\fb-poster\probe_barsky3.py, C:\Users\Amos\projects\fb-poster\probe_barsky4.py, C:\Users\Amos\projects\fb-poster\fix_barsky_url.py, C:\Users\Amos\projects\fb-poster\test_barsky_fb.py, C:\Users\Amos\projects\fb-poster\debug_barsky_fb.py, C:\Users\Amos\projects\fb-poster\probe_deepspace.py, C:\Users\Amos\projects\fb-poster\test_deepspace_fb.py, C:\Users\Amos\projects\fb-poster\debug_deepspace_fb.py, C:\Users\Amos\projects\fb-poster\fix_deepspace_url.py, C:\Users\Amos\projects\fb-poster\test_hob_library.py, C:\Users\Amos\projects\fb-poster\test_jc_library.py, C:\Users\Amos\projects\fb-poster\test_jc_library2.py, C:\Users\Amos\projects\fb-poster\fix_jcl_url.py, C:\Users\Amos\projects\fb-poster\test_jc_cultural.py, C:\Users\Amos\projects\fb-poster\move_hoboken_girl.py, C:\Users\Amos\projects\fb-poster\test_jcfamilies.py, C:\Users\Amos\projects\fb-poster\test_patch_hoboken.py, C:\Users\Amos\projects\fb-poster\move_aggregators.py, C:\Users\Amos\projects\fb-poster\check_tail.py, C:\Users\Amos\projects\fb-poster\test_patch_jc.py
Errors: Exit code 1
Traceback (most recent call last):
  File "C:\Users\Amos\projects\f; Exit code 127
/usr/bin/bash: line 1: del: command not found; Exit code 1
/usr/bin/bash: line 1: type: C:\Users\Amos\AppData\Local\Temp\claude; Exit code 1
=== Barsky Gallery — date context ===

  'March 20': ...isit Us Ba; Permission denied by user; Exit code 1
Moved: Patch Hoboken
Moved: Patch Jersey City
Traceback (most rece
Tools used: Read, Edit, Write, Bash, Grep, ToolSearch, mcp__claude-in-chrome__tabs_context_mcp, mcp__claude-in-chrome__navigate
URLs: https://www.hudsontheatreworks.org/tickets', https://www.hudsontheatreworks.org/tickets`, https://www.eventbrite.com/o/hudson-theatre-works-32771081953`, https://www.eventbrite.com/o/hudson-theatre-works-32771081953"}, https://www.barskygallery.com/hoboken-art-exhibitions
Dates: 2026-06-11

SUMMARY
Row 15 (JC Cultural Affairs) tested successfully via Path EB (Eventbrite organizer): 3 events, no drops, all Jersey City addresses. Currently posting the Mayor's community update series. Row 17 (Patch Hoboken) extracted 14 events via Path A with clean results including markets, wellness, theater, and community events; 5 non-Hoboken events were correctly filtered by the location check. JCFamilies (row 16 after reordering) yielded 9 family-focused events (Father's Day celebrations, Toddler Fair, Bubble Fest, Cultural Diversity Festival) through September–October. One minor quirk: stored URLs for some events pointed to pagination pages rather than detail pages, but event data extraction was correct. All three sources are producing events without issues. Testing of Patch JC (row 47 after reordering) began at session end with initial results processing. The systematic testing of rows 9–17 revealed consistent patterns: JS-heavy pages activate Path C (Playwright + LLM fallback), static pages with links activate Path A, specialized platforms (Eventbrite, LibCal, Wix) process correctly with appropriate path routing. No sources required removal or major architectural changes beyond URL corrections.
