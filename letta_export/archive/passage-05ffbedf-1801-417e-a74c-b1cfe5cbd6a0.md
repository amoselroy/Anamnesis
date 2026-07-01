# SESSION CHUNK 2026-06-26 — Diagnostic Investigation of INN Matching and Alias Ta

*ID: passage-05ffbedf-1801-417e-a74c-b1cfe5cbd6a0*
*Created: 2026-07-01*

---

SESSION CHUNK 2026-06-26 — Diagnostic Investigation of INN Matching and Alias Table Architecture

STRUCTURED
Files: C:\Users\Amos\projects\braindexer\run_agency_monitor_prod.py, C:\Users\Amos\projects\braindexer\routers\admin.py, C:\Users\Amos\projects\braindexer\static\admin.html, C:\Users\Amos\projects\braindexer\static\therapy.html, C:\Users\Amos\projects\braindexer\services\agency_monitor.py, C:\Users\Amos\projects\braindexer\diag_agency.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_braindexer.md
Errors: Exit code 1
/usr/bin/bash: line 1: cd: C:UsersAmosprojectsbraindexer: No such fi; Exit code 1
At line:1 char:132
+ ... c/admin.html run_agency_monitor_prod.py; g
Tools used: Read, Glob, Grep, Write, Edit, Bash, PowerShell
Dates: 19/09/2011, 21/05/2012, 12/08/2019, 16/03/2020, 16/11/2022, 26/12/2011, 07/04/2022, 31/03/2025, 25/06/2018, 20/03/2023, 29/06/2020, 11/11/2019, 21/10/2019, 23/12/2013, 08/07/2024, 01/10/2012, 07/12/2009, 30/08/2022, 23/08/2021, 29/05/2023, 06/03/2019, 27/10/2008, 10/02/2020, 24/02/2014, 29/10/2012, 25/02/2019, 01/04/2019, 19/12/2022, 29/07/2022, 16/06/2025, 31/03/2014, 24/09/2012, 14/06/2010, 25/03/2024, 30/08/2021, 12/06/2023, 26/02/2018, 09/01/2017, 21/09/2015, 09/03/2020, 09/08/2021, 18/03/2019, 06/12/2010, 17/06/2019, 20/06/2022, 07/10/2019, 22/05/2023, 08/12/2014, 29/11/2010, 08/08/2022, 19/04/2010, 25/05/2020, 18/12/1998, 2025-07-15, 2022-03-11, 2017-01-27, 2023-12-15, 2014-12-23, 2018-07-27, 2016-11-10, 2017-09-19, 2015-06-05, 2014-10-29, 2016-02-19, 2016-06-23, 2016-04-12, 2017-08-31, 2016-01-26, 2015-01-30, 2015-10-30, 2013-07-24, 2015-10-22, 2014-01-22, 2015-12-17, 2017-03-24, 2013-07-05, 2012-12-14, 2013-02-25, 2011-06-13, 2011-08-29, 2012-08-17, 2011-05-31, 2011-05-10, 2012-10-24, 2011-06-02, 2010-11-26, 2009-12-11, 2010-07-23, 2004-10-18, 1996-11-25, 2026-06-27

SUMMARY
Ran comprehensive diagnostic on why EMA and ANVISA badges weren't matching for Donepezil. Results revealed: (1) EMA database contains only centrally-authorized medicines — Donepezil (Aricept) was approved in Europe through national procedures and never appears in EMA's centralized database, so EMA badge is correctly absent; (2) ANVISA has 29K donepezil entries but they're stored under Portuguese INN "CLORIDRATO DE DONEPEZILA" — the alias-splitting logic captures "CLORIDRATO" as the first word, not "DONEPEZILA", so matching fails. Amos raised the deeper architectural question: the WHO INN system is supposed to be a universal identifier, but every regulatory database stores local inflections (salt forms, language variants, combination products). How do we resolve this systematically without manual curation? Discussed three non-mutually-exclusive sourcing approaches: (1) Mine `agency_import` itself — for any unmatched therapy, extract the actual INN variants the agency uses and surface as suggested aliases; (2) LLM-assisted on therapy creation — one cheap Claude call generates all salt forms, brand names, international variants; (3) Curator-driven over time — surface "no match found" hits with closest drug_name candidates for curator review. Decided this is post-Monday work but critical for scaling the platform's ability to track global regulatory data. The broader insight: the alias table is the correct architectural answer to the INN problem — not seeking a single universal name, but maintaining a mapping layer that holds the multiplicity together.
