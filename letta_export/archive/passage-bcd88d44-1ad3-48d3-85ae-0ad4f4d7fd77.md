# SESSION CHUNK 2026-07-17 — Overnight Letta container crash loop, anamnesis expor

*ID: passage-bcd88d44-1ad3-48d3-85ae-0ad4f4d7fd77*
*Created: 2026-07-28*

---

SESSION CHUNK 2026-07-17 — Overnight Letta container crash loop, anamnesis export breakage diagnosis and repair

STRUCTURED
Files: C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\b04e6cce-4f6b-4e5b-8c61-fe42032d8dc7\scratchpad\debug_monitor.py, C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\b04e6cce-4f6b-4e5b-8c61-fe42032d8dc7\scratchpad\check_keyring.py, C:\Users\Amos\.daimon\anamnesis\system\session_sync.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_memshepherd_session_sync_401.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md
Errors: Exit code 2
C:\Users\Amos\AppData\Local\Python\pythoncore-3.14-64\python.exe: ca
Tools used: Bash, Read, PowerShell, Grep, Write, Glob, Edit

SUMMARY
Overnight, the `memshepherd-letta` container crash-looped five times (RestartCount: 5), restarting until stabilizing at 10:54 UTC. Initial investigation of logs pointed to a Neon Postgres connection failure during the container's Alembic database migration step on startup: `sqlalchemy.exc.InterfaceError: (pg8000.exceptions.InterfaceError) network error`. The root cause was later clarified by the user: when logged in that morning, the network showed significant packet loss (25%) and high latency, which explained the migration's connection dropping mid-check. The container's `unless-stopped` Docker policy kept relaunching it until the network stabilized. This was not a code bug and required no action; it was a transient network condition hitting Letta's most connection-vulnerable boot step.

During the post-incident investigation, a more serious issue surfaced: the health monitor's weekly heartbeat hadn't updated since July 5th — 12 days prior — despite the Windows scheduled task reporting successful daily runs at 8 AM. The monitor's logic only sends a heartbeat when zero issues are detected; if issues are found, it sends an alert instead and skips the heartbeat. Investigation revealed a live ongoing issue: `check_anamnesis_lag` was flagging a gap between the last processed session (2026-07-16 21:28 UTC) and the last anamnesis export commit (2026-07-14 21:14 UTC). This was the same failure class as a previous July 1st incident: the SessionEnd hook (`session_sync.py`) was silently not exporting session blocks/passages to the private anamnesis repository.

Root cause analysis traced the failure to a credential/authentication issue. The Letta container had been rebuilt with `SECURE=true` on 2026-07-15 (security hardening triggered by Fable's port security audit), which implemented auto-generated passwords and required all HTTP requests to include an `Authorization: Bearer <password>` header. A centralized `letta_ops.py` module was created in the `memshepherd` hooks repository to handle this authentication pattern, and 12 scripts within that repo were updated to use it. However, `session_sync.py` lives in the separate private `anamnesis` repository and predates the auth consolidation. It was never migrated to use the new header pattern, so every API call since the SECURE-mode hardening has failed with `HTTP Error 401: Unauthorized`. This explains both why the exports stopped on exactly July 14th and why the health monitor's heartbeat couldn't fire — it was finding a real ongoing issue each day.

The fix was applied to `session_sync.py`'s `fetch_blocks()` function, adding the same `Authorization: Bearer <password>` header pattern used elsewhere in the deployment (with the password retrieved from Windows Credential Manager via `keyring`, matching the pattern in `letta_ops.py`). The repair was verified with a live test run and succeeded in backfilling 58 queued passages that had accumulated since July 14th, all of which were then pushed to `origin/main`. The health monitor subsequently ran clean with a fresh heartbeat, confirming the issue was fully resolved.

The Alembic migration step that triggered the crash loop is Letta's standard routine startup procedure: every time the container boots, it checks the Postgres schema version against what the installed Letta version expects and applies any pending DDL changes. In this case it was a fast no-op check with no schema changes, but the step requires a live database connection to run, making it the point in the boot sequence most exposed to network conditions like the 25% packet loss present that morning. Each restart hit this step, the connection dropped, migration failed, the container exited, and Docker relaunched it until the network stabilized enough for the check to complete.
