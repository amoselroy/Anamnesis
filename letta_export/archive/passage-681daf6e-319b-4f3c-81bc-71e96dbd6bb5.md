# WORLD PATTERN 2026-06-06 — SPA re-renders invalidating DOM references during ope

*ID: passage-681daf6e-319b-4f3c-81bc-71e96dbd6bb5*
*Created: 2026-06-06*

---

WORLD PATTERN 2026-06-06 — SPA re-renders invalidating DOM references during operation — 2026-06-06

PRINCIPLE: Single-page applications that re-render on state changes can invalidate DOM element references mid-operation, leaving execCommand and other operations targeting detached nodes.

NARRATIVE: Various attempts to set focus on the Lexical editor included intermediate steps like `el.click()` to set selection state before `execCommand('insertText')`. Each intermediate click triggered React to re-render the composer component, which unmounted the old editor DOM node and created a new one. The reference `el` captured before the click became detached, leaving `execCommand` executing on a node no longer in the live DOM, returning False. The solution was to minimize intermediate mutations: use JS click within the same evaluate() block as the execCommand, or avoid intermediate clicks entirely and let Playwright's built-in mechanisms handle state. This pattern applies broadly to SPAs: intermediate DOM mutations for setup/focus/state can trigger re-renders that orphan carefully captured references; prefer atomic operations over sequential DOM manipulations.
