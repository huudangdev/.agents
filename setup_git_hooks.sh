#!/bin/bash

# Antigravity Enterprise Bootstrapper (V29.4)
# Configures the Git Post-Commit hook for Incremental Delta Syncronization

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

HOOK_DIR="../.git/hooks"
POST_COMMIT_FILE="$HOOK_DIR/post-commit"

echo -e "${BLUE}=== Antigravity Enterprise Git Hooks Setup ===${NC}"

if [ ! -d "../.git" ]; then
    echo "Error: Not a git repository. Run this at the root of a Git Project."
    exit 1
fi

cat << 'EOF' > "$POST_COMMIT_FILE"
#!/bin/bash
# Antigravity Auto-Delta Sync Hook

# Get list of modified/added files in the last commit
CHANGED_FILES=$(git diff-tree -r --name-only --no-commit-id HEAD)

# Filter out deleted files and node_modules
FILES_TO_SYNC=""
for file in $CHANGED_FILES; do
    if [ -f "$file" ] && [[ "$file" != *"node_modules"* ]] && [[ "$file" != *".agents/chroma_db"* ]]; then
        FILES_TO_SYNC="$FILES_TO_SYNC $file"
    fi
done

if [ -n "$FILES_TO_SYNC" ]; then
    echo "⚙️ [Antigravity] Intercepting Git Commit: Syncing $FILES_TO_SYNC to Cognitive Matrix."
    
    # Use the isolated Venv to run the python script
    if [ -f ".agents/venv/bin/python" ]; then
        .agents/venv/bin/python .agents/adapters/trustgraph_incremental.py --files $FILES_TO_SYNC
    else
        echo "⚠️ Antigravity Venv not found. Skipping RAG sync."
    fi
fi
EOF

chmod +x "$POST_COMMIT_FILE"

echo -e "${GREEN}✓ Successfully mounted Incremental Delta Sync into .git/hooks/post-commit${NC}"
echo -e "Every 'git commit' will now automatically update Neo4j and ChromaDB transparently."
