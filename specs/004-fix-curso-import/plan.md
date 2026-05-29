# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]

**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]

**Primary Dependencies**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]

**Storage**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]

**Testing**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]

**Target Platform**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION]

**Project Type**: [e.g., library/cli/web-service/mobile-app/compiler/desktop-app or NEEDS CLARIFICATION]

**Performance Goals**: [domain-specific, e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]

**Constraints**: [domain-specific, e.g., <200ms p95, <100MB memory, offline-capable or NEEDS CLARIFICATION]

**Scale/Scope**: [domain-specific, e.g., 10k users, 1M LOC, 50 screens or NEEDS CLARIFICATION]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Spec-First Delivery: `spec.md` includes prioritized stories, requirements, assumptions,
  edge cases, and measurable outcomes.
- Independent Value Slices: User stories are independently implementable and testable.
- Verifiable Outcomes: Each story has acceptance scenarios and a reproducible validation method.
- Traceable Artifacts: Planned work maps directly to stories and target file paths.
- Minimal, Explicit Change: Added complexity includes documented rationale in this plan.

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/

# Implementation Plan: Fix `curso` import (specs/004-fix-curso-import)

**Branch**: `004-fix-curso-import` | **Date**: 2026-05-29 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/004-fix-curso-import/spec.md`

## Summary

Fix the recurring `ModuleNotFoundError: No module named 'curso'` seen when running
notebooks and CI. Deliver a minimal packaging + setup change so that `curso` is a
first-class importable package after `./scripts/setup_env.sh` runs, without modifying
notebooks.

## Technical Context

**Language/Version**: Python 3.11 (CI uses 3.11)

**Primary Dependencies**: None new (packaging via `setuptools`, `wheel` are used at build time)

**Storage**: N/A

**Testing**: Existing CI smoke test (`.github/workflows/ci-notebook-smoke.yml`) and install-check (`ci-install-check.yml`) will validate the fix.

**Target Platform**: macOS, Linux (dev + CI)

**Project Type**: Packaging / environment setup (no application code changes)

**Performance Goals**: Keep setup time impact minimal; editable install acceptable.

**Constraints**: Must work with current `scripts/setup_env.sh` flow and Python 3.11.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Spec-First Delivery: `spec.md` defines the bug, acceptance tests, and measurable outcomes.
- Independent Value Slices: The fix is a single slice (packaging/install change) that yields immediate value.
- Verifiable Outcomes: Acceptance scenarios are reproducible locally and in CI.
- Traceable Artifacts: Changes touch `setup_env.sh`, add packaging metadata (`pyproject.toml`, `setup.cfg`), and update docs.
- Minimal, Explicit Change: The plan prefers an editable install to avoid editing many notebooks.

## Project Structure (changes for this feature)

```text
specs/004-fix-curso-import/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/

# Repository changes
pyproject.toml       # build-system for packaging
setup.cfg            # setuptools config to find `curso` package
scripts/setup_env.sh # updated to `pip install -e .` during venv setup
```

**Structure Decision**: Create packaging metadata at repo root and ensure setup script installs the project in editable mode inside the created venv.

## Complexity Tracking

No constitution violations detected. The change is focused and reversable (only packaging metadata + small setup script change).

## Phase 0: Research

Create `research.md` summarizing options (editable install vs PYTHONPATH vs notebook edits) and decision to prefer editable install via `pip install -e .`.

## Phase 1: Design & Contracts

- `data-model.md`: Entity definitions (package `curso`, setup script behavior)
- `contracts/installation.md`: Installation & verification contract (what success looks like)
- `quickstart.md`: Verify steps to run `./scripts/setup_env.sh` and confirm `python -c "import curso"` works

## Phase 2: Implementation

1. Add `pyproject.toml` and `setup.cfg` to make the repository installable (package name `robots-curso`, packages=find: to include `curso`).
2. Update `scripts/setup_env.sh` to run `pip install -e .` inside the venv after installing requirements.
3. Update CI (`.github/workflows/ci-install-check.yml`) to include a `import curso` check (if not already covered).
4. Run smoke tests (existing `ci-notebook-smoke.yml`) locally in a fresh venv.
5. Update documentation (`specs/004-fix-curso-import/quickstart.md` and main quickstart) with verification steps.

## Done Criteria

- All design artifacts created: `research.md`, `data-model.md`, `contracts/installation.md`, `quickstart.md`.
- `scripts/setup_env.sh` updated and `pyproject.toml` + `setup.cfg` added and committed.
- Local validation: `./scripts/setup_env.sh` then `python -c "import curso"` returns OK.
- CI validation: `ci-install-check.yml` and `ci-notebook-smoke.yml` pass in the PR for this branch.
