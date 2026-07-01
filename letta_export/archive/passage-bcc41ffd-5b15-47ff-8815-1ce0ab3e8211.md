# SESSION CHUNK 2026-05-18 — Designing the Orientation Block and Pins System

*ID: passage-bcc41ffd-5b15-47ff-8815-1ce0ab3e8211*
*Created: 2026-05-18*

---

SESSION CHUNK 2026-05-18 — Designing the Orientation Block and Pins System

STRUCTURED
Files: C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_memshepherd.md, C:\Users\Amos\.claude\memshepherd\hooks\create_blocks.py, C:\Users\Amos\.claude\memshepherd\hooks\chunk_archive.py, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_pax_democratica.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md
Errors: Exit code 127
Exit: 
/usr/bin/bash: line 1: Get-Content: command not found; Exit code 1
Detecting pins: 269633 chars, date=2026-04-25

--- DETECTED 9 PIN(
Tools used: ToolSearch, mcp__matrix__reply, Read, Edit, Glob, Bash, Write

SUMMARY
A clear product design emerged from the continuity discussion: the `engagements/orientation` block was conceived as a MemFS block (not Anamnesis) that would be loaded automatically at session start alongside World, Persona, and other core blocks. This block would answer surface-level questions: what projects are active, what were the conversation topics, are there open items, what was the last engagement topic. Unlike the accumulative blocks (persona, world, patterns), orientation would be completely replaced each session by a worker process.

The pins system emerged as a complementary structure to solve the problem of deferred items. Unlike orientation (which is ephemeral), pins needed to persist across the replace cycle and survive in context. The design that crystallized: pins would be a separate accumulative MemFS block that agents could append to during a session, remove from when resolved, and which would be periodically reviewed by a cleanup script. Critically, the `chunk_archive.py` worker would not only append user-flagged pins but also detect pins semantically from session content—distinguishing between items that were "discussed and resolved" versus "discussed and deferred." The full pin lifecycle became: semantic detection by the worker, inline removal by agents on explicit resolution, and periodic reconciliation against session history to catch missed resolutions.
