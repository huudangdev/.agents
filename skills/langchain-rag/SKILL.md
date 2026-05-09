---
name: langchain-rag
description: Design LangChain RAG pipelines with explicit ingestion, retrieval, and verification boundaries
---

# LangChain RAG Pipeline

Use this skill when a full document ingestion and retrieval pipeline is needed.

## Required Reads

- [langchain-rag-contract.md](references/langchain-rag-contract.md)
- The corpus shape and retrieval goal when they exist.

## Operating Rules

- Keep the pipeline as small as possible.
- Make retrieval mode and failure handling explicit.
- Require a direct query test script for implementation work.

## Output Expectations

- State the ingestion, embedding, retrieval, and generation flow.
- Identify the retrieval mode and evaluation plan.
- Describe the verification required before merge.
