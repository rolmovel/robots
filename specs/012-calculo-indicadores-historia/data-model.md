# Data Model: Calculo Indicadores Historia

## Entities

- SignalResult
  - timestamp: pd.Series or index reference
  - trend: 'UP' | 'DOWN' | 'NEUTRAL'
  - short_sma: float
  - long_sma: float
  - sma_cross: 'BULL' | 'BEAR' | 'NONE'
  - rsi: float
  - vwap: float
  - vwap_distance: float
  - atr: float
  - stop_loss: float
  - target: float
  - position_size: float
  - recommendation: 'BUY' | 'SELL' | 'HOLD'
  - diagnostics: dict (keys: conditions met, values: booleans or details)

- StrategyConfig
  - strategy_type: string
  - params: dict (strategy-specific parameters)

## Notes
- Use plain Python dataclasses or simple dicts for interchange.
- `SignalResult` must be easily serializable (json-friendly) for logging.
