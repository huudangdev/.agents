# RAG Architecture Contract

Use this skill to decide retrieval topology before implementation.

## Required Inputs

- Corpus shape and scale
- Latency budget and evaluation strategy
- Operational cost limits
- Existing repo libraries, skills, and ADRs

## Decision Rules

- Prefer the smallest retrieval stack that meets the quality target.
- Make pre-filtering, chunking, reranking, and fallback behavior explicit.
- Do not add orchestration layers without a documented gain.

## Output Contract

- State the retrieval topology and why it fits the corpus.
- Describe evaluation and failure handling.
- List docs and readiness updates needed before implementation.
