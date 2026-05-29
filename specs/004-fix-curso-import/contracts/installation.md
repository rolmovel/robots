# Contract: Install repository as package (editable)

**Feature**: specs/004-fix-curso-import

## Pre-conditions

- A clean system with Python 3.11 available.
- `scripts/setup_env.sh` present and executable.

## Installation Contract

### Input

Run the standard setup script:

```bash
./scripts/setup_env.sh python3.11 .venv
```

The script will:
1. Create a venv at `.venv` (or provided path)
2. Install `curso/requirements.txt` and `curso/requirements-dev.txt` if present
3. Install the repository in editable mode (`pip install -e .`)

### Post-conditions

1. `python -c "import curso; print('OK')"` returns `OK`.
2. `jupyter labextension list` and notebook execution are unaffected by installation.
3. CI smoke tests (`ci-notebook-smoke.yml`) can execute notebooks without `ModuleNotFoundError` for `curso`.

## Verification

Programmatic check (shell):

```bash
source .venv/bin/activate
python - <<'PY'
import importlib
importlib.import_module('curso')
print('import OK')
PY
```

CLI check (CI):

```bash
python -c "import curso; print('OK')"
```
