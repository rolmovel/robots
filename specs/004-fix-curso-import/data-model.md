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
| installs | list | `curso` editable install plus `curso/requirements.txt` and dev requirements |
| post_install | string | verification steps (import check)

### CI Job

| Field | Type | Description |
|-------|------|-------------|
| workflow | string | `.github/workflows/ci-install-check.yml` |
| checks | list | `pip install`, `import curso`, optional nbconvert smoke test |

## Relationships

```
setup_env.sh --installs--> curso/requirements.txt
setup_env.sh --installs--> pip install -e . (repo)
pyproject.toml + setup.cfg --describe--> package metadata for pip install
CI --validates--> import curso and notebook smoke tests
```
