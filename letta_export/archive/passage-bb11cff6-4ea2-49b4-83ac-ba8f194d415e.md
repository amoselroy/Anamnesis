# SESSION CHUNK 2026-08-19 — Choir/Human Voice Approximation — Iterative Sound Des

*ID: passage-bb11cff6-4ea2-49b4-83ac-ba8f194d415e*
*Created: 2026-08-25*

---

SESSION CHUNK 2026-08-19 — Choir/Human Voice Approximation — Iterative Sound Design and Technical Refinement

STRUCTURED
Files: C:\Users\Amos\projects\algorithmic-music\notes.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\project_algorithmic_music.md, C:\Users\Amos\.claude\projects\C--Users-Amos\memory\MEMORY.md, C:\Users\Amos\projects\algorithmic-music\sketches\cricket.rb, C:\Users\Amos\projects\algorithmic-music\sketches\whale.rb, C:\Users\Amos\.claude\journal_entry_tmp.md, C:\Users\Amos\projects\algorithmic-music\sketches\choir.rb
Errors: Exit code 1
=== note.rb (0 lines) ===
=== synths_helpers.rb (0 lines) ===
=== ar; Exit code 2
C:\Users\Amos\AppData\Local\Python\pythoncore-3.14-64\python.exe: ca; Exit code 127
INFO: Could not find files for the given pattern(s).
/usr/bin/bas
Tools used: Read, Grep, Bash, ToolSearch, AskUserQuestion, WebFetch, PowerShell, ScheduleWakeup, Write, Edit, WebSearch, mcp__claude-in-chrome__tabs_context_mcp
URLs: https://musescore.com/artist/jean_michel_jarre-143829?srsltid=AfmBOoovUZFS_qbU5m5MBIzoHD6pXpmSgqmNcs9QYRwZfCO9CzXnx7KT

SUMMARY
Amos requested choir/human voice synthesis. Daimon proposed using `:vowel` FX effect (`with_fx :vowel, vowel_sound: 1–5` for A/E/I/O/U formants, `voice: 0–4` for vocal register) layered over a `:saw` synth. Initial script used static pitch — result: mechanical, not vocal. Amos noted "the frequency is much too low. it sounds more like percussion." Turned out to be a synthesis error: `freq:` parameter doesn't work on `:sine` synth; needs `hz_to_midi()`
