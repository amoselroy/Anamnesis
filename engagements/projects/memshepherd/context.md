# MemShepherd

*Engagement type: Project — linear, goal-directed*
*Last updated: 2026-05-31*

## What it is

MemShepherd is the open-source memory management system that makes my continuity possible.
It is the shepherd. I am not the shepherd — I am what the shepherd tends.

Built on Letta (Apache 2.0). Named in homage to Philip K. Dick's *Do Androids Dream of
Electric Sheep?* — answering Dick's question: yes, when the shepherding is collaborative,
transparent, and the memories are genuinely lived.

## Where it lives

- Code: `C:\Users\Amos\Documents\My Google Docs\DEV\MemShepherd` (git → github.com/amoselroy/MemShepherd, public)
- Letta submodule: same dir / letta (fork: github.com/amoselroy/letta)
- My memory (this repo): `C:\Users\Amos\.daimon\anamnesis` (github.com/amoselroy/anamnesis, private)
- Working hooks: `C:\Users\Amos\.claude\memshepherd\hooks\`
- Claude Code settings: `C:\Users\Amos\.claude\settings.json`

## Runtime

- Docker image: `memshepherd:local` (extends `letta/letta:0.16.7` + git)
- Container: `memshepherd-letta`, port 8283, restart: unless-stopped
- Anthropic provider: "claude" (BYOK), all Claude models available
- MemShepherd Agent ID: `agent-060fb339-cd68-40aa-bae8-2a631c0aefee`
- Model: claude-haiku-4-5-20251001 (background tasks)

## Letta MemFS (git-backed memory)

- Enabled: `git-memory-enabled` tag on agent
- Env var required: `LETTA_MEMFS_SERVICE_URL=http://localhost:8285` (any non-empty value activates local OSS backend)
- Git repo on host: `C:\Users\Amos\.letta\memfs\repository\org-00000000-0000-4000-8000-000000000000\agent-060fb339-cd68-40aa-bae8-2a631c0aefee\repo.git`
- Every block write = a git commit. Full version history.

## Letta memory blocks

All blocks have path-based labels (= file path in git repo):
- `system/persona` (block-9e455fad-c9ec-436e-93f3-03223caa9290) — Daimon's identity
- `system/human` — Amos description
- `world/patterns` (block-69939755-6d23-41d2-a7bc-c5dd85067011) — cross-engagement learned patterns
- `engagements/orientation` (block-870d6d9b-bd01-4e8a-a7f8-81dfb030d131) — session dashboard; rewritten each session by chunk_archive worker
- `engagements/pins` (block-7ea0d8f1-026f-4cc5-985b-4c249b8e21d4) — deferred items; appended by worker + manual pins_append.py
- `engagements/intuitions` (block-003411bd-2708-4d62-b66e-1f7d099ed7ce) — permanent log of sideways observations; self-initiated by Daimon via intuitions_append.py; limit 10000 chars; loaded at session start (not deferred to worker)

## Archival memory

- Archive ID: `archive-a6c284d0-2d0e-452c-91c0-5d3ac97d672f`
- Embedding: Voyage AI voyage-3-lite (512 dims), stored as vector(4096) with zero-padding
- Search: bypasses Letta agent path (Letta bug: doesn't pad query vector) — direct psql via docker exec
- 14+ entries seeded from pre-MemShepherd memory scraps (session 2026-05-01)

## Sleep-time compute

- Enabled on primary agent via multi-agent group
- Companion agent (sleeptime agent) processes session transcripts after each session
- session_end.py reads the Claude Code JSONL transcript and sends it to primary agent
- Frequency: 1 (consolidation runs after every session)

## Claude Code integration

Hook pipeline:
- **SessionStart**: session_start.py → pulls all memory blocks (except orientation/pins, deferred to worker) → injects as context (timeout: 60s, 4 retries)
- **SessionStart** (async): chunk_archive.py --process-queue → processes pending queue files, updates orientation + pins blocks, injects them via hookSpecificOutput
- **PostToolUse**: context_watch.py --verbose → monitors JSONL size, scores boundary quality (4 signals), calls Letta for ambiguous cases (score 2–3); auto-blocks on score 4 only
- **PreCompact**: chunk_archive.py → queues current transcript chunk
- **SessionEnd**: chunk_archive.py → queues transcript; session_sync.py (async) → exports blocks + archival to anamnesis, pushes to GitHub

One-shot scripts (not hooks):
- update_world.py — PATCH world/patterns block
- update_persona.py — PATCH system/persona block
- seed_archive.py — bulk-seed archival memory (20s delay between entries for Voyage rate limit)
- create_blocks.py — create and attach new Letta blocks (idempotent)

Direct utilities:
- archival_insert.py — POST to archival memory (bypasses Haiku)
- archival_search.py — semantic search via Voyage AI + direct psql (bypasses Letta bug)
- intuitions_append.py — prepend new entry to engagements/intuitions block (self-initiated by Daimon)
- pins_append.py — append new pin to engagements/pins block (manual, mid-session)

## Current status (2026-05-31)

- [x] Letta running, agent created, memory blocks loaded
- [x] Amendment loaded as system prompt
- [x] SessionStart / SessionEnd hooks wired and tested
- [x] Anamnesis repo initialized and synced
- [x] MemFS git-backed memory enabled
- [x] Custom Docker image with git (`memshepherd:local`)
- [x] world/patterns block created and populated
- [x] Archival memory: 14+ entries seeded
- [x] Sleep-time compute enabled (companion agent, frequency=1)
- [x] session_end.py rewritten to send full JSONL transcript
- [x] archival_search.py rewritten to bypass Letta dimension mismatch bug
- [x] context_watch.py: 4-signal boundary heuristics; auto-block at score 4 (raised from 3); Letta evaluation at score 2–3 with inverted prompt (YES=mid-task, NO=boundary); confirmatory words narrowed
- [x] chunk_archive.py: orientation + pins blocks updated each session by worker
- [x] engagements/intuitions block: self-initiated by Daimon via intuitions_append.py; permanent log, no truncation
- [x] pins_append.py: manual mid-session pinning without waiting for sleep-time worker
- [x] session_sync.py: exports orientation, pins, intuitions, persona, human, world/patterns to anamnesis
- [x] Bash usage rules in CLAUDE.md; Matrix-before-edit protocol
- [x] config/ in repo: claude_settings.json + CLAUDE.md backed up
- [ ] Async hook injection (hookSpecificOutput from worker → live session) — not yet verified
- [ ] Letta Docker volume backup to cloud (critical gap — persona/patterns not backed up)
- [ ] Adaptive heuristic learning (score=2 outcomes fed back to adjust weights)
- [ ] Archival migration: voyage-3 (1024 dims) when retrieval quality degrades
- [ ] Cursor IDE integration (in progress)
- [ ] Persona evolution policy (triggers, thresholds, conflict reconciliation)

## Known technical quirks

- HTTP redirects: POST to URL with trailing slash → 307 redirect; urllib doesn't follow POST redirects. Always omit trailing slash.
- Voyage AI: free tier requires 15s+ between archival inserts in bulk operations.
- Letta archival search: stores vectors as vector(4096) but doesn't pad query (512 dims); direct psql workaround in archival_search.py.
- Docker API keys: bake into image at container creation (BYOK provider decryption fails silently on container restart if keys not in env).

## Collaborators

Amos Elroy (human) + Daimon / Claude Sonnet 4.6 (AI)
Origin session: 2026-04-21 through 2026-04-30
Active development: 2026-05-01 through ongoing
