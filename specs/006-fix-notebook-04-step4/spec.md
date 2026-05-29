# Feature Specification: Fix notebook 04 backtesting step 4

**Feature Branch**: `006-fix-notebook-04-step4`

**Created**: 2026-05-29

**Status**: Draft

**Input**: User description: "revisa en el capitulo 04 el backtesting, el paso 4 falla"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ejecutar el paso 4 del notebook 04 sin errores (Priority: P1)

Como estudiante del curso, quiero ejecutar el paso 4 ("Variante: salida en banda superior") del notebook de backtesting del capítulo 04 sin errores, para poder comparar ambas variantes de la estrategia Bollinger y completar el flujo de aprendizaje.

**Why this priority**: El paso 4 es la comparación central del capítulo — sin él, el estudiante no puede evaluar el impacto de distintos puntos de salida en la estrategia de mean reversion, que es el objetivo didáctico principal.

**Independent Test**: En un entorno preparado según las instrucciones del curso, ejecutar el notebook 04 completo desde el inicio hasta el paso 4 inclusive y verificar que se genera la tabla comparativa y el gráfico de barras sin errores.

**Acceptance Scenarios**:

1. **Given** un usuario con el entorno del curso preparado y el notebook 04 ejecutado secuencialmente hasta el paso 3, **When** ejecuta el paso 4 (celda de variante con salida en banda superior), **Then** la celda completa sin errores, se imprime la comparación entre ambas estrategias y se muestra el gráfico comparativo.
2. **Given** un kernel reiniciado, **When** el usuario ejecuta todas las celdas del notebook 04 en orden hasta el paso 4, **Then** el paso 4 produce resultados consistentes y correctos sin necesidad de intervención manual.

---

### User Story 2 - Visualizar comparación entre estrategias (Priority: P2)

Como estudiante, quiero ver una comparación visual clara entre la estrategia de salida en banda media y la de salida en banda superior, para tomar una decisión informada sobre cuál variante funciona mejor.

**Why this priority**: La comparación visual es el artefacto de aprendizaje que cierra el ciclo del capítulo y permite al estudiante internalizar las diferencias de rendimiento.

**Independent Test**: Verificar que el gráfico comparativo muestra barras etiquetadas correctamente para ambas estrategias con los valores numéricos de la métrica seleccionada.

**Acceptance Scenarios**:

1. **Given** que ambas estrategias se han ejecutado correctamente en los pasos 3 y 4, **When** se invoca la comparación, **Then** se genera un DataFrame con métricas lado a lado y un gráfico de barras legible.

### Edge Cases

- La estrategia `BollingerUpperExit` no genera operaciones porque el precio nunca alcanza la banda superior durante el período de datos.
- La función `compare_strategies` recibe objetos del tipo incorrecto (Series en lugar de BacktestMetrics).
- Los datos descargados tienen un rango temporal insuficiente para que ambas estrategias generen suficientes trades para comparación significativa.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El paso 4 del notebook 04 MUST ejecutarse sin errores cuando las celdas anteriores (pasos 1-3) se han ejecutado correctamente.
- **FR-002**: La función `compare_strategies` MUST recibir objetos del tipo esperado (`BacktestMetrics`) para generar la tabla comparativa.
- **FR-003**: El notebook MUST invocar `extract_metrics` sobre los resultados de cada backtest antes de pasarlos a `compare_strategies`.
- **FR-004**: El gráfico comparativo generado por `plot_comparison` MUST renderizarse correctamente con los datos de ambas estrategias.
- **FR-005**: El flujo completo del notebook 04 (pasos 1-5) MUST poder ejecutarse de principio a fin sin errores bloqueantes.

### Key Entities

- **Notebook 04 backtesting**: Material interactivo del capítulo de mean reversion con el flujo de backtesting y comparación de variantes.
- **Paso 4**: Celda que define la variante `BollingerUpperExit`, ejecuta su backtest y genera la comparación con la estrategia base.
- **`compare_strategies`**: Función de `curso.lib.backtest` que acepta un diccionario de `BacktestMetrics` y devuelve un DataFrame comparativo.
- **`BacktestMetrics`**: Dataclass que encapsula las métricas estándar extraídas de un backtest.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: El 100% de las ejecuciones del notebook 04 en un entorno limpio completan el paso 4 sin errores.
- **SC-002**: La tabla comparativa muestra métricas numéricas válidas para ambas estrategias (sin valores nulos o inesperados).
- **SC-003**: Un estudiante puede ejecutar el notebook 04 completo (pasos 1-5) en menos de 2 minutos sin intervención manual.
- **SC-004**: La corrección no introduce cambios de comportamiento en otros notebooks del curso que utilicen las mismas funciones de la librería compartida.

## Assumptions

- El fallo del paso 4 se debe a un error de tipo: `compare_strategies` espera objetos `BacktestMetrics` pero recibe `pd.Series` (resultados crudos de `run_backtest`).
- La corrección se limita al notebook del capítulo 04, paso 4, ajustando la invocación para pasar métricas extraídas en lugar de stats crudos.
- Las funciones de la librería compartida (`compare_strategies`, `extract_metrics`, `plot_comparison`) funcionan correctamente cuando reciben los tipos esperados.
- El entorno del curso tiene las dependencias necesarias instaladas y los datos de mercado accesibles.

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Este documento define historias, requisitos, supuestos, casos límite y resultados medibles para el fallo del paso 4 del notebook 04.
- **Independent Value Slices**: P1 resuelve el bloqueo funcional; P2 asegura que la comparación visual cumple su objetivo didáctico.
- **Verifiable Outcomes**: Cada historia incluye escenarios de aceptación y una prueba independiente reproducible.
- **Minimal, Explicit Change**: El alcance queda limitado al fallo en el paso 4 y la corrección de tipos en la invocación de `compare_strategies`.
