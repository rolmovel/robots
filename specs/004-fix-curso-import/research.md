# Research: Fix curso import

**Feature**: specs/004-fix-curso-import
**Date**: 2026-05-29

## Problem

Two import failures affect notebooks in `curso/`:

1. **Original**: `ModuleNotFoundError: No module named 'curso'` — the `curso` package was not
   importable because the repo wasn't installed as a Python package.
2. **Current (blocking)**: `ModuleNotFoundError: No module named 'pkg_resources'` — triggered
   when `curso/lib/indicators.py` imports `pandas_ta`, which does
   `from pkg_resources import get_distribution` in its `__init__.py`.

### Root Cause Analysis (pkg_resources)

- `pandas_ta` 0.3.14b uses `pkg_resources` (from `setuptools`) at import time.
- `setuptools` 78+ removed `pkg_resources` as a standalone importable module.
- The current venv has `setuptools==82.0.1` installed (via `pip install --upgrade pip setuptools wheel` in `setup_env.sh`), which no longer provides `pkg_resources`.
- A shim workaround exists in `setup_env.sh` but does not work reliably.

## Options considered

### Option A — Pin setuptools<72 (recommended)

- Action: Pin `setuptools<72` in `curso/requirements.txt` and in the `setup_env.sh` upgrade step.
- Pros:
  - `pkg_resources` is fully available in setuptools <72.
  - No changes to `pandas_ta` or notebooks.
  - Simple, reversible constraint.
- Cons:
  - Pins an older setuptools; acceptable since only needed for `pandas_ta` compatibility.

### Option B — Install separate `setuptools-pkg-resources` shim package

- Action: Install a third-party compatibility package.
- Pros:
  - Keeps setuptools modern.
- Cons:
  - No official package exists for this; unreliable third-party sources.

### Option C — Patch pandas_ta locally to use importlib.metadata

- Action: Monkey-patch or fork pandas_ta to replace `pkg_resources` with `importlib.metadata`.
- Pros:
  - Uses modern stdlib.
- Cons:
  - Requires maintaining a fork/patch; fragile across updates.

### Option D — Install repository as editable package (already done)

- Action: `pip install -e .` (already implemented in previous iteration).
- Pros:
  - Makes `curso` importable.
- Cons:
  - Does NOT fix the `pkg_resources` issue (separate problem).

## Decision

Choose Option A + D combined:
1. **Pin `setuptools<72`** in requirements and setup script to restore `pkg_resources`.
2. **Keep editable install** (`pip install -e .`) for `curso` importability.
3. **Remove the fragile shim** workaround from `setup_env.sh`.

**Rationale**: Pinning setuptools is the minimal change that restores compatibility with `pandas_ta` 0.3.14b while keeping the existing packaging setup intact. The shim was unreliable and should be replaced by a proper version constraint.

## Implementation notes

- Update `curso/requirements.txt`: add `setuptools<72` as explicit dependency.
- Update `scripts/setup_env.sh`: change `pip install --upgrade pip setuptools wheel` to `pip install --upgrade pip "setuptools<72" wheel`.
- Remove the `pkg_resources` shim script from `setup_env.sh`.
- Verify: `curso/.venv/bin/python -c "import pkg_resources; print('OK')"` passes.
- Verify: notebook chapter 01 executes without `ModuleNotFoundError`.

