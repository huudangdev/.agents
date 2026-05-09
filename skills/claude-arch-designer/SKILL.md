---
name: claude-arch-designer
description: Produce durable architecture artifacts, diagrams, and docs for active scope
---

# Architecture Artifact Designer

Use this skill when the task is to produce durable docs or diagrams.

## Required Reads

- [artifact-contract.md](references/artifact-contract.md)
- Current spec package and ADRs when they exist.

## Operating Rules

- Prefer small, targeted artifacts over documentation theater.
- Choose Mermaid, ADR, guide update, or appendix based on need.
- Keep diagrams and docs tied to active scope.

## Output Expectations

- State the artifact chosen and why.
- Keep the output physically useful and reviewable.
- Reflect implementation expectations in the docs when needed.
