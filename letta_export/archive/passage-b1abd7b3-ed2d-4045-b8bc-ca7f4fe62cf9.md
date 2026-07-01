# WORLD PATTERN 2026-06-05 — Browser event-loop dependent waits can stall during h

*ID: passage-b1abd7b3-ed2d-4045-b8bc-ca7f4fe62cf9*
*Created: 2026-06-06*

---

WORLD PATTERN 2026-06-05 — Browser event-loop dependent waits can stall during heavy processing — 2026-06-06

PRINCIPLE: page.wait_for_timeout() depends on the browser's event loop and will block indefinitely if the page becomes temporarily unresponsive.

NARRATIVE: After Pexels image upload to Facebook composer, an 8-second browser-dependent wait was added to allow FB to process the image. In practice, the upload operation made the tab unresponsive enough that page.wait_for_timeout(8000) never resolved, hanging the script indefinitely. Switching to Python's time.sleep(8) unblocked it immediately — the sleep doesn't depend on the browser's event loop, only real elapsed time. This is particularly risky for file uploads and heavy DOM mutations where temporary unresponsiveness is expected but not guaranteed to resolve within the timeout.
