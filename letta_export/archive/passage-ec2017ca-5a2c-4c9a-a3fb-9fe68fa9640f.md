# WORLD PATTERN 2026-06-22 — WHO International Nonproprietary Names enable multili

*ID: passage-ec2017ca-5a2c-4c9a-a3fb-9fe68fa9640f*
*Created: 2026-06-22*

---

WORLD PATTERN 2026-06-22 — WHO International Nonproprietary Names enable multilingual data matching without translation — 2026-06-22

PRINCIPLE: Active ingredient names follow international standards across all languages, eliminating the need for full translation support when matching drugs across language-specific regulatory databases.

NARRATIVE: During the regulatory agency audit, concern arose about monitoring Chinese (NMPA) and Portuguese (ANVISA) sources without language support. However, the WHO International Nonproprietary Name (INN) system means drugs are identified by the same Latin-script compound names across all databases and languages — "lecanemab" appears as "lecanemab" in Japanese, Chinese, and Brazilian pharmaceutical records. Status values differ (`批准` vs. `批准` vs. `REGISTRADO`), but these are small lookup tables per agency, not full translation layers. The insight generalizes: when integrating external data sources in multiple languages, check whether the core identifying fields use universal standards before assuming translation support is necessary. International standards often eliminate that requirement entirely.
