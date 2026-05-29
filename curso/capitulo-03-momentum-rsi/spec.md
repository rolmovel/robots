# Estrategia: Momentum con RSI y Filtro de Tendencia

## Objetivo

Detectar oportunidades de reversión a la media usando RSI en sobreventa,
filtrado por tendencia general (SMA 200) para operar solo a favor de la tendencia macro.

## Hipótesis de Mercado

Los activos en tendencia alcista que experimentan caídas temporales (RSI < 30)
tienden a recuperarse. El filtro de SMA(200) asegura que solo operamos activos
con tendencia de fondo positiva.

## Reglas Operativas

- **Universo**: Acciones del S&P 500 con precio > SMA(200).
- **Indicadores**: RSI(14), SMA(200).
- **Filtro de tendencia**: Precio > SMA(200).
- **Entrada (Long)**: RSI(14) < 30 Y Precio > SMA(200).
- **Salida**: RSI(14) > 70 (sobrecompra → tomar beneficios).
- **Stop-loss**: -8% desde precio de entrada.

## Gestión de Riesgo

- Posición máxima: 100% del capital por señal.
- Stop-loss: 8%.
- Drawdown tolerable: 15%.
- Timeout: cerrar posición si no se alcanza salida en 30 días.

## Parámetros Optimizables

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| rsi_period | 7-21 | 14 | Período RSI |
| rsi_lower | 20-40 | 30 | Umbral de sobreventa |
| rsi_upper | 60-80 | 70 | Umbral de sobrecompra |
| sma_trend | 100-300 | 200 | Período SMA de tendencia |
| stop_loss | 5-15 | 8 | Stop-loss % |

## Métricas de Evaluación

- Win rate (target > 55%)
- Sharpe Ratio (target > 0.8)
- Max Drawdown (target < 15%)
- Average trade duration (días)
- Profit factor
- Comparación con/sin filtro de tendencia
