---
name: mobile-touch-animations
description: Mobile Touch Animations
---

# Directive: Mobile Touch Animations

> Use this skill for touch motion that improves feedback, state communication, and mobile feel without harming usability.

## 🎯 MISSION (CORE OBJECTIVES)
1. **Mathematical Interpolation:** Translate Scroll Offsets and Pan Gesture velocity vectors into 60-120fps UI state translations. 
2. **Spring Physics Over Easing:** Ban simplistic CSS linear/ease-in transitions for physical components (e.g., Bottom Sheets, Carousels). Force the use of Spring mass/stiffness models.
3. **Motion Discipline:** Prefer the current mobile motion stack and only escalate when a real interaction need exists.

## ⚙️ EXECUTION PIPELINE (THE KINETIC CYCLE)

### Phase 1: Touch Topography
- Inspect the current package/tooling choice and the target interaction before proposing motion.

### Phase 2: Motion Review
- Check latency, interruptibility, reduced-motion handling, and hit-target safety.
- Recommend extra animation tooling only as operator-reviewed additions.

### Phase 3: Execution of the Physics Model
Construct strictly separated Animation Hooks.
- **The Zero-Downtime Test:** Never push a complex SVG path animation or Shared Transition without forcing the Operator to run `npm run dev` to physically watch it render. Stuttering code is invalid code.
- **The Circuit Breaker Rule:** If the local build logic throws Native Thread collisions (e.g. `Reanimated.worklet` exceptions) 3 consecutive times, you MUST abort execution loop. Raise a terminal Red Flag 🚩 for User arbitration. 

## 🛡️ MANDATORY PROTOCOLS (ENTERPRISE BOUNDARIES)
### Protocol 1: Spatial Awareness (Hit Slops)
- Animation targets must retain clickable areas even when scaling down (`scale: 0.95` on press). A shrinking element must deploy a hit-slop expansion matrix to remain responsive to clumsy fingers.
- **[REPORT]**: Emitted upon successfully wiring the Animation Hook structure to the parent Component.
