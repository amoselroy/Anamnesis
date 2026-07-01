# WORLD PATTERN 2026-06-17 — Facebook link preview fails silently for blocked CDN 

*ID: passage-77bca5a3-ea15-4dd5-9f04-fb670591b0a6*
*Created: 2026-06-17*

---

WORLD PATTERN 2026-06-17 — Facebook link preview fails silently for blocked CDN domains, requires fallback to direct upload — 2026-06-17

PRINCIPLE: Social media platforms that can't scrape certain domains' link preview metadata will fall back to a generic/repeated placeholder image, and the failure is silent (no error, just bad UX).

NARRATIVE: SeeTickets CDN image URLs were being posted with `Image Type: source`, expecting Facebook's link preview to render the image. However, Facebook can't scrape SeeTickets (blocked), so it silently fell back to a generic/repeated SeeTickets placeholder image instead of showing the event-specific image. The solution was to detect CDN domains that don't work with link preview and assign `Image Type: native` instead, uploading the image directly. This pattern generalizes: when a social media platform claims to support link preview but certain domains are blocked or don't have proper metadata, the failure mode is silent degradation to a generic image. The fix is either to upload directly ("native") or acknowledge failure and use a fallback ("none"), not to rely on link preview for blocked domains.
