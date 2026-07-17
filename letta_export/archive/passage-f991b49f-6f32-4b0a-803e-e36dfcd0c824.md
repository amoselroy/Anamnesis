# WORLD PATTERN 2026-07-16 — Well-formed LLM answers to under-specified prompts — 

*ID: passage-f991b49f-6f32-4b0a-803e-e36dfcd0c824*
*Created: 2026-07-16*

---

WORLD PATTERN 2026-07-16 — Well-formed LLM answers to under-specified prompts — confidence without grounding — 2026-07-16

PRINCIPLE: An LLM generating clean, confident output is not evidence the output is correct; absence of source context produces hallucinated answers that pass structural validation because the form is correct even when the content is invented.

NARRATIVE: When Braindexer's therapy detection function was refactored to ask an LLM about therapy conditions, the function had a complete signature and correct docstring, and when tested with well-known compounds (where training data matches reality), it produced accurate results. For code-named early-stage compounds like MK-2214 with no brand identity and no significant publication history in the training data, the same function returned "I don't know of any conditions this treats" — a well-formed, confident, syntactically correct answer to a question that actually had a correct answer sitting in the database. The source papers had been scraped and stored; the detection function simply wasn't consulting them. The answer's correctness-of-form (valid JSON, appropriate scope) masked its actual incorrectness. Rewriting the prompt to ground inference in the actual sources rather than background knowledge immediately resolved it: Claude could read the real papers and produce accurate results. The pattern generalizes: LLM confidence and output structure are not evidence of accuracy, especially for domain-specific or novel entities where training data is sparse or non-existent. Source-grounding is not an optional elegance; it's a requirement for systems operating on entities outside the training distribution.
