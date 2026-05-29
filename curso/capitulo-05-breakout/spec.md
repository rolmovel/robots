# Estrategia: Breakout con Canales de Donchian + Trailing Stop

## Objetivo

Capturar movimientos explosivos tras rupturas de canales de precio,
usando trailing stop basado en ATR para maximizar ganancias en tendencias
mientras se limitan pérdidas.

## Hipótesis de Mercado

Los precios que rompen el canal de N días (máximo o mínimo) tienden a
continuar en esa dirección. Los períodos de compresión de volatilidad
(canal estrecho) preceden a movimientos significativos.

## Reglas Operativas

- **Universo**: Commodities ETFs (GLD, SLV, USO) o acciones de alta beta.
- **Indicadores**: Donchian Channel(20), ATR(14).
- **Entrada (Long)**: Precio supera el máximo de 20 días (canal superior).
- **Entrada (Short)**: Precio rompe el mínimo de 20 días (canal inferior).
- **Salida**: Trailing stop a 3×ATR del máximo desde entrada.
- **Alternativa**: Salida en canal contrario (mínimo 10 días para long).

## Gestión de Riesgo

- Position sizing: Riesgo fijo del 2% del capital por trade.
- Tamaño = (Capital × 0.02) / (3 × ATR).
- Drawdown tolerable: 25% (estrategia de tendencia → mayor drawdown esperado).
- Máximo posiciones simultáneas: 1 (simplificado para el curso).

## Parámetros Optimizables

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| entry_period | 10-55 | 20 | Período del canal de entrada |
| exit_period | 5-20 | 10 | Período del canal de salida |
| atr_period | 7-21 | 14 | Período ATR |
| atr_trailing | 2.0-4.0 | 3.0 | Multiplicador ATR para trailing |
| risk_per_trade | 0.01-0.03 | 0.02 | Riesgo por operación (% capital) |

## Métricas de Evaluación

- CAGR (target > 10%)
- Profit factor (target > 1.8)
- Average winner / Average loser ratio (target > 2.0)
- Win rate (aceptable < 50% si ratio win/loss es alto)
- Max Drawdown (target < 25%)
- Longest drawdown period (días)
- Trade frequency (trades por año)
