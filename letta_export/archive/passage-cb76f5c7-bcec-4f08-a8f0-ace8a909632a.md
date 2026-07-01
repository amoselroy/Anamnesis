# SESSION CHUNK 2026-06-19 — UI Redesign from Remove/Restore to Hide/Add Toggles w

*ID: passage-cb76f5c7-bcec-4f08-a8f0-ace8a909632a*
*Created: 2026-06-19*

---

SESSION CHUNK 2026-06-19 — UI Redesign from Remove/Restore to Hide/Add Toggles with Hidden-by-Default Fetch

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/main.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/static/admin.html, C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/pseudocode.md, C:/Users/Amos/.claude/journal_entry_tmp.md, C:/Users/Amos/.claude/projects/C--Users-Amos/memory/feedback_journal_append_only.md
Errors: Exit code 2
C:\Users\Amos\AppData\Local\Python\pythoncore-3.14-64\python.exe: ca; The user doesn't want to proceed with this tool use. The tool use was rejected (
Tools used: Bash, Read, Edit, Grep, Glob, Write, PowerShell

SUMMARY
User feedback highlighted that the UI language of "Remove/Restore" implied deletion rather than condition-scoped visibility management. The modal was redesigned to use "Hide" and "Add" language, more accurately reflecting that articles are being shifted between active and hidden states per condition, not deleted globally. Simultaneously, the fetch behavior was changed so that all new articles land in the hidden state by default (dimmed, green "Add" button). This inverts the curation workflow: newly fetched articles are hidden until explicitly promoted to active. Pre-existing articles (from backfilled data) remain active to maintain continuity. The modal was restructured to show a single unified list with a count summary in the breadcrumb (`N active · M hidden`) rather than split active/hidden sections, making the toggle workflow clearer. Toast messages were updated to reflect the new semantics: "Article hidden from this condition" and "Article added to this condition."
