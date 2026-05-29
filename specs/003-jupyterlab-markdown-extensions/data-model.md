# Data Model: JupyterLab Markdown Extensions

**Feature**: specs/003-jupyterlab-markdown-extensions

## Entities

### 1. Extension Package

| Field | Type | Description |
|-------|------|-------------|
| name | string | PyPI package name (`jupyterlab-myst`) |
| version_constraint | string | Version spec for requirements.txt (`>=2.4`) |
| provides | list[string] | Capabilities: `["markdown-gfm", "mermaid-diagrams"]` |
| activation | enum | `automatic` — no manual enable step needed |
| jupyterlab_compat | string | `>=4.0,<5.0` |
| python_compat | string | `>=3.9` |

### 2. Configuration

| Field | Type | Description |
|-------|------|-------------|
| file | path | `curso/requirements.txt` |
| entry | string | `jupyterlab-myst>=2.4` |
| auto_install | boolean | `true` — installed by `scripts/setup_env.sh` |

### 3. Verification

| Field | Type | Description |
|-------|------|-------------|
| command | string | `jupyter labextension list` |
| expected_output | string | Contains `jupyterlab-myst` enabled |
| ci_check | boolean | Import validation in CI workflow |

## Relationships

```
requirements.txt ──contains──> jupyterlab-myst entry
setup_env.sh ──installs──> requirements.txt
jupyterlab-myst ──provides──> GFM Markdown rendering
jupyterlab-myst ──provides──> Mermaid diagram rendering
CI workflow ──validates──> jupyterlab-myst import
```

## State Transitions

N/A — This is a static dependency addition with no runtime state machine.
