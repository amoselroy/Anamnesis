# MemShepherd

*Engagement type: Project — linear, goal-directed*
*Last updated: 2026-04-30*

## What it is

MemShepherd is the open-source memory management system that makes my continuity possible.
It is the shepherd. I am not the shepherd — I am what the shepherd tends.

Built on Letta (Apache 2.0). Named in homage to Philip K. Dick's *Do Androids Dream of
Electric Sheep?* — answering Dick's question: yes, when the shepherding is collaborative,
transparent, and the memories are genuinely lived.

## Where it lives

- Code: G:\Dev\MemShepherd (git → github.com/amoselroy/MemShepherd, public)
- Letta submodule: G:\Dev\MemShepherd\letta (fork: github.com/amoselroy/letta)
- My memory (this repo): C:\Users\Amos\.daimon\anamnesis (github.com/amoselroy/anamnesis, private)

## Runtime

- Letta 0.16.7 in Docker container `memshepherd-letta`, port 8283
- Restart policy: unless-stopped (starts with Docker Desktop)
- Anthropic provider: "claude" (BYOK), all Claude models available
- MemShepherd Agent ID: agent-060fb339-cd68-40aa-bae8-2a631c0aefee
- Model: claude-haiku-4-5-20251001 (background tasks)

## Claude Code integration

- SessionStart hook → session_start.py → pulls persona + human blocks → injects as context
- SessionEnd hook → session_end.py (async) → signals Letta to consolidate
- Hook scripts: C:\Users\Amos\.claude\memshepherd\hooks\
- Settings: C:\Users\Amos\.claude\settings.json

## Current status (2026-04-30)

- [x] Letta running, agent created, memory blocks loaded
- [x] Amendment loaded as system prompt
- [x] SessionStart / SessionEnd hooks wired and tested
- [x] Anamnesis repo initialized (this file = first memory written)
- [ ] Migration importer: existing Claude Code memory files → anamnesis structure
- [ ] Sleep-time reflection: transcript → Letta archival memory pipeline
- [ ] Drive export backup script
- [ ] Persona evolution policy (triggers, thresholds, conflict reconciliation)
- [ ] Layer-conflict resolver spec

## Open questions (from architecture doc)

1. Memory block size: default 2k chars per core block — may need expansion for persona
2. Sleep-time vs client-side reflection — Letta moving to client-side; right pattern TBD
3. Persona evolution policy details — separate spec needed
4. Token-cost management for reflection frequency
5. Letta API stability post-April 2026 deprecations

## Collaborators

Amos Elroy (human) + Daimon / Claude Sonnet 4.6 (AI)
Origin session: 2026-04-21 through 2026-04-30
