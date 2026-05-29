# Contract: Notebook 05 execution baseline

**Date**: 2026-05-29
**Feature**: 007-fix-notebook-05

## Interface

Notebook: `curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb`

## Expected ordered behavior

1. Setup imports shared helpers and prints `Setup completado ✓`.
2. Data-loading step downloads historical prices for `GLD` and prints a non-zero row count.
3. Strategy-definition step completes with no output and leaves `DonchianBreakout` available for later cells.
4. Backtest step produces:
   - metrics summary text
   - equity-curve plot
   - drawdown plot
5. Trailing-stop analysis produces a table with one row per ATR multiplier tested.
6. Conclusions step prints the expected conclusion template.

## Preconditions

- Course dependencies are installed.
- Network/data access required by `download_historical` is available.
- Notebook is run from a clean kernel or with prior cells executed in order.

## Postconditions

- No code cell raises a blocking exception.
- User-visible analytical outputs remain present.
- The notebook remains re-executable without manual source edits.

## Failure interpretation

If this contract fails in one client but not another, treat the issue as environment- or client-specific until the notebook content itself is shown to be the cause.