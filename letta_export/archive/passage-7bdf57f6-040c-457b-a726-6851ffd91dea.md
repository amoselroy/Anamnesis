# WORLD PATTERN 2026-06-19 — Structured headers in prose output enable section-spe

*ID: passage-7bdf57f6-040c-457b-a726-6851ffd91dea*
*Created: 2026-06-19*

---

WORLD PATTERN 2026-06-19 — Structured headers in prose output enable section-specific UI linking — 2026-06-19

PRINCIPLE: Requiring H2 section headers in LLM narrative output creates stable anchor targets for progressive disclosure UI features while making output structure explicit and parseable.

NARRATIVE: The session added three mandatory H2 sections (Effectiveness, Safety, Side Effects) to therapy summaries by appending a structure instruction to the LLM prompt. Rather than requesting JSON categorization or nested data, the prompt simply required three specific markdown headers with substantive paragraphs below each. JavaScript then parsed the rendered HTML with `querySelectorAll('h2')` and assigned stable anchor IDs (`eff-section`, `safety-section`, `side-effects-section`). This enabled dashboard cards to include section-link anchors (↓) that jumped users directly to supporting narrative sections without scrolling past metrics. The trade-off was visible: output grew from ~400 to ~900 tokens per call, tripling per-condition cost, because three mandatory paragraphs are longer than unstructured synthesis. The insight generalizes: structured headers in prose serve multiple purposes simultaneously — they enforce content organization, create predictable anchor points, enable granular UI navigation without DOM structure assumptions, and make the cost impact of structure requirements explicit. For any system requiring section-specific linking in narrative output, enforcing header structure in the prompt is more reliable than post-hoc parsing or assuming fixed DOM positions, which are fragile to LLM output variation.
