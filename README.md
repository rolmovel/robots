# sdd-project

# Robots — Curso de Trading Algorítmico

## Requisitos previos

- Python 3.11 (recomendado vía [pyenv](https://github.com/pyenv/pyenv))
- Git

## Instalación rápida (automática)

Un solo comando configura el entorno virtual, instala dependencias, registra el
kernel de Jupyter y deja la librería `curso` lista para importar:

```bash
./scripts/setup_env.sh python3.11 .venv
```

Después, activa el entorno e inicia JupyterLab:

```bash
source .venv/bin/activate
jupyter lab
```

> **Nota:** El script registra automáticamente un kernel llamado
> "Python (robots-curso)". Los notebooks del curso ya están configurados para
> usarlo. Si abres un notebook y no ves ese kernel, reinicia JupyterLab.

## Verificación

```bash
source .venv/bin/activate
python -c "from curso.lib.data import download_historical; print('OK')"
```

## Estructura del proyecto

```
curso/                  # Paquete Python con librería y notebooks del curso
  lib/                  # Módulos reutilizables (data, indicators, backtest…)
  capitulo-00-…/        # Capítulos con notebooks
  requirements.txt      # Dependencias de producción
  requirements-dev.txt  # Dependencias de desarrollo
scripts/
  setup_env.sh          # Script de instalación automática
specs/                  # Especificaciones de features (Spec Kit)
```

## Solución de problemas

| Problema | Solución |
|----------|----------|
| `ModuleNotFoundError: No module named 'curso'` | Ejecuta `pip install -e .` en la raíz del repo con el venv activo |
| Error de parquet / pyarrow | Ejecuta `pip install pyarrow` |
| Kernel no aparece en JupyterLab | Ejecuta `python -m ipykernel install --user --name robots-curso --display-name "Python (robots-curso)"` |
