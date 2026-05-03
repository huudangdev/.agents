---
description: Mobile Application Design & Engineering Protocol via Antigravity Mobile Design Doctrine.
---

# Mobile Engineering Protocol

> Use this workflow to initialize mobile-specific doctrine, architecture constraints, and verification expectations before proposing or changing mobile product work.

## Stage 1: Mobile Doctrine Synthesis
- Read the relevant local skill documents directly:
  - `mobile-design-doctrine`
  - `mobile-developer-standards`
  - `mobile-ios-design`
  - `mobile-android-design`
  - `mobile-touch-animations`
  - `react-native-architecture`
  - `flutter-architecture`
- Determine the framework recommendation based on platform constraints, offline behavior, team familiarity, and verification burden.

## Stage 2: UI Bootstrap and Design Rules
- Read the local skills covering visual system, mobile layout, and test strategy.
- Produce or update a mobile brand guideline artifact when the feature changes UI behavior.
- The guideline must define spacing, typography, safe-area behavior, interaction motion, and accessibility constraints.

## Stage 3: State Isolation and Readiness
- Break work into screen-level or flow-level scopes with explicit ownership and verification.
- Record the active mobile feature workspace under `.agents/specs/` and require it to pass:
  - `validate_specs.py`
  - `validate_execution_readiness.py`
- Update the root `agents.md` with the current mobile workstream status when the workflow materially changes direction.
