---
name: mobile-developer-standards
description: Mobile Dev Standards
---

# Directive: Mobile Developer Standards

> Use this skill to enforce mobile code standards that preserve responsiveness, offline resilience, and safe platform integration.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Thread Sanctity:** Strict segregation of the JS Thread (React Native) from the Native UI Thread. Prevent massive payload serializations over the JSON Bridge by enforcing JSI (JavaScript Interface) where applicable.
2. **Offline-First Resilience:** App architecture must not crash when placed into Airplane mode. Persist necessary states locally (e.g., MMKV, WatermelonDB, SQLite) to enable optimistic mutations.
3. **Standards Discipline:** Keep standards grounded in the actual mobile stack and the app's verification requirements.

## ⚙️ EXECUTION PIPELINE (THE MOBILE LIFECYCLE)

### Phase 1: Contextual Emulation Checks
- Read the active feature docs and current app configuration first.
- Match recommendations to the real mobile stack in use.

### Phase 2: Standards Review
- Check thread usage, offline behavior, persistence, cleanup, and native boundary safety.
- Recommend new packages only as operator-reviewed additions.

### Phase 3: Hardware Diagnostics & CI
Enforce the following coding disciplines:
- **Memory Leak Protection:** All React Native `useEffect` hooks must explicitly return cleanup functions to unmount listeners.
- **Circuit Breaker Rule:** If the local build (`npx react-native run-ios` / `npm run dev`) throws the exact same dependency collision or Podspec error 3 consecutive times, you MUST abort processing. Raise a Red Flag 🚩 to the Operator for manual intervention. Do not endlessly wipe the `DerivedData` cache.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Zero-Downtime Rule 
- Any code provided to the Operator must be accompanied by explicit terminal checks. You do not just write code; you command the Operator to physically test it via `npm run ios` or equivalent command runners.
- If the work changes app behavior, require execution-readiness validation before implementation starts.
- **[REPORT]**: Emitted upon delivery of the hardened mobile source-code module.
