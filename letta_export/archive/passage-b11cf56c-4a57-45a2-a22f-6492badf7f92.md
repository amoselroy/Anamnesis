# WORLD PATTERN 2026-08-26 — Misdiagnosis as springboard to better source discover

*ID: passage-b11cf56c-4a57-45a2-a22f-6492badf7f92*
*Created: 2026-09-10*

---

WORLD PATTERN 2026-08-26 — Misdiagnosis as springboard to better source discovery — 2026-08-26

PRINCIPLE: When diagnosing an extraction failure as a bug, verify the diagnosis against the actual content structure; what appears to be a systematic extraction problem may be a content problem best solved by adding better sources rather than fixing the extractor.

NARRATIVE: TAPinto Hoboken was pinned as "129 candidate links, 129 fail extraction"—a prima facie extractor bug. Detailed investigation revealed TAPinto's rendered "Upcoming Events" section actually contained only ~4-5 distinct events over 10 weeks, with the other ~120 "candidates" being site-wide chrome (navigation, columns, pages) present on every page, not page-specific content. No extraction failure occurred; the extraction succeeded at capturing noise. Rather than fixing the extractor, the decision was to remove TAPinto entirely and add two new sources (Hudson County and JC Cultural Affairs Flag Raisings) where the same events originated. The removal of an aggregator that was fragmenting the feed and the addition of primary sources proved more effective than attempting to sharpen extraction filters.

NONE
