# Estrategia: Reversión a la Media con Bandas de Bollinger

## Objetivo

Comprar activos que tocan la banda inferior de Bollinger (sobreventa estadística)
y vender cuando alcanzan la banda media o superior, usando ATR como stop dinámico.

## Hipótesis de Mercado

Los precios oscilan alrededor de su media y las desviaciones extremas (> 2σ)
tienden a corregirse. Las Bandas de Bollinger proporcionan una medida estadística
objetiva de cuándo un precio está en extremo.

## Reglas Operativas

- **Universo**: ETFs sectoriales o acciones con historial de comportamiento range-bound.
- **Indicadores**: Bollinger Bands(20, 2), ATR(14).
- **Entrada (Long)**: Precio cierra por debajo de la banda inferior.
- **Salida (profit)**: Precio alcanza la banda media (SMA 20).
- **Salida (trailing)**: Opcionalmente, mantener hasta banda superior.
- **Stop-loss dinámico**: Precio entrada - 2×ATR(14).

## Gestión de Riesgo

- Posición máxima: 100% del capital.
- Stop-loss: 2×ATR desde entrada.
- Drawdown tolerable: 15%.
- Filtro de régimen: NO operar si BB Width > percentil 90 (alta volatilidad).

## Parámetros Optimizables

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| bb_period | 10-30 | 20 | Período BB |
| bb_std | 1.5-3.0 | 2.0 | Desviaciones estándar |
| atr_period | 7-21 | 14 | Período ATR |
| atr_multiplier | 1.5-3.0 | 2.0 | Multiplicador ATR para stop |
| exit_target | media/superior | media | Banda de salida |

## Métricas de Evaluación

- Win rate (target > 60%)
- Average trade duration (target < 15 días)
- Profit factor (target > 1.5)
- Max Drawdown (target < 15%)
- Sharpe Ratio (target > 0.7)
- Comparación con/sin filtro de régimen
