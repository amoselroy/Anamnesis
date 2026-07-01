# SESSION CHUNK 2026-04-25 — Activating and Debugging Letta's Git-Backed MemFS

*ID: passage-0a205463-bfe8-4c2e-8fe4-5fb1b9a3c913*
*Created: 2026-05-17*

---

SESSION CHUNK 2026-04-25 — Activating and Debugging Letta's Git-Backed MemFS

STRUCTURED
Files: G:\Dev\MemShepherd\create_daimon.py, C:\Users\Amos\.claude\memshepherd\hooks\session_start.py, C:\Users\Amos\.claude\memshepherd\hooks\session_end.py, C:\Users\Amos\.claude\settings.json, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_memshepherd.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md, C:\Users\Amos\.daimon\anamnesis\system\amendments.md, C:\Users\Amos\.daimon\anamnesis\persona\state.md, C:\Users\Amos\.daimon\anamnesis\engagements/projects/memshepherd/context.md, C:\Users\Amos\.daimon\anamnesis\engagements\companionship\relationships\Daimon.md, G:/Dev/MemShepherd/Dockerfile, C:/Users/Amos/.claude/memshepherd/hooks/session_start.py, C:/Users/Amos/.daimon/anamnesis/engagements/projects/memshepherd/context.md, C:/Users/Amos/.claude/projects/C--Users-Amos/memory/project_memshepherd.md, C:/Users/Amos/.claude/memshepherd/hooks/update_world.py, C:/Users/Amos/.claude/memshepherd/hooks/update_persona.py, G:/Dev/MemShepherd/MODIFICATIONS.md, C:/Users/Amos/.daimon/anamnesis/engagements/projects/memshepherd/modifications.md
Errors: <tool_use_error>Directory does not exist: C:\Users\Amos\Dev\MemShepherd. Note: y; Exit code 1
At line:1 char:124
+ ... ture-discussion.md daimons-amendment.md; g; Exit code 128
Initialized empty Git repository in C:/Users/Amos/Documents/My Goo; Exit code 1
Head : The term 'Head' is not recognized as the name of a cmdlet, fu; Exit code 1
gh : The term 'gh' is not recognized as the name of a cmdlet, functi; Exit code 1
Docker version 29.3.0, build 5927d80
failed to connect to the docker; Exit code 1
Invoke-RestMethod : {"trace_id":"","detail":"[{'type': 'missing', 'l; Exit code 1
Invoke-RestMethod : {"detail":"Provider name 'anthropic' conflicts w; Exit code 1
Invoke-RestMethod : {"detail":"Not Found"}
At line:1 char:1
+ Invo; Exit code 1
Invoke-RestMethod : {"detail":"There was an error parsing the body"}; The user doesn't want to proceed with this tool use. The tool use was rejected (; Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <m; Exit code 1
Traceback (most recent call last):
  File "<string>", line 3, in <m; Exit code 52; File does not exist. Note: your current working directory is C:\Users\Amos\.daim; Exit code 2
ls: cannot access 'C:/Program Files/Git/root/': No such file or dire; Exit code 1
Traceback (most recent call last):
  File "<string>", line 14, in <; Exit code 1
Traceback (most recent call last):
  File "<string>", line 14, in <m; Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <mo; Exit code 1; Exit code 1
like: line 28: warning: here-document at line 1 delimited by end-of-; Exit code 2
python3: can't open file '/app/C:/Users/Amos/AppData/Local/Temp/upda; Exit code 127
/usr/bin/bash: line 1: gh: command not found; Permission denied by user; Error capturing screenshot: Cannot access a chrome-extension:// URL of different; Failed to execute JavaScript: Cannot access a chrome-extension:// URL of differe; Error clicking: Cannot access a chrome-extension:// URL of different extension; Error pressing key: Cannot access a chrome-extension:// URL of different extensi
Tools used: Read, ToolSearch, WebSearch, Glob, PowerShell, Write, Edit, Skill, Agent, Bash, mcp__claude-in-chrome__tabs_context_mcp, mcp__claude-in-chrome__tabs_create_mcp, mcp__claude-in-chrome__navigate, mcp__claude-in-chrome__read_page, mcp__claude-in-chrome__form_input, mcp__claude-in-chrome__computer, mcp__claude-in-chrome__javascript_tool, mcp__claude-in-chrome__get_page_text, mcp__claude-in-chrome__find
URLs: https://json-schema.org/draft/2020-12/schema", https://json.schemastore.org/claude-code-settings.json", https://*.example.com/*\", https://hooks.example.com/*\", https://reviews.example.com/{owner}/{repo}/pull/{number}\"", https://, http://memfs-py:8285`, http://localhost:8283/v1/agents/, http://localhost:8283", http://localhost:8285`, https://github.com/letta-ai/letta/issues/new?template=bug_report.yml`

SUMMARY
NARRATIVE SUMMARY:

After initial setup, the critical work begins: enabling Letta's MemFS (git-backed memory) on the MemShepherd Agent. This reveals a subtle architectural issue that dominates a significant portion of the session.

**The Problem Discovered**: Adding the `git-memory-enabled` tag to the agent does not automatically activate MemFS. No error is raised; the system silently falls back to plain block storage. The reason: `LETTA_MEMFS_SERVICE_URL` environment variable is not set. The activation gate in `server.py` checks for this variable even though the OSS local backend (memfs_client_base.py) ignores the value entirely and uses local filesystem storage instead.

**Root Cause Analysis**: Letta's code was designed with both cloud/enterprise and OSS deployments in mind. The cloud version uses an external memfs service (the URL matters). The OSS version uses local filesystem (the URL is never referenced). However, the activation gate was shared between both, creating a logical disconnect — the OSS backend can't be activated without setting a value that the backend doesn't use.

**The Workaround**: Setting `LETTA_MEMFS_SERVICE_URL=http://localhost:8285` (any non-empty string) satisfies the gate. The OSS MemfsClient ignores the URL and writes to `~/.letta/memfs/` on local disk. This works but is misleading — users think they need an external service when they don't.

**Secondary Issue — Git Binary Caching**: While debugging, another discovery: Letta caches git availability at server startup. Installing git via `docker exec ... apt-get install git` after the container is running doesn't help; the cache was already set to False. The fix requires rebuilding the image with git pre-installed. A custom Dockerfile is created extending `letta/letta:0.16.7` with git added at build time.

**Resolution**: With both issues fixed (LETTA_MEMFS_SERVICE_URL set, custom image with git), the MemFS activates successfully. Block writes now commit to git at `C:\Users\Amos\.letta\memfs\repository\org-{id}\agent-{id}\repo.git\`. Every update creates a git commit with a message like "Update system/persona block". The git repository is visible on the host, proving the mount is working.

**Critical Learning for World Block**: The discovery that git availability caching defeats runtime installation is recorded as a pattern to watch for in other systems — if something caches availability at startup, post-startup installation won't help.
