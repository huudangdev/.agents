#!/usr/bin/env python3
"""
TRUSTGRAPH WRITE ADAPTER (Cognitive RAG Sync)

Usage:
  python3 .agents/adapters/trustgraph_write.py --run_id "AutoFact_#9" --status "success" --target "Login.tsx" --skills "refactor-plan" --score 0.9 --reasoning "Extracted components" --retry_of "AutoFact_#8"
  
Description:
  Commits AI reasoning vectors (Graph of Thoughts) into Neo4j.
"""

import argparse
import json
import urllib.request
import urllib.error
import sys

NEO4J_HTTP_ENDPOINT = "http://localhost:7474/db/neo4j/tx/commit"
AUTH_HEADER = "Basic bmVvNGo6dHJ1c3RncmFwaF9zZWNyZXQ=" # Base64 for neo4j:trustgraph_secret

def commit_to_graph(run_id, status, target, skills, score, reasoning, retry_of):
    edge_type = "MODIFIED"
    try:
        f_score = float(score)
        if status == "failed" or f_score < 0.5:
            edge_type = "CAUSED_ERROR"
        elif status == "success" and f_score >= 0.8:
            edge_type = "OPTIMIZED"
    except ValueError:
        pass

    cypher = f"""
    MERGE (r:Run {{id: $run_id}})
    SET r.status = $status, r.score = toFloat($score), r.reasoning = $reasoning, r.timestamp = timestamp()
    
    MERGE (m:Module {{name: $target}})
    MERGE (r)-[:{edge_type} {{score: toFloat($score), reasoning: $reasoning}}]->(m)
    
    WITH r
    UNWIND split($skills, ',') AS skill_name
    MERGE (s:Skill {{name: trim(skill_name)}})
    MERGE (r)-[:LEVERAGED]->(s)
    """
    
    parameters = {
        "run_id": run_id,
        "status": status,
        "target": target,
        "skills": skills,
        "score": score,
        "reasoning": reasoning
    }

    statements = [{"statement": cypher, "parameters": parameters}]

    if retry_of:
        statements.append({
            "statement": "MATCH (r1:Run {id: $run_id}), (r2:Run {id: $retry_of}) MERGE (r1)-[:RETRY_OF]->(r2)",
            "parameters": {"run_id": run_id, "retry_of": retry_of}
        })

    payload = {"statements": statements}
    
    try:
        req = urllib.request.Request(NEO4J_HTTP_ENDPOINT, data=json.dumps(payload).encode('utf-8'))
        req.add_header('Content-Type', 'application/json')
        req.add_header('Authorization', AUTH_HEADER)
        
        response = urllib.request.urlopen(req, timeout=3)
        data = json.loads(response.read().decode('utf-8'))
        
        print("\n=== 🧠 TRUSTGRAPH COGNITIVE VECTOR COMMITTED ===")
        print(f"Archived Execution Run: {run_id}")
        print(f"Edge Mapped: [{run_id}] -> [:{edge_type}] -> [{target}]")
        print(f"Score: {score} | Skills Leveraged: {skills}")
        sys.exit(0)
        
    except urllib.error.URLError:
        print(f"\n=== 🧠 [TRUSTGRAPH COMMIT DEFERRED] ===")
        print("Warning: Could not connect to TrustGraph local cluster (Neo4j:7474).")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TrustGraph Cognitive Write Adapter")
    parser.add_argument("--run_id", required=True, help="Unique identifier for the AI run")
    parser.add_argument("--status", required=True, choices=['success', 'failed'], help="The outcome")
    parser.add_argument("--target", required=True, help="Module or File modified")
    parser.add_argument("--skills", required=True, help="Comma separated list of .agents skills used")
    parser.add_argument("--score", default="0.5", help="Confidence score 0.0 to 1.0")
    parser.add_argument("--reasoning", default="None", help="Why did the AI take this path?")
    parser.add_argument("--retry_of", default="", help="If this is a retry, what run ID did it branch from?")
    
    args = parser.parse_args()
    commit_to_graph(args.run_id, args.status, args.target, args.skills, args.score, args.reasoning, args.retry_of)
