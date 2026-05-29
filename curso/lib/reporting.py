"""
Módulo de reporting — Visualizaciones estándar del curso.

Proporciona funciones para generar gráficos de equity curve, drawdown
y tablas resumen de métricas de backtesting.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_equity_curve(
    stats: pd.Series,
    title: str = "Equity Curve",
    figsize: tuple = (12, 5),
) -> plt.Figure:
    """
    Genera gráfico de equity curve desde resultados de backtesting.py.

    Args:
        stats: Serie de resultados de Backtest.run().
        title: Título del gráfico.
        figsize: Tamaño de la figura.

    Returns:
        Figure de matplotlib.
    """
    equity = stats["_equity_curve"]["Equity"]
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(equity.index, equity.values, linewidth=1.5, color="#2196F3")
    ax.set_title(title, fontsize=14)
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Equity ($)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def plot_drawdown(
    stats: pd.Series,
    title: str = "Drawdown",
    figsize: tuple = (12, 4),
) -> plt.Figure:
    """
    Genera gráfico de drawdown desde resultados de backtesting.py.

    Args:
        stats: Serie de resultados de Backtest.run().
        title: Título del gráfico.
        figsize: Tamaño de la figura.

    Returns:
        Figure de matplotlib.
    """
    equity = stats["_equity_curve"]["Equity"]
    peak = equity.cummax()
    drawdown = (equity - peak) / peak * 100

    fig, ax = plt.subplots(figsize=figsize)
    ax.fill_between(drawdown.index, drawdown.values, 0, alpha=0.4, color="#F44336")
    ax.plot(drawdown.index, drawdown.values, linewidth=0.8, color="#D32F2F")
    ax.set_title(title, fontsize=14)
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Drawdown (%)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def plot_price_with_signals(
    df: pd.DataFrame,
    signals: pd.DataFrame,
    title: str = "Precio y Señales",
    figsize: tuple = (14, 6),
) -> plt.Figure:
    """
    Grafica precio con señales de compra/venta superpuestas.

    Args:
        df: DataFrame OHLCV.
        signals: DataFrame con columnas 'buy' y 'sell' (bool o NaN).
        title: Título del gráfico.
        figsize: Tamaño de la figura.

    Returns:
        Figure de matplotlib.
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(df.index, df["Close"], linewidth=1, color="#333333", label="Close")

    if "buy" in signals.columns:
        buy_mask = signals["buy"].fillna(False).astype(bool)
        buy_dates = df.index[buy_mask]
        buy_prices = df["Close"][buy_mask]
        ax.scatter(buy_dates, buy_prices, marker="^", color="#4CAF50", s=80, label="Compra", zorder=5)

    if "sell" in signals.columns:
        sell_mask = signals["sell"].fillna(False).astype(bool)
        sell_dates = df.index[sell_mask]
        sell_prices = df["Close"][sell_mask]
        ax.scatter(sell_dates, sell_prices, marker="v", color="#F44336", s=80, label="Venta", zorder=5)

    ax.set_title(title, fontsize=14)
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Precio ($)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def print_metrics_table(metrics_df: pd.DataFrame) -> None:
    """Imprime tabla de métricas en formato legible para notebooks."""
    print("=" * 40)
    print("  RESUMEN DE BACKTESTING")
    print("=" * 40)
    for _, row in metrics_df.iterrows():
        print(f"  {row['Métrica']:.<30} {row['Valor']}")
    print("=" * 40)


def plot_comparison(
    comparison_df: pd.DataFrame,
    metric: str = "Sharpe",
    title: str | None = None,
    figsize: tuple = (10, 5),
) -> plt.Figure:
    """
    Gráfico de barras comparando una métrica entre estrategias.

    Args:
        comparison_df: DataFrame de compare_strategies().
        metric: Columna a graficar.
        title: Título del gráfico.
        figsize: Tamaño de la figura.

    Returns:
        Figure de matplotlib.
    """
    if title is None:
        title = f"Comparación: {metric}"

    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(comparison_df.index, comparison_df[metric], color="#2196F3", alpha=0.8)
    ax.set_title(title, fontsize=14)
    ax.set_ylabel(metric)
    ax.grid(True, alpha=0.3, axis="y")

    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:.2f}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            fontsize=9,
        )

    fig.tight_layout()
    return fig
