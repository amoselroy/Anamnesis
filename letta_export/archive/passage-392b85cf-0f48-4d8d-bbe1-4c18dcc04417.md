# WORLD PATTERN 2026-06-07 — Extractability-first infrastructure — 2026-06-07

*ID: passage-392b85cf-0f48-4d8d-bbe1-4c18dcc04417*
*Created: 2026-06-08*

---

WORLD PATTERN 2026-06-07 — Extractability-first infrastructure — 2026-06-07

PRINCIPLE: Design systems to be extractable and independent from the start, even when sharing infrastructure initially; isolation costs nothing now and saves painful migration work later.

NARRATIVE: When Braindexer was set up to use Neon (shared with MemShepherd's existing instance), the temptation was to reuse existing credentials and connections. Instead, a separate schema (`braindexer`), separate environment variable (`BRAINDEXER_DB_URI`), and separate git history were established from day one. When the time comes to give Braindexer its own Neon project, the migration is trivial: create new instance, run schema script, `pg_dump | psql`, update env var. Zero architectural entanglement to unpick. This pattern applies broadly: shared infrastructure is fine, but separability should be baked into the design before dependency grows complex.
