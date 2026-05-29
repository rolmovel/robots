# Estrategia: Multi-Factor con Ranking y Rebalanceo

## Objetivo

Construir un portfolio que selecciona los mejores activos de un universo
basándose en un score compuesto de múltiples factores técnicos, con
rebalanceo periódico.

## Hipótesis de Mercado

La combinación de múltiples factores técnicos (momentum, tendencia, volatilidad)
produce una señal más robusta que cualquier indicador individual. Los activos
con las mejores puntuaciones compuestas tienden a superar al mercado.

## Reglas Operativas

- **Universo**: 20 acciones del S&P 500 de diferentes sectores.
- **Factores**:
  - Momentum: RSI(14) + Rate of Change(20)
  - Tendencia: Distancia a SMA(200) normalizada
  - Baja Volatilidad: 1/ATR(14) normalizado
- **Pesos factores**: Momentum 40%, Tendencia 40%, Volatilidad 20%.
- **Selección**: Top 5 activos por score compuesto.
- **Asignación**: Equal weight (20% por posición).
- **Rebalanceo**: Mensual (primer día hábil del mes).

## Gestión de Riesgo

- Diversificación obligatoria: mínimo 5 posiciones.
- Máximo por sector: 40% del capital.
- Stop portfolio: -15% desde máximo (circuit breaker).
- Drawdown tolerable: 20%.

## Parámetros Optimizables

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| top_k | 3-10 | 5 | Número de activos en portfolio |
| rebalance_freq | semanal/mensual/trimestral | mensual | Frecuencia rebalanceo |
| w_momentum | 0.2-0.6 | 0.4 | Peso factor momentum |
| w_trend | 0.2-0.6 | 0.4 | Peso factor tendencia |
| w_volatility | 0.1-0.3 | 0.2 | Peso factor volatilidad |
| rsi_period | 7-21 | 14 | Período RSI |
| roc_period | 10-30 | 20 | Período Rate of Change |

## Métricas de Evaluación

- Portfolio return vs benchmark (SPY)
- Sharpe Ratio (target > 1.0)
- Max Drawdown (target < 20%)
- Turnover (% capital rotado por rebalanceo)
- Information Ratio vs benchmark
- Sector concentration
- Factor attribution (contribución de cada factor)
