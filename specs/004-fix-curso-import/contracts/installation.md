# Contract: Install repository as package (editable)

**Feature**: specs/004-fix-curso-import

## Pre-conditions

- A clean system with Python 3.11+ available.
- `scripts/setup_env.sh` present and executable.

## Installation Contract

### Input

Run the standard setup script:

```bash
./scripts/setup_env.sh python3 .venv
```

The script will:
1. Create a venv at `.venv` (or provided path)
2. Upgrade pip and install `setuptools<72` + `wheel`
3. Install `curso/requirements.txt` and `curso/requirements-dev.txt` if present
4. Install the repository in editable mode (`pip install -e .`)
5. Register ipykernel for JupyterLab

### Post-conditions

1. `python -c "import curso; print('OK')"` returns `OK`.
2. `python -c "import pkg_resources; print('OK')"` returns `OK`.
3. `python -c "from curso.lib.indicators import sma; print('OK')"` returns `OK` (validates pandas_ta loads).
4. Notebook execution (chapter 01) completes without `ModuleNotFoundError`.
5. CI smoke tests (`ci-notebook-smoke.yml`) pass.

## Verification

Programmatic check (shell):

```bash
source .venv/bin/activate
python - <<'PY'
import pkg_resources
print('pkg_resources OK')
import curso
print('curso OK')
from curso.lib.indicators import sma
print('indicators OK')
PY
```

CLI check (CI):

```bash
python -c "from curso.lib.indicators import sma; print('OK')"
```

## Constraints

- `setuptools` MUST be pinned to `<72` to ensure `pkg_resources` is available for `pandas_ta` 0.3.14b.
- The shim workaround previously in `setup_env.sh` MUST be removed (replaced by proper version pin).
