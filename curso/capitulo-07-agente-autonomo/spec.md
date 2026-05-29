# Estrategia: Agente Autónomo Multi-Estrategia con Walk-Forward

## Objetivo

Crear un orquestador que selecciona dinámicamente la mejor estrategia según
el régimen de mercado detectado, validado con walk-forward analysis para
asegurar robustez temporal.

## Hipótesis de Mercado

Ninguna estrategia individual funciona en todas las condiciones de mercado.
Un sistema que detecta el régimen actual y asigna la estrategia más apropiada
debería superar a cualquier estrategia individual a largo plazo.

## Reglas Operativas

- **Universo**: SPY (benchmark) + activos de capítulos anteriores.
- **Régimen Detection**:
  - ADX > 25 + SMA(50) > SMA(200): Trending Up
  - ADX > 25 + SMA(50) < SMA(200): Trending Down
  - ADX < 20: Range-bound
  - VIX > 30 o ATR > 2× media: High Volatility
- **Strategy Selection**:
  - Trending Up → SMA Cross (Cap 02)
  - Trending Down → Cash (no operar)
  - Range-bound → Bollinger Mean Reversion (Cap 04)
  - High Volatility → Reducir posiciones 50%
- **Walk-Forward**: Rolling window de 2 años train + 6 meses test.
- **Reoptimización**: Cada 6 meses (inicio de nueva window).

## Gestión de Riesgo

- Circuit breaker: Si drawdown > 15% → cerrar todas las posiciones + 30 días de pausa.
- Máxima exposición: 80% del capital (20% siempre en cash).
- Log obligatorio de todas las decisiones.
- Kill switch manual (el humano puede parar el agente en cualquier momento).

## Parámetros del Agente

| Parámetro | Default | Descripción |
|-----------|---------|-------------|
| train_window | 504 días | Ventana de training |
| test_window | 126 días | Ventana de test (walk-forward) |
| reoptimize_freq | 126 días | Frecuencia de reoptimización |
| adx_threshold | 25 | Umbral ADX para trending |
| vix_threshold | 30 | Umbral VIX para alta volatilidad |
| max_drawdown | 15% | Circuit breaker |
| cash_reserve | 20% | Reserva mínima de cash |

## Métricas de Evaluación

- CAGR over full walk-forward period
- Sharpe Ratio (target > 1.0)
- Max Drawdown (target < 15%)
- Regime detection accuracy (backtest)
- Strategy selection hit rate
- Walk-forward efficiency (out-of-sample / in-sample ratio)
- Comparison: Agent vs best individual strategy vs buy&hold
