# Feature Specification: Calculo Indicadores Historia

**Feature Branch**: `012-calculo-indicadores-historia`

**Created**: 2026-06-03

**Status**: Draft

**Input**: User description: "quiero implementar en mi libreria una metodo que me permita el calculo en base al documento /Users/rolmov/Documents/github/sdd-project/curso/docs/analisis-indicadores-historia.md . La estrategia a aplicar, iniclamente sera la definida en el documento pero quisiera poder configrarla a medida de mis necesidades"

## Resumen ejecutivo

Crear un método reutilizable en la librería que calcule las señales y métricas descritas en el documento de referencia `curso/docs/analisis-indicadores-historia.md`. La implementación inicial seguirá la estrategia propuesta en el documento (filtro de tendencia + condición de timing + gestión de riesgo), pero deberá ser configurable para ajustar parámetros (periodos, umbrales, activos, gestión de riesgo) sin cambiar código.
Además podremos cambiar la estrategia combinando diferentes indicadores de manera sencilla.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Calcular señales para un activo (Priority: P1)

Un analista desea obtener las señales de entrada/salida y métricas de riesgo para un activo concreto usando datos históricos.

**Why this priority**: Permite evaluar la regla en datos históricos y generar alertas/manuales de decisión.

**Independent Test**: Ejecutar el método sobre una serie de precios limpias y comprobar que devuelve: tendencia (por encima/por debajo media larga), cruce de medias, RSI, distancia al VWAP, y stop/target calculados.

**Acceptance Scenarios**:

1. **Given** datos limpios de OHLCV, **When** se ejecuta `calculate_signals()` con parámetros por defecto, **Then** devuelve un objeto con las métricas listadas y una decisión preliminar (`BUY`/`SELL`/`HOLD`).
2. **Given** parámetros ajustados (periodos y umbrales), **When** se ejecuta el método, **Then** las señales reflejan dichos parámetros (p.ej. SMA 50/200 en lugar de 20/50).

---

### User Story 2 - Usar la función en un workflow diario (Priority: P2)

Un usuario quiere ejecutar el cálculo diariamente y registrar resultados para revisión humana.

**Independent Test**: Ejecutar en un día de muestra y confirmar que output incluye timestamp, señales y recomendaciones de tamaño de posición.

**Acceptance Scenarios**:

1. **Given** feed de datos actualizado, **When** se ejecuta el cálculo, **Then** se produce un resumen diario con las métricas y una recomendación de acción.

---

### User Story 3 - Configuración parametrizable (Priority: P3)

Un desarrollador quiere ajustar parámetros sin tocar la lógica interna.

**Independent Test**: Cambiar archivo de configuración o pasar argumentos y verificar que los resultados cambian según parámetros.

**Acceptance Scenarios**:

1. **Given** parámetros personalizados, **When** se ejecuta el método, **Then** se aplican dichos parámetros a los cálculos.

---

### Edge Cases

- Datos con ventanas insuficientes para las medias (periodo mayor que la serie): el método debe devolver error claro o resultado parcial documentado.
- Datos con NaNs o duplicados: el método debe validar y limpiar o devolver advertencia.
- Señales contradictorias: la salida debe incluir razón de conflicto y recomendación `HOLD`.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: El sistema MUST aceptar series de OHLCV limpias y validar formato.
- **FR-002**: Debe calcular: media larga (filtro de tendencia), medias rápida y lenta (cruce), RSI, VWAP, y ATR o volatilidad para stops.
- **FR-003**: Debe exponer una API programática `calculate_signals(data, config)` que devuelve métricas y una recomendación (`BUY`/`SELL`/`HOLD`).
- **FR-004**: La lógica inicial deberá seguir la regla: filtro de tendencia + timing + gestión de riesgo.
- **FR-005**: Parámetros (periodos, umbrales RSI, límite de riesgo %) deben ser configurables vía argumentos o archivo de configuración.
- **FR-006**: Devolver información de diagnóstico (qué condiciones se cumplieron) para cada recomendación.
- **FR-007**: Documentar claramente inputs/outputs en la librería y ejemplos de uso.
 - **FR-008**: El sistema MUST soportar múltiples "tipos de estrategia" seleccionables por configuración (p.ej. `baseline`, `momentum`, `mean_reversion`, `custom`).
 - **FR-009**: Debe existir una estrategia por defecto (`baseline`) que implemente la regla descrita en el documento de referencia.
 - **FR-010**: La librería MUST exponer una interfaz/contrato para estrategias (p.ej. `StrategyInterface`) que permita registrar e invocar estrategias personalizadas sin alterar el núcleo.
 - **FR-011**: La configuración (`config`) debe aceptar un campo `strategy_type` y parámetros específicos por estrategia; el sistema debe validar compatibilidad de parámetros con la estrategia seleccionada.
 - **FR-012**: Debe proporcionarse un mecanismo para registrar una estrategia personalizada en tiempo de ejecución (por ejemplo mediante registro por clase/función o vía entry-points si aplica).

### Key Entities

- **Serie OHLCV**: tiempo, open, high, low, close, volume.
- **SignalResult**: objeto que contiene: tendencia, cruce, rsi, vwap_distance, atr, stop_loss, target, position_size, recommendation, diagnostics.
 - **SignalResult**: objeto que contiene: tendencia, cruce, rsi, vwap_distance, atr, stop_loss, target, position_size, recommendation, diagnostics.
 - **StrategyConfig**: configuración que incluye `strategy_type` y parámetros de estrategia (periodos, umbrales, risk_limit, etc.).
 - **StrategyInterface**: contrato que define métodos mínimos que debe implementar una estrategia, p.ej. `compute_signals(data, config) -> SignalResult`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: El método devuelve resultados válidos (sin excepciones) para el 99% de series con longitud >= 2×media_larga.
- **SC-002**: Para un conjunto de pruebas históricas (3 activos, 1 año), la función genera señales y métricas en menos de 5 segundos por activo (medido en entorno de desarrollo razonable).
- **SC-003**: 95% de las claves del `SignalResult` están documentadas con ejemplos de inputs/outputs en README.
- **SC-004**: El usuario puede cambiar parámetros y ver efecto en las señales en menos de 1 iteración (configurable invocation).

## Assumptions

- Los usuarios pasarán series de tiempo limpias o aceptarán que la función realice limpieza mínima (rellenar NaNs, eliminar duplicados).
- La estrategia inicial se limita a indicadores mencionados en el documento (SMA cross, RSI, VWAP, ATR).
- No se incluirá ejecución automática de órdenes en esta fase; solo cálculo y recomendación.

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Este documento describe historias, requisitos, y criterios verificables.
- **Independent Value Slices**: Las historias P1/P2/P3 son independientes y verificables.
- **Verifiable Outcomes**: Cada historia incluye escenarios de aceptación y pruebas.
- **Minimal, Explicit Change**: La función añade cálculo y configuración sin cambiar APIs existentes salvo añadir `calculate_signals()`.

---

**Referencia**: contenido base tomado de [curso/docs/analisis-indicadores-historia.md](curso/docs/analisis-indicadores-historia.md#L1)
