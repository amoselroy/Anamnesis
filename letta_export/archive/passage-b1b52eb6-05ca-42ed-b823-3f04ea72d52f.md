# SESSION CHUNK 2026-06-29 — Post-Demo Fixes — Attribution Correction, Preventive 

*ID: passage-b1b52eb6-05ca-42ed-b823-3f04ea72d52f*
*Created: 2026-07-01*

---

SESSION CHUNK 2026-06-29 — Post-Demo Fixes — Attribution Correction, Preventive Mode, Donepezil Re-entry

STRUCTURED
Files: /c/Users/Amos/projects/braindexer/routers/therapies.py, /c/Users/Amos/projects/braindexer/static/index.html, /c/Users/Amos/projects/braindexer/ROADMAP.md, /c/Users/Amos/projects/braindexer/AGENCY_MIGRATION_PLAN.md
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: mcp__claude-in-chrome__javascript_tool, mcp__claude-in-chrome__navigate, mcp__claude-in-chrome__computer, Bash, Glob, Grep, Read, Edit, ToolSearch, mcp__claude-in-chrome__tabs_context_mcp, Write
Dates: June 29

SUMMARY
After the live demo, three fixes were needed to finalize the benfotiamine profile and re-establish Donepezil's agency status. First, the BenfoTeam trial attribution needed to change from "Feldman et al., 2024" to "Sano, Feldman et al., 2024" so Dr. Sano would see her name in the clinical summary. This required adding a `summary_clinical` field to the `ConditionScoresUpdate` model in models.py, which was completed and pushed but took multiple Render deploy cycles to land. Second, benfotiamine's Mode of Action badges needed a second badge to fill out the sparse single-badge appearance — "Neuroprotective" alone looked incomplete. Amos and Daimon agreed "Preventive" was the appropriate addition (reflecting the prevention-oriented hypothesis of the BenfoTeam trial and the thiamine-deficiency-correction mechanism). Third, Donepezil's FDA and EMA approval badges didn't appear after the live re-add during the demo because the new therapy record had no `therapy_status` rows with agency data. Daimon manually set the agency status using the override API (`set_agency_status()` endpoint) with correct NDA numbers and approval dates for both FDA (NDA020690) and EMA (EU/1/00/137). The Donepezil re-add itself was smooth, but the absence of pre-populated agency status highlighted a broader issue: when therapies are created without running the full pipeline, they need an explicit mechanism to populate agency data. This also raised the question of whether Donepezil needed fresh research/summarization or could rely on training knowledge — Amos correctly asked why the summarizer needed to run at all for such a well-established drug, leading to the distinction between "full research" (paper fetching) and "summarize-only" (LLM assessment from training data).
