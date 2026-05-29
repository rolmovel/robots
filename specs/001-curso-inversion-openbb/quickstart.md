# Quickstart: Curso de Inversión en Bolsa con OpenBB

## Prerrequisitos

- **Python 3.11** (recomendado; la versión 3.12+ no es compatible con todas las dependencias)
- pip disponible
- Editor con soporte Jupyter (VS Code con extensión Jupyter o JupyterLab)

## Setup inicial

La forma más rápida es usar el script de setup incluido:

```bash
# Clonar el repositorio
git clone https://github.com/rolmovel/robots
cd robots

# Ejecutar el script de setup (crea venv + instala dependencias)
chmod +x scripts/setup_env.sh
./scripts/setup_env.sh python3.11 .venv

# Activar el entorno
source .venv/bin/activate
```

> **Nota**: Si no tienes Python 3.11 como `python3.11`, puedes usar `pyenv`:
> ```bash
> pyenv install 3.11.10
> pyenv shell 3.11.10
> ./scripts/setup_env.sh python3 .venv
> ```

### Setup manual (alternativa)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r curso/requirements.txt
```

### Nota sobre `pkg_resources`

`pandas-ta 0.3.14b` depende de `pkg_resources`, que ya no se incluye por
defecto en versiones recientes de `setuptools`. El script `setup_env.sh`
crea automáticamente un shim si detecta que falta. Si haces la instalación
manual y `import pandas_ta` falla con *"No module named pkg_resources"*,
ejecuta:

```bash
python -c "
import os, sys
sp = next(p for p in sys.path if p.endswith('site-packages'))
os.makedirs(os.path.join(sp,'pkg_resources'), exist_ok=True)
with open(os.path.join(sp,'pkg_resources','__init__.py'),'w') as f:
    f.write('from pip._vendor.pkg_resources import *\\n')
print('shim created')
"
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
