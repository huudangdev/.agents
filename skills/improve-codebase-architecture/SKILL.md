---
name: improve-codebase-architecture
description: Plan structural cleanup across modules with bounded migration and verification
---

# Improve Codebase Architecture

Use this skill when structural cleanup crosses module boundaries.

## Required Reads

- [refactor-architecture-contract.md](references/refactor-architecture-contract.md)
- The current dependency graph and affected modules when they exist.

## Operating Rules

- Prefer migration paths over rewrites.
- Map callers and contracts before moving shared code.
- Keep behavior stable unless a change is explicitly justified.

## Output Expectations

- Name the target boundaries and migration plan.
- Identify the blast radius.
- State the verification that protects the refactor.
