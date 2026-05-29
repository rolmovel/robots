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
