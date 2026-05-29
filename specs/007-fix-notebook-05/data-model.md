# Data Model: Fix notebook 05 execution

**Date**: 2026-05-29
**Feature**: 007-fix-notebook-05

## Entities

### Notebook 05
- Represents the full chapter 05 backtesting workflow.
- Contains sequential cells for setup, data acquisition, strategy definition, backtest execution, trailing-stop analysis, and conclusions.
- Primary file: `curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb`

### Execution Step
- Represents one ordered notebook cell in the learning flow.
- Relevant attributes:
  - section name
  - expected inputs from prior cells
  - expected outputs (table, figure, printed text, or none)
  - blocking status if execution fails

### Analytical Output
- Represents user-facing notebook results that must remain available after any fix.
- Includes:
  - metrics summary table
  - equity-curve plot
  - drawdown plot
  - ATR trailing-stop comparison table
  - conclusions text

### Reproducible Validation Run
- Represents one clean-kernel execution of the notebook from first executable cell to last.
- Validation rule: all code cells complete without error and expected outputs remain present.

## Relationships
- `Notebook 05` contains ordered `Execution Step` entries.
- Successful `Execution Step` entries generate `Analytical Output`.
- A `Reproducible Validation Run` verifies all `Execution Step` entries and resulting `Analytical Output`.

## Validation Rules
- Each code cell must run with only the state created by earlier cells in the notebook.
- No analytical output may be removed as a side effect of a fix.
- Any future correction must preserve clean-kernel re-execution of the notebook.