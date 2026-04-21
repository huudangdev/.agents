# Marcus Fleet Constitution

> Version: 1.0.0
> Ratified: 2026-04-20
> Scope: All work coordinated by the Marcus Fleet `.agents` system.

This constitution is the stable contract that all Marcus Fleet agents must obey.
Workflow files, skill files, and implementation plans may evolve, but they must
remain compatible with these articles unless an amendment is recorded here.

## Article I: Specification Is the Source of Truth

Every non-trivial change must trace back to a feature-scoped specification under
`.agents/specs/<feature-id>/`. Code, diagrams, tests, and operational scripts are
implementation artifacts. If implementation and specification disagree, update
the specification or explicitly record the exception before changing code.

Required feature artifacts:

- `spec.md`: user value, stories, requirements, acceptance criteria, risks.
- `plan.md`: technical translation, architecture, dependencies, migration path.
- `tasks.md`: executable task list with ownership and verification.
- `verification.md`: test and evidence log for completion.

## Article II: Clarify Before Planning

Agents must not silently invent product behavior, security posture, data
retention policy, tenant boundaries, or rollback expectations. Unknowns must be
recorded as `[NEEDS CLARIFICATION: ...]` in `spec.md`. Planning and implementation
are blocked until the remaining ambiguity is explicitly accepted or resolved.

## Article III: Contracts Before Code

Any interface boundary must be documented before implementation:

- API request/response contracts belong in `contracts/`.
- Data entities belong in `data-model.md`.
- Agent handoffs belong in `agent-routing.md`.
- Operational validation belongs in `quickstart.md` and `verification.md`.

Implementation work without contracts is allowed only for scoped discovery spikes
that are marked as non-production and time-boxed in `tasks.md`.

## Article IV: Test-First Verification

Every task that changes behavior must name its verification method before code is
written. Tests may be automated or manual, but they must be concrete and
repeatable. A task cannot be marked complete unless `verification.md` contains
the command, result, date, and residual risk.

## Article V: Security and Execution Boundaries

Agent-generated terminal activity must use bounded executors and project-local
tools. Shell `eval`, hardcoded production secrets, destructive filesystem
commands, and unreviewed network installers are not acceptable in production
paths. Any exception requires explicit human approval and a rollback note.

## Article VI: Multi-Agent Ownership

Multi-agent work must use explicit ownership. Each task must name one primary
agent or skill and define its output. Parallel tasks must be marked `[P]` only
when their write scopes are disjoint. Agents must not revert or overwrite another
agent's work without a documented handoff.

## Article VII: Simplicity Gate

Plans must prefer direct framework capabilities and small cohesive modules. New
abstractions require a named reason: reduced duplication, isolated risk, stable
interface, or measurable complexity reduction. Speculative features are rejected.

## Article VIII: Observability and Memory

Significant work must produce durable memory:

- Update the feature's `verification.md`.
- Update root `agents.md` with a concise session history entry.
- Attempt a TrustGraph write with run id, target, skills, score, and reasoning.

If TrustGraph is offline, the deferred state must be treated as acceptable only
when the filesystem memory was updated.

## Article IX: Amendment Process

Constitution changes require:

- A feature spec explaining the reason for change.
- A migration note for affected workflows or skills.
- A new version number and dated amendment entry.

## Amendments

- `2026-04-20`: Initial constitution created to align Marcus Fleet with
  specification-driven development while preserving TrustGraph, skills, and
  enterprise governance workflows.
