"""
Módulo de datos — Wrapper de OpenBB con cache local.

Proporciona funciones para descargar datos de mercado, almacenarlos
en cache local (CSV/Parquet) y manejar gaps en datos históricos.
"""

import os
from pathlib import Path
from datetime import datetime, timedelta

import pandas as pd


# Directorio de cache por defecto
CACHE_DIR = Path(__file__).parent.parent / "data"


def get_cache_path(ticker: str, fmt: str = "parquet") -> Path:
    """Devuelve la ruta de cache para un ticker dado."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return CACHE_DIR / f"{ticker.upper()}.{fmt}"


def download_historical(
    ticker: str,
    start_date: str | None = None,
    end_date: str | None = None,
    provider: str = "yfinance",
    use_cache: bool = True,
    cache_max_age_hours: int = 24,
) -> pd.DataFrame:
    """
    Descarga datos históricos de precios vía OpenBB.

    Args:
        ticker: Símbolo del activo (ej. "AAPL", "JNJ").
        start_date: Fecha inicio formato "YYYY-MM-DD". Default: 5 años atrás.
        end_date: Fecha fin formato "YYYY-MM-DD". Default: hoy.
        provider: Proveedor de datos OpenBB. Default: "yfinance".
        use_cache: Si True, intenta leer de cache local primero.
        cache_max_age_hours: Máxima antigüedad del cache en horas.

    Returns:
        DataFrame con columnas: Open, High, Low, Close, Volume (index: Date).
    """
    cache_path = get_cache_path(ticker)

    # Intentar leer de cache
    if use_cache and cache_path.exists():
        age_hours = (
            datetime.now() - datetime.fromtimestamp(cache_path.stat().st_mtime)
        ).total_seconds() / 3600
        if age_hours < cache_max_age_hours:
            return _read_cache(cache_path)

    # Descargar desde OpenBB
    from openbb import obb

    if start_date is None:
        start_date = (datetime.now() - timedelta(days=5 * 365)).strftime("%Y-%m-%d")
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")

    result = obb.equity.price.historical(
        ticker, start_date=start_date, end_date=end_date, provider=provider
    )
    df = result.to_dataframe()

    # Normalizar columnas
    df = _normalize_columns(df)

    # Guardar en cache
    if use_cache:
        _write_cache(df, cache_path)

    return df


def download_multiple(
    tickers: list[str],
    start_date: str | None = None,
    end_date: str | None = None,
    provider: str = "yfinance",
) -> dict[str, pd.DataFrame]:
    """Descarga datos para múltiples tickers. Devuelve dict {ticker: DataFrame}."""
    results = {}
    for ticker in tickers:
        try:
            results[ticker] = download_historical(
                ticker, start_date=start_date, end_date=end_date, provider=provider
            )
        except Exception as e:
            print(f"[WARN] No se pudo descargar {ticker}: {e}")
    return results


def detect_gaps(df: pd.DataFrame, max_gap_days: int = 5) -> pd.DataFrame:
    """
    Detecta gaps (días hábiles faltantes) en el DataFrame.

    Returns:
        DataFrame con las fechas donde se detectaron gaps > max_gap_days.
    """
    if df.index.name != "date":
        df = df.copy()
        if "date" in df.columns:
            df = df.set_index("date")

    df.index = pd.to_datetime(df.index)
    diffs = df.index.to_series().diff()
    gaps = diffs[diffs > timedelta(days=max_gap_days)]
    return gaps.to_frame(name="gap_duration")


def interpolate_gaps(df: pd.DataFrame, method: str = "linear") -> pd.DataFrame:
    """
    Interpola valores faltantes en el DataFrame.

    Args:
        df: DataFrame con posibles NaN.
        method: Método de interpolación pandas (linear, ffill, etc.).

    Returns:
        DataFrame con gaps interpolados.
    """
    return df.interpolate(method=method).ffill().bfill()


def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normaliza nombres de columnas a formato estándar."""
    col_map = {}
    for col in df.columns:
        lower = col.lower()
        if "open" in lower:
            col_map[col] = "Open"
        elif "high" in lower:
            col_map[col] = "High"
        elif "low" in lower:
            col_map[col] = "Low"
        elif "close" in lower and "adj" not in lower:
            col_map[col] = "Close"
        elif "volume" in lower:
            col_map[col] = "Volume"
    df = df.rename(columns=col_map)

    # Asegurar index como fecha
    if "date" in [c.lower() for c in df.columns]:
        date_col = [c for c in df.columns if c.lower() == "date"][0]
        df = df.set_index(date_col)
    df.index = pd.to_datetime(df.index)
    df.index.name = "date"

    return df[["Open", "High", "Low", "Close", "Volume"]].dropna()


def _read_cache(path: Path) -> pd.DataFrame:
    """Lee cache desde Parquet o CSV."""
    if path.suffix == ".parquet":
        return pd.read_parquet(path)
    return pd.read_csv(path, index_col=0, parse_dates=True)


def _write_cache(df: pd.DataFrame, path: Path) -> None:
    """Escribe cache en formato Parquet."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".parquet":
        df.to_parquet(path)
    else:
        df.to_csv(path)
