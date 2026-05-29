# Data Model: Curso de Inversión en Bolsa con OpenBB

**Feature**: 001-curso-inversion-openbb  
**Date**: 2026-05-29

## Entities

### ModuloCurso

Unidad de contenido del curso (un capítulo).

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | string | Identificador único (ej. `cap-01`) |
| titulo | string | Nombre del capítulo |
| nivel | enum | `principiante`, `intermedio`, `avanzado` |
| objetivo | string | Resultado de aprendizaje principal |
| prerrequisitos | list[string] | IDs de capítulos previos requeridos |
| estrategia_id | string? | Referencia a EstrategiaInversion (null para cap-00) |
| materiales | list[Material] | Ficheros asociados (README, notebooks, spec) |
| criterio_evaluacion | string | Descripción de cómo se valida la completitud |

### EstrategiaInversion

Método de inversión enseñado en un capítulo.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | string | Identificador único (ej. `sma-filter-health`) |
| nombre | string | Nombre descriptivo |
| hipotesis | string | Premisa de mercado que explota |
| tipo | enum | `trend-following`, `mean-reversion`, `momentum`, `breakout`, `multi-factor` |
| horizonte_temporal | string | Ej. "diario", "semanal" |
| instrumentos | list[string] | Tipos de activos aplicables |
| indicadores | list[string] | Indicadores técnicos necesarios (SMA, RSI, BB...) |
| reglas_entrada | list[string] | Condiciones para abrir posición |
| reglas_salida | list[string] | Condiciones para cerrar posición |
| gestion_riesgo | RiskProfile | Parámetros de riesgo |
| parametros_optimizables | list[Param] | Variables tuneables |

### RiskProfile

Parámetros de gestión de riesgo de una estrategia.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| stop_loss_pct | float? | Porcentaje de stop-loss (si aplica) |
| take_profit_pct | float? | Porcentaje de take-profit (si aplica) |
| max_posicion_pct | float | % máximo del portfolio en una posición |
| max_drawdown_tolerable | float | Drawdown máximo aceptable |

### EspecificacionEstrategia

Documento SDD producido por el estudiante al finalizar un capítulo.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | string | Identificador (ej. `spec-cap-01`) |
| estrategia_id | string | Referencia a EstrategiaInversion |
| version | string | Semver de la especificación |
| objetivo | string | Qué busca lograr la estrategia |
| reglas_operativas | list[string] | Reglas formales entry/exit/risk |
| supuestos | list[string] | Condiciones asumidas del mercado |
| restricciones | list[string] | Limitaciones conocidas |
| metricas_evaluacion | list[string] | KPIs esperados del backtesting |
| estado | enum | `draft`, `validated`, `automated` |

### EjercicioBacktesting

Resultado de evaluación de una estrategia con datos históricos.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | string | Identificador único |
| especificacion_id | string | Referencia a EspecificacionEstrategia |
| periodo_datos | DateRange | Rango de datos utilizados |
| ticker_o_universo | list[string] | Instrumentos evaluados |
| metricas | BacktestMetrics | Resultados numéricos |
| conclusiones | string | Interpretación del estudiante |
| decision | enum | `aprobar`, `iterar`, `descartar` |

### BacktestMetrics

Métricas estándar de un backtest.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| retorno_total_pct | float | Rendimiento total |
| retorno_anualizado_pct | float | CAGR |
| sharpe_ratio | float | Ratio de Sharpe |
| sortino_ratio | float | Ratio de Sortino |
| max_drawdown_pct | float | Máximo drawdown |
| num_operaciones | int | Número de trades |
| win_rate_pct | float | Porcentaje de trades ganadores |
| profit_factor | float | Ganancia bruta / Pérdida bruta |
| buy_and_hold_pct | float | Benchmark pasivo |

### PerfilEstudiante

Estado de avance del estudiante.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | string | Identificador |
| nivel_actual | enum | `principiante`, `intermedio`, `avanzado` |
| capitulos_completados | list[string] | IDs de módulos aprobados |
| especificaciones_creadas | list[string] | IDs de specs entregadas |
| backtests_realizados | list[string] | IDs de ejercicios completados |

## Relationships

```
ModuloCurso 1──1 EstrategiaInversion (cap-01+)
ModuloCurso 1──* Material
EstrategiaInversion 1──1 RiskProfile
EstrategiaInversion 1──* EspecificacionEstrategia (versiones del estudiante)
EspecificacionEstrategia 1──* EjercicioBacktesting
EjercicioBacktesting 1──1 BacktestMetrics
PerfilEstudiante *──* ModuloCurso (completados)
```

## State Transitions

### EspecificacionEstrategia.estado

```
draft → validated   (cuando pasa revisión de pares)
validated → automated  (cuando existe implementación + backtesting reproducible)
```

### EjercicioBacktesting.decision

```
[evaluación completada] → aprobar | iterar | descartar
iterar → [nuevo EjercicioBacktesting con parámetros ajustados]
```
