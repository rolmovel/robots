# Implementation Plan: Fix notebook 04 execution at step 2

**Branch**: `005-fix-notebook-04` | **Date**: 2026-05-29 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/005-fix-notebook-04/spec.md`

## Summary

Fix `KeyError: 'upper'` that occurs when running notebook `04_estrategia.ipynb` step 2
("Calcular Bollinger Bands + ATR"). The `bollinger_bands()` wrapper in
`curso/lib/indicators.py` returns raw `pandas_ta` column names (e.g., `BBL_20_2.0`)
instead of the stable names (`upper`, `middle`, `lower`) the notebook expects. The fix
normalizes the column names inside the wrapper function.

## Technical Context

**Language/Version**: Python 3.12 (local), Python 3.11 (CI)

**Primary Dependencies**: `pandas_ta==0.3.14b`, `pandas`

**Storage**: N/A

**Testing**: Manual notebook execution + CI smoke test (`ci-notebook-smoke.yml`)

**Target Platform**: macOS, Linux (dev + CI)

**Project Type**: Educational course library + Jupyter notebooks

**Performance Goals**: N/A (single function rename)

**Constraints**: Must not break other notebooks that import `bollinger_bands`.

**Scale/Scope**: Single function fix in `curso/lib/indicators.py`.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Spec-First Delivery**: ✅ `spec.md` defines the bug, acceptance tests, and measurable outcomes.
- **Independent Value Slices**: ✅ Single slice (column rename in wrapper) yields immediate value.
- **Verifiable Outcomes**: ✅ Acceptance scenarios are reproducible locally and in CI.
- **Traceable Artifacts**: ✅ Changes touch exactly one file (`curso/lib/indicators.py`).
- **Minimal, Explicit Change**: ✅ A 1-line column rename in the wrapper — no notebook edits needed.

## Project Structure

### Documentation (this feature)

```text
specs/005-fix-notebook-04/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── bollinger-bands.md  # Phase 1 output
└── tasks.md             # Phase 2 output (NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
curso/
└── lib/
    └── indicators.py    # Fix: normalize bollinger_bands() return columns
```

**Structure Decision**: Existing single-project layout. Only one library file changes.

## Complexity Tracking

No constitution violations detected. The change is a single column rename in a wrapper function.

## Phase 0: Research

See [research.md](research.md). Key finding: `pandas_ta.bbands()` returns columns with
parameter-encoded names (`BBL_20_2.0`, `BBM_20_2.0`, `BBU_20_2.0`, etc.). The
`bollinger_bands()` wrapper must rename them to stable names (`lower`, `middle`, `upper`,
`bandwidth`, `percent`) before returning.

## Phase 1: Design & Contracts

- [data-model.md](data-model.md): Column mapping from `pandas_ta` to stable names
- [contracts/bollinger-bands.md](contracts/bollinger-bands.md): Return contract for `bollinger_bands()`
- [quickstart.md](quickstart.md): Steps to verify the fix

## Constitution Re-Check (post-design)

- **Spec-First Delivery**: ✅ Spec, research, data model, and contract are complete.
- **Independent Value Slices**: ✅ Single-slice fix with immediate user value.
- **Verifiable Outcomes**: ✅ Quickstart provides a reproducible verification script.
- **Traceable Artifacts**: ✅ All artifacts trace back to the spec and to `curso/lib/indicators.py`.
- **Minimal, Explicit Change**: ✅ One column rename in the wrapper; no notebook edits.

## Phase 2: Implementation

1. In `curso/lib/indicators.py`, update `bollinger_bands()` to rename the returned
   DataFrame columns from `pandas_ta` names to `['lower', 'middle', 'upper', 'bandwidth', 'percent']`.
2. Verify locally: run `04_estrategia.ipynb` steps 0 → 1 → 2 without error.
3. Run CI smoke tests.

## Done Criteria

- All design artifacts created: `research.md`, `data-model.md`, `contracts/bollinger-bands.md`, `quickstart.md`.
- `bollinger_bands()` returns stable column names.
- Notebook `04_estrategia.ipynb` completes step 2 without `KeyError`.
- CI smoke tests pass.
