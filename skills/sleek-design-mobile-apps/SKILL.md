---
name: sleek-design-mobile-apps
description: Sleek Mobile Design
---

# Directive: Sleek Mobile Design

> Use this skill for premium mobile visual polish only when the underlying layout, flow, and accessibility are already sound.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Premium Optics (Glass & Shadow):** Enforce multi-layered Box Shadows (`ambient` and `directional` depth) alongside pure iOS/Android Frosted Glass filters to provide premium UI depth.
2. **Typography Geometry:** Strictly demand Geometric Sans-Serifs (e.g., Inter, SF Pro, Roboto) adhering to rigid Line-Height to Font-Size ratios ($> 1.4$).
3. **Polish Discipline:** Visual polish must serve readability, hierarchy, and touch ergonomics.

## ⚙️ EXECUTION PIPELINE (THE SLEEK CYCLE)

### Phase 1: Emulation & Visual Sync 
- Read the active mobile design docs and constraints before changing visual style.

### Phase 2: Polish Review
- Check hierarchy, spacing, contrast, hit bounds, and platform feel.
- Recommend extra styling tooling only as operator-reviewed additions.

### Phase 3: The Zero-Downtime Rule
- Do not output hypothetical UI structures. Ensure every component block is verified locally on `npm run dev` or the iOS/Android simulator.
- **The Circuit Breaker Rule (Style Compile Error):** If tailwind/CSS modules output PostCSS compiling crashes 3 consecutive times, ABORT. Raise a Terminal Red Flag 🚩 to the Operator.

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Ouch-less Hit Bounds
- High luxury UI must never frustrate the Operator's physical touch. A "Sleek" button must look minimal but command an invisible `hitSlop` of `44px x 44px` minimum.
- **[REPORT]**: Emitted upon completing the Premium Component CSS/StyleSheet output.
