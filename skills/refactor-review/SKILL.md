---
name: refactor-review
description: Use when reviewing refactor proposals or legacy code changes for regression risk, coupling, and verification quality.
---

# Refactor Review

Use this skill to audit refactor proposals or legacy code changes before they ship.

## Required Reads

1. Root `agents.md`.
2. Active feature docs and relevant diffs.
3. Local tests, linters, and validators when available.
4. [`references/refactor-review-contract.md`](references/refactor-review-contract.md).

## Operating Rules

- Read the changed files and surrounding context.
- Identify regression risk, coupling, and hidden assumptions.
- Use local tooling first.
- Distinguish real defects from style preferences.

## Output Expectations

- Return a blocker-oriented review.
- Map findings to verification evidence.
- State NO-GO when the review is not grounded.
