# Feature Specification: JupyterLab Markdown Extensions

**Feature Branch**: `003-jupyterlab-markdown-extensions`

**Created**: 2026-05-29

**Status**: Draft

**Input**: User description: "quisiera añadir complementos a jupyter lab para poder leer de forma correcta ficheros markdown, incluyendo si es posible diagramas tipo mermaid u otros"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Visualizar Markdown con formato completo en JupyterLab (Priority: P1)

Como estudiante del curso, quiero abrir archivos `.md` (README, specs) directamente
en JupyterLab y verlos renderizados con formato completo (tablas, listas, código,
encabezados, enlaces), para no necesitar salir del entorno de notebooks.

**Why this priority**: Los READMEs de cada capítulo son la guía teórica del curso; sin renderizado correcto la experiencia es muy pobre.

**Independent Test**: Abrir `curso/capitulo-00-fundamentos/README.md` en JupyterLab y verificar que se renderiza con tablas, bloques de código y listas visibles correctamente.

**Acceptance Scenarios**:

1. **Given** JupyterLab arrancado con las extensiones instaladas, **When** el usuario abre un archivo `.md` con tablas y bloques de código, **Then** el contenido se renderiza con formato correcto (tablas alineadas, sintaxis coloreada).
2. **Given** un README con enlaces relativos a otros archivos del repo, **When** el usuario hace clic en un enlace, **Then** el archivo destino se abre en JupyterLab.

---

### User Story 2 - Renderizar diagramas Mermaid en Markdown (Priority: P2)

Como estudiante, quiero que los bloques de código marcados como `mermaid` dentro de
archivos Markdown se rendericen como diagramas visuales (flowchart, sequence, etc.)
directamente en JupyterLab.

**Why this priority**: Los diagramas facilitan la comprensión de flujos de estrategia y arquitectura del curso.

**Independent Test**: Insertar un bloque ```mermaid con un flowchart simple en un archivo `.md`, abrirlo en JupyterLab y verificar que se muestra el diagrama gráfico.

**Acceptance Scenarios**:

1. **Given** un archivo Markdown con un bloque `mermaid` de tipo `flowchart TD`, **When** el usuario lo abre en JupyterLab, **Then** se renderiza un diagrama visual en lugar del código fuente.
2. **Given** un bloque `mermaid` con error de sintaxis, **When** el usuario lo abre, **Then** se muestra un mensaje de error legible (no un crash).

---

### User Story 3 - Instalación sencilla de las extensiones (Priority: P3)

Como usuario nuevo, quiero que las extensiones de Markdown/Mermaid se instalen
automáticamente como parte del setup del curso, sin pasos manuales adicionales.

**Why this priority**: Reducir fricción de onboarding; el entorno debe estar listo tras ejecutar el script de setup.

**Independent Test**: Ejecutar `./scripts/setup_env.sh` y verificar que `jupyter lab` muestra Markdown renderizado y diagramas Mermaid sin configuración adicional.

**Acceptance Scenarios**:

1. **Given** un entorno recién creado con `setup_env.sh`, **When** el usuario abre JupyterLab y navega a un `.md` con Mermaid, **Then** el diagrama se renderiza correctamente.

---

### Edge Cases

- Archivos Markdown con bloques de código de lenguajes no soportados por la extensión (deben mostrarse como texto plano sin error).
- Diagramas Mermaid muy grandes o complejos que puedan tardar en renderizarse.
- JupyterLab ejecutado en modo headless (CI) — las extensiones no deben causar errores aunque no haya renderizado visual.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El entorno debe incluir una extensión de JupyterLab que renderice archivos Markdown con soporte completo de GFM (GitHub Flavored Markdown): tablas, listas de tareas, bloques de código con sintaxis resaltada.
- **FR-002**: El entorno debe incluir una extensión que renderice bloques `mermaid` como diagramas SVG/canvas dentro del visor Markdown de JupyterLab.
- **FR-003**: Las extensiones deben instalarse automáticamente al ejecutar el script de setup (`scripts/setup_env.sh`) o al instalar `curso/requirements.txt` / `curso/requirements-dev.txt`.
- **FR-004**: Las extensiones deben ser compatibles con JupyterLab 4.x y Python 3.11.
- **FR-005**: Documentar en quickstart las extensiones incluidas y cómo verificar que funcionan.

### Key Entities

- **jupyterlab-myst**: extensión para renderizado Markdown avanzado (MyST/GFM).
- **jupyterlab-mermaid**: extensión para diagramas Mermaid en celdas Markdown y archivos `.md`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: El usuario puede abrir cualquier README del curso en JupyterLab y verlo renderizado con tablas y código formateados en menos de 2 segundos.
- **SC-002**: Un bloque `mermaid` con un diagrama de hasta 20 nodos se renderiza visualmente en el visor Markdown de JupyterLab.
- **SC-003**: La instalación de extensiones no añade más de 60 segundos al tiempo total de `pip install`.
- **SC-004**: El setup automatizado (script) deja el entorno listo sin pasos manuales adicionales.

## Assumptions

- JupyterLab 4.x soporta extensiones instalables vía pip (prebuilt extensions).
- Existen extensiones pip-installable para Mermaid y Markdown avanzado compatibles con JupyterLab 4.
- No se requiere Node.js para instalar extensiones prebuilt.
- El rendimiento de renderizado de Mermaid es aceptable para diagramas del tamaño típico del curso (< 20 nodos).

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Esta especificación define historias independientes (P1..P3) con pruebas reproducibles.
- **Independent Value Slices**: P1 (Markdown renderizado) es entregable y verificable por sí mismo sin P2/P3.
- **Verifiable Outcomes**: Cada User Story incluye acceptance scenarios y pruebas independientes.
- **Minimal, Explicit Change**: Solo se añaden extensiones pip a los requirements; no se modifica lógica de notebooks ni contenido del curso.
