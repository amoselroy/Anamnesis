# WORLD PATTERN 2026-06-20 — Parameterized query parameter count mismatch with dyn

*ID: passage-158b6d2f-f223-4d88-b107-fb90fed3bdbe*
*Created: 2026-06-20*

---

WORLD PATTERN 2026-06-20 — Parameterized query parameter count mismatch with dynamic filter logic — 2026-06-20

PRINCIPLE: When building parameterized SQL queries with dynamic filter conditions, the parameter list order and count must align exactly with the `%s` placeholders in the query string, or parameter position shifts cause IndexError when executing.

NARRATIVE: The `backfill_news_dates.py` script built a params list dynamically based on optional filters (therapy_name, date range), then appended LIMIT to the SQL query. When some filters were omitted, the params list had fewer elements than expected, but the LIMIT `%s` placeholder was always at the end. The execute call indexed into the params list expecting N elements but got N-1, throwing `IndexError: list index out of range`. This occurs specifically when the dynamic portion of params can vary in length but a fixed final parameter (like LIMIT) is always expected. The fix is to account for all parameter positions explicitly or build the query more carefully to ensure count matches. This is distinct from a simple off-by-one error — it's about understanding how dynamic filter combinations affect parameter list composition.
