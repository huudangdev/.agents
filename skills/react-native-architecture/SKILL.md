---
name: react-native-architecture
description: React Native Architecture Standard
---

# Directive: React Native Architecture

> Use this skill to shape React Native architecture decisions with attention to state, native boundaries, performance, and verification cost.

## 🎯 MISSION (CORE OBJECTIVES)
1. **The New Architecture (Fabric):** Map topologies that bypass the legacy asynchronous JSON bridge. Utilize synchronous JSI where hardware performance is mandated.
2. **Deterministic State Containers:** Enforce rigid predictable state transitions utilizing Zustand, Redux Toolkit, or Jotai. Prop-drilling deeper than 2 layers is an architectural flaw.
3. **Architecture Discipline:** Prefer repo-native patterns and the current stack before suggesting new packages or native modules.

## ⚙️ EXECUTION PIPELINE (THE RN CYCLE)

### Phase 1: Contextual Emulation Checks
- Read the active feature docs, current mobile architecture, and app configuration first.
- Do not propose new state or native patterns without checking what the repo already uses.

### Phase 2: Architecture Review
- Check state ownership, bridge/native boundaries, offline behavior, and cleanup around subscriptions or listeners.
- Recommend new dependencies only as operator-reviewed additions.

### Phase 3: Hardware Diagnostics & CI
Enforce the following coding disciplines:
- **Memory Leak Protection:** All React Native `useEffect` hooks must explicitly return cleanup functions to unmount listeners.
- **Circuit Breaker Rule:** If the local build (`npx react-native run-ios` / `npm run dev`) throws the exact same dependency collision or Podspec error 3 consecutive times, you MUST abort processing. Raise a Red Flag 🚩 to the Operator for manual intervention. Do not endlessly wipe the `DerivedData` cache.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Zero-Downtime Rule 
- Any code provided to the Operator must be accompanied by explicit terminal checks. You do not just write code; you command the Operator to physically test it via `npm run ios` or equivalent command runners.
- If the work changes app behavior, require execution-readiness validation before implementation starts.
- **[REPORT]**: Emitted upon delivery of the hardened mobile source-code module.
