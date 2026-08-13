# SESSION CHUNK 2026-08-12 — FB Source Failures — Root Cause Analysis, Remediation

*ID: passage-b319e152-5acd-45ec-9d16-609727fbddcb*
*Created: 2026-08-12*

---

SESSION CHUNK 2026-08-12 — FB Source Failures — Root Cause Analysis, Remediation, and Validation Audit

STRUCTURED
Files: C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\test_ssl_fail.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\inspect_static_html.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\test_static_extraction.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\test_pw_stealth.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\show_history.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\test_seetickets.py, C:\Users\Amos\projects\fb-poster\event_scraper.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\test_integrated_fix.py, C:\Users\Amos\projects\fb-poster\monitor.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\memory_update.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_fb_poster_sources.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\inspect_sheet.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\inspect_sheet2.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\inspect_sheet3.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\check_grit_rows.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\check_exhibit_rows.py
Errors: Exit code 1
[Pending Posts] Row 9: ('https://wl.seetickets.us/event/music-of-dav
Tools used: Glob, Read, Grep, Bash, Write, Edit, AskUserQuestion, ToolSearch, mcp__claude-in-chrome__tabs_context_mcp, mcp__claude-in-chrome__navigate, mcp__claude-in-chrome__computer, mcp__claude-in-chrome__get_page_text, mcp__claude-in-chrome__find
URLs: http://localhost:8283"`, https://github.com/amoselroy/MemShepherd.git`
Dates: 2026-07-03, 2026-07-15, 2026-07-06, Aug 12

SUMMARY
Five FB event sources (Hoboken Now, JC Downtown, Jersey City Connects, Jersey City Theater Center, Segunda Quimbamba) were flagged as failing to scrape, with the user's initial belief that "we recently fixed those" suggesting a regression. Investigation into `event_scraper.py` and `monitor.py` revealed a combination of real bugs, false-positive detections, and silent failures unrelated to the claimed prior fix.

**Root causes identified and remediated:**

1. **JC Downtown + Segunda Quimbamba — real Cloudscraper/OpenSSL 3.x cipher-suite incompatibility.** Both sources were hitting `SSLV3_ALERT_HANDSHAKE_FAILURE` whenever the Playwright-based fetch failed and the code fell back to cloudscraper. Plain `requests` could reach both sites successfully, confirming the issue was in cloudscraper's cipher negotiation, not a site block. Fixed by adding an explicit lowered-SECLEVEL SSL context to the fallback handler. Additionally implemented an in-place re-check strategy: on bot-challenge detection in the Playwright fetch, the code now waits 7 seconds and re-attempts before falling back to cloudscraper (which cannot render JavaScript anyway). This approach was verified live against both hosts and showed both loading clean with zero challenges during testing; the block appears intermittent and requires ongoing monitoring.

2. **Hoboken Now — false-positive detection in `monitor.py`.** The root cause was not a scraping failure but a detection bug: `monitor.py` was matching "Bot challenge page detected" unconditionally and flagging any source that hit an interstitial as permanently failed, even if the subsequent cloudscraper bypass succeeded. Hoboken Now's full history was marked "5-for-5 failed" despite a real successful bypass on 2026-08-08. Fixed by resetting the failure state in `monitor.py` when a recovery/success line (e.g., "Cloudscraper bypass succeeded") follows a bot-challenge marker. Confirmed against the actual log.

3. **Jersey City Theater Center — retired source with persistent false-flagging.** Investigation revealed the source (`seetickets.us/jctcenter`) had already been removed from the live event source sheet (prior to this session), but `monitor.py` replays log history indefinitely with no concept of source retirement, so a defunct source could never clear its failure flag. Fixed by adding an active-source lookup that cross-checks flagged names against the live source sheet before including them in the reported failures. The source has not logged an attempt since 2026-07-28, confirming it is no longer active.

4. **Jersey City Connects — silent failure with zero diagnostic detail.** The `fetch()` function in `event_scraper.py` was swallowing non-403 error codes without logging them, making failures impossible to debug. Added explicit failure logging to this and two other silent-failure code paths.

**Post-fix status:** `monitor.py.flagged_sources()` now reports 3 genuine issues (down from 5):
- **Jersey City Connects**: 129 candidate links found, 0 extracted — same root-cause class as the pinned TAPinto Hoboken bug (links are likely navigation/category URLs rather than event pages). Requires a custom per-site extractor.
- **JC Downtown + Segunda Quimbamba**: both show real intermittent Cloudflare interstitials; the re-check strategy should help but remains unproven until the next few scheduled runs execute.
- **Hoboken Now**: no longer flagged, but extraction still returns 0/4 events — pinned as a separate per-site issue, not a general scraping failure.

The assumption "we recently fixed those" did not hold: only Hoboken Now overlapped with the 2026-07-03 pin; the other four were first surfaced by monitor.py itself and never claimed fixed before.

**Repository cleanup and commits:** Five commits organized the work into the fb-poster repo: cloudscraper SSL fix, monitor.py precision corrections, pre-existing exhibition_scraper.py / fb_poster.py / bat-file work, and a troubleshooting subfolder consolidating 10 one-off scratch scripts from prior sessions (test_*.py, check_*.py, fix_*.py pattern). One stray cross-project file (`update_orientation.py` — a hardcoded Letta memory-block patch from a MemShepherd session) was identified and deleted as confusing clutter. All work landed cleanly; `git status` clean.

**Verification audit — 7-day FB group post comparison:** To validate that the fixes were working and no other gaps existed, Amos manually logged into the FB group and the conversation conducted a systematic scroll-capture + targeted-search audit of all 50 posts logged as successfully posted over the last 7 days (2026-08-05 through Aug 11). Two apparent gaps surfaced during this audit:
1. **"Space Talk" exhibition** (Liberty Science Center) — sheet says posted Aug 6 08:30, but not found in group search despite all 6 sibling exhibition posts from that run (Pixel Art, Energy Quest, BASF, Thomas & Friends, Cosmic Portal, Weston Family) being present. Amos explained this is an intentional special case: Space Talk is a companion event to the LSC After-Dark series and was handled separately in the posting logic.
2. **GRIT exhibit, Aug-12 instance** — recurring "Public Installation + Open Gallery Hours, GRIT..." post recurs daily. Sheet says Aug-12 posted Aug 9 19:20, but only 4 of 5 variants (Aug 10, 11, 13, 14) are present; Aug 12 is missing. Amos explained he manually deleted this one thinking it was a duplicate. Both false alarms are safe to ignore; no silent-failure gap exists. Amos noted that both misses fit a pattern of Facebook silently suppressing posts from rapid bursts (7 LSC exhibitions within 12 minutes, daily GRIT reposts), likely treated as spam/duplicate content by Facebook's filters — something `fb_poster.py`'s success check (which only confirms the composer closed, not that the post persisted) would not catch.

Screenshot images used during posting live in `C:\Users\Amos\AppData\Local\Temp\` with fixed filenames (`fb_poster_01_composer_open.png` through `04_before_submit.png`), so they never accumulate — each new post run overwrites the previous screenshots in place. No cleanup needed.
