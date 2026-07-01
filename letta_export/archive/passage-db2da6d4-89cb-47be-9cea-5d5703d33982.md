# WORLD PATTERN 2026-06-04 — JavaScript offsetParent filtering for element visibil

*ID: passage-db2da6d4-89cb-47be-9cea-5d5703d33982*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — JavaScript offsetParent filtering for element visibility — 2026-06-02

When querying visible elements in Playwright, `.is_visible()` can return True for elements that are not actually user-interactable (e.g., behind modal overlays or in display:none ancestors). More reliable visibility check: `element.offsetParent !== null`. The offsetParent property is null if an element or any ancestor has `display: none`, is not rendered, or is outside the visible viewport. Combining both approaches catches visibility issues: collect all matching elements, filter by `offsetParent !== null` to identify genuinely renderable elements, then select by proximity. Applied to Facebook action bar button selection — eliminated false-positive visibility matches that Playwright missed.
