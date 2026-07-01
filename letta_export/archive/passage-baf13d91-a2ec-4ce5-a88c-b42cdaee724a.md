# SESSION CHUNK 2026-06-19 — Therapy Page Display Not Reflecting Hide/Add Actions

*ID: passage-baf13d91-a2ec-4ce5-a88c-b42cdaee724a*
*Created: 2026-06-19*

---

SESSION CHUNK 2026-06-19 — Therapy Page Display Not Reflecting Hide/Add Actions

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/main.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/static/admin.html, C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/pseudocode.md, C:/Users/Amos/.claude/journal_entry_tmp.md, C:/Users/Amos/.claude/projects/C--Users-Amos/memory/feedback_journal_append_only.md
Errors: Exit code 2
C:\Users\Amos\AppData\Local\Python\pythoncore-3.14-64\python.exe: ca; The user doesn't want to proceed with this tool use. The tool use was rejected (
Tools used: Bash, Read, Edit, Grep, Glob, Write, PowerShell

SUMMARY
After implementing the toggle system in the modal, Amos noticed that Hide/Add actions in the Manage News modal had no effect on articles displayed on the therapy page itself. Root cause: the therapy detail API (`get_therapy`) only applied the `shown_condition_ids` filter when a `?condition=` query parameter was present. Without it, the endpoint returned all non-deleted articles regardless of visibility state. The initial fix added auto-selection of the first active condition when no condition was in the URL, silently updating the browser URL to include it. This ensured the visibility filter always applied. However, Amos later requested the opposite approach: suppress news entirely when no condition is selected, showing a notice "Select a condition above to see curated news articles" instead of auto-selecting. This gives users explicit control over condition selection and makes clear that news is condition-scoped, not a global pool.
