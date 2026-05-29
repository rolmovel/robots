# Research: Fix curso import

**Feature**: specs/004-fix-curso-import
**Date**: 2026-05-29

## Problem

Notebooks in `curso/` import internal modules via `from curso.lib.data import ...`.
When running notebooks outside the repository root or without installing the repo,
Python cannot find the `curso` package and raises `ModuleNotFoundError`.

## Options considered

### Option A — Install repository as a package (recommended)

- Action: Add minimal packaging metadata (`pyproject.toml`, `setup.cfg`) and update
  `scripts/setup_env.sh` to `pip install -e .` inside the venv.
- Pros:
  - Explicit and standard Python packaging approach.
  - Works in JupyterLab and any Python execution context (scripts, tests, CI).
  - No changes required to notebooks.
- Cons:
  - Adds a small packaging overhead during setup (editable install).

### Option B — Modify `scripts/setup_env.sh` to export `PYTHONPATH` on activation

- Action: When creating the venv, write an activation hook or echo instructions to
  set `PYTHONPATH=$PWD` on activation.
- Pros:
  - Simple to implement.
  - No packaging metadata required.
- Cons:
  - Less explicit (relies on environment vars), can be confusing to users.
  - Some tools (e.g., editors) may not pick up `PYTHONPATH` consistently.

### Option C — Add path hacks in notebooks (`sys.path.append(...)`)

- Action: Add a cell at the top of notebooks to insert the repo root into `sys.path`.
- Pros:
  - Quick, simple, guaranteed to work locally.
- Cons:
  - Pollutes notebooks with environment-specific code.
  - Not acceptable per spec (we want no notebook edits).

## Decision

Choose Option A: Add packaging metadata and perform an editable install in `setup_env.sh`.

**Rationale**: It's the most robust and standard solution; it avoids editing notebooks and works across editors, CI, and interactive sessions.

## Implementation notes

- Create `pyproject.toml` with `setuptools` build backend.
- Create `setup.cfg` with `packages = find:` so `curso` is installed.
- Update `scripts/setup_env.sh` to run `pip install -e .` after installing requirements.
- Update CI to verify `import curso` in the install-check job.

