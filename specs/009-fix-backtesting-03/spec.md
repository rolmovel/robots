# Feature Specification: Fix Backtesting Notebook – Capítulo 03

**Feature Branch**: `009-fix-backtesting-03`

**Created**: 2026-05-29

**Status**: Draft

**Input**: User description: "corrige bugs en el backtesting del tema 03"

## User Scenarios & Testing *(mandatory)*

### User Story 1 – Notebook ejecuta sin errores de inicio a fin (Priority: P1)

Un estudiante abre `03_backtesting.ipynb`, ejecuta todas las celdas con
"Run All" y obtiene resultados completos sin ninguna excepción.

**Why this priority**: El error en la celda de comparación interrumpe la
ejecución y hace que el estudiante no pueda ver la tabla comparativa entre
ambas estrategias, que es el objetivo central del capítulo.

**Independent Test**: Ejecutar `jupyter nbconvert --to notebook --execute 03_backtesting.ipynb`
y confirmar que el resultado contiene 0 celdas con output type `error`.

**Acceptance Scenarios**:

1. **Given** el notebook con todas sus celdas en orden, **When** el estudiante
   ejecuta "Run All Cells", **Then** todas las celdas completan sin excepciones.
2. **Given** que los backtests de ambas estrategias han corrido (celdas 1–9),
   **When** se ejecuta la celda de comparación (celda 11), **Then** se muestra
   una tabla con las métricas de RSI Simple y RSI + Trend Filter.

---

### User Story 2 – Tabla comparativa de estrategias se muestra correctamente (Priority: P2)

El estudiante puede leer la tabla comparativa de métricas lado a lado para
las dos variantes de la estrategia RSI (sin filtro y con filtro de tendencia).

**Why this priority**: La comparación entre estrategias es la aportación
pedagógica única de este capítulo — sin ella el estudiante no puede evaluar
el impacto del filtro de tendencia SMA(200).

**Independent Test**: Ejecutar celdas 1, 3, 5, 7, 9 y 11 en orden y confirmar
que la celda 11 imprime una tabla con dos filas (una por estrategia) y que el
gráfico comparativo se renderiza sin error.

**Acceptance Scenarios**:

1. **Given** que `stats_nf` y `stats_wf` están en scope (producidos en celda 9),
   **When** se ejecuta la celda de comparación, **Then** la tabla muestra
   métricas para "RSI Simple" y "RSI + Trend Filter" con valores numéricos.
2. **Given** los resultados observados, **When** el estudiante lee la tabla,
   **Then** puede comparar Retorno, Sharpe, Max DD y Win Rate entre estrategias.

---

### User Story 3 – Conclusiones concretas y sin marcadores de posición (Priority: P3)

El estudiante lee la sección de conclusiones (celda 13) con valores reales
de los backtests en lugar de marcadores `[mejora/empeora]` y `[comparar]`.

**Why this priority**: Los marcadores sin valor hacen que la celda sea
puramente decorativa y no aporta comprensión al estudiante.

**Independent Test**: Ejecutar celda 13 y confirmar que la salida no contiene
texto entre corchetes `[...]`.

**Acceptance Scenarios**:

1. **Given** los resultados observados (RSI Simple: Retorno 24.40%, Sharpe 0.207,
   Max DD -28.01%; RSI+Trend: Retorno 13.02%, Sharpe 0.217, Max DD -17.91%),
   **When** el estudiante ejecuta la celda de conclusiones, **Then** ve valores
   numéricos concretos y una decisión explícita (aprobar / iterar / descartar).

---

### Edge Cases

- ¿Qué ocurre si `stats_nf` o `stats_wf` no están en scope al ejecutar la
  celda de comparación (ejecución parcial)? El error debe ser un `NameError`
  descriptivo, no un `AttributeError` confuso.
- ¿El gráfico `plot_comparison` funciona correctamente si una de las
  estrategias no generó ninguna operación? Debe manejarse con un aviso.
- ¿El notebook produce resultados deterministas? Los datos de yfinance pueden
  variar; el ticker y rango de fechas deben ser fijos para garantizar
  reproducibilidad.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: La celda de comparación (celda 11) DEBE producir una tabla con
  filas para cada estrategia comparada sin lanzar `AttributeError` ni ninguna
  otra excepción no controlada.
- **FR-002**: La corrección de celda 11 DEBE ser mínima: sólo añadir la
  llamada a `extract_metrics()` sobre los objetos `stats`; no se deben
  cambiar otros aspectos del flujo.
- **FR-003**: La celda de conclusiones (celda 13) DEBE imprimir valores
  numéricos concretos derivados de los resultados observados; ninguna
  línea de salida debe contener `[...]` sin resolver.
- **FR-004**: El notebook completo DEBE ejecutarse sin errores con "Run All
  Cells" desde un entorno limpio con el `venv` del proyecto activado.
- **FR-005**: El gráfico de comparación (`plot_comparison`) DEBE renderizarse
  sin error como parte de la celda 11.

## Key Entities

- **Notebook `03_backtesting.ipynb`**: Archivo Jupyter de 14 celdas que
  implementa y compara dos variantes de la estrategia RSI: sin filtro y con
  filtro de tendencia SMA(200).
- **`stats_nf`, `stats_wf`**: Objetos `backtesting._Stats` (Series de pandas)
  devueltos por `run_backtest()`. Son el tipo incorrecto para `compare_strategies`.
- **`BacktestMetrics`**: Dataclass definida en `curso/lib/backtest.py` con
  atributos como `.retorno_total_pct`, `.sharpe_ratio`, etc. Es el tipo
  esperado por `compare_strategies()`.
- **`extract_metrics(stats)`**: Función en `curso/lib/backtest.py` que convierte
  un `_Stats` en un `BacktestMetrics`. Faltaba en la llamada de celda 11.
- **`compare_strategies(results: dict[str, BacktestMetrics])`**: Función en
  `curso/lib/backtest.py` línea 132. Falla cuando recibe `_Stats` en lugar de
  `BacktestMetrics`.
- **Celda 13 (Conclusiones)**: Celda con marcadores `[mejora/empeora]` y
  `[comparar ambas]` que necesitan ser reemplazados con valores concretos.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Al ejecutar "Run All Cells", el notebook completa con 0 celdas
  con output type `error` (actualmente 1 celda con error).
- **SC-002**: La celda de comparación muestra una tabla con exactamente 2 filas
  de estrategias y al menos 5 columnas de métricas.
- **SC-003**: La celda de conclusiones no contiene ningún marcador `[...]`
  sin resolver en su salida impresa.
- **SC-004**: El notebook se puede ejecutar de forma reproducible en el entorno
  del proyecto sin instalar dependencias adicionales.

## Assumptions

- Los datos de yfinance para `AAPL` en el período usado por el notebook están
  disponibles y producen los resultados ya observados (RSI Simple: Retorno 24.40%,
  Sharpe 0.207, Max DD -28.01%; RSI+Trend: Retorno 13.02%, Sharpe 0.217,
  Max DD -17.91%).
- La causa raíz del `AttributeError` es que `compare_strategies` recibe `_Stats`
  en lugar de `BacktestMetrics`: la corrección mínima es envolver cada stats con
  `extract_metrics()` en la llamada de celda 11.
- No hay bug en `compare_strategies` ni en `plot_comparison` — sólo en cómo se
  llaman desde el notebook.
- El alcance se limita a celdas 11 y 13; el resto del notebook es correcto.
- El notebook `03_estrategia.ipynb` está fuera del alcance de este fix.
- No existe un problema de Bokeh en este notebook (no hay `bt.plot()` call).

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Este documento define historias priorizadas,
  requisitos funcionales, supuestos, edge cases y criterios de éxito medibles.
- **Independent Value Slices**: P1 (ejecución sin errores), P2 (tabla comparativa),
  P3 (conclusiones concretas) son independientemente verificables.
- **Verifiable Outcomes**: Cada historia incluye Given/When/Then y un método
  de test independiente reproducible.
- **Minimal, Explicit Change**: El alcance está acotado a dos celdas (11 y 13);
  no se modifica lógica de estrategia ni helpers compartidos.
