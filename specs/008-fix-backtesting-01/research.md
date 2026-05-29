# Research: Fix Backtesting Notebook – Capítulo 01

**Date**: 2026-05-29
**Feature**: 008-fix-backtesting-01

## Decision: Root cause is a Bokeh 3.x API breaking change in `backtesting._plotting`

**Rationale**: `backtesting.py` 0.3.3 was released in 2022 against Bokeh 2.x. In Bokeh 3.0
the `DatetimeTickFormatter` fields (`days`, `months`, etc.) changed from accepting a list of
format strings to accepting a single format string. The installed environment has
Bokeh 3.9.0 and backtesting 0.3.3, which are incompatible at this API point.

**Evidence**:
- `bokeh==3.9.0`, `backtesting==0.3.3` confirmed from venv.
- Traceback from saved notebook output: `ValueError: failed to validate
  DatetimeTickFormatter(...).days: expected a value of type str, got ['%d %b', '%a %d']
  of type list`
- Location in library: `.venv/lib/python3.12/site-packages/backtesting/_plotting.py`
  line 250: `DatetimeTickFormatter(days=['%d %b', '%a %d'], months=['%m/%Y', "%b'%y"])`
- No other chapter notebook currently calls `bt.plot()` in a way that reproduces the error
  (chapters 05, 06 do not include `bt.plot()` cells).

**Alternatives considered**:
1. **Downgrade Bokeh to <3.0** via `requirements.txt`.
   Evaluated and rejected: Bokeh 3.x is a transitive dependency pulled by JupyterLab 4.x.
   Pinning to <3.0 would conflict with JupyterLab 4 and break other parts of the course.
2. **Upgrade backtesting.py to a newer release** that supports Bokeh 3.x.
   Evaluated and rejected: No release of backtesting.py after 0.3.3 exists at time of writing
   (the project is effectively unmaintained). No compatible release is available on PyPI.
3. **Patch the installed `_plotting.py`** in the venv.
   Evaluated and rejected: Patching a file inside `.venv/` is fragile — it is silently lost on
   every `pip install` or venv recreation. Not suitable for a reproducible educational course.
4. **Add a monkey-patch cell in the notebook that fixes `_plotting.py` at import time**.
   Considered viable but adds complexity and is an unusual pattern for beginner students.
5. **Wrap `bt.plot()` in `try/except`** with a clear informative message.
   **Selected**: Simplest change confined entirely to the notebook cell. Students see a clear
   explanation of the incompatibility and the course can still demonstrate the equity curve
   via `plot_equity_curve()` (matplotlib). Consistent with the minimal-change principle.

---

## Decision: Cell 14 (comparison) requires no logic changes — only execution order fix

**Rationale**: Cell 14 references the `metrics` object produced in cell 8. The variable is
in scope and produces valid output when cells are executed in order. The cell had no recorded
output because execution was halted by the error in cell 12. Once cell 12 is wrapped in
`try/except` (so it no longer raises), cells 13–17 will execute normally.

**Alternatives considered**:
1. Re-assign `metrics` redundantly in cell 14 as a defensive guard.
   Rejected: `metrics` is in scope from cell 8; redundancy adds noise without safety.
2. Restructure cell ordering to move `bt.plot()` after cell 14.
   Rejected: Changes notebook pedagogy without benefit; simpler to fix cell 12 alone.

---

## Decision: Cell 16 conclusions — replace placeholders with values from observed backtest

**Rationale**: The backtest output from cell 8 is deterministic given a fixed ticker and
date range. The observed values (retorno 2.85%, Sharpe 0.109, Max DD -9.05%, Win Rate 57.14%,
7 trades) can be written directly into the conclusions cell as concrete illustrations, with a
brief note that individual runs may differ if the YFinance data range changes.

**Alternatives considered**:
1. Keep placeholders and ask students to fill them in as an exercise.
   Partially accepted: Conclusions that invite student reflection are kept, but the backtest
   numbers used as concrete examples are filled in to give students a baseline interpretation.
2. Automate conclusion generation from `metrics` variables.
   Rejected: Over-engineered for a conclusions cell; a readable, static text block is
   more appropriate pedagogically and is easier to maintain.

---

## Best-practice note: Fixed date range for reproducibility

**Decision**: The notebook should load data with an explicit `start`/`end` range to guarantee
reproducible metrics across runs and environments.

**Rationale**: `yfinance` returns different row counts depending on the execution date. Without
a fixed window the metrics in cell 8 and the conclusions in cell 16 can diverge.

**Alternatives considered**:
1. Leave the date range dynamic (as currently coded).
   Accepted as-is for now: the spec explicitly restricts scope to cells 12, 14, 16.
   The date-range fix is out-of-scope for this feature but noted for a future improvement.

---

## Conclusion

All unknowns are resolved:

| Unknown | Resolution |
|---------|-----------|
| Root cause of `bt.plot()` failure | Bokeh 3.x API break (lists → string for `DatetimeTickFormatter`) |
| Best fix approach for cell 12 | `try/except ValueError` wrapper with informative message |
| Cell 14 fix required? | No code change; execution fix from cell 12 unblocks it |
| Cell 16 fix required? | Yes — replace `[...]` placeholders with observed backtest values |
| Dependencies affected | None beyond the single notebook |
| Reproducibility concern | Noted but deferred — out of scope for this feature |
