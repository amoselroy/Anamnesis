# SESSION CHUNK 2026-05-29 — Debugging and Fixing `promo_poster.py` Facebook Group

*ID: passage-b6e9f198-fe36-4ac3-a67a-cb327da19948*
*Created: 2026-05-29*

---

SESSION CHUNK 2026-05-29 — Debugging and Fixing `promo_poster.py` Facebook Group Posting

STRUCTURED
Files: C:/Users/Amos/projects/fb-poster/promo_poster.py
Errors: none
Tools used: Glob, Read, Grep, Edit, ToolSearch
URLs: https://www.pexels.com/photo/traditional-turkish-breakfast-spread-outdoors-36720654/, https://www.pexels.com/photo/portrait-1-27903749/, https://www.pexels.com/photo/classic-yellow-school-bus-on-urban-street-37493121/
Dates: 2026-05-29

SUMMARY
The session focused on diagnosing and fixing a persistent failure in the `promo_poster.py` script that posts promotional content with Pexels images to the Hoboken Connection Facebook group. The script was successfully fetching images from Pexels ("brunch culture," "nightlife," "commuting to NYC") but consistently failing to open the post composer.

**Initial Investigation:**
Comparing the failing `promo_poster` to the working `re_poster` revealed a critical difference: `re_poster` scrolls 700px down the page before searching for the composer, while `promo_poster` was attempting to find the composer immediately on page load. A debug screenshot captured during the first failure attempt revealed that the share link `https://www.facebook.com/share/g/18ZmUoDBGK/` was landing on the group's **About** tab rather than the **Discussion** tab where the post composer exists.

**First Fix Iteration:**
The script was updated with three improvements: (1) added `window.scrollTo(0, 400)` plus a 1.5-second wait to allow the composer to come into view (mirroring the approach that works in re_poster), (2) broadened the contenteditable selectors to include `aria-placeholder='Write something...'` as an exact match alongside existing fallbacks, and (3) added a debug screenshot on failure to capture what Facebook actually rendered.

**Second Test and Refined Diagnosis:**
When the script was tested again, it progressed further — successfully switching to the personal account (Amos Elroy) — but now failed with a timeout waiting for `div[role='dialog']` containing a `contenteditable` element. The error indicated the composer had opened but the locator strategy was incorrect. This revealed a fundamental difference between page and group composer UI: Facebook group composers expand inline on the page rather than rendering as modal dialogs like the Team page composer does.

**Root Cause and Major Refactoring:**
The entire `fb_post` function was refactored to use a dual-scope approach. A new `_composer_scope()` helper function probes for a dialog element first, then falls back to the page-level if no dialog exists. All three critical operations (typing into contenteditable, selecting image input, finding the Post button) now use this scope-first, page-fallback strategy. The contenteditable search was updated to use `.last` (which matches the active editor, not hidden elements), the image input search was made scope-agnostic, and the Post button search was expanded to five selector variants across both scopes. Additionally, a debug screenshot was added immediately after opening the composer to capture what Facebook rendered when typing was attempted, providing visibility into any subsequent failures.

**Session Status:**
The refactored version was ready for testing but Amos exited before verification. The next session should run the script again to confirm whether the dual-scope refactoring resolves the composer interaction issues.
