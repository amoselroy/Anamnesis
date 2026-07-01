# WORLD PATTERN 2026-06-27 — Regulatory aliases require separate table path from d

*ID: passage-a22520af-c54f-41e6-ae73-e0c61c1ba35c*
*Created: 2026-07-01*

---

WORLD PATTERN 2026-06-27 — Regulatory aliases require separate table path from display aliases — matching-aware alias classification — 2026-06-27

PRINCIPLE: Aliases serving different purposes (regulatory database matching vs. user-facing search) must be architecturally separated or filtered at query time to prevent noise and false positives in matching logic.

NARRATIVE: Amos proposed consolidating all therapy name variations into a single alias table, then recognized the problem: regulatory matching against FDA/EMA/ANVISA databases would have to search through display aliases like "Cu(ATSM)" or "brain copper compound" — names that will never appear in regulatory registries. The insight splits aliases into two categories: INN aliases (salt forms, regulatory codes, international variants) that actually exist in agency databases and must be matched, and display aliases (brand names, common names, descriptive tags) that serve user search and condition detection but would create noise and false positives if fed to regulatory matchers. Solution: either add an `alias_type` column filtering regulatory queries to only INN aliases, or maintain them in separate tables/indices. The pattern generalizes: when aliases serve fundamentally different matching contexts (regulatory lookup vs. full-text search vs. semantic discovery), conflating them in a single structure creates systematic matching failure. The matching logic itself determines what aliases are actually useful, so alias architecture should reflect the matcher's requirements, not just maintain a consolidated namespace.
