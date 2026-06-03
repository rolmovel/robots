# Contract: `calculate_signals(data, config)`

## Request
- `data`: pandas.DataFrame with index (datetime) and columns: `open`, `high`, `low`, `close`, `volume`.
- `config`: dict with keys:
  - `strategy_type`: string
  - `params`: dict of strategy-specific parameters

## Response (SignalResult as JSON-serializable dict)
- `trend`: string
- `short_sma`, `long_sma`: numbers
- `sma_cross`: string
- `rsi`: number
- `vwap`, `vwap_distance`: numbers
- `atr`: number
- `stop_loss`, `target`: numbers
- `position_size`: number
- `recommendation`: one of `BUY`, `SELL`, `HOLD`
- `diagnostics`: dict describing which conditions were met

## Errors
- Raises `ValueError` for invalid input shapes or missing columns.
- Returns partial results with `diagnostics['incomplete'] = True` for too-short series.
