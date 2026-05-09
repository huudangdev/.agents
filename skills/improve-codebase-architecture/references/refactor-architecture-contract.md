# Architecture Refactor Contract

Use this skill when structural cleanup crosses module boundaries.

## Required Inputs

- The current dependency graph and affected modules
- The target boundaries and migration sequence
- Verification commands and docs updates

## Decision Rules

- Prefer migration paths over rewrites.
- Map callers and contracts before moving shared code.
- Keep behavior stable unless a change is explicitly justified.

## Output Contract

- Name the target boundaries and migration plan.
- Identify the blast radius.
- State the verification that protects the refactor.
