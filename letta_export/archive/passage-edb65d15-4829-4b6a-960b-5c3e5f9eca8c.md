# SESSION CHUNK 2026-06-29 — Product Roadmap Documentation and Phases I–V Planning

*ID: passage-edb65d15-4829-4b6a-960b-5c3e5f9eca8c*
*Created: 2026-07-01*

---

SESSION CHUNK 2026-06-29 — Product Roadmap Documentation and Phases I–V Planning

STRUCTURED
Files: /c/Users/Amos/projects/braindexer/routers/therapies.py, /c/Users/Amos/projects/braindexer/static/index.html, /c/Users/Amos/projects/braindexer/ROADMAP.md, /c/Users/Amos/projects/braindexer/AGENCY_MIGRATION_PLAN.md
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: mcp__claude-in-chrome__javascript_tool, mcp__claude-in-chrome__navigate, mcp__claude-in-chrome__computer, Bash, Glob, Grep, Read, Edit, ToolSearch, mcp__claude-in-chrome__tabs_context_mcp, Write
Dates: June 29

SUMMARY
Amos asked for a comprehensive product roadmap document capturing all planned phases of development, building on the earlier agency migration plan. Daimon created `ROADMAP.md` at the repository root, documenting five phases: Phase 0 (agency migration, completed schema design), Phase 1 (agency migration implementation, UINN utility, null-clobber fix), Phase 2 (read path cutover to new tables, mirror removal), Phase 3 (full elimination of therapy_status, cleanup), Phase 4 (membership/login infrastructure, reviewer board accreditation audit, claim-level annotation system), Phase 5 (AI classification layer for annotations, advanced features). The reviewer board system was fully specified in Phase IV including the annotation data model (`claim_annotations` table with therapy_id, condition_id, layer, claim_text, critique_type, scope, reviewer_id), bias mitigation approach (transparent disagreement flagging, factual/interpretive claim separation, structural diversity), and dependency graph showing how it requires membership and accreditation audit as prerequisites. The roadmap also clarifies why certain technical decisions are deferred: the reviewer system can't be built until reviewer identity and credentials are persistent (requiring login). The clinical review system emerged as a major architectural addition whose scope and sequencing needed explicit documentation to prevent premature implementation.
