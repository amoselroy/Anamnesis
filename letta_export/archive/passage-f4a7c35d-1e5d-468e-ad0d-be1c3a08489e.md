# WORLD PATTERN 2026-06-11 — Cross-domain link rejection causing architectural fal

*ID: passage-f4a7c35d-1e5d-468e-ad0d-be1c3a08489e*
*Created: 2026-06-11*

---

WORLD PATTERN 2026-06-11 — Cross-domain link rejection causing architectural false path failures — 2026-06-11

PRINCIPLE: Link extraction tools that restrict to same-domain links will reject event links that live on third-party ticketing platforms, leaving only navigation pages and causing false cascade failures across all subsequent paths.

NARRATIVE: Jersey City Theater Center's actual events live on `seetickets.us/jctcenter`, but the homepage is `jctcenter.org`. The `get_event_links` depth filter rejects cross-domain links, so it returns only 9 navigation pages (`/history`, `/past-performances`, etc.). Path A tries these pages and fails (no event data); Path B doesn't trigger because 9 links exceed the threshold; Path C runs Playwright and finds the exact same navigation pages, failing again. The issue appeared to be a scraping/rendering failure, but it was actually architectural: the event data was inaccessible via the restricted link scope. This pattern generalizes widely: when a venue outsources event hosting to a third-party platform, same-domain-only link extraction will always fail, and the failure will cascade through all downstream paths as if rendering or extraction were broken. The lesson is to validate that the URL itself actually contains the desired content before debugging why link following doesn't work.
