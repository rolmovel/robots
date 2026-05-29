# Data Model: Fix Backtesting Notebook – Capítulo 01

**Date**: 2026-05-29
**Feature**: 008-fix-backtesting-01

## Overview

This feature modifies a single Jupyter notebook. There are no new persistent data
entities, database schemas, or API contracts. The "data model" here describes the
in-memory objects produced by the notebook and the notebook's cell structure that
must be preserved.

---

## Notebook Cell Inventory

| # | Type | Title | Status |
|---|------|-------|--------|
| 0 | markdown | Title & metadata | ✅ No change |
| 1 | markdown | Section 1: Setup | ✅ No change |
| 2 | code | Imports + sys.path | ✅ No change |
| 3 | markdown | Section 2: Datos | ✅ No change |
| 4 | code | Download JNJ data | ✅ No change |
| 5 | markdown | Section 3: Estrategia | ✅ No change |
| 6 | code | SMAFilterStrategy definition | ✅ No change |
| 7 | markdown | Section 4: Ejecutar Backtest | ✅ No change |
| 8 | code | `run_backtest` + `extract_metrics` | ✅ No change |
| 9 | markdown | Section 5: Equity Curve & Drawdown | ✅ No change |
| 10 | code | `plot_equity_curve` | ✅ No change |
| 11 | markdown | Section 6: Plot interactivo | ✅ No change |
| **12** | **code** | **`bt.plot()`** | **🔴 Fix: wrap in `try/except`** |
| 13 | markdown | Section 7: Comparación vs B&H | ✅ No change |
| **14** | **code** | **Comparación numérica** | **🟡 Unblocked by cell 12 fix** |
| 15 | markdown | Section 8: Conclusiones | ✅ No change |
| **16** | **code** | **Conclusions text** | **🔴 Fix: replace `[...]` placeholders** |
| 17 | markdown | Resumen | ✅ No change |

**Total cells**: 18 | **Cells modified**: 2 (cells 12 and 16) | **Cells unblocked**: 1 (cell 14)

---

## In-Memory Objects (key variables)

These objects are produced by existing cells and consumed downstream. No changes to
their definitions are required by this feature.

### `df` — Price DataFrame
- **Produced by**: cell 4
- **Type**: `pandas.DataFrame` with DatetimeIndex
- **Fields**: `Open`, `High`, `Low`, `Close`, `Volume`
- **Consumed by**: cell 6 (strategy), cell 8 (backtest), cell 12 (`bt.plot()`)

### `stats` — Backtesting Stats Object
- **Produced by**: cell 8 (`run_backtest`)
- **Type**: `pandas.Series` (backtesting.py stats format)
- **Consumed by**: cell 8 (`extract_metrics`), cell 10 (`plot_equity_curve`)

### `bt` — Backtest Instance
- **Produced by**: cell 8 (`run_backtest`)
- **Type**: `backtesting.Backtest`
- **Consumed by**: cell 12 (`bt.plot()`)
- **Note**: `bt.plot()` call fails at Bokeh 3.x; the instance itself is valid.

### `metrics` — Extracted Metrics Object
- **Produced by**: cell 8 (`extract_metrics(stats)`)
- **Consumed by**: cell 14 (numeric comparison)
- **Fields accessed**:
  - `metrics.retorno_total_pct` → 2.85 (observed)
  - `metrics.buy_and_hold_pct` → 39.43 (observed)
  - `metrics.max_drawdown_pct` → -9.05 (observed)

### `metrics_df` — Metrics DataFrame
- **Produced by**: cell 8 (`metrics_to_dataframe(metrics)`)
- **Consumed by**: cell 8 (`print_metrics_table`) for terminal output

---

## State Transitions

```
Cell 4 → df
Cell 6 → SMAFilterStrategy class
Cell 8 → stats, bt, metrics, metrics_df
Cell 10 → matplotlib figure (equity curve)
Cell 12 → [Bokeh plot OR try/except message]   ← CHANGED
Cell 14 → printed comparison table             ← UNBLOCKED
Cell 16 → printed conclusions                  ← CHANGED
```

---

## Validation Rules

- `metrics` object MUST be in scope when cell 14 executes.
- `bt` instance MUST be in scope when cell 12 executes (even with the fix applied).
- The `try/except` block in cell 12 MUST NOT suppress unexpected exceptions —
  only `ValueError` from the Bokeh `DatetimeTickFormatter` API.
