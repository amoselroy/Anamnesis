# SESSION CHUNK 2026-06-19 — LLM-Based Relevance Filtering for News Articles

*ID: passage-edfc76b0-9980-46be-b49d-ba1bb49fa701*
*Created: 2026-06-19*

---

SESSION CHUNK 2026-06-19 — LLM-Based Relevance Filtering for News Articles

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/main.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/static/admin.html, C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/pseudocode.md, C:/Users/Amos/.claude/journal_entry_tmp.md, C:/Users/Amos/.claude/projects/C--Users-Amos/memory/feedback_journal_append_only.md
Errors: Exit code 2
C:\Users\Amos\AppData\Local\Python\pythoncore-3.14-64\python.exe: ca; The user doesn't want to proceed with this tool use. The tool use was rejected (
Tools used: Bash, Read, Edit, Grep, Glob, Write, PowerShell

SUMMARY
With the modal and visibility system operational, Amos observed that many fetched articles were irrelevant — articles about cooking Rosemary, general Alzheimer's news without specific therapy content, or articles mentioning the therapy only incidentally. A second-stage filtering function was added to the `scrape_news_for_therapy()` pipeline: after scraping all candidate articles and applying outlet whitelisting, the full list (titles only) is passed to Haiku with the therapy name, synonyms, and condition name as context. The prompt is deliberately strict: articles are only included if they specifically focus on this therapy as an intervention for this condition; when in doubt, exclude. The filter drops general condition news, unrelated context, and incidental mentions while keeping scientific evidence, research, trials, and clinical use cases. The function fails gracefully: if the LLM call fails, the unfiltered list is returned rather than losing articles. This tightens the quality significantly — existing articles in the database are not retroactively filtered (users can Hide them manually), but new fetches produce much more relevant results.
