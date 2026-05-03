---
name: tailwindcss-mobile-first
description: Tailwind CSS Mobile First
---

# Directive: Tailwind Mobile First

> Use this skill to keep Tailwind-based UI consistent, mobile-first, and aligned with the existing token system.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Utility-First Precision:** Output `className` strings sequentially (Layout $\rightarrow$ Spacing $\rightarrow$ Typography $\rightarrow$ Colors). Disorganized Tailwind strings are algorithmic spam.
2. **Mobile Layout Supremacy:** Assume the hardware viewport is a mobile browser or WebView. Build the component vertically (Flex-Col) by default, switching to Row geometries only when the `md:` breakpoint demands.
3. **Utility Discipline:** Keep utility composition readable and consistent with the repo's current setup.

## ⚙️ EXECUTION PIPELINE (THE RESPONSIVE CYCLE)

### Phase 1: Contextual Emulation Checks
- Read the current Tailwind config, theme tokens, and active feature docs first.

### Phase 2: Layout Review
- Check responsive structure, token usage, class readability, and dynamic class composition.
- Recommend extra plugins only as operator-reviewed additions.

### Phase 3: The DOM Simulation
- **Zero-Downtime Verification:** You MUST physically verify the CSS classes via the local browser daemon (`localhost:3000`).
- **The Circuit Breaker Rule:** If the local Webpack/Vite server triggers compilation failures (`SyntaxError in globals.css`) 3 consecutive times, you MUST abort processing. Raise a Terminal Red Flag 🚩 for User investigation. Do not rewrite `tailwind.config.ts` infinitely.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Class Accumulation Strategy
- Use utility mergers (e.g., `clsx`, `tailwind-merge`) when computing dynamic variations of components to prevent CSS cascading conflicts.
- **[REPORT]**: Emitted upon delivery of the synchronized Tailwind React/Vue component.
