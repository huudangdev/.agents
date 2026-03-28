#!/usr/bin/env python3
"""
TRUSTGRAPH QUERY ADAPTER (Antigravity Context Extractor)

Usage:
  python3 .agents/adapters/trustgraph_query.py --task "refactor login" --target "Login.tsx"
  
Description:
  Called by Antigravity Orchestrators (Phase 0) to extract Neo4j relationships, 
  historical bugs, and User Persona preferred skills before executing an LLM request.
"""

import argparse
import json
import urllib.request
import urllib.error
import sys

# TrustGraph Neo4j HTTP Endpoint (Default)
NEO4J_HTTP_ENDPOINT = "http://localhost:7474/db/neo4j/tx/commit"
AUTH_HEADER = "Basic bmVvNGo6dHJ1c3RncmFwaF9zZWNyZXQ=" # Base64 for neo4j:trustgraph_secret

def query_graph(task, target):
    # This is the Cypher payload to extract context
    payload = {
        "statements": [
            {
                "statement": "MATCH (m:Module {name: $target})<-[:DEPENDS_ON]-(deps) RETURN deps.name AS dependents LIMIT 5",
                "parameters": {"target": target}
            },
            {
                "statement": "MATCH (m:Module {name: $target})-[:HAD_BUG]->(b:Bug) RETURN b.description AS bug_history LIMIT 3",
                "parameters": {"target": target}
            },
            {
                "statement": "MATCH (u:UserPersona)-[:PREFERS_SKILL]->(s:Skill) RETURN s.name AS preferred_skills LIMIT 3"
            }
        ]
    }
    
    try:
        req = urllib.request.Request(NEO4J_HTTP_ENDPOINT, data=json.dumps(payload).encode('utf-8'))
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', AUTH_HEADER)
        
        response = urllib.request.urlopen(req, timeout=3)
        data = json.loads(response.read().decode('utf-8'))
        
        print("\n=== 🧠 TRUSTGRAPH CONTEXT ASSEMBLED ===")
        print(f"Target Module: {target}")
        print("Data retrieved from Local TrustGraph Core:")
        print(json.dumps(data, indent=2))
        sys.exit(0)
        
    except urllib.error.URLError:
        # Fallback if Docker cluster isn't running yet
        print(f"""
=== 🧠 [TRUSTGRAPH OFFLINE FALLBACK] ===
Warning: Could not connect to TrustGraph local cluster (Neo4j:7474).
Agent Notification: Proceed with standard RAG or File-read operations.

Simulated Context for '{target}' (if DB was online):
- Coupling: [Authentication, SessionManager] rely on this module.
- Historical Bugs: 'Race condition on token refresh (Fixed in Run_102)'
- Preferred Style: 'Avoid unnecessary Redux, use Zustand or Context API'
========================================""")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TrustGraph Native Query Adapter")
    parser.add_argument("--task", required=True, help="Task description")
    parser.add_argument("--target", required=False, default="CoreModule", help="Target File or Component")
    
    args = parser.parse_args()
    query_graph(args.task, args.target)
