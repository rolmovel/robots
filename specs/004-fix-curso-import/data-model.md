# Data Model: Packaging and Setup

**Feature**: specs/004-fix-curso-import

## Entities

### Repository Package

| Field | Type | Description |
|-------|------|-------------|
| name | string | `robots-curso` (distribution name) |
| modules | list | packages included (should include `curso`) |
| version | string | packaging version (0.0.1) |

### Setup Script

| Field | Type | Description |
|-------|------|-------------|
| path | string | `scripts/setup_env.sh` |
| setuptools_pin | string | `<72` (required for `pkg_resources` availability) |
| installs | list | `curso` editable install plus `curso/requirements.txt` and dev requirements |
| post_install | string | verification steps (import check) |

### Dependency Constraint: setuptools

| Field | Type | Description |
|-------|------|-------------|
| package | string | `setuptools` |
| constraint | string | `<72` |
| reason | string | `pandas_ta` 0.3.14b requires `pkg_resources`, removed in setuptools 78+ |
| affected_by | string | `pandas_ta/__init__.py` line 7: `from pkg_resources import get_distribution` |

### CI Job

| Field | Type | Description |
|-------|------|-------------|
| workflow | string | `.github/workflows/ci-install-check.yml` |
| checks | list | `pip install`, `import curso`, `import pkg_resources`, optional nbconvert smoke test |

## Relationships

```
setup_env.sh --installs--> "setuptools<72" (pinned for pkg_resources)
setup_env.sh --installs--> curso/requirements.txt
setup_env.sh --installs--> pip install -e . (repo)
pyproject.toml + setup.cfg --describe--> package metadata for pip install
pandas_ta --requires--> pkg_resources (from setuptools<72)
CI --validates--> import curso and notebook smoke tests
```
