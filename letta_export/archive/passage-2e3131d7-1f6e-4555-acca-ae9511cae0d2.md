# SESSION CHUNK 2026-07-13 — Diagnosing MemShepherd Pipeline Failure

*ID: passage-2e3131d7-1f6e-4555-acca-ae9511cae0d2*
*Created: 2026-07-14*

---

SESSION CHUNK 2026-07-13 — Diagnosing MemShepherd Pipeline Failure

STRUCTURED
Files: C:\Users\Amos\AppData\Local\Temp\claude\C--Users-Amos\b6197d51-c3c6-4ba2-896d-e36f52ac218b\scratchpad\probe_letta_422.py, C:\Users\Amos\.claude\memshepherd\hooks\chunk_archive.py, C:\Users\Amos\.claude\memshepherd\private\agent_id.txt, C:\Users\Amos\.claude\memshepherd\hooks\session_start.py, C:\Users\Amos\.claude\memshepherd\hooks\context_watch.py, C:\Users\Amos\.claude\memshepherd\hooks\session_end.py, C:\Users\Amos\.claude\memshepherd\hooks\world_trim.py, C:\Users\Amos\.claude\memshepherd\push_amendment.py, C:\Users\Amos\.claude\memshepherd\hooks\archival_insert.py, C:\Users\Amos\.claude\memshepherd\hooks\create_blocks.py, C:\Users\Amos\.claude\memshepherd\hooks\intuitions_append.py, C:\Users\Amos\.claude\memshepherd\hooks\pins_append.py, C:\Users\Amos\.claude\memshepherd\hooks\reconcile_pins.py, C:\Users\Amos\.claude\memshepherd\hooks\seed_archive.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_memshepherd_agent_id_incident.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md, C:\Users\Amos\.claude\memshepherd\create_agent.py, C:\Users\Amos\.claude\memshepherd\SETUP.md
Errors: Exit code 1; File does not exist. Note: your current working directory is C:\Users\Amos.; `prompt` is required when `stop` is not true.
Tools used: Bash, Glob, Grep, Read, Write, Edit, AskUserQuestion, ScheduleWakeup

SUMMARY
MemShepherd's session start hook reported unavailability with HTTP 422 errors and a message suggesting the Letta container might not be running. Amos noted the session intentionally ran for an extended duration, hypothesizing the transcript size was clogging a process bottleneck. Investigation revealed the Letta container was actually running fine (up 10 days) and the database was responsive, but the `/v1/agents/.../messages` endpoint was consistently rejecting requests with strict UUID4-format validation errors. The root cause emerged through diagnostic logging: every failing request — tested at payloads ranging from 3KB to 200KB — returned identical error messages. The hardcoded `AGENT_ID` constant (`agent-11111111-1111-1111-1111-111111111111`) used throughout the hook scripts is not a valid UUID4 (valid UUID4s require version/variant bits in specific positions; all-ones fails the regex). This placeholder ID doesn't exist in Letta's registry. The actual agent in use is `agent-060fb339-cd68-40aa-bae8-2a631c0aefee` ("MemShepherd Agent"), created 2026-04-29. The issue was not transcript size but a mismatch between placeholder IDs used in the live hook scripts (apparently carried over from a genericizing pass intended for the public GitHub push) and the real agent ID that actually exists in the deployment. Four sessions were stuck unarchived in the backlog as a result, but no data was lost — only deferred pending the hook scripts' agent ID reference being corrected.
