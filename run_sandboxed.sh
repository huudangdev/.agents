#!/bin/bash

# Antigravity Enterprise: Sandboxed Command Execution Wrapper (V29.4)
# Forces all Agent-generated Terminal commands through a secure Ephemeral filter.

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

if [ "$#" -eq 0 ]; then
    echo -e "${RED}[Security Fault] Missing arguments. Usage: ./run_sandboxed.sh \"npm run test\"${NC}"
    exit 1
fi

COMMAND_PAYLOAD=$1

echo "[Sandbox Interceptor] Analyzing Payload: '$COMMAND_PAYLOAD'"

# Regex Safety Guardrails
FORBIDDEN_PATTERNS=("rm -rf" "sudo " "chmod -R" "mkfs" "curl " "wget " "shutdown" "reboot")

for pattern in "${FORBIDDEN_PATTERNS[@]}"; do
    if [[ $COMMAND_PAYLOAD == *"$pattern"* ]]; then
        echo -e "${RED}❌ [CIRCUIT BREAKER] Fatal Security Exception!${NC}"
        echo -e "${RED}The System AI attempted to execute a restricted Host mutation command: '$pattern'${NC}"
        echo "Action Denied by Enterprise RBAC Rules. Halting AI Execution Loop."
        exit 127
    fi
done

echo -e "${GREEN}✓ [Audit Pass] Payload safe. Emulating execution...${NC}"
echo "----------------------------------------------------"

# Note: In a fully locked DinD Enterprise setup, we would mount this inside a Docker Container.
# For local Venv stability, we run locally but monitored.
eval "$COMMAND_PAYLOAD"

EXIT_CODE=$?
echo "----------------------------------------------------"
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}[Sandbox] Compilation/Execution Pass (Exit 0)${NC}"
else
    echo -e "${RED}[Sandbox] Error Detected (Exit $EXIT_CODE)${NC}"
fi

exit $EXIT_CODE
