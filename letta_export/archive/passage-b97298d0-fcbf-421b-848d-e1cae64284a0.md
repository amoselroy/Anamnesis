# SESSION CHUNK 2026-06-19 — Summary Section Output Refinement and Truncation Issu

*ID: passage-b97298d0-fcbf-421b-848d-e1cae64284a0*
*Created: 2026-06-19*

---

SESSION CHUNK 2026-06-19 — Summary Section Output Refinement and Truncation Issues

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\services\summarizer.py, C:\Users\Amos\projects\braindexer\routers\therapies.py, C:\Users\Amos\projects\braindexer\static\admin.html, C:\Users\Amos\projects\braindexer\static\therapy.html, C:\Users\Amos\projects\braindexer\main.py, C:\Users\Amos\projects\braindexer\models.py, C:\Users\Amos\projects\braindexer\services\scraper.py, C:\Users\Amos\projects\braindexer\routers\admin.py
Errors: Exit code 1
/usr/bin/bash: line 1: cd: C:UsersAmosprojectsbraindexer: No such fi; Exit code 1
At line:1 char:154
+ ... services/scraper.py static/therapy.html; g; Exit code 1
On branch master
Your branch is up to date with 'origin/master'.

Ch; <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Read, Edit, Bash, PowerShell, Grep, Glob

SUMMARY
After deploying the structured section architecture (Effectiveness, Safety, Side Effects), the output was completely wrong: the LLM was outputting only the three sections with no main summary content. The `_SECTION_INSTRUCTION` prompt said "Structure your **entire** response using exactly these three headers," which the LLM correctly interpreted literally. The fix changed the language to "After your main summary, append" so the LLM would write the full summary first, then add the three sections below. Separately, Amos requested that the three sections shift from narrative synthesis to analytical and factual content — pulling actual numbers like participant counts, percentages, incident rates, study durations, effect sizes measured via imaging — rather than prose summaries. The prompt was updated to emphasize numeric data extraction and study specifics. Additionally, the Informed and Clinical summaries were being truncated mid-output (Informed cut off at Safety, Clinical missing Side Effects entirely), revealing that `max_tokens=1800` was still insufficient for the longer structured content. The limit was raised to 3000, which accommodated the full structured output across all three audience levels without cutoff. Finally, the mechanism field was rendering as the literal string "Other" when no mechanism was specified — `_build_context` was treating "Other" as a real value. A filter was added to convert "Other" to "Not specified" before passing to the LLM, and the display logic in therapy.html was updated to treat both "Other" and "Not specified" as falsy so blank/unassessed sections render instead of the literal string.
