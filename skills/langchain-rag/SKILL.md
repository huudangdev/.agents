---
description: Complete RAG pipeline for document ingestion, embedding, retrieval, and LLM-powered response generation.
---
# langchain-rag

Complete RAG pipeline for document ingestion, embedding, retrieval, and LLM-powered response generation.
- Supports multiple document loaders (PDF, web pages, directories) and persistent vector stores (Chroma, FAISS, Pinecone)
- Includes similarity search, MMR (Maximal Marginal Relevance) retrieval, and metadata filtering
- Works with OpenAI embeddings and integrates seamlessly with LangChain agents
- Best-practice guidance on chunk sizing (500–1500 chars).

**Pipeline:**
1. Index: Load → Split → Embed → Store
2. Retrieve: Query → Embed → Search → Return docs
3. Generate: Docs + Query → LLM → Response
