"""
Módulo de indicadores técnicos — Wrappers de pandas-ta con defaults del curso.

Proporciona funciones simplificadas para calcular los indicadores más usados
en el curso, con parámetros por defecto alineados a las estrategias enseñadas.
"""

import pandas as pd
import pandas_ta as ta


def sma(df: pd.DataFrame, length: int = 30, column: str = "Close") -> pd.Series:
    """
    Media Móvil Simple (SMA).

    Args:
        df: DataFrame con columna de precios.
        length: Período de la media. Default: 30.
        column: Columna sobre la que calcular.

    Returns:
        Serie con valores de SMA.
    """
    return ta.sma(df[column], length=length)


def ema(df: pd.DataFrame, length: int = 20, column: str = "Close") -> pd.Series:
    """
    Media Móvil Exponencial (EMA).

    Args:
        df: DataFrame con columna de precios.
        length: Período de la media. Default: 20.
        column: Columna sobre la que calcular.

    Returns:
        Serie con valores de EMA.
    """
    return ta.ema(df[column], length=length)


def rsi(df: pd.DataFrame, length: int = 14, column: str = "Close") -> pd.Series:
    """
    Relative Strength Index (RSI).

    Args:
        df: DataFrame con columna de precios.
        length: Período del RSI. Default: 14.
        column: Columna sobre la que calcular.

    Returns:
        Serie con valores de RSI (0-100).
    """
    return ta.rsi(df[column], length=length)


def macd(
    df: pd.DataFrame,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9,
    column: str = "Close",
) -> pd.DataFrame:
    """
    Moving Average Convergence Divergence (MACD).

    Returns:
        DataFrame con columnas: MACD, Signal, Histogram.
    """
    result = ta.macd(df[column], fast=fast, slow=slow, signal=signal)
    result.columns = ["MACD", "Histogram", "Signal"]
    return result


def bollinger_bands(
    df: pd.DataFrame, length: int = 20, std: float = 2.0, column: str = "Close"
) -> pd.DataFrame:
    """
    Bollinger Bands.

    Args:
        df: DataFrame con columna de precios.
        length: Período de la media. Default: 20.
        std: Número de desviaciones estándar. Default: 2.0.
        column: Columna sobre la que calcular. Default: "Close".

    Returns:
        DataFrame con columnas: lower, middle, upper, bandwidth, percent.

    Raises:
        KeyError: Si la columna ``column`` no existe en ``df``.
    """
    if column not in df.columns:
        raise KeyError(
            f"La columna '{column}' no existe en el DataFrame. "
            f"Columnas disponibles: {list(df.columns)}"
        )
    result = ta.bbands(df[column], length=length, std=std)
    result.columns = ["lower", "middle", "upper", "bandwidth", "percent"]
    return result


def atr(df: pd.DataFrame, length: int = 14) -> pd.Series:
    """
    Average True Range (ATR).

    Args:
        df: DataFrame con columnas High, Low, Close.
        length: Período del ATR.

    Returns:
        Serie con valores de ATR.
    """
    return ta.atr(df["High"], df["Low"], df["Close"], length=length)


def donchian(df: pd.DataFrame, upper_length: int = 20, lower_length: int = 10) -> pd.DataFrame:
    """
    Donchian Channels.

    Returns:
        DataFrame con columnas: DC_Upper, DC_Mid, DC_Lower.
    """
    dc_upper = df["High"].rolling(window=upper_length).max()
    dc_lower = df["Low"].rolling(window=lower_length).min()
    dc_mid = (dc_upper + dc_lower) / 2
    return pd.DataFrame({"DC_Upper": dc_upper, "DC_Mid": dc_mid, "DC_Lower": dc_lower})


def momentum(df: pd.DataFrame, length: int = 10, column: str = "Close") -> pd.Series:
    """
    Momentum (Rate of Change).

    Returns:
        Serie con el porcentaje de cambio respecto a `length` períodos atrás.
    """
    return ta.roc(df[column], length=length)
