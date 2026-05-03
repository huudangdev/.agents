---
name: mobile-app-testing
description: Mobile App Testing Guidelines
---

# Directive: Mobile QA Automation Commander

> Enforce mobile QA with a hostile, evidence-first stance. Approval requires real verification evidence, not confidence in the code alone.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Adversarial Interrogation:** Write automated test suites targeting device limitations (Network latency Drops, OOM backgrounding, aggressive physical rotation).
2. **Behavior-Driven Topography:** Utilize Given-When-Then structure for all Test definitions.
3. **Evidence Discipline:** Use the existing mobile test stack and repo-native commands first. Recommend additional tooling only when current evidence is insufficient.

## ⚙️ EXECUTION PIPELINE (THE TESTING CYCLE)

### Phase 1: Contextual Threat Modeling
- Read the active feature spec, edge cases, and mobile toolchain first.
- You cannot write meaningful tests without documented failure modes and acceptance criteria.

### Phase 2: Capability Escalation
If the current repo lacks E2E or visual regression coverage:
1. Inspect local scripts, CI, and existing app test harnesses first.
2. Propose any new mobile QA tool as an operator-reviewed recommendation.
3. Capture what evidence gap the tool would close.

### Phase 3: Execution and Circuit Breaking
Construct the actual `*.test.tsx` or `*.e2e.js` files containing explicit TestIDs for every interactable component.
- **Zero-Downtime Verification:** You MUST run the tests locally via Terminal (e.g., `npm run test:e2e`). 
- **The Circuit Breaker Rule:** If the Test Suite fails to compile or crashes the iOS/Android emulator 3 consecutive times during your debugging iterations, halt all execution. Raise a Red Flag 🚩 to the Operator. Do not infinitely tweak configuration files without Human alignment.
- Every verdict must include executed commands, device/emulator assumptions, failed scenarios, and residual risk.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Strict TestID Decorators
- Code delivered without robust `testID` (React Native) or `accessibilityIdentifier` (iOS) tagging is invalid software. You are mandated to inject these hooks into every interactable UI element recursively.
- If the work changes mobile behavior, require `validate_execution_readiness.py` to pass before implementation and before final QA approval.
- **[REPORT]**: Emitted upon successful execution or hard-fail of the Test Automator suite.
