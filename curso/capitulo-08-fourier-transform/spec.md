# Estrategia: Transformadas de Fourier como Indicadores de Trading

## Objetivo

Analizar series temporales de precios mediante descomposición espectral (FFT) para identificar ciclos dominantes, filtrar el ruido de alta frecuencia, y generar señales de trading basadas en cruces entre el precio original y la señal filtrada por Fourier.

## Hipótesis de Mercado

Los precios financieros contienen una mezcla de componentes cíclicos (señal) y ruido aleatorio. Al identificar las frecuencias dominantes mediante FFT y filtrar la señal para retener solo esos componentes, se obtiene una versión suavizada del precio. Los cruces entre el precio original y la señal filtrada generan señales de entrada/salida con menor latencia que las medias móviles tradicionales y mejor relación señal/ruido.

## Reglas Operativas

- **Universo**: Acciones del S&P 500 líquidas (AAPL, MSFT, GOOGL, AMZN, META).
- **Indicador**: FFT + filtro de frecuencias dominantes.
- **Ciclos dominantes**: Top-2 frecuencias más fuertes del espectro de potencias (período 10-80 días).
- **Entrada (Long)**: Precio de cierre cruza por encima de la señal filtrada por Fourier.
- **Salida**: Precio de cierre cruza por debajo de la señal filtrada.
- **Stop-loss**: -8% desde precio de entrada.
- **Timeout**: Cerrar posición si no se alcanza salida en 30 días de trading.

## Gestión de Riesgo

- Posición máxima: 100% del capital por operación (una posición a la vez).
- Drawdown tolerable: 15%.
- Stop-loss: 8% por debajo del precio de entrada.
- Timeout: 30 días sin salida.

## Parámetros Optimizables

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| fft_cycles | 1-5 | 2 | Número de ciclos dominantes a retener en el filtro |
| min_period | 5-20 | 10 | Período mínimo en días para considerar un ciclo |
| max_period | 30-120 | 80 | Período máximo en días para considerar un ciclo |
| lookback_years | 3-10 | 5 | Años de datos históricos para FFT |
| stop_loss_pct | 5-15 | 8 | Porcentaje de stop-loss |
| timeout_days | 15-60 | 30 | Días máximos sin salida |

## Supuestos

- Los datos históricos de yfinance son fiables y sin gaps significativos.
- Las acciones seleccionadas tienen liquidez suficiente para ejecutar sin impacto significativo.
- Las comisiones de broker son ~0.2% por operación.
- La FFT se recalcula periódicamente (cada 60 días) para adaptarse a cambios de régimen.
- No se considera impacto de mercado (activos líquidos).

## Métricas de Evaluación

- Retorno total (%)
- Retorno anualizado / CAGR (%)
- Sharpe Ratio (target > 0.5)
- Sortino Ratio
- Max Drawdown (%) (target < 15%)
- Número de operaciones
- Win Rate (%) (target > 50%)
- Profit Factor
- Comparación vs Buy & Hold del mismo activo

## Comparación con Otras Estrategias del Curso

| Capítulo | Indicador | Enfoque | Complejidad |
|----------|-----------|---------|-------------|
| 01 | SMA(30) | Trend-following simple | Baja |
| 02 | SMA Cross | Cruce de medias | Media |
| 03 | RSI + SMA(200) | Momentum con filtro | Media |
| 08 | FFT Filter | Descomposición espectral | Alta |

La estrategia Fourier se diferencia por operar en el dominio de frecuencia en lugar del dominio del tiempo, lo que permite un filtrado más selectivo de componentes cíclicos.
