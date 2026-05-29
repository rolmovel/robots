# Contract: Extension Delivery

**Feature**: specs/003-jupyterlab-markdown-extensions  
**Type**: Dependency integration contract

## Pre-conditions

- Python 3.11 virtual environment active
- `jupyterlab>=4.0,<5.0` installed
- pip available and functional

## Installation Contract

### Input
```
pip install jupyterlab-myst>=2.4
```

### Post-conditions
1. `jupyter labextension list` includes `jupyterlab-myst` as enabled
2. Opening a `.md` file or Markdown cell in JupyterLab renders:
   - GFM elements (tables, task lists, strikethrough)
   - MyST directives (admonitions, tabs, cards)
   - Mermaid diagrams via ````mermaid` code blocks or `{mermaid}` directive

## Verification Contract

### Programmatic check
```python
import importlib
assert importlib.import_module("jupyterlab_myst") is not None
```

### CLI check
```bash
jupyter labextension list 2>&1 | grep -q "jupyterlab-myst"
```

## Compatibility Matrix

| Component | Required | Verified |
|-----------|----------|----------|
| JupyterLab | >=4.0,<5.0 | ✅ |
| Python | 3.11 | ✅ |
| jupyterlab-myst | >=2.4 | ✅ |

## Markdown Rendering Contract

### Supported syntax elements

| Syntax | Format | Rendered |
|--------|--------|----------|
| Mermaid diagram | ````mermaid ... ``` | SVG diagram |
| Mermaid directive | `{mermaid}` | SVG diagram |
| Admonition | `:::{note}` | Styled callout |
| Table | GFM pipe tables | HTML table |
| Task list | `- [ ] item` | Interactive checkbox |
| Math | `$...$` / `$$...$$` | KaTeX/MathJax |
