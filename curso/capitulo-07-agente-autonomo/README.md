# Capítulo 07: Agente Autónomo de Trading

> **Nivel**: Avanzado-Experto  
> **Prerrequisitos**: Capítulos 01-06  
> **Estrategia**: Orquestador Multi-Estrategia con Walk-Forward  
> **Objetivo**: Crear un agente que selecciona, ejecuta y monitoriza múltiples estrategias de forma autónoma, con validación walk-forward.

---

## 1. Del Backtesting al Trading Autónomo

Hasta ahora hemos:
1. Diseñado estrategias individuales.
2. Evaluado con backtesting estático.
3. Optimizado parámetros.

El siguiente paso es crear un **agente** que:
- Decide QUÉ estrategia usar y CUÁNDO.
- Ejecuta de forma autónoma según reglas predefinidas.
- Se adapta a cambios en el mercado.

---

## 2. Arquitectura del Agente

```
┌─────────────────────────────────────────────────┐
│                 AGENTE AUTÓNOMO                   │
├─────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────┐│
│  │  Detector   │  │  Selector   │  │ Monitor ││
│  │  de Régimen │→ │  Estrategia │→ │ & Risk  ││
│  └─────────────┘  └─────────────┘  └─────────┘│
│         ↑                                  ↓    │
│  ┌─────────────┐                    ┌─────────┐│
│  │  Data Feed  │                    │  Logger ││
│  │  (OpenBB)   │                    │ & Alert ││
│  └─────────────┘                    └─────────┘│
└─────────────────────────────────────────────────┘
```

### Componentes

1. **Data Feed**: Descarga datos vía OpenBB de forma periódica.
2. **Detector de Régimen**: Clasifica el mercado (trending/ranging/volatile).
3. **Selector de Estrategia**: Elige la estrategia óptima para el régimen actual.
4. **Monitor de Riesgo**: Supervisa posiciones, drawdown, y aplica circuit breakers.
5. **Logger**: Registra todas las decisiones y resultados para auditoría.

---

## 3. Walk-Forward Analysis

El backtesting estático tiene una limitación: usa datos futuros implícitamente.
Walk-forward lo soluciona:

1. **Window 1**: Train [2015-2018], Test [2019].
2. **Window 2**: Train [2016-2019], Test [2020].
3. **Window 3**: Train [2017-2020], Test [2021].
4. **Window N**: Train [20XX-20YY], Test [20ZZ].

Esto simula cómo operaría realmente la estrategia en tiempo real.

---

## 4. Scheduling y Automatización

```python
# Pseudocódigo del agente
schedule.every().day.at("09:30").do(agent.run_daily)

def run_daily():
    data = fetch_latest_data()
    regime = detect_regime(data)
    strategy = select_strategy(regime)
    signals = strategy.generate_signals(data)
    execute(signals)
    log_results()
```

---

## 5. Multi-Estrategia: Allocation

Con múltiples estrategias disponibles:

| Régimen | Estrategia Primaria | Estrategia Secundaria |
|---------|--------------------|-----------------------|
| Trending Up | SMA Cross | Breakout Donchian |
| Trending Down | Short SMA Cross | - (cash) |
| Range-bound | Bollinger Mean Rev | RSI Momentum |
| High Volatility | - (cash) | Reduce posiciones |

---

## Siguiente paso

Revisa `spec.md` y luego implementa el agente en los notebooks.

---

> ⚠️ **Disclaimer**: Este curso es exclusivamente educativo. No constituye asesoría financiera.
> Este agente es una herramienta de aprendizaje y NO debe usarse con dinero real sin supervisión.
