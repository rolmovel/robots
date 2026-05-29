# Curso de Inversión en Bolsa: De Principiante a Experto

> **Plataforma de datos**: OpenBB SDK v4+  
> **Motor de backtesting**: backtesting.py  
> **Indicadores**: pandas-ta  
> **Enfoque**: Strategy-Driven Development (SDD)

---

## Objetivo

Aprender a crear tus propias estrategias de inversión y automatizarlas.
Al final de cada capítulo habrás implementado y evaluado una estrategia completa
incluyendo backtesting formal con métricas estándar.

---

## Estructura del Curso

| Cap | Título | Estrategia | Nivel |
|-----|--------|-----------|-------|
| 00 | [Fundamentos](capitulo-00-fundamentos/) | - (teoría) | Principiante |
| 01 | [Media Móvil](capitulo-01-media-movil/) | SMA Filter (sector salud) | Principiante |
| 02 | [SMA Cross](capitulo-02-sma-cross/) | Cruce de medias + optimización | Principiante-Intermedio |
| 03 | [Momentum RSI](capitulo-03-momentum-rsi/) | RSI + filtro de tendencia | Intermedio |
| 04 | [Mean Reversion](capitulo-04-mean-reversion/) | Bollinger Bands + stop ATR | Intermedio |
| 05 | [Breakout](capitulo-05-breakout/) | Donchian + trailing stop | Intermedio-Avanzado |
| 06 | [Multi-Factor](capitulo-06-multi-factor/) | Scoring + ranking + portfolio | Avanzado |
| 07 | [Agente Autónomo](capitulo-07-agente-autonomo/) | Multi-estrategia + walk-forward | Avanzado-Experto |

---

## Progresión de Conceptos

```
Cap 00: Mercados → Activos → Riesgo/Retorno → OpenBB → Backtesting
    │
Cap 01: Un indicador → Una señal → Un backtest simple
    │
Cap 02: Dos indicadores → Cruces → Optimización → Overfitting
    │
Cap 03: Osciladores → Combinación de indicadores → Filtros
    │
Cap 04: Volatilidad → Stops dinámicos → Regímenes de mercado
    │
Cap 05: Canales → Position sizing → Trailing stops
    │
Cap 06: Múltiples factores → Ranking → Portfolio → Rebalanceo
    │
Cap 07: Orquestación → Walk-forward → Automatización
```

---

## Instalación

```bash
# Clonar repositorio
git clone <repo-url>
cd curso

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

# Instalar dependencias
pip install -r requirements.txt

# Lanzar JupyterLab
jupyter lab
```

---

## Estructura de Cada Capítulo

```
capitulo-XX-nombre/
├── README.md              # Teoría y conceptos
├── spec.md                # Especificación formal de la estrategia (SDD)
└── notebooks/
    ├── XX_estrategia.ipynb    # Implementación de señales
    └── XX_backtesting.ipynb   # Evaluación con métricas
```

---

## Librería Compartida

El directorio `lib/` contiene funciones reutilizables para todos los capítulos:

- **data.py**: Descarga y cache de datos vía OpenBB.
- **indicators.py**: Wrappers para indicadores técnicos (SMA, RSI, MACD, BB, ATR, Donchian).
- **backtest.py**: Ejecución de backtests y extracción de métricas estándar.
- **reporting.py**: Visualizaciones (equity curve, drawdown, comparaciones).

---

## Requisitos

- Python 3.11+
- Cuenta OpenBB (opcional, para datos premium)
- JupyterLab

---

## Disclaimer

Este curso es exclusivamente educativo. No constituye asesoría financiera,
recomendación de inversión, ni solicitud de compra o venta de ningún activo.

Los resultados de backtesting son simulaciones sobre datos históricos y
**no garantizan rendimientos futuros**. Invertir en bolsa conlleva riesgo
de pérdida de capital.

El autor no se responsabiliza de pérdidas derivadas del uso de las
estrategias presentadas en este material.

---

## Licencia

Uso educativo. Consulta LICENSE para detalles.
