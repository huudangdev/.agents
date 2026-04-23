# Data Model: Epic-First Development Ledger

## Development Manifest

- `version`: `31.0`
- `topology`: `epic_first`
- `id_convention`: canonical examples for epic, feature, module, page, task
- `epics`: map of epic ID to path, status, and child IDs
- `minimum_children`: per-epic child counts
- `quality_gates`: V30.4 gates plus V31 topology gates

## Epic Directory

- Directory name: `E-###-description`
- Required file: `epic.md`
- Optional child folders: `features/`, `modules/`, `pages/`, `tasks/`, `sync/`

## Child Note

- Filename stem equals `id`.
- `parent_epic` equals containing epic directory.
- Mermaid, code trace, PM notes, verification, and change log are mandatory.
