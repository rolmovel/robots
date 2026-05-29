# Quickstart: Curso de Inversión en Bolsa con OpenBB

## Prerrequisitos

- Python 3.11+ instalado
- pip o conda disponible
- Editor con soporte Jupyter (VS Code con extensión Jupyter o JupyterLab)

## Setup inicial

```bash
# Clonar el repositorio
git clone <repo-url>
cd sdd-project

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r curso/requirements.txt
```

## Verificar instalación

```python
from openbb import obb
import backtesting
import pandas_ta

# Descargar datos de prueba
data = obb.equity.price.historical("AAPL", provider="yfinance")
df = data.to_dataframe()
print(f"Registros descargados: {len(df)}")
print(df.tail())
```

## Estructura del curso

```
curso/
├── capitulo-00-fundamentos/     ← Empieza aquí
├── capitulo-01-media-movil/     ← Primera estrategia automatizada
├── capitulo-02-sma-cross/
├── capitulo-03-momentum-rsi/
├── capitulo-04-mean-reversion/
├── capitulo-05-breakout/
├── capitulo-06-multi-factor/
├── capitulo-07-agente-autonomo/
├── lib/                         ← Utilidades compartidas
└── requirements.txt
```

## Flujo por capítulo (01+)

1. Leer `README.md` del capítulo (teoría y fundamentos de la estrategia).
2. Crear `spec.md` siguiendo el contrato de entrega.
3. Implementar en `notebooks/<NN>_estrategia.ipynb`.
4. Evaluar en `notebooks/<NN>_backtesting.ipynb`.
5. Documentar conclusiones y decisión (aprobar/iterar/descartar).

## Primer ejercicio rápido

Abrir `curso/capitulo-00-fundamentos/notebooks/00_intro_openbb.ipynb` y seguir
las instrucciones para familiarizarte con OpenBB y la descarga de datos.

## Recursos

- [OpenBB Docs](https://docs.openbb.co/python/reference)
- [backtesting.py Docs](https://kernc.github.io/backtesting.py/doc/backtesting/)
- [pandas-ta Docs](https://github.com/twopirllc/pandas-ta)
