# WORLD PATTERN 2026-06-06 — Directed graph with typed edges for semantic relation

*ID: passage-1ff6e922-ae6f-404c-91cc-8eebe2d084d6*
*Created: 2026-06-07*

---

WORLD PATTERN 2026-06-06 — Directed graph with typed edges for semantic relationship mapping — 2026-06-07

PRINCIPLE: Represent relationships between entities using a directed graph with semantically typed edges rather than pairwise connections, enabling future visualization and semantic querying.

NARRATIVE: Braindexer's `therapy_relationships` table uses a directed graph structure where any therapy connects to any number of others, each edge typed with relationship kind (shares_mechanism, synergistic, complementary, competing, variant_of, prerequisite). This departs from simpler two-slot approaches that model limited connection patterns. The typed edges enable future semantic map visualization where different edge types render differently, support Cypher-like queries ("find all therapies synergistic with senolytic compounds"), and represent genuine domain knowledge about how treatments relate. The pattern generalizes: whenever you have interconnected entities where the *kind* of connection matters, a typed-edge graph structure is more powerful than alternatives and costs little more to implement at inception.
