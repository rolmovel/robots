# Feature Specification: Fix `curso` import in notebooks

**Feature Branch**: `004-fix-curso-import`

**Created**: 2026-05-29

**Status**: Draft

**Input**: al ejecutar el notebook del capítulo 0 veo el error "ModuleNotFoundError: No module named 'curso'". Esto ocurre en múltiples notebooks; necesito corregirlo para que los notebooks puedan importarse y ejecutarse sin ajustar rutas manualmente.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Import `curso` works when running notebooks (Priority: P1)

Como estudiante o revisor del curso, quiero abrir y ejecutar los notebooks del repositorio (por ejemplo, `curso/capitulo-00-fundamentos/notebooks/00_intro_openbb.ipynb`) sin editar el código ni modificar `sys.path`, para que la experiencia sea sencilla y reproducible.

**Why this priority**: Los notebooks son el principal artefacto del curso; si `curso` no se importa, ninguna instrucción ni ejemplo funciona.

**Independent Test**: En un entorno nuevo (venv creado por `./scripts/setup_env.sh`), abrir y ejecutar el notebook `curso/capitulo-00-fundamentos/notebooks/00_intro_openbb.ipynb` y confirmar que la celda que hace `from curso.lib.data import ...` se importa sin errores.

**Acceptance Scenarios**:

1. **Given** un entorno virtual limpio donde se ejecutó `./scripts/setup_env.sh`, **When** el usuario abre `00_intro_openbb.ipynb` en JupyterLab y ejecuta la celda que importa módulos de `curso`, **Then** la importación completa sin `ModuleNotFoundError`.
2. **Given** el mismo notebook ejecutado por `nbconvert`/CI en modo headless, **When** el pipeline ejecuta las celdas de ejemplo, **Then** no ocurre `ModuleNotFoundError` y la conversión/smoke test pasa.
3. **Given** un desarrollador que clona el repo y ejecuta scripts localmente, **When** usa `python -c "from curso.lib.data import download_historical"`, **Then** la importación es exitosa.

---

### Edge Cases

- Si un usuario ejecuta el notebook desde un directorio distinto al repositorio raíz, la import debe seguir funcionando.
- Si el repositorio se instala en un entorno global ya con paquetes con nombres colisionantes, la solución debe evitar conflictos (p. ej. instalando el paquete con nombre único o usando editable install en el entorno virtual).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Al ejecutar `./scripts/setup_env.sh` en una máquina nueva, el paquete `curso` debe quedar importable desde Python y desde JupyterLab sin necesidad de editar `sys.path` en los notebooks.
- **FR-002**: No se deben exigir cambios manuales en los notebooks para ajustar rutas (evitar `sys.path.append` en celdas de ejemplo).
- **FR-003**: CI debe ejecutar al menos un notebook smoke-test (ya existe) y pasar sin `ModuleNotFoundError` relacionados con `curso`.
- **FR-004**: La solución debe ser compatible con Python 3.11 y no requerir herramientas propietarias externas.

### Non-Functional Requirements

- **NFR-001**: La instalación adicional no debe aumentar significativamente el tiempo de setup (añadir una instalación editable es aceptable).
- **NFR-002**: Mantener compatibilidad con `scripts/setup_env.sh` y la política actual de dependencias en `curso/requirements.txt`.

## Success Criteria *(mandatory)*

- **SC-001**: Ejecutar `./scripts/setup_env.sh` en un entorno limpio y luego ejecutar `python -c "import curso; print('OK')"` devuelve `OK` sin errores.
- **SC-002**: El notebook `curso/capitulo-00-fundamentos/notebooks/00_intro_openbb.ipynb` se ejecuta (por nbconvert or Jupyter) en CI sin `ModuleNotFoundError: No module named 'curso'`.
- **SC-003**: Documentación (`quickstart.md`) actualizada con el comportamiento y verificación, y ejemplo de import exitoso.

## Assumptions

- Los notebooks esperan que el paquete `curso` esté disponible como un package Python (es decir, importable por nombre `curso`).
- Es aceptable instalar el repo en modo editable (`pip install -e .`) durante el setup para exponer `curso` como paquete.
- No se desea modificar todos los notebooks para añadir hacks de `sys.path`.

## Implementation Options (informed defaults)

- Option A (recommended): Add a minimal `pyproject.toml`/`setup.cfg` and update `scripts/setup_env.sh` to `pip install -e .` as part of setup. This installs the repository as a package in the venv, making `curso` importable.
- Option B: Modify `scripts/setup_env.sh` to export `PYTHONPATH=$PWD` or create a small activation helper that sets `PYTHONPATH` when activating the venv. Simpler but may be less explicit than installing the package.
- Option C: Add an `__init__.py` and restructuring; however installing the package is the cleaner long-term approach.

## Key Entities

- **curso**: Top-level package containing notebooks and source code (must be importable).
- **setup_env.sh**: Script responsible for creating venv and installing dependencies; primary integration point for the fix.
- **CI pipelines**: `.github/workflows/ci-notebook-smoke.yml` and `ci-install-check.yml` must validate the fix.

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: This spec describes the problem, acceptance tests, and measurable success criteria.
- **Independent Value Slices**: P1 (fixing imports) is independently valuable and testable.
- **Verifiable Outcomes**: Acceptance scenarios include reproducible tests and CI automation.
- **Minimal, Explicit Change**: Prefer small packaging + setup change vs mass edits in notebooks.
