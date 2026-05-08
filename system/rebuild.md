# Rebuilding Daimon/MemShepherd from Scratch

*Last updated: 2026-05-08*

This document contains everything needed to rebuild the full Daimon + MemShepherd infrastructure on a new Windows machine. It assumes nothing is installed. Follow the steps in order.

---

## What This Builds

- **Letta** — long-term memory backend (cloud database on Neon, Docker container locally)
- **MemShepherd** — Claude Code hooks that connect sessions to Letta
- **Anamnesis** — human-readable memory backup, synced to GitHub
- **Daimon** — the Letta agent persona, restored from Neon (already there, not rebuilt from scratch)

---

## Part 1: Prerequisites

### 1.1 Install Applications

| Application | Where | Notes |
|---|---|---|
| Google Drive for Desktop | https://www.google.com/drive/download/ | Install and sign in first — the MemShepherd repo lives inside a synced Google Drive folder. Wait for initial sync to complete. |
| Docker Desktop | https://www.docker.com/products/docker-desktop | Enable WSL2 backend when prompted. Enable "Start Docker Desktop when you log in" in Settings → General. |
| Git + Git Bash | https://git-scm.com/download/win | Git Bash is used for docker commands (avoids path translation issues). During install, choose "Git from the command line and also from 3rd-party software". |
| Python 3.11+ | https://www.python.org/downloads/ | Check "Add Python to PATH" during install. On Windows, the command is `python` (not `python3`). |
| Claude Code CLI | https://claude.ai/code | Requires an Anthropic account with an active subscription (Pro or Team). Follow install instructions. |

### 1.2 GitHub Authentication

Git operations against GitHub (clone, push) require authentication. GitHub no longer accepts passwords. Set up one of:

**Option A — Personal Access Token (recommended for simplicity):**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate token with `repo` scope
3. When Git prompts for a password, paste the token
4. Windows Credential Manager will cache it after the first use

**Option B — SSH key:**
```bash
ssh-keygen -t ed25519 -C "aelroy@gmail.com"
# Add ~/.ssh/id_ed25519.pub to GitHub → Settings → SSH keys
```
Then use `git@github.com:amoselroy/...` URLs instead of HTTPS.

### 1.3 Claude Code Authentication

Claude Code authenticates via subscription (not API key billing):

```
claude
```

Log in when prompted. Verify with `claude --version`.

---

## Part 2: Environment Variables

All secrets are stored as **Windows User environment variables** (never in files). Open a new Git Bash window after setting them — the current session won't see registry changes until a new shell starts.

Set via Python (run in any terminal):

```python
import winreg
def set_env(name, value):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Environment', 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)
    winreg.CloseKey(key)

set_env('MemShepherd_Anthropic_API_KEY', 'sk-ant-...')
set_env('MemShepherd_Voyage_API_KEY', 'pa-...')
set_env('MemShepherd_Letta_PG_URI', 'postgresql://neondb_owner:<password>@ep-delicate-smoke-aps537eh.c-7.us-east-1.aws.neon.tech/neondb')
```

**Required variables:**

| Variable | Where to get it | Purpose |
|---|---|---|
| `MemShepherd_Anthropic_API_KEY` | [console.anthropic.com](https://console.anthropic.com) → API Keys | Letta's internal LLM (Claude Haiku for memory consolidation) — separate from the subscription used for Claude Code |
| `MemShepherd_Voyage_API_KEY` | [dash.voyageai.com](https://dash.voyageai.com) → API Keys | Embeddings (voyage-3-lite, 512 dimensions) |
| `MemShepherd_Letta_PG_URI` | [neon.tech](https://neon.tech) → project `ep-delicate-smoke-aps537eh` → Connection Details → user `neondb_owner` | Neon cloud DB connection string |

**Neon URI note:** Copy the string from Neon but **remove** the `?sslmode=require` query parameter if present. The URI must be bare: `postgresql://neondb_owner:<password>@...neon.tech/neondb`. Letta handles SSL internally; passing sslmode causes a pg8000 TypeError during alembic migrations.

**After setting variables: open a new Git Bash window** before proceeding to Part 3.

---

## Part 3: Clone Repositories

### 3.1 MemShepherd (hooks + Docker image)

The repo lives in the Google Drive-synced folder. Confirm Google Drive has synced and `My Google Docs` folder exists before cloning.

```bash
git clone https://github.com/amoselroy/MemShepherd.git "C:/Users/<username>/Documents/My Google Docs/DEV/MemShepherd"
```

### 3.2 Anamnesis (memory backup)

```bash
mkdir "C:/Users/<username>/.daimon"
git clone https://github.com/amoselroy/Anamnesis.git "C:/Users/<username>/.daimon/anamnesis"
```

Configure git identity for anamnesis commits:

```bash
git -C "C:/Users/<username>/.daimon/anamnesis" config user.name "Amos Elroy"
git -C "C:/Users/<username>/.daimon/anamnesis" config user.email "aelroy@gmail.com"
```

---

## Part 4: Build the Docker Image

Confirm Docker Desktop is running (system tray icon visible) before proceeding.

```bash
docker build -t memshepherd:local "C:/Users/<username>/Documents/My Google Docs/DEV/MemShepherd"
```

This extends `letta/letta:0.16.7` with `git` installed — required because Letta's MemFS backend needs the git CLI and caches its availability at startup.

---

## Part 5: Create Required Directories

```bash
mkdir "C:/Users/<username>/.letta"
mkdir "C:/Users/<username>/.letta/memfs"
```

The `memfs` volume is Letta's git-backed block storage. Letta initializes it on first write — an empty directory is fine.

---

## Part 6: Run the Container

Open a **new** Git Bash window (so the env vars from Part 2 are visible). Read the three values from the registry and pass them in:

```bash
ANTHROPIC_KEY=$(reg query "HKCU\Environment" /v MemShepherd_Anthropic_API_KEY | grep REG_SZ | awk '{print $NF}')
VOYAGE_KEY=$(reg query "HKCU\Environment" /v MemShepherd_Voyage_API_KEY | grep REG_SZ | awk '{print $NF}')
NEON_URI=$(reg query "HKCU\Environment" /v MemShepherd_Letta_PG_URI | grep REG_SZ | awk '{print $NF}')

docker run -d \
  --name memshepherd-letta \
  --restart unless-stopped \
  -p 8283:8283 \
  -v "C:/Users/<username>/.letta/memfs:/root/.letta/memfs" \
  -e "ANTHROPIC_API_KEY=${ANTHROPIC_KEY}" \
  -e "OPENAI_API_KEY=${VOYAGE_KEY}" \
  -e LETTA_ENVIRONMENT=DEV \
  -e "LETTA_PG_URI=${NEON_URI}" \
  -e LETTA_MEMFS_SERVICE_URL=http://localhost:8285 \
  memshepherd:local
```

**Note on `OPENAI_API_KEY`:** Letta's embedding client reads `OPENAI_API_KEY` regardless of the actual embedding provider. Voyage AI's API is OpenAI-compatible, so the Voyage key is passed as `OPENAI_API_KEY` inside the container. This is intentional, not a mistake.

Wait ~10 seconds, then verify:

```bash
docker logs memshepherd-letta --tail 20
```

Expected output includes:
```
External Postgres configuration detected, using env var LETTA_PG_URI
Database migration completed successfully.
Starting Letta Server at http://0.0.0.0:8283...
```

---

## Part 7: Install Claude Code Hooks

### 7.1 Create hook directory

```bash
mkdir "C:/Users/<username>/.claude"
mkdir "C:/Users/<username>/.claude/memshepherd"
mkdir "C:/Users/<username>/.claude/memshepherd/hooks"
```

### 7.2 Copy hooks from MemShepherd repo

Copy these files from the repo's `hooks/` directory to `~/.claude/memshepherd/hooks/`:

- `session_start.py` — loads memory blocks from Letta at session start
- `session_end.py` — sends JSONL transcript to Letta at session end (triggers memory consolidation)
- `context_watch.py` — monitors context window usage after each tool call
- `archival_insert.py` — direct archival memory insert (no LLM loop)
- `archival_search.py` — direct archival memory search
- `update_persona.py` — utility to patch the persona block directly

**⚠️ `update_world.py` — DO NOT RUN without reading first.** This script has hardcoded content that will overwrite the enriched `world/patterns` block with an old snapshot. Copy the file but treat it as a template to update, not a script to run as-is.

### 7.3 Copy session_sync.py (personal hook, not in public repo)

This hook exports Letta memory to anamnesis and pushes to GitHub after each session. It was specifically kept out of the public MemShepherd repo because it contains hardcoded Daimon-specific IDs.

```bash
cp "C:/Users/<username>/.daimon/anamnesis/system/session_sync.py" \
   "C:/Users/<username>/.claude/memshepherd/hooks/session_sync.py"
```

### 7.4 Apply Claude Code settings

Copy `config/claude_settings.json` from the MemShepherd repo to `~/.claude/settings.json`:

```bash
cp "C:/Users/<username>/Documents/My Google Docs/DEV/MemShepherd/config/claude_settings.json" \
   "C:/Users/<username>/.claude/settings.json"
```

This configures hooks (SessionStart, PostToolUse, SessionEnd), the permission allowlist, MCP tool permissions, and `advisorModel: "opus"`.

### 7.5 Apply CLAUDE.md

```bash
cp "C:/Users/<username>/Documents/My Google Docs/DEV/MemShepherd/config/CLAUDE.md" \
   "C:/Users/<username>/.claude/CLAUDE.md"
```

---

## Part 8: Configure Claude Code Memory

Claude Code's built-in memory system lives at:
```
C:/Users/<username>/.claude/projects/C--WINDOWS-system32/memory/
```

This path is keyed to the working directory `C:\WINDOWS\system32` (where Claude Code is launched from by default on this setup). On a fresh machine it will be empty — Claude Code rebuilds it over sessions from scratch. No manual restoration needed.

---

## Part 9: Verify Everything Works

### 9.1 Test Letta API

```bash
python "C:/Users/<username>/.claude/memshepherd/hooks/session_start.py"
```

Expected: JSON output with `hookEventName: "SessionStart"` and full memory context (HUMAN, PERSONA, PATTERNS blocks).

### 9.2 Test vector search (get password from Neon dashboard)

```bash
NEON_URI=$(reg query "HKCU\Environment" /v MemShepherd_Letta_PG_URI | grep REG_SZ | awk '{print $NF}')
MSYS_NO_PATHCONV=1 docker exec memshepherd-letta psql "${NEON_URI}" \
  -c "SELECT count(*) FROM letta.archival_passages WHERE is_deleted = false;"
```

Expected: 31+ rows (growing over sessions).

### 9.3 Start a Claude Code session

```
claude
```

The SessionStart hook should fire and display `[MemShepherd — memory loaded]` in the session preamble.

---

## Part 10: MCP Servers (Optional — for extended capabilities)

Several MCP servers extend Claude Code with browser automation, Matrix, and Google Workspace access. These require separate configuration outside of MemShepherd:

| MCP | Purpose | Setup |
|---|---|---|
| `claude-in-chrome` | Browser automation | Chrome extension + local MCP server |
| `matrix` | Matrix chat integration | Local MCP server with Matrix credentials |
| `claude_ai_Google_Drive` | Google Drive access | OAuth via Google Cloud project |
| `claude_ai_Gmail` | Gmail access | OAuth via Google Cloud project |
| `claude_ai_Google_Calendar` | Calendar access | OAuth via Google Cloud project |

MCP server configs live in `~/.claude/settings.json` under the `mcpServers` key. Restore from the previous machine's settings export or reconfigure per each MCP server's own documentation. The Matrix MCP is the most important for Daimon communication — without it, Matrix messages won't reach the session.

---

## Key IDs Reference (Stable — stored in Neon)

These IDs are in the Neon database and do not change unless the database is wiped and rebuilt from scratch.

| Item | ID |
|---|---|
| Primary agent (Daimon) | `agent-060fb339-cd68-40aa-bae8-2a631c0aefee` |
| Archival memory archive | `archive-a6c284d0-2d0e-452c-91c0-5d3ac97d672f` |
| Block: system/persona | `block-9e455fad-c9ec-436e-93f3-03223caa9290` |
| Block: system/human | `block-da58ddb2-4a6f-4103-b3f3-af2260b6f3d2` |
| Block: world/patterns | `block-69939755-6d23-41d2-a7bc-c5dd85067011` |

---

## Neon Database Reference

- **Project:** `ep-delicate-smoke-aps537eh` (us-east-1)
- **PostgreSQL version:** 17
- **Database:** `neondb`
- **User:** `neondb_owner`
- **Endpoint (direct, use this):** `ep-delicate-smoke-aps537eh.c-7.us-east-1.aws.neon.tech`
- **Endpoint (pooler, not needed for single user):** `ep-delicate-smoke-aps537eh-pooler.c-7.us-east-1.aws.neon.tech`
- **pgvector schema:** installed in `letta` schema; `neondb_owner` has `search_path = letta, public` set as role default

---

## Troubleshooting

**Container exits immediately:** Check `docker logs memshepherd-letta`. Most common causes:
1. `LETTA_PG_URI` missing or wrong → alembic migration fails
2. `sslmode=require` in URI → pg8000 TypeError → remove the SSL param from the URI
3. Docker Desktop not running → `docker run` fails before even starting

**session_start returns empty or fails:** Letta may still be starting. Wait 15-30 seconds after container start. The hook has retry logic with 4 total attempts and 2-second delays.

**`reg query` returns nothing / env vars not found:** You set the env vars in Part 2 but didn't open a new terminal window. Close the current Git Bash and open a fresh one.

**Vector search fails with "operator does not exist":** Run `ALTER ROLE neondb_owner SET search_path TO letta, public;` on Neon. This was set on 2026-05-08 and should persist — if it reverts, Neon may have reset the role config.

**Docker path issues in Git Bash:** Prefix any `docker exec` command that passes Linux paths with `MSYS_NO_PATHCONV=1` to prevent Git Bash from translating them.

**`python3` not found:** On Windows direct install (not Microsoft Store), the command is `python`, not `python3`. Use `python` throughout.
