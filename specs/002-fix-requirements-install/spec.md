# Feature Specification: Fix requirements installation

**Feature Branch**: `002-fix-requirements-install`

**Created**: 2026-05-29

**Status**: Draft

**Input**: User description: "quisiera añadir una nueva especificacion para corregir los problemas de instalacion relacionados con el requirements"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Instalar dependencias en entorno limpio (Priority: P1)

Como desarrollador/estudiante, quiero poder instalar todas las dependencias del curso
en un entorno virtual limpio usando `pip install -r requirements.txt` sin errores,
para ejecutar los notebooks y los ejemplos locales.

**Why this priority**: Sin instalación reproducible el curso no es utilizable.

**Independent Test**: Crear `python -m venv .venv && .venv/bin/pip install -U pip && .venv/bin/pip install -r requirements.txt` en macOS/Linux y comprobar que la instalación finaliza sin errores.

**Acceptance Scenarios**:

1. **Given** un repositorio clonado en una máquina con Python 3.11, **When** el usuario crea un venv y ejecuta `pip install -r requirements.txt`, **Then** la instalación completa sin errores y `jupyter lab` arranca.
2. **Given** la instalación en CI (GitHub Actions ubuntu-latest), **When** se ejecuta el job `install-check`, **Then** el job finaliza con exit code 0.

---

### User Story 2 - Documentación y pasos reproducibles (Priority: P2)

Como usuario nuevo, quiero instrucciones claras y un script de setup para evitar pasos manuales y errores de plataforma.

**Independent Test**: Ejecutar `./scripts/setup_env.sh` en una máquina de desarrollo limpia y verificar que el entorno queda funcional.

**Acceptance Scenarios**:

1. **Given** un sistema macOS con Python 3.11 instalado, **When** el usuario ejecuta `./scripts/setup_env.sh`, **Then** crea un venv y realiza `pip install` correctamente.

---

### User Story 3 - Validación automática en CI (Priority: P3)

Como mantenedor, quiero que el repositorio valide automáticamente que las dependencias instalables y que los notebooks no fallan en el setup inicial.

**Independent Test**: GitHub Actions con job `install-check` y `notebook-smoke` que instalan dependencias y ejecutan un notebook pequeño (ej. 00_intro_openbb.ipynb) en modo no interactivo.

**Acceptance Scenarios**:

1. **Given** un push/PR, **When** se dispara la pipeline, **Then** los jobs `install-check` y `notebook-smoke` pasan.

---

### Edge Cases

- Instalación en máquinas con versiones de Python distintas a 3.11.
- Entornos con dependencias del sistema ausentes (e.g., librerías C) que provoquen fallos en paquetes binarios.
- Red limitada o sin acceso a PyPI.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Actualizar `curso/requirements.txt` con versiones pinneadas comprobadas para Python 3.11.
- **FR-002**: Añadir `requirements-dev.txt` (herramientas de desarrollo) si procede.
- **FR-003**: Añadir script `scripts/setup_env.sh` que crea venv, actualiza `pip`, instala `wheel` y ejecuta `pip install -r curso/requirements.txt`.
- **FR-004**: Añadir job de GitHub Actions `ci/install-check.yml` que prueba la instalación en `ubuntu-latest` y `macos-latest` (si es posible).
- **FR-005**: Añadir job `ci/notebook-smoke.yml` que ejecuta un notebook de ejemplo en modo headless para detectar errores de importación.
- **FR-006**: Documentar los pasos en `specs/001-curso-inversion-openbb/quickstart.md` y en `curso/README.md` con comandos exactos.
- **FR-007**: En caso de paquetes problemáticos con compilación, proveer instrucciones alternativas (rueda precompilada, constraints, o usar `pip install --no-binary` según corresponda).

### Key Artifacts

- `curso/requirements.txt` — archivo de dependencias principal (actualizado)
- `curso/requirements-dev.txt` — dependencias de desarrollo (opcional)
- `scripts/setup_env.sh` — script de automatización de entorno
- `.github/workflows/ci-install-check.yml` — workflow de CI para instalación
- `.github/workflows/ci-notebook-smoke.yml` — workflow que ejecuta notebook de prueba
- `specs/002-fix-requirements-install/checklists/requirements.md` — checklist de calidad

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `pip install -r curso/requirements.txt` completa sin errores en Python 3.11 dentro de 10 minutos en `ubuntu-latest` (GitHub Actions) y local en macOS.
- **SC-002**: El job CI `install-check` pasa en PRs y push a main.
- **SC-003**: El script `scripts/setup_env.sh` crea un entorno funcional y documentado con pasos reproducibles.
- **SC-004**: Reducir el número de issues/reports relacionados con instalación en >50% tras la entrega (medible en el repo issue tracker).

## Assumptions

- Target Python principal: 3.11.
- Acceso a PyPI en la mayoría de los entornos; en entornos restringidos se documentará el uso de caches.
- Usuarios tienen permisos para crear venv y pip en su máquina.
- No se pretende resolver incompatibilidades profundas de sistema (p.ej., dependencias C que requieran instalación avanzada) — se documentarán como pasos adicionales.

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Esta especificación define historias independientes (P1..P3) y pruebas reproducibles.
- **Independent Value Slices**: P1 (instalación reproducible) es entregable y verificable por sí mismo.
- **Verifiable Outcomes**: Cada User Story incluye acceptance scenarios y pruebas independientes.
- **Minimal, Explicit Change**: Cambios propuestos se limitan a archivos de dependencias, scripts de setup y workflows CI; la implementación no modifica la lógica de los notebooks.
