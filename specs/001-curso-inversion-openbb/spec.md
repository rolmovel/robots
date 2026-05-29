# Feature Specification: Curso de Inversion en Bolsa de Principiante a Experto con OpenBB

**Feature Branch**: `001-crear-curso-inversion`

**Created**: 2026-05-29

**Status**: Draft

**Input**: User description: "quiero crear una tarea que NO sea de desarrollo, mas bien de investigacion. Quiero crear un curso de inversion en bolsa de principiante a experto. El objetivo es aprender a crear tus propias estrategias de inversion y automatizarlas. Partimos de OpenBB como plataforma de datos abiertas. En el primer capitulo, deberiamos de tener inforamcion general sobre inversion, y a partir de este empezamos ya directamente con un captitulo por estrategia, incrementando la complejidad. De cada una de estas estrategias podremos crear nuestras propia especioficacion para posteriormente crear el robot. Al final del curso tengo que tener claros todos los ceonceptos siendo capaz de crear mis agentes de inversion con backtesting para evaluacion de resultadaos"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Capítulos con entrega de automatización y backtesting (Priority: P1)

Como estudiante quiero recorrer capítulos organizados por estrategia donde cada capítulo termina con:

- una especificación clara y ejecutable de la estrategia,
- una guía para la implementación automatizada mínima que ejecuta la estrategia sobre datos de OpenBB,

**Why this priority**: Fusiona teoría y práctica; garantiza que el estudiante pueda diseñar, automatizar y evaluar una estrategia al terminar cada capítulo.

**Independent Test**: Para cada capítulo, el estudiante debe entregar la especificación, el código de automatización y un notebook o script de backtesting que produzca las métricas de evaluación solicitadas.

**Acceptance Scenarios**:

1. **Given** una estrategia enseñada en el capítulo (ej. índice de empresas del sector salud por debajo de la media mensual), **When** el estudiante completa el capítulo, **Then** entrega:
	- especificación operativa (reglas de entrada/salida, gestión de riesgo, parámetros),
	- código que implementa la lógica y descarga datos desde OpenBB,
	- resultados de backtesting con métricas (rendimiento, drawdown, Sharpe, número de operaciones) y conclusiones.
2. **Given** la entrega del capítulo, **When** otro estudiante reproduce el notebook con los mismos datos, **Then** obtiene resultados concordantes y puede verificar la especificación.
3. **Given** la estrategia ejemplo inicial (sector salud, precio por debajo de MA(30) durante 1 mes), **When** el estudiante la implementa, **Then** demuestra que el agente ejecuta señales de entrada/salida y produce un informe de backtesting.


### Edge Cases

- Que ocurre si los datos historicos necesarios para una estrategia no estan disponibles o tienen huecos relevantes.
- Como se trata una estrategia que aparenta alto rendimiento en backtesting pero presenta riesgo extremo o sobreajuste.
- Como se procede cuando una estrategia no puede traducirse de forma clara a una especificacion operativa.
- Que acciones se toman si el estudiante intenta saltar capitulos sin cumplir prerrequisitos de comprension.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El curso MUST incluir un capitulo inicial de fundamentos de inversion en bolsa con terminologia basica y principios de riesgo/rendimiento.
- **FR-002**: El curso MUST presentar el rol de OpenBB como fuente de datos abiertos para analisis de estrategias.
- **FR-003**: El curso MUST organizar los capitulos por estrategia, con complejidad incremental y prerrequisitos explicitos.
- **FR-004**: Cada capitulo de estrategia MUST definir objetivo, contexto de uso, reglas operativas y criterios de exito.
- **FR-005**: Cada capitulo MUST incluir al menos un ejercicio practico evaluable.
- **FR-006**: El contenido MUST permitir que el estudiante documente una especificacion estructurada por cada estrategia aprendida.
- **FR-007**: La especificacion de estrategia MUST incluir reglas de entrada/salida, gestion de riesgo, supuestos y metricas de evaluacion.
- **FR-008**: El curso MUST incluir una seccion dedicada a principios de automatizacion de estrategias y diseno de agentes de inversion.
- **FR-009**: El curso MUST incluir un modulo de backtesting con metodologia de evaluacion y criterios para interpretar resultados.
- **FR-010**: El curso MUST requerir una evaluacion final donde el estudiante integre conceptos y justifique una estrategia automatizable.
- **FR-011**: El curso MUST explicitar limitaciones, sesgos y riesgos del backtesting para evitar interpretaciones engañosas.
- **FR-012**: El curso MUST definir resultados de aprendizaje observables para nivel principiante, intermedio y experto.
 - **FR-012**: El curso MUST definir resultados de aprendizaje observables para nivel principiante, intermedio y experto.
 - **FR-013**: Cada capítulo de estrategia MUST entregar una implementación automatizada mínima (script/agent/notebook) y un ejercicio de backtesting reproducible con informe de métricas.

### Key Entities *(include if feature involves data)*

- **ModuloCurso**: Unidad de contenido del curso con nivel, objetivo, prerrequisitos, materiales y criterios de evaluacion.
- **EstrategiaInversion**: Metodo de inversion con hipotesis, reglas operativas, horizonte temporal, perfil de riesgo y condiciones de mercado.
- **EspecificacionEstrategia**: Documento estructurado creado por el estudiante para habilitar implementacion posterior de un robot.
- **EjercicioBacktesting**: Actividad de evaluacion con datos historicos, metricas reportadas, interpretacion y decision final.
- **PerfilEstudiante**: Estado de avance del estudiante con nivel alcanzado y competencias demostradas.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Al menos 90% de los estudiantes que completan el capitulo 1 aprueban una evaluacion de fundamentos en el primer intento.
- **SC-002**: El 100% de los capitulos de estrategia publicados incluyen objetivo, reglas, ejercicio practico y criterio de aprobacion.
- **SC-003**: Al finalizar el curso, al menos 80% de los estudiantes entregan una especificacion de estrategia completa y revisable por pares sin ambiguedades criticas.
- **SC-004**: Al menos 75% de los estudiantes completan una evaluacion de backtesting con conclusiones justificadas por metricas y riesgos.
- **SC-005**: Al menos 70% de los estudiantes completan una entrega final donde definen un agente de inversion conceptual y su plan de validacion.
 - **SC-005**: Al menos 70% de los estudiantes completan una entrega final donde definen un agente de inversion conceptual y su plan de validacion.
 - **SC-006**: El 100% de los capítulos publicados incluyen artefactos de automatización y backtesting reproducibles (código + notebook/informe) antes de considerarse finalizados.

## Assumptions

- El curso se orienta a aprendizaje educativo y no constituye asesoria financiera personalizada.
- Los estudiantes tienen acceso a herramientas basicas de analisis y conectividad para consultar datos abiertos.
- La implementacion tecnica de robots se realiza en fases posteriores a partir de especificaciones, no en este alcance inicial.
- El alcance inicial prioriza mercados liquidos y datos historicos accesibles para aprendizaje reproducible.

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Esta especificacion define historias, requisitos, supuestos, casos borde y resultados medibles.
- **Independent Value Slices**: Cada historia representa un bloque de valor independiente y verificable.
- **Verifiable Outcomes**: Cada historia incluye escenarios de aceptacion y criterio de prueba independiente.
- **Minimal, Explicit Change**: El alcance se limita a investigacion y diseno curricular; la construccion de robots queda para especificaciones posteriores.
