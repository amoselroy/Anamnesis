# WORLD PATTERN 2026-06-27 — Indication-specific entities cannot be collapsed to t

*ID: passage-71040dcc-eeba-4b14-83a1-d9bb4ed0b1ce*
*Created: 2026-07-01*

---

WORLD PATTERN 2026-06-27 — Indication-specific entities cannot be collapsed to therapy level — approvals and trials belong at therapy-condition junction — 2026-06-27

PRINCIPLE: When an entity (approval record, trial) has semantically distinct variations at the therapy-condition junction level, attempting to represent it at the therapy level alone produces data loss and architectural brittleness.

NARRATIVE: Amos's proposed consolidated agency table — one row per therapy with columns for FDA approval, EMA approval, trial phase — would have failed on real data. Three problems surfaced: combination drugs like Namzaric (donepezil + memantine) have multiple INNs and cannot fit in a single-INN schema; FDA approves the same INN multiple times for different formulations and indications, requiring separate records; trial phase is indication-specific (Phase III for Alzheimer's, Phase II for Parkinson's simultaneously). This revealed a fundamental architectural truth: approval records and trial records are not therapy-level metadata; they are indication-specific facts that belong at the therapy-condition junction. The correct model separates agency_approvals (one per regulatory approval event, keyed by INN/agency/indication) and trial_records (one per NCT + condition), with join tables (therapy_approvals, therapy_trials) resolving the matches back to specific therapies and conditions. The pattern generalizes: when a medical/regulatory entity has legitimate variation at a relationship level (therapy-condition, therapy-diagnosis, patient-treatment), representing it as a single flat field per parent entity creates silent data loss and makes the system unmappable to real scenarios. The relationship itself becomes a first-class data-bearing unit.
