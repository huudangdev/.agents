#!/usr/bin/env python3
"""
TRUSTGRAPH VECTOR SEARCH (Semantic Retrieval)

Usage:
  python3 .agents/adapters/trustgraph_vector_search.py --query "Where is the auth logic?"
  
Description:
  Takes a natural language query, computes the embedding locally,
  and fetches top K nearest code chunks from ChromaDB. Output is standard JSON.
"""

import argparse
import sys
import json
import chromadb
from chromadb.utils import embedding_functions
from trustgraph_config import CHROMA_COLLECTION, CHROMA_HOST, CHROMA_PORT

def initialize_chroma_client():
    try:
        client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
        client.heartbeat()
        return client
    except Exception as e:
        print(json.dumps({"error": "ChromaDB cluster offline"}))
        sys.exit(1)

def search_codebase(query, top_k):
    client = initialize_chroma_client()
    try:
        collection = client.get_collection(CHROMA_COLLECTION)
    except ValueError:
        print(json.dumps({"error": f"Collection '{CHROMA_COLLECTION}' does not exist. Run vectorize script first."}))
        sys.exit(1)
        
    emb_fn = embedding_functions.DefaultEmbeddingFunction()
    
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    
    formatted_results = []
    
    if results['documents'] and len(results['documents']) > 0:
        docs = results['documents'][0]
        metas = results['metadatas'][0]
        distances = results['distances'][0]
        
        for i in range(len(docs)):
            formatted_results.append({
                "source": metas[i].get("source", "Unknown"),
                "chunk_id": metas[i].get("chunk_id", 0),
                "distance": distances[i], # Lower is better in Cosine/L2 usually (depends on HNSW space)
                "content": docs[i]
            })
            
    print(json.dumps({"query": query, "results": formatted_results}, ensure_ascii=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TrustGraph Vector Search")
    parser.add_argument("--query", required=True, help="Natural language search query")
    parser.add_argument("--top_k", type=int, default=3, help="Number of chunks to return")
    args = parser.parse_args()
    
    search_codebase(args.query, args.top_k)
