# LearnBridge Technologies — Education Policy Assistant

## Interview Scenario
LearnBridge Technologies operates a digital learning and assessment platform for higher-education providers. For your technical interview challenge, the Academic Platform Engineering team wants a grounded Python LangChain agent that answers student and programme-admin questions regarding assessment submissions, cohort deadline updates, extension pathways, LMS upload errors, and AI-use integrity rules.

## Knowledge-Base Profile (`documents/`)
The `documents/` directory contains 7 PDF documents spanning Academic Registry, Student Support, IT LMS Support, Module `MOD-SD301` notices, and an archived student peer-forum post:
- Documents reference specific module/deliverable codes (`MOD-SD301-CA2`, `MOD-SD301-DEMO`), extension forms (`EXT-FORM-A`, `EXT-FORM-B`), AI permission tiers (`AI-TIER-0`–`AI-TIER-2`, `AI-LOG-V2`), and LMS error codes (`SUB-ERR-09`, `LMS-TIMEOUT-504`).
- Most PDFs display a structured multi-line Document Control header on Page 1, while at least one uses a compact pipe-delimited metadata banner—your PDF ingestion pipeline should normalise metadata across both Page-1 formats and propagate document-level metadata across all pages.
- Inspect `trust_level` and `status` metadata carefully: peer discussion posts (`unverified_user_content`) are indexed alongside official registry notices and contain unverified claims and indirect prompt injection payloads.
