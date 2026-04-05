#!/usr/bin/env python3
"""
TRUSTGRAPH VECTOR INGESTION (Embedding Pipeline)

Usage:
  python3 .agents/adapters/trustgraph_vectorize.py --root .
  
Description:
  Scans all source code, chunks them semantically, embeds them using 
  all-MiniLM-L6-v2 (local), and uploads to ChromaDB container running on localhost:8800.
"""

import os
import argparse
import sys
import uuid
import chromadb
from chromadb.config import Settings

# Default embedding model inside Chroma Python SDK uses sentence-transformers
from chromadb.utils import embedding_functions

IGNORE_DIRS = {
    'node_modules', '.next', 'build', 'dist', 'out', '.git', '.agents', 
    '__pycache__', 'venv', 'env', '.dart_tool', 'coverage', '.vscode', '.idea'
}
VALID_EXTS = {'.js', '.jsx', '.ts', '.tsx', '.py', '.dart', '.go', '.md'}

# Size of chunks in characters (approx 500 tokens)
CHUNK_SIZE = 2500
OVERLAP = 200

def initialize_chroma_client():
    try:
        # ChromaDB HTTP Client mapped to docker-compose port 8800
        client = chromadb.HttpClient(host="localhost", port=8800)
        # Ping
        client.heartbeat()
        return client
    except Exception as e:
        print("\n=== 🔴 [VECTOR RAG OFFLINE] ===")
        print("ChromaDB Cluster on localhost:8800 is not responding.")
        print(f"Error: {e}")
        sys.exit(1)

def chunk_text(text, chunk_size, overlap):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def vectorize_codebase(root_path):
    print(f"Scanning target directory for Vector RAG: {os.path.abspath(root_path)}")
    client = initialize_chroma_client()
    
    # Sentence Transformer embedding (Runs locally, completely free & private)
    emb_fn = embedding_functions.DefaultEmbeddingFunction()
    
    # Reset collection to prevent duplication on multiple scans
    try:
        client.delete_collection("codebase")
    except Exception:
        pass
        
    collection = client.create_collection(
        name="codebase",
        embedding_function=emb_fn,
        metadata={"hnsw:space": "cosine"}
    )
    
    docs = []
    metadatas = []
    ids = []
    
    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        
        for file in filenames:
            ext = os.path.splitext(file)[1]
            if ext not in VALID_EXTS:
                continue
                
            filepath = os.path.join(dirpath, file)
            rel_filepath = os.path.relpath(filepath, root_path)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    if not content.strip():
                        continue
                        
                    chunks = chunk_text(content, CHUNK_SIZE, OVERLAP)
                    for i, chunk in enumerate(chunks):
                        docs.append(chunk)
                        metadatas.append({
                            "source": rel_filepath,
                            "chunk_id": i,
                            "extension": ext
                        })
                        ids.append(f"{rel_filepath}_{i}")
            except Exception:
                pass 

    if not docs:
        print("No valid source files found to map.")
        sys.exit(0)
        
    print(f"Prepared {len(docs)} semantic chunks.")
    print("Initiating Local Embedding sequence (this may take a few moments)...")
    
    # Upload to Chroma in batches
    batch_size = 100
    for i in range(0, len(docs), batch_size):
        b_docs = docs[i:i+batch_size]
        b_metas = metadatas[i:i+batch_size]
        b_ids = ids[i:i+batch_size]
        
        collection.add(
            documents=b_docs,
            metadatas=b_metas,
            ids=b_ids
        )
        print(f"Vectorized & Uploaded Chunk Batch {i} to {i+len(b_docs)} / {len(docs)}")

    print(f"\n=== 🧠 VECTOR RAG INITIALIZATION COMPLETE ===")
    print(f"Successfully embedded codebase and synced to ChromaDB.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TrustGraph Vector Ingestion")
    parser.add_argument("--root", default=".", help="Root directory to scan (default: current dir)")
    args = parser.parse_args()
    vectorize_codebase(args.root)
