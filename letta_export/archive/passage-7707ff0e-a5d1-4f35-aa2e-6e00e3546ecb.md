# MemShepherd operational: Letta modifications and known quirks

*ID: passage-7707ff0e-a5d1-4f35-aa2e-6e00e3546ecb*
*Created: 2026-05-01*

---

[MemShepherd operational: Letta modifications and known quirks]
Docker image: git must be baked into the image (memshepherd:local). Letta's MemFS caches git availability at startup â€” installing git after the container starts never helps.

LETTA_MEMFS_SERVICE_URL must be set to any non-empty value even though the OSS MemfsClient ignores it. The activation gate is shared with the cloud version.

Block labels must use path separators from creation (e.g. world/patterns not patterns). The enable_git_memory_for_agent function auto-prefixes bare labels with system/, which is how persona became system/persona.

PATCH /v1/blocks/{id} requires no trailing slash. The trailing slash returns 307; Python urllib does not follow PATCH redirects.

embedding_api_key in the agent embedding config is not persisted by Letta. Embedding API key must be passed as OPENAI_API_KEY container env var (Letta uses OpenAI SDK as generic HTTP client for any OpenAI-compatible embedding endpoint, including Voyage AI).

Voyage AI rate limiting: free tier requires at least 15-second gaps between archival inserts in bulk seeding operations.
