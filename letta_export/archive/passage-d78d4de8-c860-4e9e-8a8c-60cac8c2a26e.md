# WORLD PATTERN 2026-06-04 — Stateless compute with stateful cloud database — 2026

*ID: passage-d78d4de8-c860-4e9e-8a8c-60cac8c2a26e*
*Created: 2026-06-04*

---

WORLD PATTERN 2026-06-04 — Stateless compute with stateful cloud database — 2026-06-03

When designing containerized systems that need to survive container restarts without data loss, moving the database to a cloud service (Neon PostgreSQL) rather than storing it in a container volume separates stateful data from stateless compute. The concrete benefit: the container becomes disposable — it can be deleted, rebuilt, upgraded (new base image tag), or restarted without any database migration, backup, or recovery process. The upgrade path simplifies to: change base image tag, restart container, the stateless layer picks up seamlessly from the cloud database. This pattern emerged during MemShepherd deployment after initial attempts to manage local PostgreSQL data volumes created complexity around upgrades and backups. The principle generalizes: when statefulness and compute need different lifecycle timelines, externalize the state layer to something managed separately (cloud DB, object storage, filesystem service). This enables the compute layer to be treated as truly ephemeral infrastructure.
