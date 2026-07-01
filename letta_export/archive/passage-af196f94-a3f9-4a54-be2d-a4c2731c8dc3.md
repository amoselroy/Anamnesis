# SESSION CHUNK 2026-05-31 — Claude Code Remote Control Session Management on Andr

*ID: passage-af196f94-a3f9-4a54-be2d-a4c2731c8dc3*
*Created: 2026-06-02*

---

SESSION CHUNK 2026-05-31 — Claude Code Remote Control Session Management on Android App

STRUCTURED
Files: none
Errors: The user doesn't want to proceed with this tool use. The tool use was rejected (
Tools used: Agent, AskUserQuestion
URLs: https://claude.ai/code/routines, https://github.com/ORG/REPO"}}, https://drivemcp.googleapis.com/mcp/v1, https://claude.ai/customize/connectors, https://..."}], https://claude.ai/code/routines/{ROUTINE_ID}`, https://github.com/org/repo
Dates: Jun 2, 2026

SUMMARY
Amos asked how to properly close a remote control session on the Claude mobile Android app. The initial confusion centered on whether the back arrow button actually terminates the session or merely disconnects the mobile client while leaving the desktop session alive.

Investigation revealed that the back arrow is a navigation control only — it disconnects the mobile client from viewing the session, but the remote control session on the desktop continues running. The session appears in the mobile app's list because the underlying Claude Code process on the desktop is still active. To actually close the session, the user must go to the desktop terminal and either press `Ctrl+C` or type `/exit` to stop the Claude Code process entirely. The mobile app has no independent "end session" control — it can only disconnect from the current view.

Sessions in the mobile app's list persist as long as the desktop Claude Code process is running. Seeing a session in the list indicates it is still active and available for reconnection. Understanding this distinction — between mobile client disconnect (back arrow) and actual session termination (desktop-side Ctrl+C or /exit) — clarifies the expected behavior.
