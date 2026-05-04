#!/bin/bash

# Antigravity Enterprise Bootstrapper (V29.4)
# Configures Git hooks for mandatory docs gates and incremental delta sync.

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
HOOK_DIR="$ROOT_DIR/.git/hooks"
POST_COMMIT_FILE="$HOOK_DIR/post-commit"
PRE_COMMIT_FILE="$HOOK_DIR/pre-commit"
PRE_PUSH_FILE="$HOOK_DIR/pre-push"

echo -e "${BLUE}=== Antigravity Enterprise Git Hooks Setup ===${NC}"

if [ ! -d "$ROOT_DIR/.git" ]; then
    echo "Error: Not a git repository. Run this at the root of a Git Project."
    exit 1
fi

cat << 'EOF' > "$PRE_COMMIT_FILE"
#!/bin/bash
# Marcus Fleet Mandatory Docs Gate
set -e

CHANGED_FILES=$(git diff --cached --name-only --diff-filter=ACMR)

if echo "$CHANGED_FILES" | grep -Eq '^(docs/|\.agents/specs/|\.agents/workflows/|\.agents/scripts/|README\.md|USAGE_GUIDE\.md|SLASH_COMMAND_REGISTRY\.md|agents\.md)'; then
    echo "[Marcus Fleet] Running mandatory docs gates before commit..."
    python3 .agents/scripts/run_required_docs_gates.py --root . --mode auto
    python3 .agents/scripts/validate_command_surface.py --root .
fi

if echo "$CHANGED_FILES" | grep -Ev '^(docs/|\.agents/|README\.md|USAGE_GUIDE\.md|SLASH_COMMAND_REGISTRY\.md|agents\.md|.*\.md$)' | grep -q .; then
    echo "[Marcus Fleet] Source-like changes detected; requiring development docs closeout..."
    python3 .agents/scripts/run_required_docs_gates.py --root . --mode execution --require-development-docs
fi
EOF

cat << 'EOF' > "$PRE_PUSH_FILE"
#!/bin/bash
# Marcus Fleet Mandatory Closeout Gate
set -e

echo "[Marcus Fleet] Running mandatory postflight/docs gates before push..."
python3 .agents/scripts/run_required_docs_gates.py --root . --mode auto
python3 .agents/scripts/validate_command_surface.py --root .

CHANGED_SINCE_UPSTREAM=$(git diff --name-only @{upstream}...HEAD 2>/dev/null || true)
if echo "$CHANGED_SINCE_UPSTREAM" | grep -Ev '^(docs/|\.agents/|README\.md|USAGE_GUIDE\.md|SLASH_COMMAND_REGISTRY\.md|agents\.md|.*\.md$)' | grep -q .; then
    echo "[Marcus Fleet] Source-like commits detected; requiring development docs closeout..."
    python3 .agents/scripts/run_required_docs_gates.py --root . --mode execution --require-development-docs
fi
EOF

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

chmod +x "$PRE_COMMIT_FILE" "$PRE_PUSH_FILE" "$POST_COMMIT_FILE"

echo -e "${GREEN}✓ Mounted mandatory docs gates into .git/hooks/pre-commit${NC}"
echo -e "${GREEN}✓ Mounted mandatory closeout gates into .git/hooks/pre-push${NC}"
echo -e "${GREEN}✓ Successfully mounted Incremental Delta Sync into .git/hooks/post-commit${NC}"
echo -e "Every commit/push now runs local gate scripts before Git accepts the action."
