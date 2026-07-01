# WORLD PATTERN 2026-06-10 — Prompt structure as enforcer of data categorization —

*ID: passage-e0a35fa9-7c5d-45ea-8c9f-348924cbe999*
*Created: 2026-06-10*

---

WORLD PATTERN 2026-06-10 — Prompt structure as enforcer of data categorization — 2026-06-10

PRINCIPLE: Using prompt structure to return categorized JSON (e.g., `{"neurological": [...], "general": [...]}`) enforces data type and category assignment at generation time, reducing downstream parsing and validation complexity.

NARRATIVE: When building the condition detection system, the challenge was distinguishing between neurological/psychiatric conditions (appropriate for condition-specific therapy pages) and general medical conditions (informational only via popup). Rather than returning a flat array and implementing categorization logic post-generation, the prompt was structured to return a JSON object with two arrays. This enforced the categorization at the LLM output level: the model had to decide during generation whether each condition was neurological or general, rather than the application having to infer category after the fact. The benefit is that the prompt's reasoning path includes the categorization decision, making errors visible in the raw prompt output and easier to debug. More broadly, when a system needs categorized or structured output, encoding that structure into the prompt architecture (rather than post-processing unstructured output) creates a tighter feedback loop and reduces the likelihood of miscategorized data flowing into the database.
