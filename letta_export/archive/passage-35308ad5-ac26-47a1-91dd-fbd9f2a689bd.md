# WORLD PATTERN 2026-06-04 — Facebook session separation pattern — 2026-06-02

*ID: passage-35308ad5-ac26-47a1-91dd-fbd9f2a689bd*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Facebook session separation pattern — 2026-06-02

When multiple automation scripts share a single session file, one script running in page-actor context (logged in as a Page) will overwrite the session and contaminate the other script's next run. Pattern observed: `re_poster.py` runs as HobokenNJRealEstate page, saves session; `fb_poster.py` loads same file and tries to post to a personal-account-only venue (group), failing silently. Fix: dedicated session files per script. `fb_poster.py` uses `facebook_session_personal.json` (personal account context required for group posting); `re_poster.py` and `brokerage_sharer.py` use their own files or script-specific files. One-time setup: `fb_poster.py --login` to create the clean personal session. Separation is permanent — the two scripts never touch each other's session files.
