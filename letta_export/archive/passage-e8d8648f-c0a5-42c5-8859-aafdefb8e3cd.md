# SESSION CHUNK 2026-05-31 — Listing Active Sessions in Claude Code Terminal

*ID: passage-e8d8648f-c0a5-42c5-8859-aafdefb8e3cd*
*Created: 2026-06-02*

---

SESSION CHUNK 2026-05-31 — Listing Active Sessions in Claude Code Terminal

STRUCTURED
Files: none
Errors: The user doesn't want to proceed with this tool use. The tool use was rejected (
Tools used: Agent, AskUserQuestion
URLs: https://claude.ai/code/routines, https://github.com/ORG/REPO"}}, https://drivemcp.googleapis.com/mcp/v1, https://claude.ai/customize/connectors, https://..."}], https://claude.ai/code/routines/{ROUTINE_ID}`, https://github.com/org/repo
Dates: Jun 2, 2026

SUMMARY
Amos accidentally triggered the `/schedule` command (which presents a workflow for creating scheduled remote agents) when he was actually trying to list active Claude Code sessions from the terminal.

Clarification was provided that there is no direct "list sessions" command in the Claude Code terminal itself. However, the following alternatives exist for viewing active sessions:
- **`claude --resume`** — Shows the session list from the terminal, including remote control sessions, allowing the user to see which sessions are currently active
- **`/status`** — If already inside a session, displays remote control connection status for that specific session
- **Web interface at claude.ai/code** — Shows all active sessions with connection status in the browser

For Amos's use case of checking active sessions from the terminal, `claude --resume` is the most direct equivalent to a session listing command.
