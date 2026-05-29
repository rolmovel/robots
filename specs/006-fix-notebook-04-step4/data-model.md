# Data Model: Fix notebook 04 backtesting step 4

**Date**: 2026-05-29
**Feature**: 006-fix-notebook-04-step4

## Entities

### BacktestMetrics (existing — no changes)

Dataclass defined in `curso/lib/backtest.py` that encapsulates standard metrics from a backtest run.

| Field | Type | Description |
|-------|------|-------------|
| retorno_total_pct | float | Total return percentage |
| retorno_anualizado_pct | float | Annualized return percentage |
| sharpe_ratio | float | Sharpe ratio |
| sortino_ratio | float | Sortino ratio |
| max_drawdown_pct | float | Maximum drawdown percentage |
| num_operaciones | int | Number of trades executed |
| win_rate_pct | float | Win rate percentage |
| profit_factor | float | Profit factor |
| buy_and_hold_pct | float | Buy & hold return percentage |

### Data Flow (step 4 correction)

```
run_backtest(df, Strategy)
    → pd.Series (stats)
        → extract_metrics(stats)
            → BacktestMetrics
                → compare_strategies({name: BacktestMetrics, ...})
                    → pd.DataFrame
                        → plot_comparison(df)
                            → matplotlib Figure
```

## State Transitions

N/A — no state management involved. The fix corrects a data flow pipeline in a single notebook cell.

## Validation Rules

- `compare_strategies` MUST receive `BacktestMetrics` instances (not raw `pd.Series`).
- The `metrics` variable from step 3 MUST be reused (already contains `extract_metrics(stats)`).
- A new variable `metrics_up` MUST be created for the upper-exit variant before comparison.
