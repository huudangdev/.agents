# LangChain RAG Contract

Use this skill when a full document ingestion and retrieval pipeline is needed.

## Required Inputs

- Corpus shape and retrieval goal
- Chunking, retrieval, and fallback constraints
- Latency and evaluation expectations

## Decision Rules

- Keep the pipeline as small as possible.
- Make retrieval mode and failure handling explicit.
- Require a direct query test script for implementation work.

## Output Contract

- State the ingestion, embedding, retrieval, and generation flow.
- Identify the retrieval mode and evaluation plan.
- Describe the verification required before merge.
