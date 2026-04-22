# Research: Substantive Development Docs Quality

> Feature ID: `007-substantive-development-docs-quality`

## Questions

- Why did generated development docs remain shallow?
- What makes a code-phase note useful for a PM and a future agent?
- Which checks can reject template-only output reliably?

## Findings

| Finding | Source | Decision Impact |
| --- | --- | --- |
| Documentation frameworks emphasize audience, clarity, and consistency. | Google developer documentation style guidance | Add PM-readable commentary and clear required sections |
| Architecture knowledge needs rationale and consequences. | ADR practice | Require decision, tradeoff, risk, and evidence fields |
| Quality requirements should be measurable and scenario-based. | arc42 quality guidance | Add minimum depth and validation gates |
| Existing validators only checked structure. | Local scripts | Add content-quality checks |

## Rejected Alternatives

- Relying on prompt wording only: rejected because agents can still output
  templates.
- Manual PM review only: rejected because poor docs should fail before handoff.
