---
name: ui-mobile-bootstrap
description: UI Mobile Bootstrap
---

# Directive: Mobile UI Bootstrap

> Use this skill to scaffold mobile UI only after routing, tokens, and feature scope are already documented.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Instant Application Scaffolding:** Generate Navigation topologies (Bottom Tabs, Stack Routers, Drawers) immediately mirroring the `screen_map.md` specifications.
2. **Standardized Base Tokens:** Output fully functional, cross-platform Base Components (`<Box>`, `<Text>`, `<Button>`) wrapped in Theme contexts instantly.
3. **Scaffold Discipline:** Bootstrap only the minimum shell needed for the documented screens and flows.

## ⚙️ EXECUTION PIPELINE (THE BOOTSTRAP CYCLE)

### Phase 1: Contextual Emulation Checks
- Read the active feature docs, routing plan, and mobile design constraints before scaffolding.
- Do not build routes or screens that exceed the documented scope.

### Phase 2: Scaffold Review
- Check route structure, base components, token usage, and testability.
- Recommend new generators only if the current repo cannot support the documented bootstrap path.

### Phase 3: Immediate Compilation Testing
Enforce the following Execution laws:
- **Zero-Downtime Rendering:** Output the code, but you MUST demand the local OS Terminal run the bundler (`npx expo start`) to verify the React Node tree doesn't immediately crash.
- **The Circuit Breaker Rule:** If the local scaffold throws Metro Bundler resolution errors (Missing Babel plugins or Unregistered Views) 3 consecutive times, STOP. Raise a Terminal 🚩 to alert the Human Operator. Infinite dependency caching is prohibited.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Drop-In Component Fidelity
- Never drop a half-finished component (`// Add styling here`). A bootstrapped screen must compile into a pixel-perfect, interactive React application.
- If the bootstrap changes shipped behavior, require execution-readiness validation before implementation starts.
- **[REPORT]**: Emitted upon completing the entire App Component tree bootstrap.
