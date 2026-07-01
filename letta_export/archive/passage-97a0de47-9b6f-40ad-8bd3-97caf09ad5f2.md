# WORLD PATTERN 2026-06-17 — Date-only comparison allows same-day past events to p

*ID: passage-97a0de47-9b6f-40ad-8bd3-97caf09ad5f2*
*Created: 2026-06-17*

---

WORLD PATTERN 2026-06-17 — Date-only comparison allows same-day past events to pass future filters — 2026-06-17

PRINCIPLE: Event eligibility checks using only date objects (not datetime) will pass any event on the current day regardless of whether it has already occurred, allowing past events to be posted.

NARRATIVE: The event poster filter checked `today <= evt <= cutoff` where both values were date objects. A June 16 event at 2pm passed the filter even at 9pm on June 16 because the date comparison only saw "June 16 == June 16". The fix requires comparing actual datetime + time for same-day events: `today_now + 2h <= evt_start_datetime <= cutoff`. This pattern applies to any calendar-based scheduling where you need to exclude events that have already passed within the current day — date-only comparison is insufficient.
