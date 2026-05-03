# Feature Specification: Harness Observability and Dynamic Context

> Feature ID: `012-harness-observability-and-dynamic-context`
> Created: `2026-05-03`
> Status: Draft
> Source Prompt: Extend .agents harness with lightweight structured observability for preflight/postflight runs and dynamic execution-brief inputs from changed files and failing evidence, while keeping the system bounded and replayable.

## 1. Purpose

Extend the `.agents` harness so it not only enforces checks, but also leaves a
small, structured trail of what happened and why. Feature `011` added replayable
preflight/postflight wrappers and a freshness validator. This next slice adds
lightweight structured observability for those wrapper runs and improves
`execution-brief.md` so it can carry dynamic execution signals such as changed
files and failing evidence.

The goal is practical, not grandiose: when a harness phase runs, operators
should be able to inspect a structured log without re-reading raw console text,
and when a feature brief is rebuilt, it should optionally foreground the exact
files and failure signals driving the current slice. This reduces both harness
blind spots and unnecessary context loading.

## 2. User Stories

- [x] As an operator, I need structured harness logs so that I can see which
      checks ran, which ones warned, and which one failed first.
- [x] As an implementation agent, I need execution briefs to highlight changed
      files and failing evidence so that I can stay focused on the active slice.
- [x] As a harness maintainer, I need these additions to remain bounded and
      replayable so that `.agents` does not turn into an opaque telemetry
      subsystem.

## 3. Functional Requirements

- `FR-001`: The system MUST emit a structured local log entry for every harness
  preflight and postflight run, including phase, feature, command list, and
  outcome.
- `FR-002`: The system MUST record per-command status within a harness run so a
  reviewer can tell which command passed, warned, or failed first.
- `FR-003`: The execution-brief builder MUST accept optional changed-file input
  and include it in the generated brief as dynamic context.
- `FR-004`: The execution-brief builder MUST accept optional failing-evidence
  input and include it in the generated brief as dynamic context.
- `FR-005`: The updated dynamic context and structured logging MUST preserve the
  current bounded-context philosophy rather than widening default reads.

Requirement writing rules:

- Every requirement must be testable.
- Every requirement must describe observable behavior, not implementation taste.
- Every requirement must name the actor, trigger, and outcome when relevant.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: logging and brief augmentation must stay lightweight
  and local; no external services or heavy indexing.
- `NFR-002`: Security: logs must not collect secrets or raw environment values.
- `NFR-003`: Observability: log output should be machine-readable and append-only.
- `NFR-004`: Maintainability: new helpers should be shared instead of duplicating
  JSONL/logging logic across scripts.
- `NFR-005`: Documentation and traceability: docs and verification must name the
  new flags and log locations explicitly.

For any item that is intentionally deferred, say so explicitly and record the
accepted risk instead of leaving the field vague.

## 5. Acceptance Criteria

- `AC-001`: Given a harness preflight or postflight run in standalone `.agents`,
  when the command completes, then a structured log file is appended with run
  metadata and per-command results.
- `AC-002`: Given a failing harness command, when the wrapper exits non-zero,
  then the log still records the failing command and its exit code.
- `AC-003`: Given `build_execution_brief.py --changed-files ...`, when the brief
  is generated, then it includes those files in a dynamic context section and
  prioritizes them as current execution signals.
- `AC-004`: Given `build_execution_brief.py --failing-evidence ...`, when the
  brief is generated, then it includes a bounded summary of that evidence in the
  brief.
- `AC-005`: Given no dynamic inputs, when the brief is generated, then current
  behavior remains valid and no required sections disappear.

Acceptance criteria rules:

- Every `FR-*` must map to at least one `AC-*`.
- If a requirement cannot be verified yet, mark it in Clarifications or Risks.
- Do not use generic criteria like "works correctly" or "looks good".

## 6. Clarifications

Record unresolved questions as explicit markers. Planning is blocked while any
marker remains unless the operator accepts the risk.

- No unresolved clarifications. Success means harness logs are produced locally
  in `.agents`, wrappers replay cleanly, and briefs can optionally carry changed
  files and failing evidence without widening default reads.

## 7. Constraints

- Constitution articles that apply: Article I, Article IV, Article IX, and
  Article XI.
- Existing files or modules in scope: `scripts/run_harness_preflight.py`,
  `scripts/run_harness_postflight.py`, `scripts/build_execution_brief.py`,
  shared script helpers, README/USAGE/workflows, and this feature package.
- Files or modules out of scope: downstream repos, long-term metrics backends,
  TrustGraph, and non-harness agent memory systems.
- Compatibility requirements: preserve wrapper compatibility from feature `011`
  and keep `build_execution_brief.py` working when no new flags are passed.
- Documentation prerequisites already reviewed: feature `011` package and
  current `build_execution_brief.py` contract.
- Rollback or containment expectations: logs can be ignored or deleted without
  breaking wrappers; optional brief flags must remain additive.

Out of scope:

- Full dashboards, alerting, or background telemetry pipelines.
- Semantic ranking of changed files beyond straightforward listing and grouping.
- Automatic retrieval from GitHub, CI, or external observability systems.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Logging grows into noisy artifacts | Operators ignore it | keep logs local, append-only, and phase-oriented |
| Dynamic context widens the brief too much | context discipline regresses | place changed files and failing evidence in explicit bounded sections |
| Raw failure evidence leaks sensitive text | local risk inside repo | log only operator-provided evidence snippets, not environment dumps |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3-architecture` | `T002`, `T004` | structured log entries exist after wrapper runs |
| `FR-002` | `plan.md#5-data-model` | `T002`, `T004` | failing run records command and exit code |
| `FR-003` | `plan.md#3-architecture` | `T003`, `T004` | brief includes changed files |
| `FR-004` | `plan.md#3-architecture` | `T003`, `T004` | brief includes failing evidence |
| `FR-005` | `plan.md#7-migration-and-rollback` | `T003`, `T004` | no-regression brief generation and wrapper replay |

## 10. Review Loop

Document the review rounds that must happen before implementation is allowed to
proceed.

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | logging stays lightweight and local; dynamic context stays bounded | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | flags, logs, and acceptance criteria are concrete and replayable | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | spec package is stable enough for `plan.md` and script work | Complete |
