# SESSION CHUNK 2026-06-29 — Condition Filter Prominence and Sticky User Selection

*ID: passage-7ee44c08-e09d-4ca4-85f7-e2d75d1c672d*
*Created: 2026-07-01*

---

SESSION CHUNK 2026-06-29 — Condition Filter Prominence and Sticky User Selection

STRUCTURED
Files: /c/Users/Amos/projects/braindexer/routers/therapies.py, /c/Users/Amos/projects/braindexer/static/index.html, /c/Users/Amos/projects/braindexer/ROADMAP.md, /c/Users/Amos/projects/braindexer/AGENCY_MIGRATION_PLAN.md
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: mcp__claude-in-chrome__javascript_tool, mcp__claude-in-chrome__navigate, mcp__claude-in-chrome__computer, Bash, Glob, Grep, Read, Edit, ToolSearch, mcp__claude-in-chrome__tabs_context_mcp, Write
Dates: June 29

SUMMARY
The decision to make Alzheimer's Disease the default condition on the homepage led to design work on condition visibility and user preference persistence. Since scores are stored per `therapy_conditions` row, the listing view becomes meaningless without a condition context — showing NULLs or arbitrary scores. The solution: add a prominent blue banner between the search box and filter row reading "Condition: **Alzheimer's Disease** [change]" with the ability to click "change" to open the condition dropdown. The banner serves two purposes: it makes the condition context highly visible so users understand which condition's evidence scores they're looking at, and it provides a clear interaction point to switch conditions if needed. Additionally, Amos requested that the last user-selected condition be sticky across page reloads, using localStorage to persist the selection with fallback to Alzheimer's Disease if no prior selection exists. This mirrors the existing view-toggle localStorage pattern. The implementation chains condition loading: load saved preference → fall back to AD → save on every change. When member login arrives in the future, member attributes should take precedence over localStorage. Amos was clear that Alzheimer's Disease should be permanently pinned as default (not rely on API ordering) to ensure consistency as more conditions are added to the platform. The sticky condition was already implemented and deployed in the final commit of this session.
