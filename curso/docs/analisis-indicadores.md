# Análisis de Indicadores Técnicos de Mercado

## Resumen

Análisis comparativo de los indicadores técnicos implementados en el curso versus los estándares utilizados por analistas profesionales en los mercados financieros.

---

## Indicadores IMPLEMENTADOS en el Curso

| # | Indicador | Abreviatura | Categoría | Capítulo | Archivo |
|---|-----------|-------------|-----------|----------|---------|
| 1 | Media Móvil Simple | SMA | Tendencia | 01, 02, 03 | `lib/indicators.py` |
| 2 | Media Móvil Exponencial | EMA | Tendencia | 01, 02, 03 | `lib/indicators.py` |
| 3 | Índice de Fuerza Relativa | RSI | Momento | 03, 06 | `lib/indicators.py` |
| 4 | MACD | MACD | Tendencia/Momento | — (usado en notebooks) | `lib/indicators.py` |
| 5 | Bandas de Bollinger | BB | Volatilidad | 04 | `lib/indicators.py` |
| 6 | Average True Range | ATR | Volatilidad | 04, 05, 06 | `lib/indicators.py` |
| 7 | Canales de Donchian | DC | Tendencia/Breakout | 05 | `lib/indicators.py` |
| 8 | Momentum / Rate of Change | ROC/MOM | Momento | 06 | `lib/indicators.py` |
| 9 | Transformada Rápida de Fourier | FFT | Espectral | 08 | `notebooks/` |

**Total implementados: 9 indicadores**

---

## Indicadores NO IMPLEMENTADOS (Estándar del Mercado)

### Tendencia

| # | Indicador | Abreviatura | Descripción | Uso en Mercado |
|---|-----------|-------------|-------------|----------------|
| 10 | **ADX / +DI / -DI** | ADX | Fuerza de tendencia (sin dirección). DI+ y DI- indican dirección. | ⭐⭐⭐⭐⭐ Esencial para filtrar mercados range vs trending |
| 11 | **Parabolic SAR** | PSAR | Puntos que indican dirección y trailing stop dinámico. | ⭐⭐⭐⭐ Muy usado en commodities y swing trading |
| 12 | **SuperTrend** | SuperTrend | Indicador de tendencia basado en ATR, muy popular en India y Asia. | ⭐⭐⭐⭐ Popular en trading algorítmico |
| 13 | **Archer Moving Average Trend** | AMAT | Versión mejorada de EMA para detección de tendencia. | ⭐⭐⭐ Uso especializado |
| 14 | **Vortex Indicator** | VT | Identifica tendencias y reversales usando alto/bajo. | ⭐⭐ Uso nicho |
| 15 | **TEA (Trend Evaluation Average)** | TEA | Evaluación cuantitativa de fuerza de tendencia. | ⭐⭐ Uso nicho |

### Momento / Osciladores

| # | Indicador | Abreviatura | Descripción | Uso en Mercado |
|---|-----------|-------------|-------------|----------------|
| 16 | **Estocástico** | %K / %D | Compara cierre con rango de precios en período N. | ⭐⭐⭐⭐⭐ Uno de los indicadores más usados del mundo |
| 17 | **Estocástico Rápido** | Fast Stoch | Versión más sensible del estocástico. | ⭐⭐⭐⭐ Uso muy extendido |
| 18 | **Williams %R** | WilliamsR | Similar al estocástico, mide sobrecompra/sobreventa. | ⭐⭐⭐⭐ Muy popular en análisis técnico clásico |
| 19 | **CCI** | CCI | Commodity Channel Index, mide desviación de precio respecto a media estadística. | ⭐⭐⭐⭐ Estándar en commodities y futuros |
| 20 | **TRIX** | TRIX | EMA triple para eliminar ruido y detectar cruces de tendencia. | ⭐⭐⭐ Uso moderado |
| 21 | **Awesome Oscillator** | AO | Diferencia entre SMA 5 y SMA 34 del punto medio. | ⭐⭐⭐ Uso popular |
| 22 | **Force Index** | FI | Combina precio y volumen para medir fuerza de compra/venta. | ⭐⭐⭐ Uso moderado |
| 23 | **DeMarker** | DeM | Compara máximos/mínimos recientes con máximos/mínimos históricos. | ⭐⭐ Uso nicho |
| 24 | **Ultimate Oscillator** | UO | Combina 4 períodos para reducir señales falsas. | ⭐⭐ Uso nicho |
| 25 | **KST (Know Sure Thing)** | KST | Suma ponderada de 4 ROCs con diferentes períodos. | ⭐⭐ Uso nicho |

### Volatilidad

| # | Indicador | Abreviatura | Descripción | Uso en Mercado |
|---|-----------|-------------|-------------|----------------|
| 26 | **Keltner Channels** | KC | Canal basado en EMA ± múltiplo de ATR. | ⭐⭐⭐⭐ Alternativa a Bollinger, muy usado |
| 27 | **Historical Volatility** | HV | Desviación estándar de retornos logarítmicos. | ⭐⭐⭐⭐⭐ Estándar en opciones y derivativos |
| 28 | **Donchian Channel Width** | DCW | Ancho del canal de Donchian normalizado. | ⭐⭐ Complemento a DC |

### Volumen

| # | Indicador | Abreviatura | Descripción | Uso en Mercado |
|---|-----------|-------------|-------------|----------------|
| 29 | **On-Balance Volume** | OBV | Volumen acumulado basado en dirección de precio. | ⭐⭐⭐⭐⭐ Indicador de volumen más usado |
| 30 | **Volume Weighted Average Price** | VWAP | Precio promedio ponderado por volumen. | ⭐⭐⭐⭐⭐ Estándar institucional para ejecución de órdenes |
| 31 | **VWAP Bandas** | VWAP Bands | Bandas de desviación estándar alrededor de VWAP. | ⭐⭐⭐⭐ Uso institucional |
| 32 | **Chaikin Money Flow** | CMF | Flujo de dinero de Chaikin en período N. | ⭐⭐⭐⭐ Muy popular |
| 33 | **Accumulation/Distribution** | A/D | Línea que acumula basándose en cierre dentro del rango. | ⭐⭐⭐⭐ Uso muy extendido |
| 34 | **Money Flow Index** | MFI | RSI ponderado por volumen. | ⭐⭐⭐⭐ Alternativa volumétrica al RSI |
| 35 | **Negative Volume Index** | NVI | Índice que solo cambia cuando volumen disminuye. | ⭐⭐⭐ Uso nicho |
| 36 | **Ease of Movement** | EOM | Mide facilidad del movimiento de precio vs volumen. | ⭐⭐ Uso nicho |
| 37 | **Volume Profile** | VP | Distribución de volumen por nivel de precio (no por tiempo). | ⭐⭐⭐⭐⭐ Estándar en market profile |
| 38 | **Chaikin Oscillator** | CO | MACD del volumen (EMA rápida - lenta del ADL). | ⭐⭐⭐ Uso moderado |
| 39 | **Chaikin Accumulation/Distribution** | ADL | Línea acumulativa de Chaikin. | ⭐⭐⭐ Uso moderado |

### Precio / Canales

| # | Indicador | Abreviatura | Descripción | Uso en Mercado |
|---|-----------|-------------|-------------|----------------|
| 40 | **Ichimoku Cloud** | Ichimoku | Sistema completo: 5 líneas que muestran tendencia, soporte/resistencia, señal. | ⭐⭐⭐⭐⭐ Muy popular en Asia, estándar en análisis japonés |
| 41 | **Envelopes** | Env | Medias móviles ± porcentaje fijo. | ⭐⭐ Uso básico |
| 42 | **Fibonacci Retracement** | Fib | Niveles de retroceso basados en secuencia de Fibonacci (23.6%, 38.2%, 50%, 61.8%). | ⭐⭐⭐⭐⭐ Estándar universal en análisis técnico |
| 43 | **Fibonacci Extension** | FibExt | Niveles de extensión para targets de precio. | ⭐⭐⭐⭐ Uso muy extendido |

### Otros / Avanzados

| # | Indicador | Abreviatura | Descripción | Uso en Mercado |
|---|-----------|-------------|-------------|----------------|
| 44 | **Stochastic RSI** | StochRSI | Estocástico aplicado al RSI. | ⭐⭐⭐⭐ Muy popular en trading algorítmico |
| 45 | **Hull Moving Average** | HMA | Media móvil que reduce lag y mejora respuesta. | ⭐⭐⭐ Uso especializado |
| 46 | **Linear Regression** | LR | Regresión lineal del precio (tendencia estadística). | ⭐⭐⭐ Uso cuantitativo |
| 47 | **Linear Regression Slope** | LRS | Pendiente de la regresión lineal. | ⭐⭐⭐ Uso cuantitativo |
| 48 | **Linear Regression Std** | LRSd | Desviación estándar de la regresión lineal. | ⭐⭐⭐ Uso cuantitativo |
| 49 | **Schaff Trend Cycle** | STC | MACD estocástico combinado con ciclos. | ⭐⭐ Uso nicho |
| 50 | **Trix Signal** | TRIX_Signal | Señal EMA del TRIX. | ⭐⭐ Uso nicho |

**Total NO implementados: 41 indicadores**

---

## Tabla Resumen

| Categoría | Implementados | No Implementados | % Cobertura |
|-----------|:-------------:|:----------------:|:-----------:|
| **Tendencia** | 2 (SMA, EMA) | 5 | 28.6% |
| **Momento / Osciladores** | 3 (RSI, MACD, ROC) | 10 | 23.1% |
| **Volatilidad** | 2 (BB, ATR) | 2 | 50.0% |
| **Volumen** | 0 | 9 | 0.0% |
| **Precio / Canales** | 1 (Donchian) | 3 | 25.0% |
| **Avanzados / Otros** | 1 (FFT) | 6 | 14.3% |
| **TOTAL** | **9** | **35** | **20.5%** |

> **Nota:** Los indicadores con ⭐⭐⭐⭐⭐ son los más utilizados por analistas profesionales y en la industria financiera.

---

## Top 10 Indicadores del Mercado MÁS Faltantes (Prioridad Alta)

Estos son los indicadores estándar del mercado que **deberían** implementarse primero:

| Prioridad | Indicador | Razón |
|-----------|-----------|-------|
| 🔴 1 | **VWAP** | Estándar institucional absoluto. Sin él, no hay análisis de ejecución de órdenes. |
| 🔴 2 | **OBV** | Indicador de volumen más usado. Complemento esencial al precio. |
| 🔴 3 | **Ichimoku Cloud** | Sistema completo de análisis técnico. Muy usado en Asia y por traders profesionales. |
| 🔴 4 | **Estocástico** | Uno de los 3 indicadores más populares del mundo junto con RSI y MACD. |
| 🔴 5 | **ADX** | El filtro de tendencia más usado. Sin ADX no se puede filtrar range vs trending. |
| 🔴 6 | **Fibonacci Retracement** | Estándar universal en análisis técnico. Todos los analistas lo usan. |
| 🔴 7 | **CCI** | Estándar en commodities y futuros. |
| 🔴 8 | **Keltner Channels** | Alternativa principal a Bollinger Bands. |
| 🔴 9 | **Williams %R** | Oscilador de sobrecompra/sobreventa muy popular. |
| 🔴 10 | **Money Flow Index** | RSI volumétrico. Complemento natural al RSI ya implementado. |

---

## Indicadores Ya Usados en Notebooks (fuera de `indicators.py`)

Algunos notebooks calculan indicadores directamente sin usar los wrappers de `lib/indicators.py`:

| Indicador | Capítulo | Notebook |
|-----------|----------|----------|
| ATR (custom) | 04 | `04_backtesting.ipynb` |
| Bollinger Bands (custom) | 04 | `04_backtesting.ipynb` |
| FFT | 08 | `01_fft_analysis.ipynb`, `02_fourier_strategy.ipynb` |

---

## Recomendaciones

1. **Implementar primero los indicadores de volumen** (0 de 9 implementados es la mayor brecha).
2. **VWAP es crítico** para cualquier curso serio de trading — es el indicador más usado por traders institucionales.
3. **Estocástico y ADX** son complementos naturales al RSI ya implementado.
4. **Ichimoku** merece un capítulo propio dado que es un sistema completo.
5. **Fibonacci** debería implementarse como función utilitaria reutilizable.
