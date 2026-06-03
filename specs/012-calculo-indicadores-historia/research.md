# Research: Calculo Indicadores Historia

## Decision: Strategy model and registration

- Decision: Use a pluggable strategy pattern. Implement `StrategyInterface` (class/protocol) with method `compute_signals(data, config) -> SignalResult`.
- Rationale: Allows users to swap different algorithmic rules (baseline, momentum, mean_reversion, custom) without changing core code.
- Alternatives considered:
  - Hardcoded branching inside `calculate_signals()`: simpler but brittle and not extensible.
  - Plugin discovery via entry-points: powerful but adds packaging complexity; postpone unless packaging requested.

## Decision: Configuration format

- Decision: Accept `config` as a Python dict or YAML-loaded mapping with `strategy_type` and nested `params`.
- Rationale: Simple, no external dependencies; works for programmatic and file-based configuration.
- Example:

```yaml
strategy_type: baseline
params:
  long_sma: 200
  short_sma: 50
  rsi_period: 14
  rsi_overbought: 70
  risk_pct: 0.01
```

## Decision: Implementation location

- Decision: Add `curso/lib/signals.py` with registry and API `calculate_signals(data, config)`.
- Rationale: Keeps feature co-located with existing indicators (`curso/lib/indicators.py`). Easier to test and import.

## Validation and tests

- Create unit tests for:
  - `baseline` strategy outputs on synthetic data
  - Strategy registration and custom strategy invocation
  - Error handling for short series and NaNs

## Next steps

- Implement `StrategyInterface` and `baseline` strategy.
- Add `calculate_signals()` wrapper and registry.
- Write quickstart and unit tests.
