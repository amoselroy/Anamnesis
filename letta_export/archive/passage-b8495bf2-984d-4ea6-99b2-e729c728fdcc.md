# SESSION CHUNK 2026-06-18 — Overall Assessment Score Formula Correction and Rever

*ID: passage-b8495bf2-984d-4ea6-99b2-e729c728fdcc*
*Created: 2026-06-18*

---

SESSION CHUNK 2026-06-18 — Overall Assessment Score Formula Correction and Reverse Proportion Handling

STRUCTURED
Files: C:/Users/Amos/projects/braindexer/services/scraper.py, C:/Users/Amos/projects/braindexer/routers/therapies.py, C:/Users/Amos/projects/braindexer/main.py, C:/Users/Amos/projects/braindexer/setup_db.py, C:/Users/Amos/projects/braindexer/static/admin.html, C:/Users/Amos/projects/braindexer/static/therapy.html, C:/Users/Amos/projects/braindexer/models.py
Errors: <tool_use_error>File has not been read yet. Read it first before writing to it.<
Tools used: Grep, Read, Edit, Bash

SUMMARY
Amos identified that the Overall Assessment (OA) score calculation was incorrect because it failed to account for the directional reversal of the side_effects_score: effectiveness increases with higher values (1=none, 5=strong), safety increases with higher values (1=risk, 5=excellent), but side_effects_severity increases with higher values meaning worse effects (1=minimal, 5=severe). The correct formula is `OA = (effectiveness + safety − side_effect_severity) / 3`, but this produces a range mismatch. The code was using the algebraically equivalent but practically clearer form: `OA = (effectiveness + safety + (6 − severity)) / 3`, clamped to [1,5]. Amos initially proposed his formula, which is mathematically correct but shifts the scale; the code already implements the same logic. The root issue was that the LLM was also computing overall_score itself (adding another layer of unreliability), when it should have only been generating the three component inputs. This led to refactoring to remove LLM computation of overall_score entirely, having it return only the three 1–5 component dimensions which Python then combines deterministically using the formula. The implementation was corrected, and existing stored scores flagged as stale until therapies were re-researched.
