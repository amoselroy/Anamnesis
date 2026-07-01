# SESSION CHUNK 2026-06-09 — Designing User Experience for Condition-Aware Therapy

*ID: passage-92be0f1d-bfa0-4cfd-a06f-0c50531b323d*
*Created: 2026-06-09*

---

SESSION CHUNK 2026-06-09 — Designing User Experience for Condition-Aware Therapy Pages

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\setup_db.py, C:\Users\Amos\projects\braindexer\models.py, C:\Users\Amos\projects\braindexer\routers\conditions.py, C:\Users\Amos\projects\braindexer\main.py, C:\Users\Amos\projects\braindexer\routers\therapies.py, C:\Users\Amos\projects\braindexer\static\index.html, C:\Users\Amos\projects\braindexer\static\therapy.html, C:\Users\Amos\projects\braindexer\static\admin.html
Errors: Exit code 1
Traceback (most recent call last):
  File "C:\Users\Amos\projects\b
Tools used: Read, Edit, Write, Bash
URLs: https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>

SUMMARY
User proposed a sophisticated user experience design: when a therapy is accessed via a condition search (e.g., user browses "Alzheimer's Disease" therapies), the page defaults to that condition's condition-specific data. When a therapy is accessed directly through browsing (no condition context), the page shows a generalized summary page listing all associated conditions as selectable chips at the top, with a general summary that synthesizes what is known about the therapy across all its relevant conditions. Clicking a condition chip then loads the condition-specific page with that condition's summaries and scores. This two-mode design elegantly handles both entry paths: search-driven access gets condition-specific data immediately, while browsing-driven access gets a unified view with ability to drill into condition-specific details. The design recognizes the difference between "I'm researching what can help Alzheimer's" (condition-first entry, expects Alzheimer's-specific data) and "I found this therapy called Lecanemab, tell me what I need to know" (therapy-first entry, wants the full picture before choosing a condition). This architectural insight requires two distinct UI templates or conditional rendering: a therapy page vs a therapy-condition page, with router logic to determine which to display based on the entry point.
