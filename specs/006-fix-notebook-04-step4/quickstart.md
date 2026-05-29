# Quickstart: Fix notebook 04 backtesting step 4

**Date**: 2026-05-29
**Feature**: 006-fix-notebook-04-step4

## What to fix

File: `curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb`
Cell: Step 4 — "Variante: salida en banda superior"

## Current (broken)

```python
class BollingerUpperExit(BollingerMeanReversion):
    def next(self):
        price = self.data.Close[-1]
        if not self.position:
            if price < self.bb_low[-1]:
                sl = price - self.atr_mult * self.atr[-1]
                self.buy(sl=sl)
        else:
            if price >= self.bb_up[-1]:
                self.position.close()

stats_up, _ = run_backtest(df, BollingerUpperExit)
comparison = compare_strategies({'Exit BB Media': stats, 'Exit BB Superior': stats_up})
plot_comparison(comparison)
plt.show()
```

## Fixed

```python
class BollingerUpperExit(BollingerMeanReversion):
    def next(self):
        price = self.data.Close[-1]
        if not self.position:
            if price < self.bb_low[-1]:
                sl = price - self.atr_mult * self.atr[-1]
                self.buy(sl=sl)
        else:
            if price >= self.bb_up[-1]:
                self.position.close()

stats_up, _ = run_backtest(df, BollingerUpperExit)
metrics_up = extract_metrics(stats_up)
comparison = compare_strategies({'Exit BB Media': metrics, 'Exit BB Superior': metrics_up})
plot_comparison(comparison)
plt.show()
```

## Changes

1. Added `metrics_up = extract_metrics(stats_up)` to convert raw stats to `BacktestMetrics`.
2. Changed `compare_strategies` arguments from `stats`/`stats_up` to `metrics`/`metrics_up`.
3. `metrics` (from step 3) is already a `BacktestMetrics` instance — reused directly.

## Validation

Run all cells of `04_backtesting.ipynb` sequentially (steps 1–5). Step 4 should produce a comparison DataFrame and bar chart without errors.
