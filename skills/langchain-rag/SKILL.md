---
name: langchain-rag
description: Complete RAG pipeline for document ingestion, embedding, retrieval, and LLM-powered response generation.
---

# Directive: LangChain RAG Pipeline

> Use this skill for full RAG pipelines when the problem genuinely requires ingestion, retrieval, and grounded generation.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Semantic Indexing:** Configure Document Loaders (PDF, Markdown, Web) and precise semantic chunking matrices (e.g., overlapping tokens) preserving natural text boundaries.
2. **Hybrid Retrieval Topography:** Construct retrievers utilizing both Dense Embedding (Cosine Similarity) and Sparse indexing (BM25) to return high-fidelity nodes.
3. **RAG Discipline:** Keep the pipeline as small as possible while preserving retrieval quality and evaluation clarity.

## ⚙️ EXECUTION PIPELINE (THE RAG LIFECYCLE)

### Phase 1: Ingestion & Vector Initialization
- Inspect the corpus and current retrieval assumptions before choosing chunking or storage strategies.

### Phase 2: Pipeline Review
- Check chunking, retrieval mode, evaluation, and fallback behavior.
- Recommend extra vector tooling only as operator-reviewed additions.

### Phase 3: Information Synthesis Logic
Enforce prompt constraints on the generation model:
- The LLM must be injected with a system prompt demanding: "If the context matrix is null, yield `NO_DATA`. Never extrapolate."
- **The Circuit Breaker Rule:** When developing a data parsing pipeline on localhost via Terminal (`npm run ingest`/`python embed.py`), if the Document loader crashes 3 consecutive times due to bad binary formatting, ABORT. Raise a Terminal Red Flag 🚩.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Zero-Downtime Data Testing
- RAG code must be accompanied by a direct query test script. Instruct the Operator to physically test the retrieval latency bounds.
- If implementation is active, require docs and execution-readiness gates before coding starts.
- **[REPORT]**: Emitted upon successful delivery of the Chunking/Retrieval python or JS logic matrices.
