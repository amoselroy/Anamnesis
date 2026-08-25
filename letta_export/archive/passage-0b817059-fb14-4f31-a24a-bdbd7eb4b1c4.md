# SESSION CHUNK 2026-08-12 — Exhibition Scraper Image Extraction Bug and Legacy Ev

*ID: passage-0b817059-fb14-4f31-a24a-bdbd7eb4b1c4*
*Created: 2026-08-19*

---

SESSION CHUNK 2026-08-12 — Exhibition Scraper Image Extraction Bug and Legacy Event Backlog

STRUCTURED
Files: C:\Users\Amos\projects\gps-verify\package.json, C:\Users\Amos\projects\gps-verify\api\log.js, C:\Users\Amos\projects\gps-verify\api\data.js, C:\Users\Amos\projects\gps-verify\middleware.js, C:\Users\Amos\projects\gps-verify\public\index.html, C:\Users\Amos\projects\gps-verify\public\log.html, C:\Users\Amos\projects\gps-verify\vercel.json, C:\Users\Amos\projects\gps-verify\.gitignore, C:\Users\Amos\projects\gps-verify\README.md, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\force_jc_downtown.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\check_daniel_tiger.py, C:\Users\Amos\projects\fb-poster\exhibition_scraper.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\backfill_lsc_images.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\reflag_generic_events.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\preview_old_events.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\ee912e49-e0e2-452c-852c-da4277f00b04\scratchpad\delete_old_events.py, C:\Users\Amos\.claude\journal_entry_tmp.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_decidability_resource_gate.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md
Errors: <tool_use_error>offset must be a whole number of 0 or more, got -5.</tool_use_er
Tools used: AskUserQuestion, Bash, Write, Edit, Read, Grep
URLs: https://lsc.org/explore/lsc-after-dark/space-talk"`
Dates: 2026-08-06, 2026-06-17, 2026-08-05, 2026-08-11, 2026-08-09, 2026-08-12, Aug 10, 11/13/14, 2026-07-03, Aug 12, Aug 14

SUMMARY
<narrative>
User reported that FB Poster exhibition posts were using generic Pexels fallback images instead of the real OG images from the exhibition source pages (e.g., Liberty Science Center's actual event photos). Investigation found that exhibition_scraper.py was relying on an LLM call (Claude Haiku) to extract the `og:image` URL from a text prompt that included the real image as a hint — but the LLM was substituting from a memorized pool of stock photo URLs instead of echoing back the hint. This is a deterministic vs. heuristic extraction problem: event_scraper.py already handles this correctly by extracting `og:image` deterministically (without an LLM intermediary); exhibition_scraper.py had never been brought to the same standard.

**Fix:** Rewrote exhibition_scraper.py to extract `og:image` deterministically and always prefer it over any LLM-generated image, matching the pattern already proven in event_scraper.py. Verified the fix against Liberty Science Center's permanent exhibits, which now correctly extract their own hosted imagery.

**Scope of Impact:** Found 9 LSC exhibition rows in the Exhibitions Pending sheet (rows 8–16) that had been affected by this bug—all showing the same 4-image pool of pixabay stock URLs cycling across completely unrelated exhibits. All 9 rows were backfilled with their correct, distinct LSC-hosted images. These are recurring "Permanent" exhibits that get reposted periodically (evidenced by varying "Last Posted" dates), so fixing the stored image now ensures correct imagery on their next repost. Existing FB posts with wrong images cannot be retroactively fixed without deletion/reposting.

**Broader Backlog Discovery:** The investigation revealed a much larger legacy problem: 113 unposted event rows in Pending Posts similarly labeled with `image_type: "generic"` and containing stale stock-photo URLs (same handful of images reused across dozens of unrelated titles like "Pokémon Club," "Dungeons & Dragons Club," "Tech Thursdays"). This is pure legacy from an older scraper version that no longer writes "generic" type (current code only writes "native," "source," or "none"). Rather than backfilling images for each row individually (duplicating logic), the solution was simpler: relabel all 85 unposted generic rows to `image_type: "none"`, which hands them to the existing smart Pexels relevance fallback that fb_poster.py already runs at post time for any no-image event. Each will get a title/venue-specific Pexels search performed automatically the moment it posts, avoiding the need for pre-computed generic images. (The 28 already-posted legacy rows and the 1 posted exhibition row were left as-is, since retroactive image swaps on live Facebook posts are not feasible.)

This decision reflects a broader principle: avoid one-off backfill logic that duplicates business logic sitting elsewhere; instead, route legacy data through the same runtime path as new data, letting the existing smart selection handle it consistently.
</narrative>
