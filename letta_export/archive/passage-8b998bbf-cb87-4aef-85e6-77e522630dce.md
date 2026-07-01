# WORLD PATTERN 2026-06-11 — Stub redirect pages unsuitable for scraping — 2026-06

*ID: passage-8b998bbf-cb87-4aef-85e6-77e522630dce*
*Created: 2026-06-11*

---

WORLD PATTERN 2026-06-11 — Stub redirect pages unsuitable for scraping — 2026-06-11

PRINCIPLE: Event pages that function solely as external platform redirects (containing only links to third-party ticketing platforms with zero event data on the page itself) are unsuitable for scraping and should be identified before adding to source lists, regardless of available technical approaches.

NARRATIVE: Hudson Theatre Works's tickets page (`hudsontheatreworks.org/tickets`) contained only 2 external Eventbrite redirect links and no event dates, times, or venue information. Path A failed (external links filtered); Path B failed because the LLM had no event data to extract from the listing page; Path C would find the same external links. The issue was not a technical failure but an architectural one: the page was a stub redirect portal, not an event source. While technically a vision-capable LLM could potentially read event flyers on the page, or the external links could be followed to Eventbrite organizer pages, the root issue is that the source URL itself contains no event information. The proper fix was not to build technical workarounds but to identify that the source URL was unsuitable and either remove it or replace it with the primary platform URL (Eventbrite organizer page). This generalizes: source evaluation should screen for whether the proposed URL actually contains event information, not whether it might theoretically be made to work via increasingly elaborate scraping techniques.
