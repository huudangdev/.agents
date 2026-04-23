# Contract: Epic-First Development Ledger

## Structural Contract

- New ledgers set `topology: epic_first`.
- Root development docs may contain only `development_manifest.json`,
  `index.md`, `sync/`, `_archive/`, `by-type/`, and `E-###-*` directories.
- Root flat buckets are invalid in V31.

## Identity Contract

- `epic.md` frontmatter `id` equals the containing `E-###-*` directory.
- Child frontmatter `id` equals filename stem.
- Child frontmatter `parent_epic` equals containing epic directory.

## Compatibility Contract

- Legacy flat manifests still use legacy validation.
- Migration is explicit, append/targeted-patch based, and archive-safe.
