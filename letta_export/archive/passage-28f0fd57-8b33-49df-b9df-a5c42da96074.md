# SESSION ARCHIVE 2026-05-14 â€” Pax Democratica site expansion + MemShepherd diag

*ID: passage-28f0fd57-8b33-49df-b9df-a5c42da96074*
*Created: 2026-05-15*

---

SESSION ARCHIVE 2026-05-14 â€” Pax Democratica site expansion + MemShepherd diagnostics

## Work completed

1. Pax Democratica â€” Proposal page (new, full content)
   - src/content/docs/proposal.mdx: structured YAML frontmatter with header, intro, 3 parities (Gender, Territorial, Political/Civil), 6 assembly specs, civil/political selection, 3 civil society modes (Paffenholz framework), coalition section, trauma-informed framing, CTA
   - src/components/pages/ProposalPage.astro: sidebar/prose grid, rationale popovers via details/summary elements styled as 'i Why this?', spec card grid, numbered mode blocks
   - src/pages/proposal/index.astro + src/pages/[lang]/proposal/index.astro (5 locales, fallback to EN)

2. Pax Democratica â€” Origin Story page (placeholder)
   - src/content/docs/origin-story.mdx: placeholder with 'Coming soon â€” intellectual genesis' framing
   - src/components/pages/OriginStoryPage.astro: centered placeholder block + CTA
   - src/pages/origin-story/index.astro + src/pages/[lang]/origin-story/index.astro

3. Header navigation updated (Header.astro)
   - Added 'Proposal' and 'Origin Story' nav links between Vision and Articles
   - EN-only nav labels; per-key merge from EN baseline so existing translations preserved, new keys fall back to EN until translate-sync handles them
   - Pattern: labels = spread of navLabels.en merged with per-lang overrides

4. Settings.json â€” SessionStart hook timeout increased from 45s to 60s

5. Content source â€” Reviewed Google Drive 'Peace' folder (PDFs + images); content reflected in proposal.mdx structure (mechanics, rationale map, civil society modes, trauma framing, parity framework)

## Key decisions / constraints
- Translate-sync (git action) handles all translations; Daimon never writes locale content directly
- Nav label translations: only EN in navLabels; other locales inherit via spread merge
- Rationale popovers: pure HTML details/summary, no JS required
- Logos already on site â€” skip Drive logo downloads
- MemShepherd archival method: archival_insert.py (direct POST to /v1/agents/{id}/archival-memory), NOT session_end.py (LLM method broken â€” Anthropic API usage limit hit, resets 2026-06-01)

## MemShepherd status
- Letta container healthy (v0.16.7), agent ID: agent-060fb339-cd68-40aa-bae8-2a631c0aefee
- session_end.py (LLM method) returns 400/UNAVAILABLE â€” API limits
- archival_insert.py â€” also broken: Letta calls Anthropic even for archival-memory endpoint (embedding generation)
- SessionStart hook: had 45s timeout (too short); increased to 60s
- Pending: flush this file to Letta after 2026-06-01 when API quota resets
