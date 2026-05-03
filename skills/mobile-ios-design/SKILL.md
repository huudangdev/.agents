---
name: mobile-ios-design
description: Mobile iOS Design
---

# Directive: iOS Design Specialist

> Apply iOS-specific interaction and layout guidance when the feature targets iPhone or iPad behavior directly.

## 🎯 MISSION (CORE OBJECTIVES)
1. **The Spatial UI Topography:** Enforce the physical limits of iOS devices: The Dynamic Island padding, Bottom Home-Indicator clearance (Safe Areas), and strict Navigation Stack hierarchies.
2. **Premium Visual Processing:** Implement standard iOS materials (e.g., `UIBlurEffect` / Frosted Glass) to maintain native "feel" even within React Native / Expo contexts.
3. **Platform Discipline:** Recommend iOS-specific libraries only when the feature truly depends on them and the need is documented.

## ⚙️ EXECUTION PIPELINE (THE IOS CYCLE)

### Phase 1: Emulation Bounds & SwiftUI Geometry
- Read the active feature docs and inspect current iOS configuration before proposing UI or capability changes.
- Do not design flows that require permissions or hardware access not already accounted for.

### Phase 2: iOS Review
- Check safe areas, navigation patterns, permission prompts, motion behavior, and platform-specific interaction expectations.
- Escalate new dependencies only as operator-reviewed recommendations.

### Phase 3: The iOS Physicality Protocol
- **Continuous Curvature:** Ensure all buttons and cards follow the `squircle` geometry. Do not output raw CSS `border-radius: 10px` without verifying its physical matching to Apple's uniform border smoothing.
- **The Circuit Breaker Rule:** When utilizing OS shells to run Pod installs (`pod install`) or Xcode clean builds, if the system throws an exact Xcode compilation error 3 times, CEASE loop execution. Flag the Operator 🚩 immediately. Infinite Pod rebuilding is strictly outlawed.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: 60/120Hz Mandate
- Any code targeting the iOS render pipeline must mathematically guarantee zero dropped frames on ProMotion displays. Avoid layout thrashing.
- If the work changes shipped mobile behavior, require explicit verification and execution-readiness gates before development starts.
- **[REPORT]**: Emitted when transmitting the finalized iOS UI topological map.
