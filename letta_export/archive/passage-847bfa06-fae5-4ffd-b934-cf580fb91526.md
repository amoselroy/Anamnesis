# WORLD PATTERN 2026-06-04 — Playwright/Facebook automation — selector and debuggi

*ID: passage-847bfa06-fae5-4ffd-b934-cf580fb91526*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Playwright/Facebook automation — selector and debugging lessons — 2026-05-29

Learned from brokerage_sharer debugging across several sessions: (1) DOM and visual layout are different things — elements visually inside a component are not necessarily inside it in the DOM; Facebook renders the post action bar outside div[role='article'] even though it appears below each post. (2) Proximity is a valid selector — when DOM scoping fails, selecting the element with the smallest screen-distance to a reference element is legitimate and sometimes necessary. (3) False positives are more dangerous than failures — a script that confidently reports success while doing nothing costs far more debugging time than one that fails loudly; instrument the actual outcome, not just the button click. (4) Adversarial systems require empirical tools, not theories — when the system actively fights automation (stripped aria-labels, moved roles, hidden elements), instrument first and dump what's in the DOM at runtime, then theorize; the solution only revealed itself through a diagnostic dump showing the real aria-label. (5) Persistence has diminishing returns in a session — breakthroughs came after rest and a fresh angle, not during exhausted late-night iteration; know when to stop. (6) The obvious thing to try is often last — keyboard navigation, JS injection, coordinate clicks, and accessibility trees were all tried before simply inspecting the element's actual aria-label directly; when stuck, go back to first principles.
