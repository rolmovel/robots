# Feature Specification: Fix notebook 04 execution at step 2

**Feature Branch**: `005-fix-notebook-04`

**Created**: 2026-05-29

**Status**: Draft

**Input**: User description: "Revisar la ejecucion del notebook 04, falla en el paso 2"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ejecutar el notebook 04 sin bloqueo en el paso 2 (Priority: P1)

Como estudiante o revisor del curso, quiero ejecutar el notebook del capitulo 04 hasta completar el paso 2 sin errores bloqueantes, para poder seguir el flujo de aprendizaje previsto sin detenerme a depurar el entorno o el contenido.

**Why this priority**: El notebook es el artefacto principal de aprendizaje del capitulo. Si el paso 2 falla, el recorrido queda interrumpido antes de completar la estrategia central del tema.

**Independent Test**: En un entorno preparado segun la documentacion vigente, abrir el notebook del capitulo 04, ejecutar desde el inicio hasta terminar el paso 2 y confirmar que no aparece ningun error bloqueante ni es necesario modificar celdas manualmente.

**Acceptance Scenarios**:

1. **Given** un usuario con el entorno del curso preparado segun las instrucciones actuales, **When** ejecuta el notebook 04 desde el inicio hasta el paso 2, **Then** el paso 2 finaliza correctamente y el usuario puede continuar con el siguiente bloque.
2. **Given** un kernel reiniciado antes de volver a correr el notebook 04, **When** el usuario reejecuta las celdas necesarias hasta el paso 2 en el orden indicado, **Then** el resultado vuelve a ser consistente y no aparece un nuevo bloqueo en ese punto.

---

### User Story 2 - Entender rapidamente una precondicion incumplida (Priority: P2)

Como revisor del material, quiero que cualquier precondicion faltante relacionada con el paso 2 se manifieste de forma clara y accionable, para distinguir un problema real del notebook de un problema de preparacion o datos.

**Why this priority**: Un fallo opaco en un notebook educativo consume tiempo de revision y genera dudas sobre si el error pertenece al contenido, al entorno o a los datos de entrada.

**Independent Test**: Forzar una ejecucion con una precondicion ausente o invalida y comprobar que el usuario recibe una indicacion clara de que falta, en lugar de un fallo ambiguo o dificil de interpretar.

**Acceptance Scenarios**:

1. **Given** que existe una precondicion no satisfecha para el paso 2, **When** el usuario intenta ejecutar ese paso, **Then** recibe una indicacion clara sobre la causa y la accion necesaria para continuar.
2. **Given** que todas las precondiciones estan satisfechas, **When** el usuario ejecuta el paso 2, **Then** no se muestra ningun mensaje de error ni advertencia irrelevante.

### Edge Cases

- El notebook se ejecuta en un entorno limpio donde no existe estado previo de una sesion anterior.
- El usuario relanza el notebook despues de reiniciar el kernel y depende solo del orden documentado de ejecucion.
- El paso 2 necesita datos, parametros o credenciales que pueden no estar disponibles en todos los entornos de revision.
- El notebook contiene resultados parciales de celdas anteriores y el usuario vuelve a ejecutar solo una parte del flujo.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El notebook del capitulo 04 MUST poder ejecutarse desde el inicio hasta completar el paso 2 sin errores bloqueantes cuando el usuario cumple las precondiciones documentadas del curso.
- **FR-002**: El usuario MUST poder ejecutar el paso 2 sin editar manualmente el contenido del notebook ni aplicar instrucciones ad hoc fuera de la documentacion oficial del curso.
- **FR-003**: Cualquier precondicion necesaria para que el paso 2 funcione MUST estar documentada o mostrarse de forma clara durante la ejecucion.
- **FR-004**: Cuando una precondicion del paso 2 no se cumpla, el sistema MUST comunicar la causa de forma comprensible y orientar la recuperacion esperada.
- **FR-005**: La revision de este problema MUST dejar una forma repetible de comprobar que el notebook 04 vuelve a completar el paso 2 correctamente.

### Key Entities *(include if feature involves data)*

- **Notebook 04**: Material interactivo del capitulo de mean reversion cuyo flujo de aprendizaje debe ejecutarse sin bloqueos hasta el paso 2.
- **Paso 2**: Hito concreto del notebook donde hoy se produce el fallo y que define el alcance minimo de la correccion.
- **Precondicion de ejecucion**: Estado, insumo o configuracion que debe existir para que el paso 2 funcione correctamente.
- **Resultado de revision**: Evidencia verificable de que el problema fue reproducido, entendido y corregido o acotado.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: El 100% de las ejecuciones de validacion acordadas para el notebook 04 en un entorno limpio completan el paso 2 sin errores bloqueantes.
- **SC-002**: Un revisor puede identificar en menos de 5 minutos si un fallo en el paso 2 se debe a una precondicion incumplida o a un defecto real del notebook.
- **SC-003**: Un segundo revisor puede repetir la comprobacion del notebook 04 hasta el paso 2 siguiendo solo la documentacion o las instrucciones formales del repositorio, sin recibir instrucciones adicionales por chat.
- **SC-004**: La incidencia queda acotada a un comportamiento verificable del paso 2, con evidencia suficiente para pasar a planificacion e implementacion sin ambiguedad pendiente.

## Assumptions

- El alcance de esta incidencia se limita al notebook del capitulo 04 y al fallo reproducible en el paso 2.
- El usuario ejecuta el notebook en el orden previsto por el material del curso.
- El entorno base del curso ya dispone de las dependencias y accesos generales esperados para ejecutar notebooks del repositorio.
- Si el paso 2 depende de una precondicion adicional no explicita, esa precondicion debe quedar reflejada como parte de la resolucion de la incidencia.

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Este documento define historias, requisitos, supuestos, casos limite y resultados medibles para la incidencia del notebook 04.
- **Independent Value Slices**: P1 asegura que el flujo educativo vuelve a ser utilizable; P2 asegura que los fallos residuales o de entorno sean interpretables.
- **Verifiable Outcomes**: Cada historia incluye escenarios de aceptacion y una prueba independiente de validacion.
- **Minimal, Explicit Change**: El alcance queda limitado al fallo reproducible en el paso 2 y a la evidencia necesaria para verificar su resolucion.