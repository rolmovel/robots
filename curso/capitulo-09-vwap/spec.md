# Estrategia: VWAP — Volume Weighted Average Price como Indicador de Trading

## Objetivo

Implementar el VWAP (Volume Weighted Average Price) como indicador de trading, calcular su versión acumulada y móvil, y desarrollar una estrategia de reversión al VWAP con backtesting y comparación contra otras estrategias del curso.

## Hipótesis de Mercado

Los activos en tendencia (filtrada por SMA 200) que se acercan al VWAP tienden a rebotar en la dirección de la tendencia. El VWAP actúa como un "precio justo" institucional donde los grandes operadores están dispuestos a ejecutar órdenes. Cuando el precio se desvía significativamente del VWAP, la probabilidad de reversión aumenta.

## Reglas Operativas

- **Universo**: Acciones líquidas (AAPL, MSFT, SPY).
- **Indicador**: VWAP acumulado (desde inicio de dataset) + VWAP móvil (20 días).
- **Filtro de tendencia**: SMA(200) — alcista si precio > SMA, bajista si precio < SMA.
- **Señal de contacto**: `abs(cierre - vwap) / vwap < 0.005` (0.5% tolerancia).
- **Entrada Long**: `cierre > sma_200` AND `cierre` subiendo AND `abs(cierre - vwap) / vwap < 0.005`.
- **Entrada Short**: `cierre < sma_200` AND `cierre` bajando AND `abs(cierre - vwap) / vwap < 0.005`.
- **Take-profit**: +2% desde precio de entrada.
- **Stop-loss**: -2% desde precio de entrada.
- **Timeout**: Cerrar posición a los 10 días si no se alcanzó salida.

## Gestión de Riesgo

- Posición máxima: 100% del capital por operación (una posición a la vez).
- Stop-loss: 2% por debajo del precio de entrada.
- Take-profit: 2% por encima del precio de entrada.
- Timeout: 10 días de trading sin salida.
- Filtro de tendencia: No operar en contra de la tendencia SMA(200).

## Parámetros Optimizables

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| vwap_tolerance_pct | 0.1-1.0 | 0.5 | Tolerancia para considerar "contacto" con VWAP |
| take_profit_pct | 1.0-5.0 | 2.0 | Objetivo de beneficio en porcentaje |
| stop_loss_pct | 1.0-5.0 | 2.0 | Límite de pérdida en porcentaje |
| timeout_days | 5-20 | 10 | Días máximos sin salida |
| sma_trend | 50-200 | 200 | Período SMA para filtro de tendencia |
| vwap_rolling_window | 10-50 | 20 | Ventana para VWAP móvil |
| confluence_pct | 0.5-2.0 | 1.0 | Umbral de confluencia para VWAP multi-temporal |

## Supuestos

- Los datos históricos de yfinance son fiables y sin gaps significativos.
- Las acciones seleccionadas tienen liquidez suficiente para ejecutar sin impacto significativo.
- Las comisiones de broker son ~0.2% por operación.
- El VWAP se recalcula cada día de trading con los datos acumulados hasta esa fecha.
- El VWAP se calcula sobre datos diarios (no intraday minuto a minuto).
- Si un ticker carece de datos de volumen, se usa SMA con advertencia clara.

## Métricas de Evaluación

- Retorno total (%)
- Retorno anualizado / CAGR (%)
- Sharpe Ratio (target > 0.5 para VWAP bounce)
- Sortino Ratio
- Max Drawdown (%) (target < 15%)
- Número de operaciones (target: 10-50 por activo)
- Win Rate (%) (target > 50%)
- Profit Factor
- Duración promedio de operaciones
- Comparación vs Buy & Hold del mismo activo

## Confluencia Multi-Temporal (P3)

Cuando el VWAP en diferentes temporalidades converge en un rango cercano, la señal es más fuerte:

- **VWAP Diario**: Calculado sobre datos diarios
- **VWAP Semanal**: Resampleado a semanal
- **VWAP Mensual**: Resampleado a mensual
- **Zona de confluencia**: 2+ VWAPs dentro de 1% entre sí
- **Señal de confluencia**: BUY cuando precio > todos los VWAPs alineados en confluencia, SELL cuando <

## Comparación con Otras Estrategias del Curso

| Capítulo | Indicador | Enfoque | Complejidad |
|----------|-----------|---------|-------------|
| 01 | SMA(30) | Trend-following simple | Baja |
| 02 | SMA Cross | Cruce de medias | Media |
| 03 | RSI + SMA(200) | Momentum con filtro | Media |
| 04 | Mean Reversion | Desviación de SMA | Media |
| 05 | Breakout | Ruptura de rangos | Media |
| 06 | Multi-Factor | Combinación de factores | Alta |
| 08 | FFT Filter | Descomposición espectral | Alta |
| 09 | VWAP Bounce | Reversión al precio promedio ponderado | Media |

La estrategia VWAP se diferencia por usar el volumen como ponderador, reflejando el precio promedio real de ejecución institucional, no solo el precio de cierre.
