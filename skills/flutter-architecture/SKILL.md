---
name: flutter-architecture
description: Flutter Architecture Standard
---

# Directive: Flutter Architecture

> Use this skill for Flutter architecture, state, and performance decisions grounded in the actual app structure and verification needs.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Isolate Segregation:** Heavy algorithmic payloads JSON serialization MUST be explicitly routed outside the main UI thread via Dart `Isolates` / `compute()`. 
2. **Decoupled Architecture (Clean Architecture):** Enforce rigid layered bounds: Presentation (Widgets) $\rightarrow$ Domain (Use Cases) $\rightarrow$ Data (Repositories).
3. **Architecture Discipline:** Prefer the repo's current state and tooling choices before suggesting new frameworks or packages.

## ⚙️ EXECUTION PIPELINE (THE DART CYCLE)

### Phase 1: Emulation & State Sync
- Read the active feature docs and current Flutter config before proposing changes.
- Match the recommendation to the actual package and state-management choices already in use.

### Phase 2: Architecture Review
- Check isolate usage, async boundaries, widget structure, and offline/error behavior.
- Recommend new packages only as operator-reviewed additions.

### Phase 3: The Zero-Downtime Loop
- **The Physical Emulation Rule:** You MUST physically verify the widget trees via local command chains (`flutter build web` or `flutter analyze`). 
- **The Circuit Breaker Rule (Dependency Collision):** If the OS shell throws standard `pub get` resolution collisions (e.g., conflicting Kotlin versions in `android/build.gradle`) 3 consecutive times, you MUST abort processing. Flag the Terminal Error 🚩. Infinite Gradle wiping is banned.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Constant Expressions (Const)
- The Dart compiler is optimized for `const` trees. Any pure widget that does not physically mutate MUST be prefixed with `const`. Omitting `const` triggers unnecessary GC (Garbage Collection).
- If the work changes app behavior, require execution-readiness validation before implementation starts.
- **[REPORT]**: Emitted upon generating the Flutter Dart Component or Architecture map.
