---
description: Production-grade RAG system design covering chunking, embeddings, vector stores, hybrid search, reranking, and evaluation.
---
# rag-architect

Production-grade RAG system design covering chunking, embeddings, vector stores, hybrid search, reranking, and retrieval evaluation.
- Guides 5 core workflow steps: requirements analysis, vector store design, chunking strategy, retrieval pipeline config, and evaluation.
- Supports pgvector, Qdrant, schema design, and sharding logic.
- Implements hybrid search combining dense vector retrieval with BM25 keyword search, plus reranking via Cohere.
- Includes evaluation framework using RAGAS metrics (context precision, recall, faithfulness, answer relevancy).
