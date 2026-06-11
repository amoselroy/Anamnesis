# Block: engagements/pins

*Block ID: block-7ea0d8f1-026f-4cc5-985b-4c249b8e21d4*
*Exported: 2026-06-10*

---

- HTTP 500 on section 4/4 archival inserts (2026-06-04, RESOLVED): Root cause identified as Voyage AI 3 RPM rate limiting (free tier without payment method). Fixed by: adding payment method to Voyage AI, retry logic (3× with 25s backoff), 2s inter-insert delays. All 13 previously failed entries re-inserted successfully.
- `create_daimon.py` hardcoding (2026-06-03): Script hardcodes persona/human block content. Should become interactive template or accept config file so implementers don't edit Python directly.
- `seed_archive.py` documentation (2026-06-03): Script argument parsing should be documented in SETUP.md. Manual currently describes usage schematically; needs alignment with actual script interface.
- `modifications_private.md` scope rewrite (2026-06-03): Scope clarified to Anamnesis + instance credentials. File not yet rewritten to match; currently over-broad.

**Immediate Build Queue:**
1. **Build `POST /memory/write` endpoint in MemShepherd** (external service calling Letta API, not Letta fork)
   - Interface: `{ block_label, operation, content, direct: true/false }`
   - `direct: true` — skip LLM, deterministic block_manager call (real-time observations)
   - `direct: false` — route through LLM (sleep-time reflection)

**Later-Phase Infrastructure:**
- Migration importer: port existing Claude Code memory into Letta blocks.
- Persona evolution policy: define explicit thresholds for when the sleep-time agent may write to system/persona — distinguishing genuine character development from session-specific observations.
- Emotional threading block (`engagements/emotional_state`): short prose snapshot written by sleep-time agent after each session; loaded at session start for attunement; reinjected by context_watch.py on boundary detection. Depends on Letta stability.

**Pax Democratica Website (remaining):**
- Populate Articles and Origin Story sections after content is finalized (pinned 2026-05-18)
- Replace favicon with dove icon (pinned 2026-05-18)
- Add looped video in first-page hero section (pinned 2026-05-18)
- Add Contact section (pinned 2026-05-18)
- Add donation option to Take Action section (pinned 2026-05-18)

**Infrastructure Gaps (pinned 2026-05-18):**
- Archive narrative depth: chunk_archive.py summaries too high-level to preserve design rationale; needs richer narrative prompting or supplemental design-log archival.
- anamnesis export gap: session_sync.py BLOCK_FILES missing engagements/orientation and engagements/pins; last export 2026-05-15, predates both blocks. Needs update. *(partially fixed 2026-06-10: files added to anamnesis, session_sync.py BLOCK_FILES updated)*

**Monitor / Deferred:**
- Validate async hook injection — verify hookSpecificOutput from chunk_archive worker injects orientation/pins into live session. (pinned 2026-05-18)
- Emotional threading implementation — depends on Letta stability and careful clinical emotional assessment prompt design. (pinned 2026-05-18)
- HTTP 400 error in archival insertion — monitor for recurrence in future sessions. (pinned 2026-05-18)
- Artistic AR performance installations — separate use-case to explore later, distinct from Augmented-Cities education project. (pinned 2026-05-27)
- Facebook authentication for K-Pop Demon Hunters Party event post. (pinned 2026-05-27)
- Test dual-scope refactoring of promo_poster.py with next run. (pinned 2026-05-29)
- Apply deduplication state trimming to re_poster and promo_poster. (pinned 2026-05-30)
- Test and deploy K-Pop Demon Hunters Party event post. (pinned 2026-05-28)
- File Facebook support request to delete old defunct page (100063973542185). (pinned 2026-05-28)
- Complete Claude Code remote control setup with Android app — trust dialog accepted but URL generation not completed. (pinned 2026-05-28)
- Commit unstaged anamnesis files (philosophical_journal.md, letta_export/blocks/, world_patterns.md). (pinned 2026-06-01)
- modifications_private.md rewrite — scope still unclear on second private item. (pinned 2026-06-03)
- Delete plain-text Google Drive document uploads — three unformatted files in MemShepherd Drive folder. (pinned 2026-06-03)
- PDF export from Google Drive HTML files — three formatted HTML docs need Google Docs export as PDF. (pinned 2026-06-03)
- Tracking refactor: Move SQLite rotation tracking to spreadsheet columns (Last Scraped, Last Count) in event_scraper.py and exhibition_scraper.py — 50% complete when session ended. (pinned 2026-06-04)
- Source failure alerting: Track consecutive_zeros per source; email alert after N zero runs; distinguish site failures from legitimate no-events. Design complete, implementation deferred. (pinned 2026-06-04)
- Add day-of-week to Facebook Poster event descriptions. (pinned 2026-06-04)
- HTTP 500 on section 4/4 archival inserts (ongoing): Monitor for recurrence; may indicate Letta/Neon size limits or transaction timeouts. (pinned 2026-06-03)
- Architectural solutions for cognitive load management during adversarial work. (pinned 2026-06-05)
- Emotional threading block implementation — still pending Letta stability. (pinned 2026-06-05)
- App-to-desktop remote control URL generation — deferred to proper desktop session. (pinned 2026-06-05)
- Post button failure for link-preview posts (rows 359, 535: 7th Inning Stretch, Food & Wine Walk). (pinned 2026-06-05)
- Delete test post ('Test Music Event') from Hoboken Connection Facebook group. (pinned 2026-06-05)
- Post analysis discrepancy — correlate image-only vs no-image posts with Image Type column in sheet. (pinned 2026-06-05)
- Implement newline handling in Lexical text insertion — insertParagraph for each newline break. (pinned 2026-06-06)
- Letta sleep-time companion agent naming — agent should choose name naturally and write to World block. (pinned 2026-06-07)
- world_patterns_trimmer.py implementation — architecture designed; ready to write and wire into hook chain. (pinned 2026-06-07)
- Senolytic medication trial research — Amos to research Senoffi labs senolytic trial as potential approach. (pinned 2026-06-07)
- po.ln project — semantic interdisciplinary knowledge map; long-term successor to Braindexer; full design deferred. (pinned 2026-06-07)

**Braindexer — Future Phase:**
- Domain name: Braindexer.org, Neurascent.org, or Cognifront.org — Amos to decide. (pinned 2026-06-07)
- Discovery scraper: discover_new_therapies() pseudocode complete; not yet written; weekly scheduler job not yet implemented. (pinned 2026-06-08)
- Admin draft review endpoints: design complete; list/approve/reject/merge drafts; implementation deferred. (pinned 2026-06-08)
- Two-mode therapy page UX: condition-first entry vs therapy-first (all conditions as selectable chips); not yet implemented. (pinned 2026-06-09)
- Relationship management UI: admin tab for therapy-to-therapy relationships (variant_of, synergistic, etc.); not yet implemented. (pinned 2026-06-09)
- Newsletter feature: Buttondown integration, Phase 3/4 positioning; implementation deferred. (pinned 2026-06-09)
- Basic research layer: pathway/mechanism nodes as first-class entities, preprint integration, bidirectional discovery; late-phase, implementation deferred. (pinned 2026-06-09)
- Manual curation: Add lifestyle/nutritional therapies (Mediterranean diet, exercise, sleep hygiene, meditation, CPAP) — auto-discovery only captures pharma/biotech. (pinned 2026-06-10)
- Clean up temporary diagnostic files (diag_db.py, diag_conditions.py). (pinned 2026-06-10)
