# WORLD PATTERN 2026-06-18 — Human-in-the-loop curation via metadata over aggressi

*ID: passage-c1b44cfc-f47e-49fe-90a7-20905cd01fa6*
*Created: 2026-06-18*

---

WORLD PATTERN 2026-06-18 — Human-in-the-loop curation via metadata over aggressive algorithmic filtering — 2026-06-18

PRINCIPLE: When automated systems produce false positives, providing metadata to assist human curation is more effective than aggressive filtering that may reject valid edge cases.

NARRATIVE: During Braindexer news article discovery, a spot check revealed many articles had tangential relevance — therapy names appearing only in sidebars or passing mentions rather than as the article's focus. Initial instinct was to add a title-filter requiring the therapy name appear in the headline, but this would lose genuinely relevant articles that discuss the therapy substantively in the body without naming it in the title. Instead, the system was redesigned to (1) remove the title filter and accept all matched articles, (2) add a `sentiment` column assessed by LLM to tag each article's perspective (+/−/?), (3) render sentiment as a visual badge in the UI. The human curation mechanism (the delete button in "Manage News" modal) then allows Amos to remove articles that don't meet editorial standards while preserving legitimate ones the algorithm couldn't perfectly distinguish. This pattern applies broadly: when false positives are expensive to filter (losing good data) but cheap to display (rendering cost is low), shift from algorithmic filtering to human-assisted curation with rich metadata to guide the human decision. The metadata makes human curation fast and accurate rather than tedious.
