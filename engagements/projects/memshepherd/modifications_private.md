# MemShepherd: Private Operational Notes

*Last updated: 2026-06-03*
*Architecture and design decisions: see architecture.md in this directory*

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
- Agent type: letta_v1_agent (no sleep-time companion; primary agent handles memory writes)
- Archive ID: archive-a6c284d0-2d0e-452c-91c0-5d3ac97d672f
- System prompt: Constitution + Amendment, 54208 chars (in sync as of 2026-06-03)

## Block IDs

| Label | Block ID | Limit |
|---|---|---|
| system/persona | block-9e455fad-c9ec-436e-93f3-03223caa9290 | 5000 |
| world/patterns | block-69939755-6d23-41d2-a7bc-c5dd85067011 | default |
| engagements/orientation | block-870d6d9b-bd01-4e8a-a7f8-81dfb030d131 | default |
| engagements/pins | block-7ea0d8f1-026f-4cc5-985b-4c249b8e21d4 | default |
| engagements/intuitions | block-003411bd-2708-4d62-b66e-1f7d099ed7ce | 10000 |

---

## Hook lifecycle (actual, as of 2026-06-03)

| Event | Script | Mode | Purpose |
|---|---|---|---|
| `SessionStart` | `session_start.py` | sync, 60s | Load blocks + Constitution + Amendment into context |
| `SessionStart` | `chunk_archive.py --process-queue` | async, 180s | Process queue → archive + update orientation/world/pins |
| `PostToolUse` | `context_watch.py --verbose` | sync, 45s | Boundary detection; block on score 4; Letta eval on 2–3 |
| `PreCompact` | `chunk_archive.py` | sync, 15s | Queue current chunk (no Letta calls) |
| `SessionEnd` | `chunk_archive.py` | sync, 15s | Queue final chunk (no Letta calls) |
| `SessionEnd` | `session_sync.py` | async, 60s | Export blocks + passages to anamnesis → GitHub |

Note: `session_end.py` exists but is NOT wired into hooks. Its role (sending transcripts to Letta) is handled by chunk_archive.py's worker mode via Letta messages API.

---

## Queue directory

`C:\Users\Amos\.claude\memshepherd\queue\`

File states:
- `.pending.json` — queued, awaiting Letta processing
- `.done.json` — fully processed
- `.abandoned.json` — source JSONL gone (session too old to recover)

---

## Log file

`C:\Users\Amos\.claude\memshepherd\logs\chunk_archive.log`

Key log tokens: INVOKE, QUEUED, WORKER START, WORKER EXIT, WORKER OK, WORKER PARTIAL,
LETTA ERROR, ORIENTATION UPDATED, WORLD UPDATED, WORLD SKIP, PINS APPENDED, OUTPUT
