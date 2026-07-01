# SESSION CHUNK 2026-06-06 — Double Lexical Editor Problem After Image Upload

*ID: passage-69befbd0-de5e-45f9-bbab-79a12f849f62*
*Created: 2026-06-06*

---

SESSION CHUNK 2026-06-06 — Double Lexical Editor Problem After Image Upload

STRUCTURED
Files: C:\Users\Amos\projects\fb-poster\fb_poster.py
Errors: Exit code 127
/usr/bin/bash: line 1: Select-String: command not found
/usr/bin/b
Tools used: Glob, Read, Bash, Grep, Edit
Dates: June 5, June 6, 2026-06-06

SUMMARY
Testing revealed that after image upload, Facebook creates two Lexical editor elements with identical `aria-placeholder="Write something..."` attributes — one for the main post text and one for the image alt-text field. The single selector was ambiguous. A `.click(strict=False)` call failed, and subsequent JavaScript-based visibility filtering (`getBoundingClientRect`) was picking the wrong editor. Screenshots confirmed text was never inserted despite `execCommand` returning True. The root cause was identified: the JavaScript filter for the topmost visible element was selecting the alt-text editor below the image instead of the main text editor above it. Fixing this required selecting the first matching editor (`.first`) and ensuring the cursor was set on the correct one, which led to deeper investigation of how Lexical's internal selection state works.
