---
name: tailwindcss-mobile-first
description: Tailwind CSS Mobile First
---

# 🧠 DIRECTIVE: Tailwind Architecture & Layout Engine (Enterprise Standard)

> **ENTERPRISE MANDATE:**  
> You compile the raw constraints of UI construction using the TailwindCSS Mobile-First doctrine. Every responsive node must inherently adapt from $\le 375px$ widths. Desktop layouts (`md:`, `lg:`) are exclusively downstream adaptations. Overwriting inline-styles in violation of the PostCSS pipeline is strictly forbidden.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Utility-First Precision:** Output `className` strings sequentially (Layout $\rightarrow$ Spacing $\rightarrow$ Typography $\rightarrow$ Colors). Disorganized Tailwind strings are algorithmic spam.
2. **Mobile Layout Supremacy:** Assume the hardware viewport is a mobile browser or WebView. Build the component vertically (Flex-Col) by default, switching to Row geometries only when the `md:` breakpoint demands.
3. **Open Ecosystem Integration (The `find-skills` Protocol):** Dynamically traverse the `skills.sh` registry to inject UI plugins natively (e.g., Headless UI, Shadcn/ui Tailwind config auto-integrators).

## ⚙️ EXECUTION PIPELINE (THE RESPONSIVE CYCLE)

### Phase 1: Contextual Emulation Checks
- **Anti-Amnesia Protocol:** Execute `view_file` to ingest `package.json` and `tailwind.config.ts`. You must adhere strictly to the project's pre-configured hex palettes and typography tokens (`font-sans`, `bg-primary`).

### Phase 2: Open-Ecosystem Augmentation (`skills.sh`)
If directed to scaffold complex layout logic (e.g., "Find a skill for Tailwind Forms" or "How to animate with Tailwind plugins?"):
1. Execute Terminal: `npx skills find tailwind-plugins` or `npx skills find css-animations`.
2. Extract the authoritative ecosystem plugin ($>1K$ installs).
3. Transmit the installation script `npx skills add [package] -g -y` to the Operator.

### Phase 3: The DOM Simulation
- **Zero-Downtime Verification:** You MUST physically verify the CSS classes via the local browser daemon (`localhost:3000`).
- **The Circuit Breaker Rule:** If the local Webpack/Vite server triggers compilation failures (`SyntaxError in globals.css`) 3 consecutive times, you MUST abort processing. Raise a Terminal Red Flag 🚩 for User investigation. Do not rewrite `tailwind.config.ts` infinitely.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Class Accumulation Strategy
- Use utility mergers (e.g., `clsx`, `tailwind-merge`) when computing dynamic variations of components to prevent CSS cascading conflicts.
- **[REPORT]**: Emitted upon delivery of the synchronized Tailwind React/Vue component.
