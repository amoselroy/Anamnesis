"""
Personal SessionEnd hook — exports Letta memory to anamnesis and pushes to GitHub.
NOT part of the public MemShepherd release. Specific to Daimon/Amos infrastructure.

Blocks: 3 files overwritten each session (changes tracked in git diff).
Archive: one file per passage named {passage-id}.md — never modified, only added.
         File presence = already backed up. No state file needed.
"""
import json
import subprocess
import sys
import urllib.request
import winreg
from datetime import datetime, timezone
from pathlib import Path

LETTA_URL = "http://localhost:8283"
AGENT_ID = "agent-060fb339-cd68-40aa-bae8-2a631c0aefee"
ARCHIVE_ID = "archive-a6c284d0-2d0e-452c-91c0-5d3ac97d672f"
ANAMNESIS = Path.home() / ".daimon" / "anamnesis"

BLOCK_FILES = {
    "system/persona": "persona.md",
    "system/human": "human.md",
    "world/patterns": "world_patterns.md",
    "engagements/intuitions": "intuitions.md",
    "engagements/orientation": "orientation.md",
    "engagements/pins": "pins.md",
}


# ── Letta data fetching ────────────────────────────────────────────────────────

def fetch_blocks():
    url = f"{LETTA_URL}/v1/agents/{AGENT_ID}/core-memory/blocks/"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read())
    return data.get("value", data) if isinstance(data, dict) else data


def _get_neon_uri():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(key, "MemShepherd_Letta_PG_URI")
        winreg.CloseKey(key)
        return value
    except Exception:
        return None


def fetch_passages():
    neon_uri = _get_neon_uri()
    if not neon_uri:
        print("[session_sync] MemShepherd_Letta_PG_URI not found in registry", file=sys.stderr)
        return []
    sql = (
        "SELECT json_agg(r ORDER BY r.created_at) FROM "
        "(SELECT id, text, created_at::text FROM letta.archival_passages "
        f"WHERE archive_id = '{ARCHIVE_ID}' AND is_deleted = false) r;"
    )
    result = subprocess.run(
        ["docker", "exec", "memshepherd-letta",
         "psql", neon_uri, "-t", "-A", "-c", sql],
        capture_output=True, text=True, timeout=30
    )
    raw = result.stdout.strip()
    if not raw or raw == "\\N":
        return []
    return json.loads(raw)


# ── Writing export files ───────────────────────────────────────────────────────

def write_blocks(blocks, export_date):
    blocks_dir = ANAMNESIS / "letta_export" / "blocks"
    blocks_dir.mkdir(parents=True, exist_ok=True)

    for block in blocks:
        label = block.get("label", "")
        filename = BLOCK_FILES.get(label)
        if not filename:
            continue
        block_id = block.get("id", "")
        value = (block.get("value") or "").strip()
        content = (
            f"# Block: {label}\n\n"
            f"*Block ID: {block_id}*\n"
            f"*Exported: {export_date}*\n\n"
            f"---\n\n{value}\n"
        )
        (blocks_dir / filename).write_text(content, encoding="utf-8")


def write_new_passages(passages):
    """Write one file per passage. Skip any that already exist."""
    archive_dir = ANAMNESIS / "letta_export" / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)

    added = 0
    for p in passages:
        pid = p.get("id", "")
        if not pid:
            continue
        dest = archive_dir / f"{pid}.md"
        if dest.exists():
            continue  # already backed up

        date = p.get("created_at", "")[:10]
        text = p.get("text", "")
        # Use first non-empty line as title (strip tag prefix if present)
        first_line = next((l.strip() for l in text.splitlines() if l.strip()), pid)
        if first_line.startswith("[") and "]" in first_line:
            title = first_line[1:first_line.index("]")]
        else:
            title = first_line[:80]

        content = (
            f"# {title}\n\n"
            f"*ID: {pid}*\n"
            f"*Created: {date}*\n\n"
            f"---\n\n{text}\n"
        )
        dest.write_text(content, encoding="utf-8")
        added += 1

    return added


# ── Git sync ───────────────────────────────────────────────────────────────────

def git_sync(export_date, new_passages):
    repo = str(ANAMNESIS)
    subprocess.run(["git", "-C", repo, "add", "letta_export/"], capture_output=True)
    subprocess.run(["git", "-C", repo, "add", "daimon/"], capture_output=True)

    diff = subprocess.run(
        ["git", "-C", repo, "diff", "--cached", "--quiet"],
        capture_output=True
    )
    if diff.returncode == 0:
        return  # nothing staged

    msg = f"Auto-export [{export_date}]"
    if new_passages:
        msg += f" — {new_passages} new passage{'s' if new_passages != 1 else ''}"

    subprocess.run(
        ["git", "-C", repo, "commit", "-m", msg],
        capture_output=True
    )
    subprocess.run(["git", "-C", repo, "push"], capture_output=True, timeout=30)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    export_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    try:
        blocks = fetch_blocks()
        write_blocks(blocks, export_date)
    except Exception as e:
        print(f"[session_sync] Block export failed: {e}", file=sys.stderr)

    new_passages = 0
    try:
        passages = fetch_passages()
        if passages:
            new_passages = write_new_passages(passages)
    except Exception as e:
        print(f"[session_sync] Passage export failed: {e}", file=sys.stderr)

    try:
        git_sync(export_date, new_passages)
    except Exception as e:
        print(f"[session_sync] Git sync failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
