#!/usr/bin/env bash

# ANSI Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "\n${CYAN}"
echo "================================================================="
echo "  🔄 ANTIGRAVITY OTA UPDATE PROTOCOL                             "
echo "  Synchronizing Cognitive Fleet, Specs, and TrustGraph Schemas   "
echo "================================================================="
echo -e "${NC}\n"

TARGET_DIR=".agents"

if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}❌ Directory '$TARGET_DIR' not found. You must run this command at the root of an initialized repository.${NC}"
    exit 1
fi

echo -e "📡 ${CYAN}Fetching Global Brain Updates...${NC}"

# Temp storage
TMP_DIR=$(mktemp -d)
ZIP_URL="https://github.com/huudangdev/.agents/archive/refs/heads/main.zip"

curl -sL $ZIP_URL -o "$TMP_DIR/agents.zip"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to download from GitHub. Please check your internet connection.${NC}"
    rm -rf "$TMP_DIR"
    exit 1
fi

echo -e "📦 ${GREEN}Unpacking intelligence matrices...${NC}"
unzip -q "$TMP_DIR/agents.zip" -d "$TMP_DIR"

if [ ! -d "$TMP_DIR/.agents-main" ]; then
    echo -e "${RED}❌ Extraction failed. The zip file structure is unrecognizable.${NC}"
    rm -rf "$TMP_DIR"
    exit 1
fi

echo -e "🧬 ${YELLOW}Merging DNA (Non-Destructive Rsync)...${NC}"

# Ensure rsync is available
if ! command -v rsync &> /dev/null; then
    echo -e "${YELLOW}⚠️ rsync not found! Falling back to standard copy. WARNING: This may overwrite local config files!${NC}"
    cp -R "$TMP_DIR/.agents-main/"* "$TARGET_DIR/"
else
    # Core OTA Rsync Logic. Preserve local memory, runtime data, and operator secrets.
    rsync -av --exclude='agents.md' \
              --exclude='trustgraph/data/' \
              --exclude='trustgraph/.env' \
              --exclude='trustgraph.env' \
              "$TMP_DIR/.agents-main/" "$TARGET_DIR/" > /dev/null
fi

# Clean up
rm -rf "$TMP_DIR"

# Ensure python adapters are executable if applicable
chmod +x "$TARGET_DIR/adapters/trustgraph_query.py" 2>/dev/null
chmod +x "$TARGET_DIR/adapters/trustgraph_write.py" 2>/dev/null

echo -e "\n${GREEN}✔ Update Complete! Fleet intelligence upgraded while preserving local memory via agents.md.${NC}\n"
