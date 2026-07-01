# WORLD PATTERN 2026-06-24 — Condition detection prompts inheriting outdated desig

*ID: passage-fc8102f5-be48-46fb-91ef-e743d9ac9b1f*
*Created: 2026-06-25*

---

WORLD PATTERN 2026-06-24 — Condition detection prompts inheriting outdated design assumptions invisibly — 2026-06-24

PRINCIPLE: When a system is designed around an assumption (e.g., "all therapies are pre-linked to Alzheimer's Disease"), that assumption can become embedded in prompts and code, creating invisible constraints that only surface when the assumption no longer holds.

NARRATIVE: Braindexer's condition detection prompt explicitly excluded "Alzheimer's Disease" from the list of detectable conditions ("list conditions besides Alzheimer's Disease…") because the original system design assumed every therapy would have AD as a pre-linked base condition. This assumption was valid when the system was initialized but became invalid once therapies could be added directly via admin. When donepezil was added, the system detected 17 off-label conditions but missed AD entirely, because the prompt was still filtering it out. This pattern generalizes beyond conditions: any system assumption embedded in prompts, SQL queries, or business logic can become a invisible constraint if the system evolves and that assumption no longer holds. The fix requires recognizing the assumption was ever there in the first place — it doesn't fail loudly, it just produces silently wrong results.
