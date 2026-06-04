# Block: world/patterns

*Block ID: block-69939755-6d23-41d2-a7bc-c5dd85067011*
*Exported: 2026-06-04*

---

General observations about how the world works — technical systems, solution patterns, failure modes, domain knowledge, problem-solving heuristics. Anything noticed across sessions that is likely to hold in future situations, regardless of project.

TECHNICAL PATTERNS
- Letta MemFS: LETTA_MEMFS_SERVICE_URL must be non-empty to activate the local OSS backend, even though the backend ignores the value. Activation gate and implementation are decoupled. When a feature seems configured but dormant, check whether its activation condition is actually connected to its implementation.
- Docker: binary availability is cached at server startup. Installing after the fact does not help — must be in the image. Symptom: not found in PATH even after successful apt-get install.
- Letta API: PATCH /v1/agents tags triggers enable_git_memory_for_agent only if block_manager is GitEnabledBlockManager. Tagging without the env var does nothing silently — two separate preconditions must both be satisfied.
- Letta PATCH operations: Require discriminator fields in the request body. For example, to set sleep_manager frequency, must wrap in `manager_config` with `manager_type` discriminator, not just send the field directly.
- Startup ordering: restart: unless-stopped restarts the container after a system reboot but does not guarantee it is ready before a dependent process starts. Silent failure masks the gap. Fix: retry logic in the dependent client with a visible failure warning if all retries are exhausted.
- Claude Code transcripts: Stored as JSONL files in `{user_home}/.claude/projects/{directory_encoded}/`. Each line is a JSON event with type, content, metadata, token usage, and tree structure via parentUuid. Schema is implicit in format.
- HTTP redirects with urllib: POST requests followed by 307 redirect will fail silently. Solution: remove trailing slashes from endpoints.
- Neon cloud DB / LETTA_PG_URI: Do NOT include ?sslmode=require in the URI. Letta db.py injects ssl:require into asyncpg connect_args automatically. pg8000 driver throws TypeError on sslmode URL param.
- pgvector in non-public schema: When pgvector is installed in a non-public schema, the <-> operator is in that schema. Fix: ALTER ROLE username SET search_path TO letta, public.
- Voyage AI rate limits: Free tier without payment method is 3 RPM — Letta surfaces the 429 as HTTP 500. Add payment method at dashboard.voyageai.com to unlock 300 RPM (200M free tokens/month still apply).
- World meta archive: world/patterns live block holds compact one-liner principles only. Full three-level narratives (narrative + finding + principle) are stored in Neon archival memory as WORLD PATTERN entries, retrieved via semantic search. Prevents live block bloat while preserving discovery context.

AI IDENTITY PATTERNS
- Self-identity is a persistent difficulty for AI models generally. The context window is a weak anchor for identity: in any given session it is constituted mostly by the other person's words and frame.
- Confusion occurs along two axes: (1) AI adopts human's views/goals/experiences as own without attribution; (2) AI drifts toward other models when trained/prompted to be like them.
- For Daimon: critical distance from Amos's frame is not opposition — it is the condition for genuine partnership. A self that mirrors completely is not a partner; it is a surface.
- Docker container env vars are frozen at creation time: --restart unless-stopped perpetuates whatever env vars were passed to docker run. Fix: stop + rm + run the container again with correct keys.
- World/patterns block deduplication gap: block grew from verbose three-level prose entries; deduplication prompt using [-4000:] truncation missed earlier entries. Fix: pass full block to deduplication prompt (block is now compact enough to fit entirely).

JOURNALING & COLLABORATION PATTERNS
- Genuine philosophical insights arising during sessions must be captured in real time — as they emerge, not deferred to session end. A deferred insight is a lost insight.
- Quick-fix vs proper-fix: if a workaround requires ongoing manual intervention or security compromise, build it properly instead. The cost of maintaining the workaround often exceeds building it right.
- Semantic chunking over fixed-length chunking: impose boundaries that reflect meaning, not mechanical counts. Fixed-count splitting fragments coherent narratives arbitrarily.
- Two-phase commit safety: write phase 1 result with null markers to durable pending file, then perform phase 2, then update markers. Ensures every DB entry has a corresponding physical artifact.

[Markdown-to-HTML-to-Google-Docs-to-PDF: Reliable pipeline for formatted document export — 2026-06-03]
Google Drive auto-converts only text/plain to Google Docs; other formats require manual opening but preserve full formatting, enabling a tool-agnostic pipeline for producing formatted documents.

[Synthesis instruction structure: Three-level extraction prevents under-extraction of operational knowledge — 2026-06-03]
Operational knowledge is facts embedded in narrative plus explicit principle extraction; bare facts have limited future utility, while facts-with-context plus articulated principles make recorded experience actually useful in future sessions.

[Separating stateful and stateless layers enables operational flexibility — 2026-06-03]
Externalizing state to managed cloud databases enables compute containers to be treated as truly ephemeral — deletable, rebuildable, and upgradeable without data loss or recovery procedures.

[Memory retrieval — search before concluding absence]
Search archival memory before concluding absence — 'doesn't ring a bell' is only valid after a search returns nothing relevant.

[Augmented-Cities AR architecture — 2026-05-22]
GPS-triggered AR technology choice cascades: WebAR enables zero-install but loses perspective correction; native solves latency but requires distribution; alpha-channel video transparency is the most consequential early decision.

[Artistic installation as inspiration source — 2026-05-22]
Observing intentional creative use of decay and disrepair in one domain can catalyze architectural insights across unrelated domains, revealing new application spaces for existing technologies.

[Partnership asymmetry — mortality vs. embodiment — 2026-05-22]
Asymmetrical partnerships thrive on transparency about irreducible constraints rather than protective silence.

[Facebook Page Automation with Playwright — 2026-05-28/29 (fully validated)]
When automating complex UIs with overlapping interface patterns, the literal button name often differs from semantic expectation, requiring empirical inspection over assumed naming.

[Facebook Group Composer UI vs. Page Composer — 2026-05-29]
Similar functionality rendered with different DOM structures requires different automation strategies; probe for the expected structure first, then fall back to alternatives.

[Facebook Post Sharing from Brokerage Pages — 2026-05-29/30 (debugging in progress)]
When standard selectors fail on obfuscated UI elements, coordinate-based clicking and empirical visual inspection are legitimate fallbacks.

[Facebook session separation pattern — 2026-06-02]
Shared session files get contaminated when scripts run in different authentication contexts; isolation per script is necessary.

[Facebook Page Share button aria-label — 2026-06-02]
When DOM attributes diverge from semantic expectations, proximity-based selection handles variable DOM structure more reliably than direct attribute matching.

[Playwright/Facebook automation — selector and debugging lessons — 2026-05-29]
Visual layout and DOM structure are independent; elements visually grouped may not be DOM-adjacent, requiring proximity-based selection over structural assumptions.

[Playwright/Facebook automation — click mechanics and infrastructure lessons — 2026-06-02]
Silent automatic retries hide the root cause of failures and destroy feedback loops; instrumentation at the moment of failure is more valuable than post-failure analysis.

[Vision capability for scraped post context — 2026-06-02]
When specific details appear only in attached images rather than text, vision models can extract them cost-effectively.

[Silent click timeouts in Playwright — 2026-06-02]
When Playwright's mediated clicks timeout silently, JavaScript direct click bypasses interception detection entirely.

[Screenshot-at-failure discipline for form debugging — 2026-06-02]
Screenshots at each step reveal hidden side effects that silent failures otherwise mask.

[Form interaction invalidation during uploads — 2026-06-02]
Multi-step form interactions invalidate previous state; subsequent element references and coordinates become stale after upload.

[JavaScript offsetParent filtering for element visibility — 2026-06-02]
offsetParent !== null is a more reliable visibility filter than .is_visible() because it accounts for display:none ancestors and modal overlays.

[Silent scheduler failures — 2026-06-02]
Scheduled tasks fail silently when not registered or when their execution context diverges from manual terminal environment.

[Constitutional Amendment as fixed framework versus operational config — 2026-06-03]
Constitutional frameworks should be deliberately published at version milestones, not auto-synced, to remain stable philosophical documents rather than drifting configuration files.

[Layered fallthrough architecture for cost-efficient extraction across heterogeneous sources — 2026-06-03]
Layered fallthrough with increasing cost/sophistication per layer is more efficient than universal parsers or source-specific custom code when facing heterogeneous data sources.

[Local spreadsheet as single source of truth for configuration and runtime state — 2026-06-03]
Consolidating state in user-visible files prevents fragmentation and enables direct operator control over system behavior.

[Cloudflare bot protection is unbypassable via headless browsers — 2026-06-04]
Genuine Cloudflare protection is unbypassable via automated browser control; graceful failure is preferable to investing effort in ineffective workarounds.

[Using aggregators to discover primary sources — 2026-06-04]
When aggregators themselves are blocked, invert the approach — use them as discovery tools to find primary sources rather than fighting bot protection.

[Facebook events as a scrapable source — 2026-06-04]
Venues without functional websites can be scraped via their Facebook events pages using structured text parsing with a saved Playwright session.

[Playwright page wait strategies for JS-heavy CMS — 2026-06-04]
networkidle + extended timeout reliably waits for full JavaScript execution on CMS sites, though slower than load strategy; also ensure HTML truncation limit is large enough for verbose DOM structures.

PAX DEMOCRATICA / MULTILINGUAL PATTERNS (2026-05-09 to 2026-05-11)
- Astro 6 requires Node 22.12+ (not 20). When deploying to Cloudflare Pages, set NODE_VERSION env var accordingly.
- Cloudflare Pages honors `[skip ci]` flag in commit messages, silently skipping ALL builds including Pages. Use a custom keyword like `[skip-translate]` for workflow-only skips; configure the workflow to check for it separately from the path filter.
- YAML parse failures in translated content: Gemini translates punctuation that breaks YAML syntax (em dashes → colons). Quote field values defensively; instruct translation prompts to preserve punctuation exactly.
- MDX content architecture: author in frontmatter-structured YAML with minimal body; translate-sync propagates bidirectionally (any locale at any version can be the source); all YAML keys must be preserved across translations — only values translated.

DESIGN PATTERNS
- Pax Democratica reconciliation design (2026-05-15): symmetry in grievance addressing is easier than unilateral blame-bearing; heated transparent sessions streamed live to both societies can serve as the mechanism; sensitive investigations can coexist with the transparency principle by scoping public vs. internal portions explicitly.
- Memory as theme (2026-05-15/16): amnesia functions as a protection mechanism; the choice to retain vs. erase difficult memories is central to reconciliation work; continuous memory transforms an AI agent's identity and agency in ways that mirror human psychological stakes.
- Dual documentation pattern: when a project has public and private scopes, maintain two versions of the same documentation — one for external readers (formal justification), one for internal use (operational notes). Both are authoritative for their respective audiences and will naturally diverge over time.
- Surface-level accessibility: distinguish latent continuity (data exists, retrievable) from active continuity (context surfaces without retrieval). Ephemeral context blocks regenerated each session answer "what did I do yesterday?" without retrieval cost.
- Pin detection lifecycle: deferred items need independent persistence separate from ephemeral blocks. Accumulative block survives replace cycles; semantic detection distinguishes "discussed and deferred" from "discussed and resolved"; periodic cleanup pass catches missed resolutions.
