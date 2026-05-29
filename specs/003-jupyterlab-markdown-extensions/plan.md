# Implementation Plan: JupyterLab Markdown Extensions

**Branch**: `003-jupyterlab-markdown-extensions` | **Date**: 2026-05-29 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/003-jupyterlab-markdown-extensions/spec.md`

## Summary

Añadir extensiones de JupyterLab para renderizado completo de Markdown (GFM) y diagramas Mermaid dentro del entorno del curso. Las extensiones se instalan vía pip como prebuilt extensions y se integran en el script de setup y requirements existentes.

## Technical Context

**Language/Version**: Python 3.11

**Primary Dependencies**: jupyterlab>=4.0,<5.0 (ya instalado), jupyterlab-myst, jupyterlab-mermaid (por añadir)

**Storage**: N/A

**Testing**: Manual (verificación visual en JupyterLab) + CI smoke (extensiones cargables sin error)

**Target Platform**: macOS/Linux (entorno local de desarrollo)

**Project Type**: Configuración de entorno / extensiones pip

**Performance Goals**: Renderizado < 2s para archivos Markdown típicos del curso

**Constraints**: No requiere Node.js; solo extensiones prebuilt pip-installable; compatible JupyterLab 4.x

**Scale/Scope**: 2-3 paquetes pip adicionales

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Spec-First Delivery: `spec.md` incluye historias priorizadas (P1-P3), requisitos funcionales, edge cases, supuestos y resultados medibles.
- ✅ Independent Value Slices: P1 (Markdown) es independiente de P2 (Mermaid) y P3 (automatización).
- ✅ Verifiable Outcomes: Cada historia tiene acceptance scenarios con Given/When/Then reproducibles.
- ✅ Traceable Artifacts: Los cambios planificados apuntan a archivos concretos (`curso/requirements.txt`, `scripts/setup_env.sh`, quickstart).
- ✅ Minimal, Explicit Change: Solo se añaden paquetes pip y documentación; no se modifica lógica de notebooks.

## Project Structure

### Documentation (this feature)

```text
specs/003-jupyterlab-markdown-extensions/
├── plan.md              # This file
├── research.md          # Phase 0: investigación de extensiones
├── data-model.md        # Phase 1: entidades y configuración
├── quickstart.md        # Phase 1: guía de verificación
└── contracts/           # Phase 1: contrato de entrega
```

### Source Code (repository root)

```text
curso/
├── requirements.txt          # Añadir extensiones aquí
└── requirements-dev.txt      # Extensiones de desarrollo (si aplica)

scripts/
└── setup_env.sh              # Ya instala requirements; no requiere cambios

specs/001-curso-inversion-openbb/
└── quickstart.md             # Actualizar con nota sobre extensiones
```

**Structure Decision**: No se crea código nuevo; se modifican requirements y documentación existentes.

## Complexity Tracking

> No hay violaciones de la constitución. El cambio es mínimo (añadir pips a requirements).
