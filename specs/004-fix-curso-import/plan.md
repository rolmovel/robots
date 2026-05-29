# Implementation Plan: Fix `curso` import (pkg_resources)

**Branch**: `docs/update-readme-install` | **Date**: 2026-05-29 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/004-fix-curso-import/spec.md`

## Summary

Fix `ModuleNotFoundError: No module named 'pkg_resources'` that occurs when running
chapter 01 notebook. The error is triggered by `pandas_ta` 0.3.14b which uses
`pkg_resources` at import time, but the current venv installs `setuptools>=82` which
no longer ships `pkg_resources`. The fix pins `setuptools<72` and removes the unreliable
shim workaround. The editable install (`pip install -e .`) for `curso` importability
remains in place from previous iteration.

## Technical Context

**Language/Version**: Python 3.12 (local), Python 3.11 (CI)

**Primary Dependencies**: `pandas_ta==0.3.14b` (requires `pkg_resources`), `setuptools<72`

**Storage**: N/A

**Testing**: Existing CI smoke test (`.github/workflows/ci-notebook-smoke.yml`) and install-check (`ci-install-check.yml`)

**Target Platform**: macOS, Linux (dev + CI)

**Project Type**: Packaging / environment setup (no application code changes)

**Performance Goals**: Keep setup time impact minimal.

**Constraints**: Must work with `scripts/setup_env.sh` flow, Python 3.11+/3.12.

**Scale/Scope**: Single dependency version constraint fix.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Spec-First Delivery**: ✅ `spec.md` defines the bug, acceptance tests, and measurable outcomes.
- **Independent Value Slices**: ✅ Single slice (setuptools pin) yields immediate value.
- **Verifiable Outcomes**: ✅ Acceptance scenarios are reproducible locally and in CI.
- **Traceable Artifacts**: ✅ Changes touch `setup_env.sh`, `curso/requirements.txt`, and docs.
- **Minimal, Explicit Change**: ✅ Pin a dependency version rather than patching libraries or editing notebooks.

## Project Structure (changes for this feature)

```text
specs/004-fix-curso-import/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── installation.md  # Phase 1 output
└── tasks.md             # Phase 2 output (NOT created by /speckit.plan)
```

### Source Code (repository root changes)

```text
curso/requirements.txt     # Add setuptools<72
scripts/setup_env.sh       # Pin setuptools<72 in upgrade step; remove shim
pyproject.toml             # Already present (no change)
setup.cfg                  # Already present (no change)
```

## Complexity Tracking

No constitution violations detected. The change is a single dependency version pin + script cleanup.

## Phase 0: Research

See [research.md](research.md). Key finding: `setuptools>=78` removed `pkg_resources` as a
standalone module. `pandas_ta` 0.3.14b still depends on it. Pin `setuptools<72` resolves the issue.

## Phase 1: Design & Contracts

- [data-model.md](data-model.md): Entity definitions (package, setup script, dependency constraint)
- [contracts/installation.md](contracts/installation.md): Installation & verification contract
- [quickstart.md](quickstart.md): Steps to verify the fix

## Phase 2: Implementation

1. Update `curso/requirements.txt`: add `setuptools<72`.
2. Update `scripts/setup_env.sh`: change `pip install --upgrade pip setuptools wheel` to `pip install --upgrade pip "setuptools<72" wheel`.
3. Remove the `pkg_resources` shim workaround from `setup_env.sh`.
4. Verify locally: recreate venv and confirm `from curso.lib.indicators import sma` works.
5. Run chapter 01 notebook to confirm no `ModuleNotFoundError`.

## Done Criteria

- All design artifacts updated: `research.md`, `data-model.md`, `contracts/installation.md`, `quickstart.md`.
- `setuptools<72` pinned in `curso/requirements.txt` and `scripts/setup_env.sh`.
- `pkg_resources` shim removed from `setup_env.sh`.
- Local validation: fresh venv with `./scripts/setup_env.sh` then `python -c "from curso.lib.indicators import sma; print('OK')"` returns OK.
- CI validation: `ci-install-check.yml` and `ci-notebook-smoke.yml` pass.
