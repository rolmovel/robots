#!/usr/bin/env bash
set -euo pipefail

# Creates a python venv and installs project requirements (macOS / Linux)
PYTHON=${1:-python3}
VENV_DIR=${2:-.venv}

echo "Using python: $(command -v "$PYTHON" || echo not-found)"
echo "Creating venv at $VENV_DIR"
$PYTHON -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
python -m pip install --upgrade pip setuptools wheel

if [ -f curso/requirements.txt ]; then
  echo "Installing curso/requirements.txt"
  pip install -r curso/requirements.txt
else
  echo "No curso/requirements.txt found"
  exit 1
fi

if [ -f curso/requirements-dev.txt ]; then
  echo "Installing curso/requirements-dev.txt"
  pip install -r curso/requirements-dev.txt
fi

echo "Environment setup complete. To activate: source $VENV_DIR/bin/activate"

# Install the repository in editable mode so `curso` is importable
echo "Installing repository in editable mode (pip install -e .)"
pip install -e .

# Ensure pkg_resources is importable (some python environments vendor it under pip)
python - <<'PY'
try:
  import pkg_resources
except Exception:
  import os, sys
  site_packages = next(p for p in sys.path if p.endswith('site-packages'))
  shim_dir = os.path.join(site_packages, 'pkg_resources')
  os.makedirs(shim_dir, exist_ok=True)
  with open(os.path.join(shim_dir, '__init__.py'), 'w') as f:
    f.write("from pip._vendor.pkg_resources import *\n")
  print('Created pkg_resources shim at', shim_dir)
PY
