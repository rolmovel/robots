# Quickstart: Fix `curso` import

**Feature**: specs/004-fix-curso-import

## Steps

1. Run setup script to create venv and install dependencies:

```bash
chmod +x scripts/setup_env.sh
./scripts/setup_env.sh python3.11 .venv
```

2. Activate venv and verify import:

```bash
source .venv/bin/activate
python -c "import curso; print('OK')"
```

3. Run the example notebook smoke test (optional):

```bash
# Convert and execute the example notebook (CI-like)
python -m nbconvert --execute curso/capitulo-00-fundamentos/notebooks/00_intro_openbb.ipynb --to notebook --output /tmp/00_intro_out.ipynb
```

## Troubleshooting

- If `import curso` fails, ensure `pyproject.toml` and `setup.cfg` are present at repo root and that `pip install -e .` ran successfully in the venv.

