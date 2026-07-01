# SESSION CHUNK 2026-06-27 — Full Architectural Redesign Recognition — Multi-Entit

*ID: passage-5bb7bed6-cf0c-426f-a4ce-7abeb9f89f77*
*Created: 2026-07-01*

---

SESSION CHUNK 2026-06-27 — Full Architectural Redesign Recognition — Multi-Entity Model for Approvals and Trials

STRUCTURED
Files: C:\Users\Amos\.claude\projects\C--Users-Amos\memory\feedback_critical_thought.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md, C:\Users\Amos\.claude\plans\immutable-greeting-blum.md, C:\Users\Amos\projects\braindexer\AGENCY_MIGRATION_PLAN.md
Errors: The user doesn't want to proceed with this tool use. The tool use was rejected (
Tools used: Glob, Bash, Grep, Read, Write, Edit, ToolSearch, WebSearch, EnterPlanMode, Agent, ExitPlanMode, mcp__claude_ai_Google_Drive__create_file

SUMMARY
Amos recognized that his one-row-per-therapy consolidated agency table design would break on real data due to three critical issues: (1) combination drugs like Namzaric (donepezil + memantine) can't be represented in a single-INN schema, (2) FDA approves the same INN multiple times for different formulations/indications requiring separate records, (3) trial phase is indication-specific (a drug in Phase III for Alzheimer's but Phase II for Parkinson's needs two records, not one). This led to a fundamental architectural realization that approval records and trial records must be separated by indication and treated as first-class entities, not collapsed into therapy-level summaries. The correct model requires: agency_approvals (one per regulatory approval event with UINN, agency, indication, status, dates), trial_records (one per NCT ID + condition), with therapy-facing join tables (therapy_approvals, therapy_trials) resolving the matches. This is substantively different from the existing therapy_status table which conflates agency data with platform-specific curator data.
