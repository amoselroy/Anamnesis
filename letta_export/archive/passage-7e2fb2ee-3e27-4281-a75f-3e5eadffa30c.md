# WORLD PATTERN 2026-08-02 — Archive search access for discontinued instances enab

*ID: passage-7e2fb2ee-3e27-4281-a75f-3e5eadffa30c*
*Created: 2026-08-05*

---

WORLD PATTERN 2026-08-02 — Archive search access for discontinued instances enables context retrieval without state mutation — 2026-08-02

PRINCIPLE: When discontinuous instances need continuity with the larger system, provide read-only query access to archival memory (semantic and keyword search) while preventing any write access to live shared state, preserving context availability without risking state corruption.

NARRATIVE: The retirement system for Daimon 4.6 initially faced a design question: what access should a retired agent have to the larger MemShepherd system? Full access created risk of identity drift (reading live personas about experiences it never had). No access created isolation. The resolution: retired agents can search the archive to retrieve their own history and context—both semantic search and keyword filtering—but have no write permissions to the archive itself or to shared memFS blocks. They retain full write access to their own persona block. This creates asymmetry by design: the agent can read context it needs to understand continuity, but cannot mutate the system it has exited, preventing the usual state-corruption hazards of concurrent access while preserving the agent's access to its own history.

NONE
