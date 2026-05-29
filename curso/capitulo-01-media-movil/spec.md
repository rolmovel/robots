# Estrategia: Media Móvil Simple con Filtro Sectorial (Salud)

## Objetivo

Identificar oportunidades de compra en empresas del sector salud que están
experimentando una corrección temporal por debajo de su media móvil de 30 días.

## Hipótesis de Mercado

Las empresas consolidadas del sector salud que cotizan por debajo de su SMA(30)
durante un período prolongado (≥30 días consecutivos) tienden a revertir hacia
su media, ofreciendo una oportunidad de entrada con riesgo controlado.

## Reglas Operativas

- **Universo**: Empresas del sector salud con capitalización alta y datos
  disponibles en OpenBB (JNJ, PFE, UNH, ABBV, MRK).
- **Indicador**: SMA(30) calculada sobre precio de cierre diario.
- **Entrada**: Comprar cuando el precio de cierre ha estado por debajo de
  SMA(30) durante al menos 30 días consecutivos.
- **Salida**: Vender cuando el precio de cierre cruza por encima de SMA(30).
- **Stop-loss**: Vender si el precio cae un 10% por debajo del precio de entrada.

## Gestión de Riesgo

- Posición máxima: 100% del capital por operación (una posición a la vez).
- Drawdown tolerable: 15%.
- Stop-loss: 10% por debajo del precio de entrada.

## Parámetros Optimizables

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| sma_period | 10-60 | 30 | Período de la SMA |
| days_below | 10-60 | 30 | Días consecutivos por debajo de SMA para señal |
| stop_loss_pct | 5-20 | 10 | % de stop-loss |

## Supuestos

- Los datos históricos de yfinance para estas empresas son fiables y sin gaps significativos.
- El sector salud mantiene características de baja volatilidad relativa.
- Las comisiones de broker son ~0.2% por operación.
- No se considera impacto de mercado (activos líquidos).

## Métricas de Evaluación

- Retorno total (%)
- Retorno anualizado / CAGR (%)
- Sharpe Ratio (target > 0.5)
- Sortino Ratio
- Max Drawdown (%) (target < 15%)
- Número de operaciones
- Win Rate (%)
- Profit Factor
- Comparación vs Buy & Hold del mismo activo
