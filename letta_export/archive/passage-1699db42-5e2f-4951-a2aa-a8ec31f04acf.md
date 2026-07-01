# SESSION CHUNK 2026-06-10 — Applying Context-Aware Filter Mode Fix

*ID: passage-1699db42-5e2f-4951-a2aa-a8ec31f04acf*
*Created: 2026-06-10*

---

SESSION CHUNK 2026-06-10 — Applying Context-Aware Filter Mode Fix

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\static\index.html, C:\Users\Amos\projects\braindexer\routers\therapies.py, C:\Users\Amos\projects\braindexer\diag_search.py, C:\Users\Amos\projects\braindexer\diag_search2.py, C:\Users\Amos\projects\braindexer\diag_search3.py
Errors: Exit code 1
/usr/bin/bash: line 10: cd: C:UsersAmosprojectsbraindexer: No such f; Exit code 7
Note: Unnecessary use of -X or --request, POST is already inferred.; Exit code 1
python : C:\Users\Amos\AppData\Local\Python\pythoncore-3.14-64\pytho; Exit code 1
C:\Users\Amos\AppData\Local\Microsoft\WindowsApps\python.exe
C:\Use; Exit code 1
C:\Users\Amos\AppData\Local\Python\bin\python.exe : C:\Users\Amos\Ap; Exit code 1; Exit code 1
C:\Users\Amos\AppData\Local\Python\bin\pip.exe
pip : WARNING: Packa; Exit code 127
/usr/bin/bash: line 1: gh: command not found; Exit code 1
gh : The term 'gh' is not recognized as the name of a cmdlet, functi; Exit code 1
python :   File "<string>", line 9
At line:1 char:41
+ cd "C:\User; Exit code 1
Rosemary, Carnosic Acid python : Traceback (most recent call last):; Exit code 2
/usr/bin/bash: eval: line 1: syntax error near unexpected token `.Li
Tools used: ToolSearch, Glob, Read, Grep, Edit, mcp__matrix__reply, Bash, PowerShell, WebFetch, Write

SUMMARY
Applied the one-line fix identified in the previous session to the `onFilterChange()` function in `static/index.html`. The bug was that when a user performed a search first (setting `currentMode = 'search'`), the flag persisted even after they switched to using the condition filter dropdown. The `onFilterChange()` function checked for this flag and called `doSearch()` instead of `loadList()`, which required `t.embedding IS NOT NULL`. Since no therapies had embeddings yet (pre-Research & Summarize), the search path filtered out all results. The fix removed the `|| currentMode === 'search'` condition, ensuring that an empty search box always triggers `loadList()` regardless of the previous interaction mode. This decouples mode state from actual user intent: if the search field is empty, the user intends to browse, not search. The commit was made and the fix was verified to be correct locally.
