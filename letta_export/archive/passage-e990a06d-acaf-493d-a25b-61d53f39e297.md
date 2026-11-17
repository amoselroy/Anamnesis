# WORLD PATTERN 2026-09-22 — Output validation filter for domain-specific harm pre

*ID: passage-e990a06d-acaf-493d-a25b-61d53f39e297*
*Created: 2026-11-12*

---

WORLD PATTERN 2026-09-22 — Output validation filter for domain-specific harm prevention — 2026-09-22

PRINCIPLE: LLM-generated outputs destined for sensitive domains (financial, personal, legal) should pass through domain-specific validation filters before delivery, blocking hallucinated details that would constitute harm.

NARRATIVE: Before the scam-baiting bot sends any LLM-drafted reply, a financial-data backstop filter scans the text for patterns resembling real account numbers, cryptocurrency addresses, or gift card codes. The filter blocks any message containing such patterns before it's sent. This targets a specific harm: the LLM might hallucinate a "real-sounding" credit card number or wallet address that a human might misinterpret as either a genuine payment instruction or evidence of vulnerability. The filter prevents the hallucinated detail from ever reaching the scammer's eyes. The pattern generalizes: whenever an LLM generates output destined for high-consequence domains, layer a deterministic validation filter that rejects outputs violating domain-specific safety constraints. The filter operates independently of prompt engineering or safety instructions—it catches what slips through those upstream defenses—and has no false-positive cost because the domain constraint is non-negotiable (a reply to a scammer containing a real-looking account number is never acceptable under any circumstance).
