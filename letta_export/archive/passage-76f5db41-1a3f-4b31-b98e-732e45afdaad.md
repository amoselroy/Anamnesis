# WORLD PATTERN 2026-06-25 — Temporary bypass as feature rather than band-aid when

*ID: passage-76f5db41-1a3f-4b31-b98e-732e45afdaad*
*Created: 2026-07-01*

---

WORLD PATTERN 2026-06-25 — Temporary bypass as feature rather than band-aid when automation becomes unreliable — 2026-06-25

PRINCIPLE: When background automation becomes unreliable on infrastructure with limited resources, building explicit curator UI to bypass the automation transforms the failure into a feature rather than a hidden failure mode.

NARRATIVE: The agency monitor's CSV download from FDA/EMA/ANVISA/ClinicalTrials succeeded at returning `{"status": "started"}` but the background thread stalled mid-download on Render's free tier, leaving `agency_import` empty and all downstream syncs with null results. Rather than investigating the root cause (which would take time on a constrained deadline) or waiting for the download to complete (it had already stalled twice), the solution was building a manual "Agency Status" button in the admin panel allowing curators to directly set FDA/EMA/ANVISA approval data without the monitor. This wasn't framed as a temporary workaround but as a permanent feature: curator knowledge is sometimes more reliable than automated downloads. The button appears in the Therapies tab, values are entered directly, and the result is immediately visible. The key difference from a traditional band-aid: the bypass is *visible* and *intentional*, not hidden. A curator using it knows they're entering data directly rather than thinking it came from automation. This has a cascading effect: it signals to users (like Dr. Sano during the Monday demo) that the system can be updated through human action when automated paths stall. The principle generalizes: when periodic automation serving limited resources becomes unreliable, building visible curator bypasses is superior to either waiting for the automation to fix itself or hiding failures behind silent retries. The bypass preserves agency and transparency.
