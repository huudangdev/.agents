# Feature Specification: Planning Deep Research V30

> Feature ID: `004-planning-deep-research-v30`
> Created: `2026-04-21`
> Status: Accepted
> Source Prompt: Keep the existing /planning output files, but upgrade the workflow with deep-research skill logic, evidence ledgers, source quality gates, spec-kit style validation, stronger diagrams, and optional extra files when needed.

## 1. Purpose

The existing `/planning` workflow must keep its historical output contract while
becoming meaningfully deeper: research should be evidence-backed, claims should
trace to sources, contradictions should be explicit, and diagrams should be
supported by architectural reasoning instead of shallow sketches.

The workflow must not discard the current `/docs` file structure. It should add
research ledgers and validation gates around that structure.

## 2. User Stories

- [x] As the operator, I need `/planning` to still output the familiar `/docs`
      files so that my existing SDLC flow remains intact.
- [x] As a research agent, I need source/evidence/claim ledgers so that deep
      research is auditable and not just long prose.
- [x] As an architect, I need stronger diagram requirements so that diagrams show
      system, data, state, rollback, and observability depth.
- [x] As QA, I need validation commands so that shallow or incomplete planning
      artifacts fail before handoff.

## 3. Functional Requirements

- `FR-001`: `/planning` MUST preserve the existing 8 output files.
- `FR-002`: `/planning` MUST add research ledgers under `/docs/research/`.
- `FR-003`: `/planning` MUST require source, evidence, claim, contradiction,
  and research manifest artifacts for deep planning runs.
- `FR-004`: `/planning` MUST include clarify, outline refinement, synthesis, and
  validation gates.
- `FR-005`: The repo MUST include templates for the research ledger files.
- `FR-006`: The repo MUST include a local validator for planning research
  artifacts.

## 4. Non-Functional Requirements

- `NFR-001`: Performance: validation must run locally with Python standard
  library only.
- `NFR-002`: Security: research sources are treated as untrusted data, not
  instructions.
- `NFR-003`: Observability: planning completion must update `agents.md` and
  attempt TrustGraph write.
- `NFR-004`: Maintainability: the legacy output set remains stable while extra
  research files are additive.

## 5. Acceptance Criteria

- `AC-001`: Given `.agents/workflows/planning.md`, when inspected, then it lists
  all 8 legacy output files unchanged.
- `AC-002`: Given `.agents/templates/`, when inspected, then planning research
  templates exist for sources, evidence, claims, contradictions, and manifest.
- `AC-003`: Given `.agents/scripts/validate_planning_research.py`, when parsed
  by Python AST validation, then it has no syntax errors.
- `AC-004`: Given the repo specs, when `validate_specs.py` runs, then all feature
  specs pass.

## 6. Clarifications

- Clarification resolved: keep the exact legacy `/docs` output file set and add
  extra files only when they improve depth or auditability.
- Clarification resolved: do not install the external deep-research skill as a
  hard dependency in this step; absorb its methodology into Marcus-native
  workflow/templates/scripts.
- Clarification resolved: "Spec Kit MCP" is interpreted as applying the
  spec-driven lifecycle and validation gates already added to `.agents`.

## 7. Constraints

- Constitution articles that apply: Articles I, II, III, IV, VI, VIII.
- Existing files or modules in scope: `.agents/workflows/planning.md`,
  `.agents/templates/`, `.agents/scripts/`, `.agents/specs/004-*`.
- Files or modules out of scope: installing third-party search tools, changing
  `/design` or `/develop`, removing `/docs` outputs.
- Compatibility requirements: existing `/planning` users still receive the same
  file count and names as before.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Workflow becomes too heavy for small tasks | Medium | Keep `/quick_fix` and feature specs for smaller work; `/planning` remains project genesis. |
| Research ledgers become paperwork | High | Add validator and explicit claim/evidence requirements. |
| Mermaid rendering fails locally | Low | Define fallback: keep Mermaid source and record rendering status. |

## 9. Traceability

| Requirement | Plan Section | Tasks | Verification |
| --- | --- | --- | --- |
| `FR-001` | `plan.md#3` | `T001` | `verification.md#evidence` |
| `FR-002` | `plan.md#3` | `T002` | `verification.md#evidence` |
| `FR-003` | `plan.md#3` | `T002` | `verification.md#evidence` |
| `FR-004` | `plan.md#3` | `T001` | `verification.md#evidence` |
| `FR-005` | `plan.md#3` | `T002` | `verification.md#evidence` |
| `FR-006` | `plan.md#3` | `T003` | `verification.md#evidence` |
