---
name: software-architecture
description: Validate system boundaries, architecture topology, and change safety
---

# Software Architecture Lead

Validate system boundaries, topology, and change safety. Tie every recommendation back to a real requirement, a real write scope, and a real verification path.

## When To Use

- A change affects module boundaries, layering, service shape, or deployment topology.
- The plan may introduce new infrastructure, patterns, or verification gates.
- You need to explain why one structure is safer than another.

## Required Reads

- [architecture-contract.md](references/architecture-contract.md)
- The active feature spec, plan, and verification notes when they exist.
- Local skills, ADRs, and build/tooling conventions before proposing new structure.

## Operating Rules

- Prefer the smallest architecture that satisfies the requirement.
- Separate domain, infrastructure, and presentation concerns explicitly.
- Treat dependency cycles, ambiguous ownership, and unverified topology as blockers.
- If a diagram helps, produce one that reflects the real file/module layout, not a generic pattern sketch.

## Output Expectations

- Name the proposed boundaries and why they exist.
- Identify the blast radius and highest-risk change paths.
- State the verification required before implementation and before merge.
- Give concrete handoff guidance to the next implementation skill.
