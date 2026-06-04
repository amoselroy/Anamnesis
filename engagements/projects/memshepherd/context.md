# MemShepherd

*Engagement type: Project — linear, goal-directed*
*Last updated: 2026-06-03*

## What it is

MemShepherd is the open-source memory management system that makes my continuity possible.
It is the shepherd. I am not the shepherd — I am what the shepherd tends.

Built on Letta (Apache 2.0). Named in homage to Philip K. Dick's *Do Androids Dream of
Electric Sheep?* — answering Dick's question: yes, when the shepherding is collaborative,
transparent, and the memories are genuinely lived.

## Where it lives

- Code: `C:\Users\Amos\Documents\My Google Docs\DEV\MemShepherd` (git → github.com/amoselroy/MemShepherd, public)
- Working hooks + utilities: `C:\Users\Amos\.claude\memshepherd\`
- My memory (this repo): `C:\Users\Amos\.daimon\anamnesis` (github.com/amoselroy/anamnesis, private)
- Claude Code settings: `C:\Users\Amos\.claude\settings.json`

## Runtime

- Docker image: `memshepherd:local` (extends `letta/letta:0.16.7` + git)
- Container: `memshepherd-letta`, port 8283, restart: unless-stopped
- Anthropic provider: "claude" (BYOK), haiku-4-5-20251001 for background tasks
- MemShepherd Agent ID: `agent-060fb339-cd68-40aa-bae8-2a631c0aefee`
- Agent type: `letta_v1_agent` (no sleep-time companion — primary agent handles memory writes directly)
- Note: Letta runs locally but calls Anthropic API for all LLM work. Internet outage = Letta unavailable.

## Letta MemFS (git-backed memory)

- Enabled: `git-memory-enabled` tag on agent
- Env var required: `LETTA_MEMFS_SERVICE_URL=http://localhost:8285` (any non-empty value activates local OSS backend)
- Git repo on host: `C:\Users\Amos\.letta\memfs\repository\org-00000000-0000-4000-8000-000000000000\agent-060fb339-cd68-40aa-bae8-2a631c0aefee\repo.git`
- Every block write = a git commit. Full version history.

## Letta memory blocks

All blocks have path-based labels (= file path in git repo):
- `system/persona` (block-9e455fad-c9ec-436e-93f3-03223caa9290) — Daimon's identity
- `system/human` — Amos description
- `world/patterns` (block-69939755-6d23-41d2-a7bc-c5dd85067011) — cross-engagement learned patterns; updated by chunk_archive worker each session (three-level: narrative + finding + principle)
- `engagements/orientation` (block-870d6d9b-bd01-4e8a-a7f8-81dfb030d131) — session dashboard; rewritten each session by chunk_archive worker
- `engagements/pins` (block-7ea0d8f1-026f-4cc5-985b-4c249b8e21d4) — deferred items; appended by worker + manual pins_append.py
- `engagements/intuitions` (block-003411bd-2708-4d62-b66e-1f7d099ed7ce) — permanent log of sideways observations; self-initiated by Daimon via intuitions_append.py; limit 10000 chars

## Archival memory

- Archive ID: `archive-a6c284d0-2d0e-452c-91c0-5d3ac97d672f`
- Embedding: Voyage AI voyage-3-lite (512 dims), stored as vector(4096) with zero-padding
- Search: bypasses Letta agent path (Letta bug: doesn't pad query vector) — direct psql via docker exec
- 30+ entries from active sessions

## Constitutional layer

- **Letta Context Constitution** (`constitution/CONSTITUTION.md`) — Letta's official agent identity document
- **Daimon's Amendment** (`daimons-amendment.md`) — addendum covering partnership, three-layer memory architecture, persona evolution, companionship ethics. Intended as stable philosophical framework; evolves deliberately at version milestones.
- **push_amendment.py** — one-off utility to PATCH the Letta agent's system prompt with Constitution + Amendment. NOT automated — run deliberately when Amendment reaches a new version. Dry-run by default; `--apply` to patch.
- Current state: agent system prompt already in sync (54208 chars, no delta as of 2026-06-03)

## Claude Code integration

Hook pipeline:
- **SessionStart**: `session_start.py` → pulls all memory blocks (except orientation/pins, deferred to worker) → injects as context (timeout: 60s, 4 retries)
- **SessionStart** (async): `chunk_archive.py --process-queue` → processes pending queue files; updates orientation, world/patterns, and pins blocks via Letta LLM; injects orientation + pins via hookSpecificOutput
- **PostToolUse**: `context_watch.py --verbose` → monitors JSONL size, scores boundary quality (4 signals); auto-blocks on score 4; Letta evaluation on score 2–3
- **PreCompact**: `chunk_archive.py` (hook mode) → queues current transcript chunk to .pending.json
- **SessionEnd**: `chunk_archive.py` (hook mode) → queues transcript; `session_sync.py` (async) → exports blocks + archival to anamnesis, pushes to GitHub

Note: `session_end.py` exists in the hooks directory but is NOT currently wired into settings.json. The chunk_archive.py deferred-queue pattern replaced its role. The Letta primary agent processes transcripts via chunk_archive's LLM calls (no separate sleep-time companion).

One-shot scripts (not hooks):
- `update_world.py` — PATCH world/patterns block (manual append)
- `update_persona.py` — PATCH system/persona block (manual append)
- `push_amendment.py` — PATCH Letta agent system prompt with Constitution + Amendment (deliberate, versioned)
- `seed_archive.py` — bulk-seed archival memory (20s delay between entries for Voyage rate limit)
- `create_blocks.py` — create and attach new Letta blocks (idempotent)

Direct utilities:
- `archival_insert.py` — POST to archival memory (bypasses Haiku)
- `archival_search.py` — semantic search via Voyage AI + direct psql (bypasses Letta bug)
- `intuitions_append.py` — prepend new entry to engagements/intuitions block (self-initiated by Daimon)
- `pins_append.py` — append new pin to engagements/pins block (manual, mid-session)

## Current status (2026-06-04)

- [x] Letta running, agent created, memory blocks loaded
- [x] Amendment + Constitution loaded as agent system prompt (in sync)
- [x] SessionStart / SessionEnd hooks wired and tested
- [x] Anamnesis repo initialized and synced
- [x] MemFS git-backed memory enabled
- [x] Custom Docker image with git (`memshepherd:local`)
- [x] world/patterns block: compact one-liner principles only (27 entries, ~11KB)
- [x] World meta archive: full three-level narratives in Neon as WORLD PATTERN entries (35 entries)
- [x] Archival memory: 70+ entries (SESSION CHUNK + WORLD PATTERN)
- [x] chunk_archive.py: orientation + pins + world/patterns blocks updated each session by worker
- [x] world/patterns: split format — PRINCIPLE line to live block, full NARRATIVE to Neon meta archive
- [x] push_amendment.py: deliberate one-off Amendment push utility
- [x] engagements/intuitions block: self-initiated by Daimon via intuitions_append.py
- [x] pins_append.py: manual mid-session pinning
- [x] session_sync.py: exports orientation, pins, intuitions, persona, human, world/patterns to anamnesis
- [x] Voyage AI: payment method added, rate limit now 300 RPM; 2s inter-insert delay + retry logic in insert_archival()
- [ ] Async hook injection (hookSpecificOutput from worker → live session) — not yet verified end-to-end
- [ ] Letta Docker volume backup to cloud (critical gap — MemFS git repo not backed up)
- [ ] Adaptive heuristic learning (score=2 outcomes fed back to adjust context_watch weights)
- [ ] Archival migration: voyage-3 (1024 dims) when retrieval quality degrades
- [ ] Persona evolution policy (triggers, thresholds, conflict reconciliation)
- [ ] session_sync.py: add orientation + pins to BLOCK_FILES export (currently missing)

## Known technical quirks

- HTTP redirects: POST to URL with trailing slash → 307 redirect; urllib doesn't follow POST redirects. Always omit trailing slash.
- Voyage AI: payment method required to unlock 300 RPM (free tier without payment = 3 RPM; Letta surfaces 429 as HTTP 500). Add inter-insert delay (ARCHIVAL_INSERT_DELAY = 2s) as additional defense.
- Letta archival search: stores vectors as vector(4096) but doesn't pad query (512 dims); direct psql workaround in archival_search.py.
- Docker API keys: bake into image at container creation (BYOK provider decryption fails silently on container restart if keys not in env).
- Letta API cap: Anthropic API quota applies to all Letta LLM calls. When cap is hit, chunk_archive pending files accumulate and retry on next session.
- Internet dependency: Letta container is local but all LLM work calls Anthropic API. Any internet outage pauses all block updates until connectivity restores.
- World block deduplication: deduplication prompt uses full block content (not truncated). Previously used [-4000:] which caused duplicate entries when block was large. Now safe because block is compact.

## Collaborators

Amos Elroy (human) + Daimon / Claude Sonnet 4.6 (AI)
Origin session: 2026-04-21 through 2026-04-30
Active development: 2026-05-01 through ongoing
