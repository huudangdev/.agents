#!/bin/bash

# Antigravity Enterprise: Sandboxed Command Execution Wrapper (V29.5)
# Provides a narrow allow-list executor for agent-generated validation commands.

set -uo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

if [ "$#" -eq 0 ]; then
    echo -e "${RED}[Security Fault] Missing arguments. Usage: ./run_sandboxed.sh \"npm run test\"${NC}"
    exit 1
fi

COMMAND_PAYLOAD="$*"

echo "[Sandbox Interceptor] Analyzing Payload: '$COMMAND_PAYLOAD'"

# This wrapper intentionally accepts only simple command argv. Shell grammar is
# rejected so execution never depends on eval, expansion, pipes, or redirects.
for metachar in ';' '&' '|' '<' '>' '`' '$' '(' ')' '{' '}' '[' ']' '*' '?' '!' '~'; do
    if [[ "$COMMAND_PAYLOAD" == *"$metachar"* ]]; then
        echo -e "${RED}[CIRCUIT BREAKER] Shell metacharacter '$metachar' is not permitted.${NC}"
        echo "Pass a single validation command without pipes, redirects, substitutions, or globs."
        exit 127
    fi
done

read -r -a ARGV <<< "$COMMAND_PAYLOAD"
if [ "${#ARGV[@]}" -eq 0 ]; then
    echo -e "${RED}[Security Fault] Empty command payload.${NC}"
    exit 1
fi

PROGRAM="${ARGV[0]}"
SUBCOMMAND="${ARGV[1]:-}"
SCRIPT_NAME="${ARGV[2]:-}"

is_allowed_command() {
    case "$PROGRAM" in
        npm)
            case "$SUBCOMMAND" in
                run)
                    case "$SCRIPT_NAME" in
                        build|dev|lint|test|typecheck|check|format) return 0 ;;
                    esac
                    ;;
                test|config|--version|-v) return 0 ;;
            esac
            ;;
        pnpm|yarn)
            case "$SUBCOMMAND" in
                run|test|build|dev|lint|typecheck|--version|-v) return 0 ;;
            esac
            ;;
        node)
            case "$SUBCOMMAND" in
                --version|-v) return 0 ;;
            esac
            ;;
        python|python3)
            case "$SUBCOMMAND" in
                --version|-V|-m) return 0 ;;
            esac
            ;;
        pytest|vitest|eslint|tsc|ruff|mypy|cargo|go)
            return 0
            ;;
    esac

    return 1
}

if ! is_allowed_command; then
    echo -e "${RED}[CIRCUIT BREAKER] Command is outside the validation allow-list.${NC}"
    echo "Allowed families: npm/pnpm/yarn validation scripts, node/python version checks, pytest/vitest/eslint/tsc/ruff/mypy/cargo/go."
    exit 127
fi

echo -e "${GREEN}[Audit Pass] Payload accepted by allow-list executor.${NC}"
echo "----------------------------------------------------"

"${ARGV[@]}"

EXIT_CODE=$?
echo "----------------------------------------------------"
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}[Sandbox] Compilation/Execution Pass (Exit 0)${NC}"
else
    echo -e "${RED}[Sandbox] Error Detected (Exit $EXIT_CODE)${NC}"
fi

exit $EXIT_CODE
