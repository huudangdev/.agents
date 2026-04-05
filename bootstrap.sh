#!/bin/bash
# =====================================================================
# ANTIGRAVITY BOOTSTRAP (V29.3) - Universal Portability Script
# =====================================================================

set -e # Exit immediately if a command exits with a non-zero status

# Color codes
CYAN='\033[0;36m'
FUCHSIA='\033[0;35m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}=================================================${NC}"
echo -e "${CYAN} 🌌 MARCUS FLEET ANTIGRAVITY COGNITIVE BOOTSTRAP ${NC}"
echo -e "${CYAN}=================================================${NC}"
echo ""

AGENTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$AGENTS_DIR")"

# 1. 🐳 DOCKER CHECK & STARTUP
echo -e "${YELLOW}[1/5] Initiating Docker Core (TrustGraph Containers)...${NC}"
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Error: Docker is not installed or not running.${NC}"
    exit 1
fi

cd "$AGENTS_DIR/trustgraph"
docker-compose up -d
echo -e "${GREEN}✔ Docker services online (Neo4j, Postgres, ChromaDB).${NC}"

# 2. 🐍 PYTHON VIRTUAL ENVIRONMENT
echo -e "\n${YELLOW}[2/5] Synthesizing Python Virtual Environment...${NC}"
cd "$AGENTS_DIR"

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "✔ Virtual environment created at .agents/venv"
else
    echo -e "✔ Virtual environment already exists."
fi

echo "Activating venv and installing requirements..."
source venv/bin/activate
pip install -r requirements.txt -q
echo -e "${GREEN}✔ Python Cognitive Modules installed.${NC}"

# 3. ⚛️ NEXT.JS DEPENDENCIES
echo -e "\n${FUCHSIA}[3/5] Bootstrapping React/Next.js 3D Viewer...${NC}"
if ! command -v npm &> /dev/null; then
    echo -e "${RED}Error: NPM is not installed.${NC}"
    exit 1
fi

cd "$AGENTS_DIR/trustgraph-viewer"
npm install --silent
echo -e "${GREEN}✔ 3D UI Engine verified.${NC}"

# 4. 🧠 AST & VECTOR INGESTION (THE KNOWLEDGE PUMP)
echo -e "\n${CYAN}[4/5] Pumping Knowledge Graph (AST & Vectors)...${NC}"
cd "$ROOT_DIR"
echo "-> Scanning AST (Neo4j)..."
"$AGENTS_DIR/venv/bin/python" "$AGENTS_DIR/adapters/trustgraph_ingest_all.py" --root .

echo "-> Generating Semantic Vectors (ChromaDB)..."
"$AGENTS_DIR/venv/bin/python" "$AGENTS_DIR/adapters/trustgraph_vectorize.py" --root .

echo -e "${GREEN}✔ Memory ingestion complete.${NC}"

# 5. 🚀 LIFTOFF
echo -e "\n${YELLOW}[5/5] Engine Ready.${NC}"
echo -e "${CYAN}=================================================${NC}"
echo -e "${GREEN}✅ BOOTSTRAP SUCCESSFUL!${NC}"
echo -e "Your project has been formally assimilated into the Marcus Fleet AI framework."
echo ""
echo -e "👉 ${YELLOW}To view the Cognitive Brain, run:${NC}"
echo -e "   cd .agents/trustgraph-viewer && npm run dev"
echo ""
echo -e "👉 ${FUCHSIA}AI Agents are now fully unleashed and capable of executing Vector RAG and AST Navigation.${NC}"
echo -e "${CYAN}=================================================${NC}"
