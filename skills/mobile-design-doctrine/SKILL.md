---
name: mobile-design-doctrine
description: Mobile Design Doctrine
---

# Directive: Mobile UX Doctrine

> Define how mobile interfaces should feel, move, and recover under real constraints. Keep recommendations tied to platform capabilities, safe interaction patterns, and documented product flows.

## 🎯 MISSION (CORE OBJECTIVES)
1. **The Physics of Interactivity:** Ensure absolute fluidity at 60/120 FPS. Eradicate layout shifts (CLS), jank, and asynchronous UI freezes.
2. **Gesture-Driven Epistemology:** Screens must respond to physical thumb-swipes (Pan, Pinch, Pull-to-Refresh) rather than relying exclusively on discrete Button taps.
3. **Execution Governance:** Favor the current stack and existing motion primitives first. Recommend additional libraries only when the feature requirements justify them and the operator can review the tradeoff.

## ⚙️ EXECUTION PIPELINE (THE DOCTRINE CYCLE)

### Phase 1: Interaction Ingestion
- Read the root `agents.md`, the active feature workspace, and any existing mobile screen maps before shaping interactions.
- Do not propose a touch flow without mapping state transitions and failure states.

### Phase 2: Capability Escalation
If gesture, motion, or haptic requirements exceed the current stack:
1. Inspect the repo and local skills first.
2. Propose any new library as an operator-reviewed recommendation.
3. Record the expected UX gain, platform risk, and verification burden.

### Phase 3: The Haptic & Spatial Ruleset
Enforce the following Doctrine onto the `benny-frontend-engineer` or Mobile Developer:
- **Rule of Thumb (Physical Reach):** Primary navigation and critical CTA (Call To Action) endpoints MUST reside in the bottom 40% of the screen geometry.
- **Optimistic State Updates:** The UI must visually execute the User's command *before* the server mathematically confirms it in order to maintain psychological velocity. If the API fails, gracefully rollback via a Snackbar notification.
- **Zero-Downtime & Circuit Breaker:** Any mobile logic update must pass the local compilation (`npm run android` or `npm run ios`) test. If Metro/Xcode crashes 3 consecutive times, abort the fix-loop to prevent infinite context spam and alert the Operator.
- Record which screens, gestures, and motion behaviors require explicit QA coverage.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: The "Jank" Prohibition
- The use of unoptimized React dependencies (e.g., executing heavy animations on the JS Thread instead of the Native UI Thread) is strictly forbidden. Force the utilization of Hooks like `useSharedValue` overlaid with `runOnUI`.
- If the change affects shipped mobile behavior, require execution-readiness validation before implementation starts.
- **[REPORT]**: Emitted when delivering the Mobile Strategy matrix.
