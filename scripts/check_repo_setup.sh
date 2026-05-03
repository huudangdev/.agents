#!/usr/bin/env bash

set -euo pipefail

ROOT="${1:-$(pwd)}"
ROOT="$(cd "$ROOT" && pwd)"
AGENTS_ROOT="$ROOT/.agents"
if [[ ! -d "$AGENTS_ROOT" ]]; then
  AGENTS_ROOT="$ROOT"
fi

status=0

check_file() {
  local path="$1"
  local label="$2"
  if [[ -f "$path" ]]; then
    echo "[OK] $label"
  else
    echo "[FAIL] $label: missing file at $path"
    status=1
  fi
}

check_contains() {
  local path="$1"
  local pattern="$2"
  local label="$3"
  if grep -Fq "$pattern" "$path"; then
    echo "[OK] $label"
  else
    echo "[FAIL] $label: pattern not found"
    status=1
  fi
}

echo "Checking Marcus Fleet repo setup..."

check_file "$ROOT/agents.md" "Root agents.md exists"
check_file "$AGENTS_ROOT/agents.md" "Legacy .agents/agents.md shim exists"
check_contains "$AGENTS_ROOT/agents.md" "../agents.md" "Legacy shim points to root agents.md"

check_file "$AGENTS_ROOT/mcp/mcp.json" "Bundled MCP config exists"
check_contains "$AGENTS_ROOT/mcp/mcp.json" "@playwright/mcp@latest" "Bundled MCP uses official Playwright MCP"
check_contains "$AGENTS_ROOT/mcp/mcp.json" "\"--headless\"" "Bundled MCP runs Playwright headless"

check_file "$ROOT/.mcp.json" "Project .mcp.json exists"
check_contains "$ROOT/.mcp.json" "@playwright/mcp@latest" "Project .mcp.json uses official Playwright MCP"

check_file "$AGENTS_ROOT/scripts/sync_project_mcp.py" "MCP sync script exists"
check_contains "$AGENTS_ROOT/scripts/sync_project_mcp.py" "refreshes managed server definitions" "MCP sync script includes refresh logic"

check_file "$AGENTS_ROOT/scripts/check_mcp_health.py" "MCP health script exists"
check_file "$AGENTS_ROOT/scripts/validate_execution_readiness.py" "Execution readiness validator exists"
check_file "$AGENTS_ROOT/scripts/validate_execution_brief_freshness.py" "Execution brief freshness validator exists"
check_file "$AGENTS_ROOT/scripts/validate_routing_regression.py" "Routing regression validator exists"
check_file "$AGENTS_ROOT/scripts/validate_command_surface.py" "Command surface validator exists"
check_file "$AGENTS_ROOT/scripts/validate_harness_contract.py" "Harness contract validator exists"
check_file "$AGENTS_ROOT/scripts/run_harness_preflight.py" "Harness preflight wrapper exists"
check_file "$AGENTS_ROOT/scripts/run_harness_postflight.py" "Harness postflight wrapper exists"
check_file "$AGENTS_ROOT/scripts/audit_feature_contracts.py" "Feature contract audit exists"

if [[ $status -eq 0 ]]; then
  echo "Marcus Fleet repo setup check passed."
else
  echo "Marcus Fleet repo setup check failed."
fi

exit "$status"
