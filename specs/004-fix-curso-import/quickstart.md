# Quickstart: Fix `curso` import

**Feature**: specs/004-fix-curso-import

## Steps

1. Run setup script to create venv and install dependencies:

```bash
chmod +x scripts/setup_env.sh
./scripts/setup_env.sh python3 .venv
```

2. Activate venv and verify imports:

```bash
source .venv/bin/activate
python -c "import pkg_resources; print('pkg_resources OK')"
python -c "from curso.lib.indicators import sma; print('indicators OK')"
```

3. Run the chapter 01 notebook (the one that triggered the error):

```bash
python -m nbconvert --execute curso/capitulo-01-media-movil/notebooks/01_estrategia.ipynb --to notebook --output /tmp/01_out.ipynb
```

## What changed

- `curso/requirements.txt`: Added `setuptools<72` to ensure `pkg_resources` remains importable (required by `pandas_ta` 0.3.14b).
- `scripts/setup_env.sh`: Changed setuptools upgrade to pin `<72`; removed unreliable `pkg_resources` shim.
- `pyproject.toml` + `setup.cfg`: Already present — make `curso` installable via `pip install -e .`.

## Troubleshooting

- If `import pkg_resources` fails: verify setuptools version is <72 (`pip show setuptools`). If it's 72+, run `pip install "setuptools<72"`.
- If `import curso` fails: ensure `pip install -e .` ran successfully in the venv.
- If the venv was created at `curso/.venv` instead of `.venv` (repo root), the editable install won't work unless run from repo root.

