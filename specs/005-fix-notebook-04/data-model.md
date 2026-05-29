# Data Model: Fix notebook 04 step 2

**Feature**: 005-fix-notebook-04 | **Date**: 2026-05-29

## Entities

### BollingerBands (return value of `bollinger_bands()`)

A DataFrame returned by `curso.lib.indicators.bollinger_bands()` with
parameter-independent column names.

| Column      | Type    | Source (`pandas_ta`)        | Description                        |
|-------------|---------|-----------------------------|------------------------------------|
| `lower`     | float64 | `BBL_{length}_{std}`        | Lower Bollinger Band               |
| `middle`    | float64 | `BBM_{length}_{std}`        | Middle band (SMA)                  |
| `upper`     | float64 | `BBU_{length}_{std}`        | Upper Bollinger Band               |
| `bandwidth` | float64 | `BBB_{length}_{std}`        | Bandwidth (volatility measure)     |
| `percent`   | float64 | `BBP_{length}_{std}`        | %B (position within bands, 0-1)    |

### Mapping rule

Column names are mapped positionally from the `pandas_ta.bbands()` output using
the fixed order: `lower, middle, upper, bandwidth, percent`. This order is
guaranteed by `pandas_ta` regardless of the parameter values.

## Relationships

- `bollinger_bands()` is called by notebook `04_estrategia.ipynb` (step 2).
- Notebook assigns `bb['upper']`, `bb['middle']`, `bb['lower']` to the price DataFrame.
- No other notebook currently accesses `bollinger_bands()` return columns directly.

## Validation Rules

- All five columns must be present in the returned DataFrame.
- Column names must be the stable names listed above, never the raw `pandas_ta` names.

## State Transitions

N/A — this is a stateless transformation.
