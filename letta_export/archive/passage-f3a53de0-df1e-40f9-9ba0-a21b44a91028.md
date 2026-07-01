# WORLD PATTERN 2026-06-10 — Similarity metrics without thresholds rank all result

*ID: passage-f3a53de0-df1e-40f9-9ba0-a21b44a91028*
*Created: 2026-06-10*

---

WORLD PATTERN 2026-06-10 — Similarity metrics without thresholds rank all results, not filter them — 2026-06-10

PRINCIPLE: A similarity or distance metric without a threshold value will rank and return all items based on their distance/similarity score, not filter to only the most similar items.

NARRATIVE: After implementing search with semantic similarity via embeddings, searching for "lecanemab" returned all 5 therapies in the database instead of filtering to only the most relevant one. The vector search `<=>` operator computed cosine distances for all 5 therapies to the query, and the ORDER BY clause ranked them by distance. Without a WHERE clause threshold on the distance value, all 5 therapies had measurable distances and all 5 were returned in order. The distances showed a gap (Lecanemab at 0.745, Sauna at 0.795, others at 0.89–0.925), making the irrelevant items obvious once visualized. A similarity threshold of 0.82 was added to filter out results below that distance. This pattern generalizes: similarity-based systems that lack explicit thresholds will return many low-quality matches on small datasets where everything has some similarity to everything else, creating the impression that the similarity metric "isn't working" when it's actually functioning as designed (ranking) rather than filtering. The threshold must be explicit.
