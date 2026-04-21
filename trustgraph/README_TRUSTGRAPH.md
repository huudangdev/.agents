# 🧠 The TrustGraph Memory Engine

This directory houses the Local GraphRAG Infrastructure explicitly engineered for the **Antigravity `.agents` Ecosystem**.

Unlike legacy static prompt structures, Antigravity uses TrustGraph as its absolute "Long-Term Cognitive Core". This means every architectural refactor, every encountered bug, and every User workflow preference is written physically into a Graph/Vector intersection.

## 🚀 Initialization Matrix

This Docker stack mimics the Enterprise-grade TrustGraph pipeline (Postgres + Neo4j + VectorDB) natively onto your local machine or active workspace server.

### 1. Boot the Brain Clusters
Navigate to this directory and raise the daemon:
```bash
cd .agents/trustgraph
docker-compose up -d
```

For non-default credentials, copy `.agents/trustgraph.env.example` to `.agents/trustgraph.env`,
edit the values, then run `.agents/bootstrap.sh` or pass the env file to Docker Compose.

### 2. Service Endpoints
Once booted, the infrastructure listens natively:
- **Neo4j (The Graph Router):** `http://localhost:7474` (Bolt: `7687`) - *Credential: neo4j / trustgraph_secret*
- **Postgres (The State Indexer):** `http://localhost:5432` - *Credential: trustgraph / trustgraph_secret*
- **ChromaDB (The Vector RAG):** `http://localhost:8800`

The Python adapters share one runtime configuration module:
- `NEO4J_USER`, `NEO4J_PASSWORD`, `NEO4J_URI`
- `TRUSTGRAPH_NEO4J_HTTP_ENDPOINT`
- `CHROMA_HOST`, `CHROMA_PORT`, `CHROMA_COLLECTION`

### 3. How Antigravity Agents Use It
You do NOT interact with this raw database manually. The Antigravity Agents will automatically leverage two compiled Python adapters located in `.agents/adapters/`:
- `trustgraph_query.py`: Executed by Orchestrators (`marcus`, `sophia`) BEFORE making plans, extracting your historical coding styles (Naming conventions, preferred architectural plugins).
- `trustgraph_write.py`: Executed by Executors (`benny`, `improve-codebase`) AFTER successfully modifying the AST, syncing the `[Module] --fixes--> [Bug]` edges directly into the Graph.

> **WARNING:** Deleting the Docker volumes (`neo4j_data`, `chromadb_data`) irreversibly wipes the AI's learned intelligence concerning your project patterns. Backup the volume payloads routinely.
