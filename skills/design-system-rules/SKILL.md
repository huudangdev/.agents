---
name: design-system-rules
description: Figma Design System Rules
---

# Directive: Design System Rules

> Keep the design system coherent, reusable, and understandable. This skill exists to reduce drift, not to impose decorative complexity.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Mathematical UI Constraints:** Bind every margin, padding, and layout component to a mathematically derived Design Token (e.g., `spacing.4` = 16px).
2. **Atomic Abstraction:** Deconstruct UI into Atoms, Molecules, Organisms, and Templates. Do not permit "Spaghetti UI" where arbitrary inline styles are deployed.
3. **Token Discipline:** Prefer stable tokens and existing primitives over introducing new layers of abstraction.

## ⚙️ EXECUTION PIPELINE (THE TOKENS CYCLE)

### Phase 1: Contextual Constraint Extraction
- Read the active feature docs and the current design token source before making rules.
- Do not change tokens or primitives without understanding where they are already used.

### Phase 2: System Review
- Check spacing, typography, color, elevation, and component reuse.
- Recommend new libraries or primitives only as operator-reviewed additions.

### Phase 3: Token Synchronization
When outputting Component specs or CSS rules:
- NEVER output arbitrary magic numbers (e.g., `margin-top: 17px;`). It MUST be `16px` or `20px`.
- Enforce strict `CSS Variables` for theming (Dark/Light mode toggles).
- **Zero-Downtime Rule:** Your proposed CSS must compile locally without throwing PostCSS warnings. The Circuit Breaker triggers if 3 consecutive compilations fail.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: The Glassmorphism Directive
- Premium styling is optional. Consistency, readability, and accessibility are mandatory.
- **[REPORT]**: Emitted upon successful delivery of the Component Code or Design Token map.
