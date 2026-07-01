# WORLD PATTERN 2026-06-04 — Facebook Post Sharing from Brokerage Pages — 2026-05-

*ID: passage-50effda2-efa0-4415-963d-e19e5d8633cd*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Facebook Post Sharing from Brokerage Pages — 2026-05-29/30 (debugging in progress)

When automating post sharing from a source Facebook Page (e.g., Exit on the Hudson Realty) to a destination page via Playwright: (1) share button location varies — icon-only buttons with no visible text, right-click inspection often blocked by Facebook; (2) Playwright's accessibility API may not be available in all versions, making aria-label queries unreliable; (3) posts may load in modal overlays on top of the feed rather than as standalone pages, placing the Share button inside the dialog; (4) CSS selectors and role-based selectors often fail on icon buttons; (5) **coordinate-based clicking works where selectors fail** — clicking at pixel coordinates identified visually can trigger the Share button when selectors miss it; (6) clicking the Share button opens Facebook's share **dropdown menu** (with destination options like "Share to Feed", "Share to Page") not a post composition field — subsequent interaction requires selecting destination and providing commentary in a different modal, not inline to the dropdown. Investigation ongoing: determining how to programmatically select share destination and add commentary post-share-button-click.
