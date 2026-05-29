# Quickstart: Validate notebook 05 execution

**Date**: 2026-05-29
**Feature**: 007-fix-notebook-05

## Scope

Target notebook: `curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb`

## Clean validation path

1. Open the notebook in VS Code or Jupyter with the course Python environment.
2. Restart the kernel or begin from a fresh kernel.
3. Run the code cells in order.
4. Confirm these outcomes:
   - setup cell prints `Setup completado ✓`
   - data cell prints a non-zero number of `GLD` records
   - backtest cell prints metrics and renders equity and drawdown plots
   - trailing-stop analysis prints a table for ATR multipliers 2.0 through 4.0
   - conclusions cell prints the expected placeholder block

## Observed baseline in planning

The notebook executed successfully end-to-end in the current planning environment with no blocking errors.

## If a failure reappears

1. Re-run from a clean kernel.
2. Check whether the failing cell depends on a value created in a prior step.
3. Compare the failing behavior in VS Code and Jupyter if both are available.
4. Limit any code change to the failing notebook cell or the directly implicated helper.

## Success condition

A reviewer can re-run the notebook from a clean kernel and reproduce the same successful ordered execution without manual code edits.