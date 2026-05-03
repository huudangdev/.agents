# Feature Specification: Marcus Spec Foundation

> Feature ID: `001-marcus-spec-foundation`
> Created: `2026-04-20`
> Status: Accepted
> Source Prompt: Apply GitHub Spec Kit ideas to Marcus Fleet by adding constitution, feature-scoped specs, templates, validation scripts, and workflow docs without replacing the existing .agents ecosystem.

## 1. Purpose

Marcus Fleet needs a spec-driven foundation inspired by GitHub Spec Kit without
replacing its existing strengths: skills, workflows, TrustGraph memory, sandbox
execution, and observability. The outcome is a durable planning layer that lets
agents work from feature-scoped contracts instead of loosely interpreted prompts.

This feature establishes the first version of that layer: a constitution,
templates, scripts, workflow documents, and a sample feature workspace that can
be validated locally.

## 2. User Stories

- [x] As the human operator, I need feature work to start from a durable
      specification so that agent output stays aligned with intent.
- [x] As the Marcus orchestrator, I need templates and validation scripts so
      that I can create consistent feature workspaces without hand-building
      every artifact.
- [x] As QA and security agents, I need acceptance criteria and constitution
      gates so that reviews can validate concrete contracts rather than style.

## 3. Functional Requirements

- `FR-001`: The system MUST provide a project-level constitution under
  `.agents/memory/constitution.md`.
- `FR-002`: The system MUST provide reusable templates for `spec.md`,
  `plan.md`, `tasks.md`, `verification.md`, `agent-routing.md`, `research.md`,
  `data-model.md`, and `quickstart.md`.
- `FR-003`: The system MUST provide a script that creates a numbered
  `.agents/specs/<feature-id>/` workspace from templates.
- `FR-004`: The system MUST provide a script that validates required feature
  artifacts and unresolved clarification markers.
- `FR-005`: The system MUST provide workflow documents for specify, clarify,
  plan, tasks, and verify phases.
- `FR-006`: The system MUST preserve the existing `.agents` ecosystem and avoid
  replacing current skills or TrustGraph adapters.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: validation must run locally without network access.
- `NFR-002`: Security: scripts must not execute generated shell payloads or
  fetch remote code.
- `NFR-003`: Observability: completed work must update `agents.md` and attempt
  a TrustGraph memory write.
- `NFR-004`: Maintainability: templates must be plain Markdown and scripts must
  use Python standard library only.

## 5. Acceptance Criteria

- `AC-001`: Given the repository root, when
  `python3 .agents/scripts/create_feature_spec.py "Example Feature"` runs, then
  a numbered feature folder is created under `.agents/specs/`.
- `AC-002`: Given a generated feature folder, when
  `python3 .agents/scripts/validate_specs.py --feature <folder>` runs after
  clarifications are resolved, then validation passes.
- `AC-003`: Given a generated draft with unresolved clarification markers, when
  validation runs without `--allow-clarifications`, then validation fails.
- `AC-004`: Given an agent planning a non-trivial change, when it reads the new
  workflow docs, then it can follow specify -> clarify -> plan -> tasks ->
  verify without using legacy global `/docs` artifacts as the only source of
  truth.

## 6. Clarifications

- Clarification resolved: this first increment should create the spec
  foundation and one sample feature workspace. It should not migrate all legacy
  workflows or rewrite all skill files in the same step.
- Clarification resolved: existing `/planning`, `/develop`, `/quick_fix`, and
  TrustGraph flows remain valid. The new Marcus spec workflows are additive.

## 7. Constraints

- Constitution articles that apply: all initial articles in
  `.agents/memory/constitution.md`.
- Existing files or modules in scope: `.agents/workflows/`, `.agents/templates/`,
  `.agents/scripts/`, `.agents/specs/`, root `agents.md`.
- Files or modules out of scope: `.agents/skills/*/SKILL.md` mass migration,
  TrustGraph schema migration, viewer lint cleanup.
- Compatibility requirements: no existing workflow file may be deleted; new
  scripts must run with `python3` and no third-party packages.
- Documentation prerequisites already reviewed: root `agents.md`,
  `.agents/README.md`, `.agents/USAGE_GUIDE.md`, and the workflow set under
  `.agents/workflows/`.
- Rollback or containment expectations: this foundation must remain additive so
  that legacy slash-command flows still operate even if feature-scoped specs are
  not yet adopted everywhere.

Out of scope:

- Rewriting every legacy skill to the new tool vocabulary in the same feature.
- Replacing the historical `/planning` package with `.agents/specs/` only.
- Introducing network-dependent spec tooling or a hosted policy service.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Agents ignore specs and continue using global docs only | Medium | Add workflow docs and update `agents.md` session history. |
| Templates become paperwork without validation | High | Add validator script and run it on this feature. |
| New structure conflicts with current workflows | Medium | Make this additive and do not rename legacy commands yet. |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#2` | `T001` | `verification.md#evidence` |
| `FR-002` | `plan.md#3` | `T002` | `verification.md#evidence` |
| `FR-003` | `plan.md#3` | `T003` | `verification.md#evidence` |
| `FR-004` | `plan.md#3` | `T004` | `verification.md#evidence` |
| `FR-005` | `plan.md#3` | `T005` | `verification.md#evidence` |

## 10. Review Loop

| Round | Reviewer | Focus | Exit Criteria | Status |
| --- | --- | --- | --- | --- |
| `R1` | `aurora-plan-challenger` | Scope challenge | additive-only scope confirmed, migration fantasy removed | Complete |
| `R2` | `sophia-product-manager` | Requirement quality | user stories, FRs, ACs, and evidence obligations aligned | Complete |
| `R3` | `marcus-ai-orchestrator` | Go/no-go to planning | spec package stable enough to create architecture artifacts | Complete |
