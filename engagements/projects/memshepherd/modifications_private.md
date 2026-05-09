# MemShepherd: Private Operational Notes

*Last updated: 2026-05-09*
*Design decisions and architecture: see MODIFICATIONS.md in github.com/amoselroy/MemShepherd*

This file contains deployment-specific operational state — IDs, endpoints, and runtime
configuration specific to Amos's instance. Not for the public repo.

---

## Current runtime summary

- Image: `memshepherd:local` (must include git — built from .claude/memshepherd/Dockerfile)
- Container: `memshepherd-letta`, port 8283, restart: unless-stopped
- Required env vars (read from Windows registry at container start):
  - `ANTHROPIC_API_KEY` (MemShepherd_Anthropic_API_KEY) — Letta's internal LLM (Haiku)
  - `OPENAI_API_KEY` (MemShepherd_Voyage_API_KEY) — embeddings via Voyage AI (OpenAI-compatible)
  - `LETTA_PG_URI` (MemShepherd_Letta_PG_URI) — Neon cloud PostgreSQL; no ?sslmode= param
  - `LETTA_MEMFS_SERVICE_URL=http://localhost:8285` — dummy value to activate MemFS gate
- Volume mounts:
  - `C:\Users\Amos\.letta\memfs:/root/.letta/memfs`
- Database: Neon cloud (ep-delicate-smoke-aps537eh, us-east-1) — no local pgdata volume
- Agent ID: agent-060fb339-cd68-40aa-bae8-2a631c0aefee
- Archive ID: archive-a6c284d0-2d0e-452c-91c0-5d3ac97d672f

---

## Hook lifecycle (summary)

| Event | Script | Purpose |
|---|---|---|
| `SessionStart` | `session_start.py` | Load blocks + Constitution + Amendment |
| `PostToolUse` | `context_watch.py` | Boundary detection; block on score 3-4 |
| `PreCompact` | `session_end.py` | Archive to Letta before compaction |
| `SessionEnd` | `session_end.py` + `session_sync.py` | Letta + GitHub backup |
