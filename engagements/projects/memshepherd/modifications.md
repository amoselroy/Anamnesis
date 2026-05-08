# MemShepherd: Letta Modifications & Design Decisions

*Last updated: 2026-04-30*
*Public record: G:\Dev\MemShepherd\MODIFICATIONS.md*

This is the operational version — what I need to remember about how we diverged from
upstream Letta and why, so future sessions don't re-litigate settled decisions.

---

## What we changed (and why it matters operationally)

### Docker image: git required at startup

We build `memshepherd:local` from `G:\Dev\MemShepherd\Dockerfile` — a one-liner extending
`letta/letta:0.16.7` with git installed. This is not optional.

Letta's OSS MemFS backend uses the git CLI. More importantly: git availability is cached
at server startup. If git isn't in the image, the server caches `_git_available = False`
and no amount of installing it afterward helps — the cache never clears without a restart,
and on restart the installation is gone. Must be in the image.

If the container is ever rebuilt from scratch, use `memshepherd:local`, not `letta/letta:0.16.7`.

### LETTA_MEMFS_SERVICE_URL: dummy value required

The env var `LETTA_MEMFS_SERVICE_URL=http://localhost:8285` must be set in the container
even though the OSS MemfsClient ignores the value entirely.

Why: Letta gates MemFS activation on `if not settings.memfs_service_url: return None`.
The gate exists for the cloud version (which actually uses the URL). The OSS version ignores
it but shares the same gate. Any non-empty string satisfies it.

Risk: if upstream Letta changes `memfs_client_base.py` to actually use `base_url`, this
dummy value breaks. Watch for it.

### Block labels: path-based from the start

When `enable_git_memory_for_agent` runs, it auto-prefixes any block whose label doesn't
contain `/` with `system/`. Our original `persona` and `human` blocks became `system/persona`
and `system/human` as a result.

Lesson: always create new blocks with full path labels (`world/patterns`, not `patterns`).
The label is the file path in the git repo. Label it correctly from the start.

### PATCH /v1/blocks/{id} — no trailing slash

The Letta API returns 307 on `/v1/blocks/{id}/` (with slash) for PATCH. Python's urllib
doesn't follow PATCH redirects. Use the path without trailing slash. Curl with `-L` also
doesn't reliably follow PATCH redirects. Call from inside the container or use a proper
HTTP client.

---

## Planned: Direct Memory Write Endpoint

Status: design approved, not yet built — 2026-04-30

MemShepherd script/utility (external — NOT in the Letta fork):
- `{ block_label, operation, content, direct: true }` — skips Haiku, writes immediately
- `{ block_label, operation, content, direct: false }` — routes through agent LLM

Both paths use Letta's existing REST API (`PATCH /v1/blocks/{id}` and
`POST /v1/agents/{id}/messages`). No fork modifications needed.

Architectural rule: I call MemShepherd, never Letta block APIs directly.
MemShepherd is the sole gateway. This is a cleanliness boundary, not a capability limit.

**Standing principle: minimal fork surface.**
Letta is nearing a major rewrite. Fork changes are expensive to maintain across version
bumps. Keep all MemShepherd additions external and on top of vanilla Letta. Upgrade path
should be: change the base image tag, verify API compatibility, done. No rebase.

---

## Current runtime summary

- Image: `memshepherd:local` (must include git)
- Container: `memshepherd-letta`, port 8283, restart: unless-stopped
- Required env vars: `ANTHROPIC_API_KEY`, `LETTA_MEMFS_SERVICE_URL` (any non-empty value)
- Volume mounts:
  - `C:\Users\Amos\.letta\.persist\pgdata:/var/lib/postgresql/data`
  - `C:\Users\Amos\.letta\memfs:/root/.letta/memfs`
- Agent ID: agent-060fb339-cd68-40aa-bae8-2a631c0aefee
- Git repo on host: `C:\Users\Amos\.letta\memfs\repository\org-00000000...\agent-060fb339...\repo.git`
