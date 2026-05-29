# Implementation Plan: Curso de Inversión en Bolsa (Principiante → Experto) con OpenBB

**Branch**: `001-crear-curso-inversion` | **Date**: 2026-05-29 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-curso-inversion-openbb/spec.md`

## Summary

Curso de investigación y desarrollo práctico que lleva al estudiante desde conceptos
básicos de inversión en bolsa hasta la creación y evaluación de agentes automatizados
con backtesting. Cada capítulo introduce una estrategia de mercado de complejidad
creciente; al finalizarlo el estudiante entrega especificación, automatización mínima
(Python + OpenBB) y resultados de backtesting reproducibles.

## Technical Context

**Language/Version**: Python 3.11+

**Primary Dependencies**: OpenBB SDK (datos de mercado), pandas, numpy, matplotlib/plotly (visualización), backtesting.py o vectorbt (motor de backtesting)

**Storage**: Ficheros locales (CSV/Parquet para datos históricos descargados de OpenBB)

**Testing**: Validación manual de notebooks + reproducibilidad de resultados de backtesting

**Target Platform**: Entorno local (Jupyter/VS Code notebooks) multiplataforma

**Project Type**: Contenido educativo + notebooks ejecutables (investigación/curso)

**Performance Goals**: N/A (orientado a aprendizaje, no a producción)

**Constraints**: Datos abiertos exclusivamente (sin necesidad de licencia premium); estrategias educativas, sin recomendación financiera

**Scale/Scope**: ~6-8 capítulos, 1 estrategia por capítulo, ~1 notebook por capítulo + 1 especificación SDD por estrategia

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principio | Evaluación |
|-----------|-----------|
| Spec-First Delivery | ✅ spec.md incluye historias priorizadas, requisitos, supuestos, edge cases y métricas |
| Independent Value Slices | ✅ Cada capítulo es auto-contenido y entrega valor independiente |
| Verifiable Outcomes | ✅ Escenarios Given/When/Then definidos; test = entrega reproducible por otro estudiante |
| Traceable Artifacts | ✅ Plan referencia spec; tareas incluirán rutas concretas por capítulo |
| Minimal, Explicit Change | ✅ Alcance limitado a diseño curricular + notebooks; robots productivos quedan fuera |

**Gate result**: PASS — proceder a Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/001-curso-inversion-openbb/
├── plan.md              # This file
├── research.md          # Phase 0: investigación de estrategias y herramientas
├── data-model.md        # Phase 1: entidades del curso
├── quickstart.md        # Phase 1: guía rápida para comenzar
├── contracts/           # Phase 1: contratos de entrega por capítulo
└── tasks.md             # Phase 2 (/speckit.tasks)
```

### Source Code (repository root)

```text
curso/
├── capitulo-00-fundamentos/
│   ├── README.md                 # Teoría y conceptos
│   └── notebooks/
│       └── 00_intro_openbb.ipynb
├── capitulo-01-media-movil/
│   ├── README.md
│   ├── spec.md                   # Especificación SDD de la estrategia
│   └── notebooks/
│       ├── 01_estrategia.ipynb
│       └── 01_backtesting.ipynb
├── capitulo-02-momentum/
│   ├── README.md
│   ├── spec.md
│   └── notebooks/
│       ├── 02_estrategia.ipynb
│       └── 02_backtesting.ipynb
├── capitulo-NN-.../              # Capítulos sucesivos
├── lib/
│   ├── data.py                   # Helpers descarga OpenBB
│   ├── backtest.py               # Helpers backtesting reutilizables
│   └── reporting.py              # Helpers métricas y visualización
└── requirements.txt
```

**Structure Decision**: Estructura tipo monorepo educativo con un directorio por capítulo.
Cada capítulo contiene su README con teoría, su spec SDD y notebooks ejecutables.
`curso/lib/` agrupa utilidades compartidas que van creciendo con cada capítulo.

## Complexity Tracking

> No se detectan violaciones de constitución que requieran justificación.
