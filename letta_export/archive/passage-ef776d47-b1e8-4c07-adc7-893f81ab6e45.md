# SESSION CHUNK 2026-06-10 — Condition Type Architecture and AI Prompt Refinement

*ID: passage-ef776d47-b1e8-4c07-adc7-893f81ab6e45*
*Created: 2026-06-10*

---

SESSION CHUNK 2026-06-10 — Condition Type Architecture and AI Prompt Refinement

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\diag_conditions.py, C:\Users\Amos\projects\braindexer\diag_db.py, C:\Users\Amos\projects\braindexer\.env, C:\Users\Amos\projects\braindexer\models.py, C:\Users\Amos\projects\braindexer\setup_db.py, C:\Users\Amos\projects\braindexer\routers\conditions.py, C:\Users\Amos\projects\braindexer\routers\therapies.py, C:\Users\Amos\projects\braindexer\services\scraper.py, C:\Users\Amos\projects\braindexer\static\therapy.html, C:\Users\Amos\projects\braindexer\main.py, C:\Users\Amos\projects\braindexer\static\index.html, C:\Users\Amos\projects\braindexer\services\summarizer.py
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<; Exit code 1
/usr/bin/bash: line 1: cd: C:UsersAmosprojectsbraindexer: No such fi; Exit code 1
At line:1 char:201
+ ... y static/index.html static/therapy.html; g
Tools used: Glob, Read, Write, Edit, Bash, PowerShell

SUMMARY
Based on diagnostic findings, a new architectural pattern emerged: distinguishing between neurological/psychiatric conditions (appropriate for deep linking and condition-specific summaries) and general medical conditions (informational only). The implementation added a `type` column to the conditions table and restructured the AI prompt to return a JSON object with two arrays: `{"neurological": [...], "general": [...]}`. This required updating `_detect_related_conditions` to use a more nuanced prompt that correctly identifies Carnosic Acid's relevance to Parkinson's, Depression, Anxiety, Epilepsy, and Cognitive Decline as neurological conditions while appropriately separating generic antioxidant benefits (Cancer, Obesity, Diabetes prevention) into the general medical category. The general medical conditions appear to users only via an "Other Medical Conditions" button that opens a simple informational popup rather than leading to full condition-specific pages. The `_upsert_detected_conditions` function was updated to tag conditions with their type on insertion, preventing duplicates and ensuring proper categorization.
