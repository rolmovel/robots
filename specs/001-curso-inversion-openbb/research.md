# Research: Curso de Inversión en Bolsa con OpenBB

**Feature**: 001-curso-inversion-openbb  
**Date**: 2026-05-29

## 1. Plataforma de datos: OpenBB

### Decision
Usar **OpenBB SDK** (`pip install openbb`) como fuente principal de datos de mercado.

### Rationale
- Proyecto open-source (AGPLv3), 68k+ estrellas en GitHub, mantenido activamente.
- API Python unificada: `from openbb import obb` → `obb.equity.price.historical("TICKER")`.
- Soporta múltiples data providers (Yahoo Finance gratuito, FMP, Polygon, etc.).
- Devuelve DataFrames directamente: `.to_dataframe()`.
- Incluye datos de equity, ETF, índices, crypto, forex — suficiente para el abanico de estrategias.

### Alternatives Considered
| Alternativa | Motivo de descarte |
|-------------|-------------------|
| yfinance directo | Menos extensible; OpenBB lo integra como provider |
| Alpha Vantage | Límites de API gratuita más restrictivos |
| Quandl/Nasdaq Data Link | Requiere clave de pago para la mayoría de datasets |

---

## 2. Motor de backtesting

### Decision
Usar **backtesting.py** (`pip install backtesting`) como motor de backtesting principal.

### Rationale
- API mínima que cabe en una página; ideal para enseñanza progresiva.
- Soporta vectorized y event-based backtesting.
- Genera charts interactivos (Bokeh) para inspección visual.
- Métricas completas out-of-the-box: Sharpe, Sortino, Calmar, drawdown, win rate, etc.
- Optimizador integrado (SAMBO) para barrido de parámetros.
- Compatible con cualquier librería de indicadores técnicos (pandas-ta, TA-Lib).

### Alternatives Considered
| Alternativa | Motivo de descarte |
|-------------|-------------------|
| vectorbt | Más potente pero curva de aprendizaje mayor; mejor para capítulos avanzados opcionales |
| Backtrader | API más compleja y documentación menos accesible para principiantes |
| Zipline | Proyecto con mantenimiento irregular; depende de pyfolio |

---

## 3. Indicadores técnicos

### Decision
Usar **pandas-ta** como librería de indicadores.

### Rationale
- Integración directa con DataFrames de pandas (método `.ta`).
- +130 indicadores disponibles sin dependencias compiladas (a diferencia de TA-Lib).
- Instalación trivial: `pip install pandas-ta`.
- Permite calcular SMA, EMA, RSI, MACD, Bollinger Bands, etc. en una línea.

---

## 4. Progresión de estrategias del curso

### Decision
Secuencia de capítulos con complejidad creciente basada en estrategias reales de mercado.

| Capítulo | Estrategia | Conceptos nuevos |
|----------|-----------|-----------------|
| 00 | Fundamentos | Mercados, tipos de activos, riesgo/rendimiento, OpenBB setup |
| 01 | Media Móvil Simple (filtro sectorial) | SMA, señales de cruce, primer agente, backtesting básico |
| 02 | Cruce de Medias Móviles (SMA Cross) | Dos MAs, señales long/short, optimización de períodos |
| 03 | Momentum / RSI | Osciladores, sobrecompra/sobreventa, combinación con filtros |
| 04 | Mean Reversion (Bollinger Bands) | Estadística de reversión, bandas, stop-loss dinámico |
| 05 | Breakout / Donchian Channels | Gestión de posición, trailing stop, volatilidad |
| 06 | Multi-factor (combinación de señales) | Scoring, pesos, portfolio simple |
| 07 | Integración final: Agente autónomo | Orquestación, scheduling, reporting, métricas de producción |

### Rationale
- Capítulo 00 cubre prerequisitos sin automatización.
- Capítulos 01-06 siguen patrón uniforme: teoría → especificación SDD → implementación → backtesting.
- Capítulo 07 sintetiza todo en un agente completo con evaluación holística.
- Estrategias elegidas son bien documentadas en literatura y comprensibles para principiantes.

---

## 5. Formato de entregable por capítulo

### Decision
Cada capítulo (01+) entrega tres artefactos:

1. **spec.md** — Especificación SDD de la estrategia (reglas, riesgo, métricas).
2. **notebooks/<NN>_estrategia.ipynb** — Implementación automatizada con OpenBB + pandas-ta.
3. **notebooks/<NN>_backtesting.ipynb** — Evaluación con backtesting.py + informe de métricas.

### Rationale
- Alinea con FR-013 (entrega automatizada + backtesting reproducible por capítulo).
- Separar implementación de evaluación fomenta pensamiento crítico.
- Especificación SDD antes de código refuerza Spec-First Delivery.

---

## 6. Herramientas auxiliares compartidas (curso/lib/)

### Decision
Crear módulos reutilizables que crecen con el curso:

| Módulo | Propósito |
|--------|----------|
| `data.py` | Wrapper OpenBB: descarga, cache local, limpieza de huecos |
| `backtest.py` | Helpers: ejecutar backtest, extraer métricas, comparar estrategias |
| `reporting.py` | Visualización estándar: equity curve, drawdown, tabla resumen |
| `indicators.py` | Wrappers pandas-ta más usados con defaults del curso |

### Rationale
- Reduce boilerplate por capítulo.
- Enseña principio DRY de forma progresiva (se introduce gradualmente).
- Permite al estudiante enfocarse en la lógica de la estrategia.

---

## 7. Entorno y dependencias

### Decision
Un único `requirements.txt` en `curso/` con pinning flexible:

```text
openbb>=4.0
backtesting>=0.3.3
pandas-ta>=0.3.14
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
plotly>=5.0
jupyterlab>=4.0
```

### Rationale
- OpenBB v4+ es la versión estable actual con la API `obb.*`.
- backtesting.py 0.3.3+ soporta Python 3.11.
- JupyterLab para ejecución interactiva.

---

## 8. Limitaciones y riesgos identificados

| Riesgo | Mitigación |
|--------|-----------|
| Datos de Yahoo Finance pueden tener gaps | Capítulo 00 enseña limpieza; `data.py` implementa interpolación |
| Sobreajuste en optimización | Capítulo 03+ enseña walk-forward y out-of-sample explícitamente |
| Estrategias no son recomendación financiera | Disclaimer en cada capítulo; alineado con Assumptions de spec |
| OpenBB API puede cambiar entre versiones | Pinning de versión + wrapper en `data.py` aísla cambios |
