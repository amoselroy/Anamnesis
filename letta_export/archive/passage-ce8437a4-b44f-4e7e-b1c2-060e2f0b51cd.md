# WORLD PATTERN 2026-06-04 — Silent scheduler failures — 2026-06-02

*ID: passage-ce8437a4-b44f-4e7e-b1c2-060e2f0b51cd*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Silent scheduler failures — 2026-06-02

When a scheduled task appears to be configured but never runs, the root cause is often: (1) batch file exists but Task Scheduler job was never registered (common when .bat file is created post-setup), (2) task runs but fails silently with no error log, (3) task context (working directory, PATH, environment variables) differs from manual terminal execution. Investigation checklist: (1) verify task exists in Task Scheduler GUI and is enabled, (2) check task history/logs for execution and error codes, (3) manually trigger task to see error messages, (4) compare environment between manual run and scheduled context. Pattern observed 2026-06-02: fb_poster .bat files existed but Task Scheduler jobs were never created, causing weeks of silent posting failure. Once recreated with working directory and PATH matching terminal environment, automation resumed without code changes.
