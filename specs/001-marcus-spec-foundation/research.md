# Research Notes: Marcus Spec Foundation

> Feature ID: `001-marcus-spec-foundation`

## Research Questions

- How can Spec Kit's spec-driven lifecycle be adapted without replacing Marcus
  Fleet's existing `.agents` ecosystem?
- Which artifacts are needed first to make the method operational?
- What should remain out of scope for the first increment?

## Findings

| Topic | Finding | Source | Decision Impact |
| --- | --- | --- | --- |
| Spec-driven workflow | GitHub Spec Kit uses constitution, specify, clarify, plan, tasks, implement, and verify phases. | `github/spec-kit` README and `spec-driven.md` | Add Marcus-native workflow docs. |
| Feature-scoped artifacts | Spec Kit stores work under numbered feature directories with spec, plan, contracts, data model, quickstart, and tasks. | `github/spec-kit` README | Add `.agents/specs/<feature-id>/`. |
| Template constraints | Spec templates reduce hallucination by separating WHAT from HOW and forcing clarification markers. | `spec-driven.md` | Add templates and validator for `[NEEDS CLARIFICATION]`. |
| Local compatibility | Marcus already has TrustGraph, skills, workflows, and sandbox scripts. | Local `.agents` review | Keep new layer additive. |

## Decisions Ready for Plan

- Build a local Spec Foundation Pack instead of depending on upstream CLI.
- Make generated feature workspaces the future source of truth for non-trivial
  agent work.
- Migrate legacy workflows incrementally in later steps.
