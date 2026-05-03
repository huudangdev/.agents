# Feature Specification: Refactor Planning Toolchain Gate

> Feature ID: `017-refactor-planning-toolchain-gate`
> Created: `2026-05-03`
> Status: Draft
> Source Prompt: Continue hardening `/refactor-planning` so any model can follow it deterministically; add an explicit toolchain prerequisite gate and wire it into the validated command surface.

## 1. Purpose

`/refactor-planning` is intentionally runtime-heavy: it calls `npx`, TypeScript,
ESLint, and a dev server. In practice, a large fraction of failures are
avoidable prerequisite issues (missing Node toolchain, missing ESLint). When
these fail late, the model tends to improvise or widen scope.

This feature adds a deterministic local toolchain gate that fails fast and
names the exact missing prerequisite. The gate is designed to be safe: it does
not execute the refactor runtime, it only verifies that the required
executables exist and that ESLint is available either globally or via local
`node_modules/.bin`.

## 2. User Stories

- [x] As an operator, I want `/refactor-planning` to fail early when the local
      toolchain is not ready so that the model does not waste time or improvise.
- [x] As an implementation model, I want `/refactor-planning` to name the exact
      prerequisite gate and where it runs so the command is deterministic.
- [x] As a governance maintainer, I want README, `USAGE_GUIDE.md`, registry, and
      workflow to stay aligned with the toolchain gate via command-surface
      validation.

## 3. Functional Requirements

- `FR-001`: The system MUST provide a local toolchain validator for
  `/refactor-planning` that checks `node`, `npm`, and `npx` are available in
  `PATH` for the target project root.
- `FR-002`: The toolchain validator MUST fail when ESLint is unavailable, where
  "available" means either `eslint` is in `PATH` or
  `<root>/node_modules/.bin/eslint*` exists.
- `FR-003`: `/refactor-planning` workflow MUST run the toolchain validator
  before calling `npx understand-anything`, `tsc`, `eslint`, or `npm run dev`.
- `FR-004`: The public command surface MUST be updated so README,
  `USAGE_GUIDE.md`, the registry, and `validate_command_surface.py` all include
  the toolchain gate for `/refactor-planning`.

## 4. Non-Functional Requirements

- `NFR-001`: The gate MUST remain non-invasive and local: it must not run any
  refactor runtime commands or require network access.
- `NFR-002`: Failures MUST identify the missing executable or missing ESLint
  condition explicitly.

## 5. Acceptance Criteria

- `AC-001`: Given a root where `node`, `npm`, and `npx` are present in `PATH` and
  ESLint is available (global or local), when
  `python3 scripts/validate_refactor_planning_toolchain.py --root <root>` runs,
  then it passes.
- `AC-002`: Given a root where ESLint is unavailable, when the same validator
  runs, then it fails and names the missing ESLint requirement.
- `AC-003`: Given README, `USAGE_GUIDE.md`, the registry, and the workflow are
  wired to the toolchain gate, when
  `python3 scripts/validate_command_surface.py --root .` runs, then it passes.

## 6. Clarifications

- This feature does not attempt to guarantee `npx understand-anything` is
  installed or runnable offline; it only validates the prerequisites that are
  deterministically checkable without executing the runtime.

## 7. Constraints

- In scope: `.agents/scripts/validate_refactor_planning_toolchain.py`,
  `.agents/workflows/refactor-planning.md`, `.agents/SLASH_COMMAND_REGISTRY.md`,
  `.agents/scripts/validate_command_surface.py`, README, `USAGE_GUIDE.md`, and
  this feature package.
- Out of scope: rewriting the refactor engine, running the full refactor runtime
  inside validators, or changing target project dependencies.

## 8. Risks

- Projects that rely on ad-hoc ESLint installation will now fail earlier. This
  is intentional and makes the prerequisite explicit.
- The validator only checks prerequisites and does not prove that the full
  runtime chain succeeds; runtime failures still need to be handled by the
  workflow and QA gates.

## 9. Traceability

- Contract: `contracts/refactor-planning-toolchain-contract.md`
- Workflow: `.agents/workflows/refactor-planning.md`
- Registry: `.agents/SLASH_COMMAND_REGISTRY.md`
- Public validation: `.agents/scripts/validate_command_surface.py`
- Gate implementation: `.agents/scripts/validate_refactor_planning_toolchain.py`

## 10. Review Loop

- `R1` Contract review: confirm the gate is non-invasive and only checks
  deterministic prerequisites.
- `R2` Wiring review: confirm workflow + registry + README + USAGE + command
  surface validation agree on the same invocation and phase.
- `R3` Verification review: confirm bounded positive/negative fixture replays are
  recorded in `verification.md` and the brief is rebuilt after evidence changes.

## 11. Rollback

- Reverting the toolchain gate and its markers restores the previous behavior
  where failures happen later at `npx/tsc/eslint/dev` time.
