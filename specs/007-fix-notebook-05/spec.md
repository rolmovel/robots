# Feature Specification: Fix notebook 05 execution

**Feature Branch**: `007-fix-notebook-05`

**Created**: 2026-05-29

**Status**: Draft

**Input**: User description: "ejecuta el notebook 05 y corrige errores."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ejecutar el notebook 05 sin bloqueos (Priority: P1)

Como estudiante del curso, quiero ejecutar el notebook de backtesting del capitulo 05 de principio a fin sin errores bloqueantes, para poder completar el flujo de aprendizaje sobre Donchian breakout y trailing stop sin tener que depurar el material.

**Why this priority**: El notebook es el artefacto principal del capitulo. Si una celda falla, el estudiante no puede completar el ejercicio ni validar la estrategia propuesta.

**Independent Test**: Abrir el notebook 05 en un entorno del curso ya preparado, ejecutar sus celdas en orden desde el inicio hasta el cierre y confirmar que todas terminan sin errores bloqueantes.

**Acceptance Scenarios**:

1. **Given** un entorno del curso correctamente preparado, **When** el usuario ejecuta el notebook 05 desde la primera celda hasta la ultima, **Then** todas las celdas completan sin errores bloqueantes y el usuario obtiene las tablas y visualizaciones esperadas.
2. **Given** un kernel reiniciado, **When** el usuario vuelve a ejecutar las celdas del notebook 05 en el orden documentado, **Then** los resultados vuelven a generarse sin requerir ediciones manuales del notebook.

---

### User Story 2 - Identificar con claridad el paso fallido (Priority: P2)

Como mantenedor del curso, quiero que cualquier paso defectuoso del notebook 05 quede identificado de forma reproducible y acotada, para corregirlo con un cambio minimo y evitar regresiones en el resto del flujo.

**Why this priority**: Un fallo no acotado obliga a revisar celdas y helpers sin foco. Acotar el error reduce el riesgo de tocar codigo correcto del curso.

**Independent Test**: Ejecutar el notebook 05 y comprobar que el paso originalmente defectuoso queda descrito con evidencia suficiente para reproducirlo y validar su correccion.

**Acceptance Scenarios**:

1. **Given** un notebook 05 con un fallo reproducible, **When** se ejecuta el flujo en orden, **Then** el paso que falla queda claramente identificado junto con su condicion de reproduccion.
2. **Given** que la correccion fue aplicada, **When** se reejecuta el notebook 05, **Then** el paso antes defectuoso completa correctamente sin introducir errores nuevos en pasos anteriores o posteriores.

---

### User Story 3 - Conservar el valor didactico del analisis (Priority: P3)

Como estudiante, quiero seguir viendo las metricas, tablas y graficos del notebook 05 despues de la correccion, para interpretar el efecto del trailing stop y del position sizing sin perder contenido didactico.

**Why this priority**: La correccion no debe resolver el error a costa de degradar la parte visual o analitica del notebook.

**Independent Test**: Ejecutar el notebook corregido y comprobar que siguen apareciendo las salidas previstas para backtest, drawdown, analisis del trailing stop y conclusiones.

**Acceptance Scenarios**:

1. **Given** el notebook 05 corregido, **When** el usuario llega a las secciones de backtest y analisis, **Then** las metricas y visualizaciones siguen estando disponibles y son interpretables.

### Edge Cases

- El notebook depende de datos descargados y puede fallar si el origen de datos no responde o devuelve una serie vacia.
- Una estrategia de breakout puede no generar operaciones suficientes para alguna combinacion de parametros y dejar metricas parciales o poco representativas.
- Un paso de analisis puede reutilizar variables creadas antes y fallar si el notebook no se ejecuta en el orden esperado.
- La correccion puede requerir distinguir entre un problema del notebook y un problema del entorno interactivo donde se ejecuta.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El notebook del capitulo 05 MUST poder ejecutarse de principio a fin sin errores bloqueantes cuando el entorno del curso esta correctamente preparado.
- **FR-002**: La revision MUST identificar el paso concreto del notebook 05 que falla y la condicion reproducible bajo la que aparece el error.
- **FR-003**: La correccion MUST limitarse al menor cambio necesario para que el paso defectuoso complete correctamente.
- **FR-004**: La correccion MUST preservar las metricas, tablas y visualizaciones previstas por el notebook 05.
- **FR-005**: El notebook corregido MUST seguir siendo reejecutable desde un kernel limpio sin depender de estado oculto o de ediciones manuales intermedias.
- **FR-006**: La resolucion MUST dejar una forma repetible de validar que el notebook 05 vuelve a funcionar segun el flujo del curso.

### Key Entities *(include if feature involves data)*

- **Notebook 05**: Material interactivo del capitulo breakout que combina descarga de datos, definicion de estrategia, backtest y analisis.
- **Paso defectuoso**: Celda o tramo concreto del notebook 05 que interrumpe la ejecucion completa y define el alcance minimo de la correccion.
- **Salida analitica**: Tablas, metricas y graficos que el notebook debe seguir mostrando tras la correccion.
- **Validacion reproducible**: Evidencia de ejecucion suficiente para distinguir entre un defecto del notebook y un problema de entorno.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: El 100% de las ejecuciones de validacion del notebook 05 en un entorno limpio completan todas las celdas sin errores bloqueantes.
- **SC-002**: Un revisor puede identificar en menos de 5 minutos el paso originalmente defectuoso y confirmar que la correccion lo resuelve.
- **SC-003**: El notebook corregido sigue mostrando las salidas analiticas principales esperadas por el capitulo sin suprimir contenido didactico.
- **SC-004**: La incidencia queda acotada a un comportamiento verificable del notebook 05 y puede pasar a planificacion sin ambiguedades pendientes.

## Assumptions

- El entorno base del curso ya tiene instaladas las dependencias necesarias para ejecutar notebooks del repositorio.
- El alcance de esta feature se limita al notebook `curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb` y a los helpers directamente implicados por un fallo reproducible de ese notebook.
- Si el notebook funciona en Jupyter pero no en otro cliente, la resolucion debe centrarse en el defecto reproducible del material o en una diferencia de ejecucion claramente documentable.
- La correccion esperada debe ser pequena y compatible con el resto de notebooks del curso.

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Este documento define historias, requisitos, edge cases, supuestos y resultados medibles para la incidencia del notebook 05.
- **Independent Value Slices**: P1 restaura la ejecucion completa; P2 acota el error; P3 protege el valor didactico del notebook.
- **Verifiable Outcomes**: Cada historia incluye escenarios de aceptacion y una forma independiente de validacion.
- **Minimal, Explicit Change**: El alcance queda limitado al notebook 05 y al menor cambio necesario para corregir el paso defectuoso.
