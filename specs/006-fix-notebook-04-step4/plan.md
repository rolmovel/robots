# Implementation Plan: Fix notebook 04 backtesting step 4

**Branch**: `006-fix-notebook-04-step4` | **Date**: 2026-05-29 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/006-fix-notebook-04-step4/spec.md`

## Summary

El paso 4 del notebook `04_backtesting.ipynb` falla porque pasa objetos `pd.Series` (resultados crudos de `run_backtest`) a `compare_strategies`, que espera objetos `BacktestMetrics`. La corrección consiste en invocar `extract_metrics()` sobre cada resultado antes de la comparación.

## Technical Context

**Language/Version**: Python 3.11

**Primary Dependencies**: backtesting.py, pandas, matplotlib, numpy

**Storage**: N/A (datos descargados en memoria vía `download_historical`)

**Testing**: Ejecución manual del notebook (validación visual en JupyterLab/VS Code)

**Target Platform**: JupyterLab / VS Code Notebooks (macOS/Linux)

**Project Type**: Material educativo (notebooks interactivos + librería compartida)

**Performance Goals**: N/A (ejecución interactiva, no hay requisitos de latencia)

**Constraints**: La corrección no debe modificar la librería compartida ni afectar otros notebooks

**Scale/Scope**: 1 celda en 1 notebook

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] Spec-First Delivery: `spec.md` incluye historias priorizadas, requisitos, supuestos, edge cases y outcomes medibles.
- [x] Independent Value Slices: P1 (ejecución sin errores) y P2 (visualización comparativa) son independientemente implementables.
- [x] Verifiable Outcomes: Cada historia incluye escenarios de aceptación Given/When/Then y test independiente.
- [x] Traceable Artifacts: El trabajo se mapea directamente a `curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb`, celda del paso 4.
- [x] Minimal, Explicit Change: Cambio de 1 línea en 1 celda. Sin complejidad adicional.

**Gate Result**: PASS — No violations. Proceeding to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/006-fix-notebook-04-step4/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
curso/
├── lib/
│   ├── backtest.py      # compare_strategies(), extract_metrics(), BacktestMetrics
│   └── reporting.py     # plot_comparison()
└── capitulo-04-mean-reversion/
    └── notebooks/
        └── 04_backtesting.ipynb  # Target file — step 4 cell fix
```

**Structure Decision**: Existing repository layout. Only the notebook cell content needs modification. No new files or structural changes required.

## Complexity Tracking

No violations. Single-line fix in a notebook cell — minimal complexity.
