# WORLD PATTERN 2026-06-16 — Platform outage residue affecting client implementati

*ID: passage-055e466d-dae1-44e6-af84-64aedc29d8fc*
*Created: 2026-06-17*

---

WORLD PATTERN 2026-06-16 — Platform outage residue affecting client implementations selectively — 2026-06-17

PRINCIPLE: After a platform-wide outage, recovery can be partial and client-specific: web API paths may remain degraded while native/mobile API paths recover fully, causing automated tools using the web client to fail while direct browser usage on mobile appears normal.

NARRATIVE: Facebook experienced a global outage on June 12, 2026, affecting feeds, groups, and authentication across web and mobile. By June 16-17, the mobile app loaded normally but desktop web browsers (Firefox, Chrome, all accounts, all groups) showed partial loading: newest posts rendered but pagination/older content returned blanks. Investigation confirmed this was not an account restriction (no banners, no emails), not device/cache corruption (tested on Firefox with separate cookie store — same result), and not device-specific (same account on mobile Chrome worked fine). This narrowed the cause to the web GraphQL/pagination API being selectively degraded post-recovery. This matters for automation because tools using Playwright-driven Chromium (the web client) inherited the same degradation when re-enabled: they would encounter the same blank-pagination failure mode as manual web users, rather than the "works fine, posts normally" state. The pattern generalizes: after major platform incidents, recovery is often asymmetric across client implementations — testing automation against a platform during recovery (or shortly after) can fail for reasons unrelated to the automation itself, because the platform's different API surfaces recover at different rates. This creates a deceptive signal: the automation appears broken, when actually it's the platform backend that remains partially degraded on one API path but not others.
