# Contract: Indicator Library — `bollinger_bands()`

**Feature**: 005-fix-notebook-04 | **Date**: 2026-05-29

## Interface

```python
def bollinger_bands(
    df: pd.DataFrame,
    length: int = 20,
    std: float = 2.0,
    column: str = "Close",
) -> pd.DataFrame:
```

## Return Contract

The returned DataFrame MUST have exactly these columns, in this order:

| Column      | Type    | Guaranteed |
|-------------|---------|------------|
| `lower`     | float64 | Yes        |
| `middle`    | float64 | Yes        |
| `upper`     | float64 | Yes        |
| `bandwidth` | float64 | Yes        |
| `percent`   | float64 | Yes        |

Column names MUST be stable across all valid combinations of `length` and `std`.

## Preconditions

- `df` contains a column named `column` (default `"Close"`) with numeric values.
- `df` has at least `length` rows.

## Postconditions

- First `length - 1` rows contain `NaN` (warm-up period).
- Remaining rows contain finite float values.
- `lower <= middle <= upper` for every non-NaN row.

## Error Behaviour

- Raises `KeyError` if `column` is missing from `df`.
- Delegates to `pandas_ta.bbands()` for other validation.
