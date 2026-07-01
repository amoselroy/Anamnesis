# WORLD PATTERN 2026-06-04 — Playwright/Facebook automation — click mechanics and 

*ID: passage-9445e0b5-d4dc-4ab3-b53f-bbf8ab6db61a*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Playwright/Facebook automation — click mechanics and infrastructure lessons — 2026-06-02

Learned from fb_poster image post debugging: (7) Silent click timeouts destroy debugging feedback loops — Playwright's .click() has a 30-second default timeout and silently retries interception failures; three selectors × 30s = 90 seconds of frozen progress with the modal closing from inactivity; use page.evaluate("el.click()") for instantaneous JS click that bypasses all retry logic. (8) Screenshot at the moment of failure, not after — adding page.screenshot() calls at key moments (composer open, text typed, after image upload, before submit) immediately revealed the modal was ready; the issue was the click mechanism, not the selectors. (9) Form interactions can invalidate earlier ones — uploading an image via set_input_files() caused Facebook to clear the text area; when automating multi-step forms, verify each action doesn't reset prior state; safe order: upload image first, type text after. (10) offsetParent !== null is a reliable visible-element filter in injected JS — when querying elements via page.evaluate(), this reliably excludes hidden and off-screen elements, more predictable than checking computed styles or obfuscated class names. (11) Scheduled tasks are silent infrastructure — fb_poster's Task Scheduler tasks were absent with no error anywhere; the script simply wasn't running; when automation goes quiet, check the scheduler before the code.
