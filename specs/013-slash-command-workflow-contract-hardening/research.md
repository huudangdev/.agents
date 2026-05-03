# Research Notes: Slash Command Workflow Contract Hardening

> Feature ID: `013-slash-command-workflow-contract-hardening`

## Research Focus

- Which slash commands are publicly published today in README and
  `USAGE_GUIDE.md`.
- Which of those commands already have workflow files and script markers.
- Which commands are visible in one public surface but missing or underspecified
  in another.

## Findings

- The previous `validate_command_surface.py` covered only a narrow subset of
  commands centered on the feature-spec lifecycle and `/develop`.
- `/bootstrap` was visible in README but not listed in the primary USAGE command
  table, which weakens discoverability for new models.
- `/marcus.routecheck` had a workflow file and validator role but was not
  treated as a first-class public command in the top-level command table.
- README, `USAGE_GUIDE.md`, and workflow files already contained enough marker
  strings to support a stronger contract check without needing a new parser or
  runtime service.

## Decision

Use a public markdown registry plus a stronger validator rather than inventing a
separate remote schema or metadata system. This keeps the contract readable to
humans and cheap to replay locally.
