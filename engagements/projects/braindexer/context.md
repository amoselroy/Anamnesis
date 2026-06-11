# Braindexer — Project Context

*Last updated: 2026-06-10*

---

## What it is

A curated, searchable index of Alzheimer's therapies — both clinical and emerging — with three-level summaries (clinical, informed layperson, plain language), evidence scores, and semantic search. Built for Amos as a research tool and potentially public-facing resource.

Live at: https://braindexer.onrender.com

**Why:** Auto-discovery scrapes pharma/biotech from AlzForum and PubMed but misses lifestyle interventions. Manual curation fills that gap. The three-audience summary model (clinician / informed patient / layperson) distinguishes it from raw literature search.

---

## Architecture

- **Backend:** FastAPI on Render free tier, auto-deploy from GitHub master (`amoselroy/Braindexer`)
- **Database:** Neon PostgreSQL with `pgvector` extension (cosine similarity search)
- **Embeddings:** Voyage AI `voyage-3`, 1024-dimensional; text = name + mechanism + summary_informed + aliases
- **AI:** Anthropic Claude (summarization, scoring, condition detection, Research & Summarize pipeline)
- **Schema:** `braindexer` schema — therapies, conditions, therapy_conditions (junction), therapy_aliases, condition_aliases, sources, therapy_relationships, scraper_sources

---

## Data model (key design decisions)

- **Condition-specific data lives on the junction table** (`therapy_conditions`): summary_clinical, summary_informed, summary_layperson, therapeutic_action, effectiveness_score, evidence_score, evidence_level, pathway_tags. Therapy-level fields are the cross-condition generalized versions.
- **Aliases on both sides**: `therapy_aliases` for search/embedding enrichment; `condition_aliases` for deduplication when AI-detected conditions vary in phrasing ("Alzheimer's" vs "Alzheimer's Disease").
- **Scores are SMALLINTs 1-10**: therapeutic_action (mechanism novelty), effectiveness_score (evidence of benefit), evidence_score (quality/quantity of trials), safety_score (risk profile).

---

## Search

- **Semantic first**: Voyage AI embedding of query → cosine distance via pgvector `<=>` operator
- **Threshold**: 0.87 cosine distance (tuned 2026-06-10; may need adjustment after Re-embed All with richer embeddings)
- **Keyword fallback**: ILIKE on name + mechanism if semantic returns nothing
- **Embedding text** includes name + mechanism + summary_informed + all aliases — richer after Research & Summarize completes

---

## Current state (2026-06-10)

**Live and working:**
- 5 therapies: Lecanemab, Rosemary, Lithium Orotate, Gamma Sensory Stimulation (40Hz), Sauna
- 1 condition: Alzheimer's Disease
- Research & Summarize completed on all 5
- Semantic search + keyword fallback functional
- Condition filter on homepage
- Admin console: full CRUD, Research & Summarize, Summarize Only, Re-embed (per-therapy), Re-embed All

**Immediate next steps:**
- Run Re-embed All from admin (embeddings were generated before aliases existed; now aliases are in embed text)
- Validate 0.87 threshold after re-embedding
- Manual curation: add lifestyle/nutritional therapies (Mediterranean diet, exercise, sleep hygiene, meditation, CPAP)

---

## Future phases (in rough priority order)

1. Manual curation of lifestyle/nutritional therapies
2. Discovery scraper: `discover_new_therapies()` — pseudocode complete, not yet written; weekly scheduler
3. Admin draft review: list/approve/reject/merge drafted therapies
4. Two-mode therapy page UX: condition-first (defaults to that condition's data) vs therapy-first (all conditions as selectable chips)
5. Relationship management UI: admin tab for therapy-to-therapy relationships (variant_of, synergistic, complementary, etc.)
6. Newsletter feature: Buttondown integration, Phase 3/4
7. Basic research layer: pathway/mechanism nodes as first-class entities, preprint integration, bidirectional discovery
8. po.ln: larger semantic interdisciplinary knowledge map — long-term successor; lessons from Braindexer inform design

---

## Domain name

Undecided. Candidates: Braindexer.org, Neurascent.org, Cognifront.org — all available as of 2026-06-07.

---

## Key files

- `main.py` — FastAPI app entry, mounts routers
- `routers/therapies.py` — all therapy + condition + search endpoints
- `services/scraper.py` — Research & Summarize pipeline
- `services/summarizer.py` — Claude summarization and scoring
- `services/embeddings.py` — Voyage AI embed + embed_therapy()
- `database.py` — ThreadedConnectionPool, get_connection() context manager
- `models.py` — Pydantic v2 models
- `setup_db.py` — idempotent schema setup + column migrations
- `static/index.html` — public therapy list + search
- `static/admin.html` — admin console
- `static/therapy.html` — therapy detail page
