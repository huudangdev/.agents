#!/usr/bin/env python3
"""
TRUSTGRAPH BATCH INGESTION (Antigravity Memory Engine)

Usage:
  python3 .agents/adapters/trustgraph_ingest_all.py --root .
  
Description:
  High-speed Regex-based Code Parser.
  Scans the entire local repository ignoring binary/build folders.
  Constructs [Module]->[DEPENDS_ON]->[Module] graph and sends to Neo4j.
"""

import os
import re
import json
import urllib.request
import urllib.error
import argparse
import sys
import time
from trustgraph_config import NEO4J_HTTP_ENDPOINT, neo4j_auth_header

AUTH_HEADER = neo4j_auth_header()

IGNORE_DIRS = {
    'node_modules', '.next', 'build', 'dist', 'out', '.git', '.agents', 
    '__pycache__', 'venv', 'env', '.dart_tool', 'coverage', '.vscode', '.idea'
}
VALID_EXTS = {'.js', '.jsx', '.ts', '.tsx', '.py', '.dart', '.go'}

# Regex patterns for various languages
PATTERNS = [
    re.compile(r'import\s+(?:[\w\s{},*]+)\s+from\s+[\'"]([^\'"]+)[\'"]'), # ES6 import X from 'Y'
    re.compile(r'import\s+[\'"]([^\'"]+)[\'"]'), # ES6 import 'Y'
    re.compile(r'require\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)'), # CommonJS require('Y')
    re.compile(r'from\s+([a-zA-Z0-9_\.]+)\s+import'), # Python from X import Y
    re.compile(r'^\s*import\s+([a-zA-Z0-9_\.]+)', re.MULTILINE), # Python import X
]

def scan_codebase(root_path):
    nodes = []
    edges = []
    
    print(f"Scanning target directory: {os.path.abspath(root_path)}")
    
    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        
        for file in filenames:
            ext = os.path.splitext(file)[1]
            if ext not in VALID_EXTS:
                continue
                
            filepath = os.path.join(dirpath, file)
            rel_filepath = os.path.relpath(filepath, root_path)
            
            nodes.append(rel_filepath)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    for pattern in PATTERNS:
                        for match in pattern.findall(content):
                            # Very basic normalization.
                            target = match
                            if target.startswith('./') or target.startswith('../'):
                                target = os.path.normpath(os.path.join(os.path.dirname(rel_filepath), target))
                            edges.append((rel_filepath, target))
            except Exception:
                pass # Silently skip unreadable files

    return nodes, edges

def commit_batch_to_neo4j(nodes, edges):
    statements = []
    
    # We'll batch in chunks if the array is too big, but for normal projects a few thousand statements is fine.
    # To be extremely robust with limits, we slice it up.
    
    # 1. Deduplicate
    unique_nodes = list(set(nodes))
    
    for node in unique_nodes:
        statements.append({
            "statement": "MERGE (m:Module {name: $name})",
            "parameters": {"name": node}
        })
        
    for src, target in edges:
        statements.append({
            "statement": """
                MERGE (a:Module {name: $src})
                MERGE (b:Module {name: $target})
                MERGE (a)-[:DEPENDS_ON]->(b)
            """,
            "parameters": {"src": src, "target": target}
        })
        
    print(f"Total Cypher statements prepared: {len(statements)}")
    
    # Send in chunks of 5000 to prevent Neo4j Payload Too Large
    chunk_size = 5000
    for i in range(0, len(statements), chunk_size):
        chunk = statements[i:i + chunk_size]
        payload = {"statements": chunk}
        
        try:
            req = urllib.request.Request(NEO4J_HTTP_ENDPOINT, data=json.dumps(payload).encode('utf-8'))
            req.add_header('Content-Type', 'application/json')
            req.add_header('Authorization', AUTH_HEADER)
            
            start = time.time()
            response = urllib.request.urlopen(req, timeout=15)
            data = json.loads(response.read().decode('utf-8'))
            
            if data.get('errors'):
                print(f"Neo4j Transaction Errors in Chunk {i}: {data['errors']}")
            else:
                print(f"Chunk {i}-{i+len(chunk)} committed inside {time.time() - start:.2f}s")
                
        except urllib.error.URLError as e:
            print(f"\n=== 🧠 [TRUSTGRAPH DEFERRED] ===")
            print(f"Neo4j cluster is offline or not responding.")
            print(f"Make sure Docker is running and 'docker-compose up -d' was successfully executed.")
            sys.exit(1)
            
    print(f"\n=== 🧠 TRUSTGRAPH INITIALIZATION COMPLETE ===")
    print(f"Successfully pumped knowledge graph mapping to the local Neo4j Network.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TrustGraph Native Ingestion")
    parser.add_argument("--root", default=".", help="Root directory to scan (default: current dir)")
    
    args = parser.parse_args()
    nodes, edges = scan_codebase(args.root)
    
    if len(nodes) == 0:
        print("No valid source files found to map.")
        sys.exit(0)
        
    commit_batch_to_neo4j(nodes, edges)
