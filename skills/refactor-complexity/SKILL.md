---
name: refactor-complexity
description: Reduce code complexity with measured extraction and behavior-safe cleanup
---

# Complexity Reduction

Use this skill when code shape is the problem.

## Required Reads

- [complexity-contract.md](references/complexity-contract.md)
- The target file or module when it exists.

## Operating Rules

- Remove complexity only where it has measurable value.
- Prefer structural extraction over broad rewrites.
- Keep behavior stable unless a change is explicitly justified.

## Output Expectations

- State the complexity source.
- Name the reduction path and its risk.
- Describe the verification that protects behavior.
