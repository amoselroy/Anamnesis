# WORLD PATTERN 2026-06-20 — LLM classification subtypes must be exhaustively enum

*ID: passage-41aba707-1252-4ca5-8eef-ea3381ab633f*
*Created: 2026-06-20*

---

WORLD PATTERN 2026-06-20 — LLM classification subtypes must be exhaustively enumerated in prompts — 2026-06-20

PRINCIPLE: LLM classification prompts that list valid categories (e.g., "systematic review") will treat unlisted subtypes (e.g., "narrative review") as not matching any category, defaulting them to a lower or baseline classification.

NARRATIVE: The tier 1 relevance definition prompt said "clinical trial, efficacy/safety study, or systematic review" but did not mention "narrative review." When Haiku encountered papers explicitly described as "narrative reviews" evaluating heat therapy for Alzheimer's disease, it classified them as tier 3 (tangential) because "narrative review" didn't match the enumerated categories. After updating the prompt to "systematic review, narrative review, or any literature review evaluating {therapy}", the same papers correctly scored as tier 1 (Direct). The phenomenon is reliable: if a category isn't named in the enumeration, the LLM doesn't confidently place items in that category even if they would logically fit. The fix is exhaustive enumeration (or phrasing as "any study or review that evaluates...") rather than assuming the LLM will infer subtypes from examples.
