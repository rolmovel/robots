# Implementation Plan: Fix notebook 05 execution

**Branch**: `007-fix-notebook-05` | **Date**: 2026-05-29 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/007-fix-notebook-05/spec.md`

## Summary

La validacion en el entorno actual muestra que `curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb` ejecuta todas sus celdas sin errores bloqueantes. El trabajo de esta feature se centra en convertir esa observacion en evidencia reproducible y, solo si aparece un fallo dependiente del cliente o del estado del notebook, aplicar el cambio minimo necesario para preservar el flujo didactico.

## Technical Context

**Language/Version**: Python 3.12 en el kernel activo del notebook

**Primary Dependencies**: pandas, numpy, matplotlib, backtesting.py, helpers de `curso.lib`

**Storage**: N/A (datos historicos descargados en memoria)

**Testing**: Ejecucion manual del notebook en VS Code/Jupyter con validacion de tablas y graficos

**Target Platform**: Notebook Python en VS Code y Jupyter

**Project Type**: Material educativo basado en notebooks y libreria compartida

**Performance Goals**: N/A para esta incidencia; la meta es ejecucion interactiva correcta de extremo a extremo

**Constraints**: Mantener cambios minimos, preservar el valor didactico y no introducir regresiones en notebooks o helpers compartidos

**Scale/Scope**: Un notebook de capitulo (`05_backtesting.ipynb`) y, solo si es imprescindible, helpers directamente implicados

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] Spec-First Delivery: `spec.md` incluye historias priorizadas, requisitos, supuestos, edge cases y resultados medibles.
- [x] Independent Value Slices: P1 cubre la ejecucion completa; P2 acota un posible fallo reproducible; P3 protege las salidas analiticas.
- [x] Verifiable Outcomes: Cada historia incluye escenarios Given/When/Then y una validacion independiente reproducible.
- [x] Traceable Artifacts: El trabajo se mapea a `curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb` y a cualquier helper directamente implicado.
- [x] Minimal, Explicit Change: El plan limita cualquier correccion al menor cambio necesario y documenta que actualmente no se reproduce fallo en este entorno.

**Gate Result**: PASS

## Project Structure

### Documentation (this feature)

```text
specs/007-fix-notebook-05/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

### Source Code (repository root)

```text
curso/
├── lib/
│   ├── backtest.py
│   ├── data.py
│   └── reporting.py
└── capitulo-05-breakout/
    └── notebooks/
        └── 05_backtesting.ipynb
```

**Structure Decision**: Se mantiene la estructura actual. El punto de entrada de la validacion y de cualquier futura correccion es `curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb`; los helpers de `curso/lib/` solo entran en alcance si un fallo reproducible lo exige.

**Post-Design Constitution Check**: PASS. Los artefactos de `research.md`, `data-model.md`, `contracts/` y `quickstart.md` mantienen trazabilidad directa con `spec.md`, no introducen complejidad extra y dejan una validacion reproducible desde kernel limpio.

## Complexity Tracking

No hay violaciones de la constitucion en el estado actual. Si no se reproduce un fallo de codigo, la implementacion debera limitarse a evidencia y normalizacion minima del notebook.
