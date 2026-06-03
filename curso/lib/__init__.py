"""
Curso de Inversión en Bolsa — Utilidades compartidas.

Módulos disponibles:
- data: Descarga y cache de datos de mercado vía OpenBB
- indicators: Wrappers de indicadores técnicos (pandas-ta)
- backtest: Helpers para ejecutar backtesting.py y extraer métricas
- reporting: Visualizaciones estándar (equity curve, drawdown, tablas)
"""

from curso.lib.data import download_historical
from curso.lib import data, backtest, reporting, signals

# indicators may require optional dependencies (pandas_ta). Import lazily and
# tolerate ImportError so that modules that don't need indicators can still be used.
try:
	from curso.lib import indicators
except Exception:  # pragma: no cover - optional dependency
	indicators = None

__all__ = [
	"download_historical",
	"data",
	"indicators",
	"backtest",
	"reporting",
	"signals",
]
