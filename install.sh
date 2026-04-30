#!/usr/bin/env bash

# ANSI Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
MAGENTA='\033[0;35m'
NC='\033[0m' # No Color

echo -e "\n${CYAN}"
echo "================================================================="
echo "  🚀 ANTIGRAVITY COGNITIVE ENGINE V31.0 (MARCUS FLEET)           "
echo "  Enterprise Neural Scaffolder (Direct from Github)              "
echo "================================================================="
echo -e "${NC}\n"

TARGET_DIR=".agents"

if [ -d "$TARGET_DIR" ]; then
    echo -e "${YELLOW}⚠️  Directory '$TARGET_DIR' already exists. Aborting to prevent data loss.${NC}"
    echo -e "If you wish to upgrade, rename or delete the existing directory first."
    exit 1
fi

echo -e "📡 ${CYAN}Fetching Neural Schemas & RAG Workflows...${NC}"

# Temp storage
TMP_DIR=$(mktemp -d)
ZIP_URL="https://github.com/huudangdev/.agents/archive/refs/heads/main.zip"

curl -sL $ZIP_URL -o "$TMP_DIR/agents.zip"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to download from GitHub. Please check your internet connection.${NC}"
    rm -rf "$TMP_DIR"
    exit 1
fi

echo -e "📦 ${GREEN}Unpacking intelligence matrix...${NC}"
unzip -q "$TMP_DIR/agents.zip" -d "$TMP_DIR"

if [ ! -d "$TMP_DIR/.agents-main" ]; then
    echo -e "${RED}❌ Extraction failed. The zip file structure is unrecognizable.${NC}"
    rm -rf "$TMP_DIR"
    exit 1
fi

# Move the actual folder contents
mv "$TMP_DIR/.agents-main" "$TARGET_DIR"
rm -rf "$TMP_DIR"

# Clean up the script itself inside the scaffolded repo
rm -f "$TARGET_DIR/install.sh"
# Ensure python adapters are executable if applicable
chmod +x "$TARGET_DIR/adapters/trustgraph_query.py" 2>/dev/null
chmod +x "$TARGET_DIR/adapters/trustgraph_write.py" 2>/dev/null
chmod +x "$TARGET_DIR/scripts/sync_project_mcp.py" 2>/dev/null

echo -e "🔌 ${CYAN}Publishing project MCP configuration...${NC}"
if command -v python3 &> /dev/null; then
    python3 "$TARGET_DIR/scripts/sync_project_mcp.py" --root .
    echo -e "   ${GREEN}✔ Project MCP config synchronized to .mcp.json${NC}"
else
    echo -e "   ${YELLOW}⚠️ python3 not found. Skipping automatic MCP config sync.${NC}"
    echo -e "   Create ${GREEN}.mcp.json${NC} from ${GREEN}.agents/mcp/mcp.json${NC} manually."
fi

echo -e "\n${GREEN}✔ Neural Matrix successfully grafted into local repository!${NC}\n"

# ==========================================
# AUTO-BOOT TRUSTGRAPH (DOCKER)
# ==========================================
echo -e "🐳 ${CYAN}Checking Local Docker Environment...${NC}"

if command -v docker &> /dev/null; then
    echo -e "   Docker found. Igniting TrustGraph Memory Core (Neo4j, Postgres, ChromaDB)..."
    
    # Check for docker compose or docker-compose
    if docker compose version &> /dev/null; then
        DOCKER_CMD="docker compose"
    elif command -v docker-compose &> /dev/null; then
        DOCKER_CMD="docker-compose"
    else
        DOCKER_CMD=""
    fi

    if [ -n "$DOCKER_CMD" ]; then
        cd "$TARGET_DIR/trustgraph" || exit
        $DOCKER_CMD up -d
        cd ../../
        echo -e "   ${GREEN}✔ TrustGraph Subsystems are online!${NC}"
    else
        echo -e "   ${YELLOW}⚠️ Docker Compose was not found. Please start the TrustGraph manually:${NC}"
        echo -e "   $ cd .agents/trustgraph && docker-compose up -d"
    fi
else
    echo -e "   ${YELLOW}⚠️ Docker is not installed on this system. TrustGraph Memory Core will be constrained.${NC}"
    echo -e "   Please install Docker (https://docs.docker.com/get-docker/) to enable Long-Term Memory."
fi

echo -e "\n⚡ ${MAGENTA}NEXT STEPS FOR OPERATOR:${NC}"
echo -e " 1. ${CYAN}Acknowledge the Constitutional Directive:${NC}"
echo -e "    Review ${GREEN}.agents/.clinerules${NC} to understand your Multi-Agent ecosystem."
echo -e " 2. ${CYAN}Spawn the Fleet:${NC}"
echo -e "    Load the project in your favorite LLM Code Editor to natively inter-op with the agents.\n"
echo -e " 3. ${CYAN}Validate the governance layer:${NC}"
echo -e "    Run ${GREEN}python3 .agents/scripts/validate_specs.py${NC} after creating feature specs."
echo -e " 4. ${CYAN}During /develop:${NC}"
echo -e "    Keep ${GREEN}docs/development/${NC} and doc sync notes current with code changes."
echo -e " 5. ${CYAN}Use project MCP servers:${NC}"
echo -e "    ${GREEN}.mcp.json${NC} has been synchronized from ${GREEN}.agents/mcp/mcp.json${NC}."

echo -e "Enjoy your Autonomous Engineering Engine!\n"
