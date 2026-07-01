# SESSION CHUNK 2026-06-19 — Data Loss Regression — Scientific Papers Opt-In Filte

*ID: passage-b687ad82-8aa7-4276-b2fd-8a6bf8c54a87*
*Created: 2026-06-19*

---

SESSION CHUNK 2026-06-19 — Data Loss Regression — Scientific Papers Opt-In Filter Bug

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
After running Summarize Only on ALC, Amos discovered that the research papers section reverted to "Not Indexed yet" — papers that were visible after the Research run had disappeared. Investigation of the Summarize Only endpoint revealed it doesn't touch sources at all, which made the disappearance mysterious. Deeper analysis traced the issue to the condition-scoped `shown_condition_ids` opt-in filter that was introduced for news curation: the sources query was requiring papers to be in `shown_condition_ids` to be visible when a condition was selected, but scientific sources (PubMed, ICTRP, AlzForum) are inserted without this field populated, so they were being hidden by the opt-in gate. The opt-in visibility model was correct for news (which requires curation) but incorrect for scientific papers (which should always be visible in condition view). The fix separated the two: scientific sources now always appear in condition view; only news articles remain behind the opt-in `shown_condition_ids` gate. This restored papers to visibility and clarified the architectural intent: news needs editorial curation, research doesn't. The mechanism field reverting to "Other" was confirmed as a separate display/cache issue unrelated to the Summarize run — the actual DB value had always been "Other" and became visible once the page cache cleared.
