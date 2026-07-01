# WORLD PATTERN 2026-06-11 — Image-based event flyers requiring vision-capable ext

*ID: passage-3e6b0ebe-8e55-43d0-ae4d-887f60fbf7de*
*Created: 2026-06-11*

---

WORLD PATTERN 2026-06-11 — Image-based event flyers requiring vision-capable extraction — 2026-06-11

PRINCIPLE: Event venues that display event information exclusively as image flyers (graphic designs rather than text) require a vision-capable LLM extraction path that downloads and analyzes image content, a capability not yet implemented in the standard scraper paths.

NARRATIVE: Barsky Gallery and Deep Space Gallery both displayed their "Meet the Artist" and opening-reception events as image flyers rather than text listings. Neither gallery posted event text like "Opening Reception, June 15, 7 PM" — the information existed only in visual form as graphic designs meant for social media. The standard scraper paths (A: static links, B: LLM listing extraction, C: Playwright + LLM) all assume text-based content extraction and would fail on image-only content. A vision-capable "Path V" could download image URLs from the page and pass them to a vision LLM (Claude's vision capability) to extract event details from flyers. This is not yet implemented. The pattern generalizes: venues using design-first event promotion (common for art galleries, some cultural institutions) will have information locked in image format, requiring either vision capability or manual extraction. The decision to move these sources to Facebook events pages (which use text-based event posting) was pragmatic for the current implementation, but the image-extraction capability represents a future enhancement.
