# Refactor Planning Toolchain Gate

Feature ID: `017-refactor-planning-toolchain-gate`

This feature hardens `/refactor-planning` by adding a deterministic local
toolchain prerequisite gate. It is intentionally non-invasive: it does not run
the AST, typecheck, lint, or dev server; it only verifies the executables and
ESLint availability so the workflow fails fast with an explicit cause.

