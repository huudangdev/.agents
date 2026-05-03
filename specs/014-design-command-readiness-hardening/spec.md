# Feature Specification: Design Command Readiness Hardening

> Feature ID: `014-design-command-readiness-hardening`
> Created: `2026-05-03`
> Status: Draft
> Source Prompt: Convert /design from workflow-only prose into a script-backed command with an explicit readiness gate, so any model can verify planning inputs before producing design artifacts.

## 1. Purpose

Harden `/design` so Phase 2 no longer depends on a model informally reading a
workflow and inferring whether planning inputs are ready or whether the design
artifacts were actually produced. Today `/design` is public, but its contract is
mostly narrative: it mentions planning docs, TrustGraph query, and the expected
outputs, yet it lacks local validator scripts that can fail early and fail
closed when required inputs or artifacts are missing.

This feature adds a deterministic command contract for `/design`. Any model
entering `.agents` should be able to run a local readiness gate before Phase 2,
produce the design artifacts, and then run a local output gate before claiming
the command is complete. The business outcome is governance clarity: design work
becomes as replayable and auditable as the stronger slash-command flows already
present in `.agents`.

## 2. User Stories

- [x] As an operator, I need `/design` to fail before Phase 2 when the planning
      inputs are missing so that design work does not start from stale context.
- [x] As an implementation model, I need `/design` to name its local scripts and
      expected outputs so that I can follow the same workflow deterministically.
- [x] As a governance maintainer, I need `/design` to be part of the validated
      command surface so that README, `USAGE_GUIDE.md`, registry, and workflow
      stay aligned.

## 3. Functional Requirements

- `FR-001`: The system MUST provide a local readiness validator for `/design`
  that checks the required Phase 2 planning inputs before design work begins.
- `FR-002`: The system MUST provide a local output validator for `/design` that
  checks whether `docs/BRAND_GUIDELINES.md` and `docs/UI_COMPONENTS_STATE.md`
  exist and are non-empty before `/design` is considered complete.
- `FR-003`: The system MUST wire `/design` into the public slash-command
  contract so README, `USAGE_GUIDE.md`, the registry, and the workflow file all
  name the same script chain.
- `FR-004`: The system MUST preserve `/design` as a non-codegen design phase
  while adding these deterministic validator gates.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: design validators must remain local and cheap; they
  should only inspect a small set of files.
- `NFR-002`: Security: no new remote execution paths or environment-secret
  reads are introduced.
- `NFR-003`: Observability: validation failures must report the exact missing or
  empty design input or output artifact.
- `NFR-004`: Maintainability: `/design` should become script-backed with minimal
  new surface area, not a new subsystem.
- `NFR-005`: Documentation and traceability: public docs and the command
  registry must point to the new `/design` validator chain explicitly.

For any item that is intentionally deferred, say so explicitly and record the
accepted risk instead of leaving the field vague.

## 5. Acceptance Criteria

- `AC-001`: Given a project with `agents.md`, `docs/prd.md`,
  `docs/planning/screens.md`, and `docs/planning/flows.md`, when
  `python3 scripts/validate_design_readiness.py --root <project>` runs, then it
  passes.
- `AC-002`: Given a project missing one of the required planning inputs, when
  `python3 scripts/validate_design_readiness.py --root <project>` runs, then it
  fails and names the missing file.
- `AC-003`: Given a project with non-empty `docs/BRAND_GUIDELINES.md` and
  `docs/UI_COMPONENTS_STATE.md`, when
  `python3 scripts/validate_design_outputs.py --root <project>` runs, then it
  passes.
- `AC-004`: Given `/design` is published in README and `USAGE_GUIDE.md`, when
  `python3 scripts/validate_command_surface.py --root .` runs, then it confirms
  `/design` points to the readiness and output validator chain.
- `AC-005`: Given `/design` hardening is added, when command-surface validation
  replays, then the broader public command contract still passes.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".

## 6. Clarifications

Record unresolved questions as explicit markers. Planning is blocked while any
marker remains unless the operator accepts the risk.

- No unresolved clarifications remain. Success means `/design` has a local
  readiness gate, a local output gate, and a command-surface contract entry.

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `workflows/design.md`,
  `scripts/validate_command_surface.py`, README, `USAGE_GUIDE.md`,
  `SLASH_COMMAND_REGISTRY.md`, and this feature package.
- Files or modules out of scope: frontend application code, remote design
  tooling, and automated Figma generation.
- Compatibility requirements: `/design` must remain Phase 2 only and must not
  become a source-code workflow.
- Documentation prerequisites already reviewed: current `/design` workflow,
  README execution-command section, and `USAGE_GUIDE.md` command table plus
  script invocation rules.
- Rollback or containment expectations: removing the new validators should
  restore the old prose-only `/design` behavior without affecting other command
  chains.

Out of scope:

- Generating the actual content of `BRAND_GUIDELINES.md` or
  `UI_COMPONENTS_STATE.md` automatically.
- Converting `/marcus_init` or `/refactor-planning` in this slice.
- Adding remote design approval, screenshots, or browser-based rendering checks.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| `/design` remains too narrative even after gating | models still improvise parts of the phase | at least fail entry and exit deterministically with local validators |
| project roots differ across repos | validators resolve the wrong files | keep the checks root-relative and narrow to explicit docs paths |
| command-surface docs drift again | models follow stale prose | add `/design` to the shared command-surface validator |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3-architecture` | `T002`, `T004` | readiness validator passes and fails on the expected input set |
| `FR-002` | `plan.md#3-architecture` | `T002`, `T004` | output validator passes on generated artifacts |
| `FR-003` | `plan.md#4-contracts`, `plan.md#7-migration-and-rollback` | `T003`, `T004` | command-surface validator includes `/design` |
| `FR-004` | `plan.md#7-migration-and-rollback` | `T004`, `T005` | README, USAGE, and workflow keep `/design` positioned as Phase 2 only |

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | hardening stays limited to `/design` command readiness and output gating | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | the gate explains exactly what `/design` needs before and after Phase 2 | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | script-backed `/design` contract is specific enough for implementation | Complete |
