# Contract: compare_strategies invocation

**Date**: 2026-05-29
**Feature**: 006-fix-notebook-04-step4

## Interface

```python
def compare_strategies(results: dict[str, BacktestMetrics]) -> pd.DataFrame
```

## Pre-conditions

- Each value in the `results` dict MUST be a `BacktestMetrics` instance.
- All `BacktestMetrics` fields MUST contain valid numeric values (not NaN for critical fields).

## Post-conditions

- Returns a `pd.DataFrame` indexed by strategy name with columns: `Retorno (%)`, `CAGR (%)`, `Sharpe`, `Sortino`, `Max DD (%)`, `Trades`, `Win Rate (%)`, `Profit Factor`, `B&H (%)`.
- DataFrame has exactly as many rows as entries in the input dict.

## Correct Usage Pattern (notebook step 4)

```python
# Step 3 already defines:
# stats, bt = run_backtest(df, BollingerMeanReversion)
# metrics = extract_metrics(stats)

# Step 4 — correct invocation:
stats_up, _ = run_backtest(df, BollingerUpperExit)
metrics_up = extract_metrics(stats_up)
comparison = compare_strategies({'Exit BB Media': metrics, 'Exit BB Superior': metrics_up})
plot_comparison(comparison)
plt.show()
```

## Error Scenario (current broken state)

```python
# WRONG: passing pd.Series instead of BacktestMetrics
comparison = compare_strategies({'Exit BB Media': stats, 'Exit BB Superior': stats_up})
# → AttributeError: 'Series' object has no attribute 'retorno_total_pct'
```
