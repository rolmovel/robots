# Research: JupyterLab Markdown Extensions

**Feature**: specs/003-jupyterlab-markdown-extensions  
**Date**: 2026-05-29

## Research Tasks

### 1. Extension para Markdown avanzado (GFM) en JupyterLab 4

**Decision**: Usar `jupyterlab-myst` (v2.6.0)

**Rationale**:
- Extensión oficial del ecosistema Jupyter Book / MyST.
- Soporta JupyterLab >= 4.0.0.
- Se instala vía pip: `pip install jupyterlab_myst` (prebuilt, no requiere Node.js).
- Renderiza Markdown con: frontmatter, admonitions, tablas, figure numbering, tabs, cards, grids, task lists editables, inline code evaluation.
- 190+ estrellas en GitHub, mantenida activamente (última release: v2.6.0, Dec 2025).

**Alternatives considered**:
- `jupyterlab-markup`: Solo JupyterLab 3.x, no compatible con JupyterLab 4. Descartado.
- Renderizador nativo de JupyterLab: Soporta Markdown básico pero no GFM completo ni extensiones como admonitions o tabs. Insuficiente.

---

### 2. Extension para diagramas Mermaid en JupyterLab 4

**Decision**: Usar `jupyterlab-myst` (mismo paquete que arriba)

**Rationale**:
- MyST soporta nativamente la directiva `{mermaid}` y también el formato de code-block ````mermaid`.
- Según la documentación oficial de MyST: "Both GitHub and JupyterLab support the translation of a code-block \`\`\`mermaid to a mermaid diagram directly, this can also be used by default in MyST."
- No es necesario un paquete separado (`jupyterlab-mermaid` no existe en PyPI).
- Los diagramas se renderizan inline como SVG.

**Alternatives considered**:
- `jupyterlab-mermaid`: No existe en PyPI. Descartado.
- `jupyterlab-markup[mermaid]`: Solo JupyterLab 3.x, extra "mermaid" no proporcionado. Descartado.

---

### 3. Compatibilidad con Python 3.11 y JupyterLab 4.x

**Decision**: Compatible sin restricciones.

**Rationale**:
- `jupyterlab-myst` v2.6.0 requiere solo `JupyterLab >= 4.0.0`.
- No tiene requisito de Python específico más allá de lo que JupyterLab 4 ya impone.
- Se instala como prebuilt extension (wheel pura `py3-none-any`), no necesita compilación.

---

### 4. Integración con setup existente

**Decision**: Añadir `jupyterlab-myst>=2.4` a `curso/requirements.txt`.

**Rationale**:
- El script `scripts/setup_env.sh` ya instala todo lo que esté en `curso/requirements.txt`.
- No se necesitan pasos adicionales de activación/configuración; la extensión se activa automáticamente al instalarse con pip.
- Verificación: `jupyter labextension list` mostrará `jupyterlab-myst` como habilitada.

---

## Summary

| Requisito | Solución | Paquete | Versión |
|-----------|----------|---------|---------|
| Markdown GFM completo | jupyterlab-myst | `jupyterlab-myst` | >=2.4 |
| Diagramas Mermaid | jupyterlab-myst (built-in) | (mismo paquete) | >=2.4 |
| Compatibilidad | JupyterLab 4 + Python 3.11 | ✅ | — |
| Instalación | pip install (prebuilt) | ✅ | — |

**Conclusión**: Un solo paquete (`jupyterlab-myst>=2.4`) resuelve P1 (Markdown) y P2 (Mermaid) simultáneamente. La implementación consiste en añadir una línea a `curso/requirements.txt` y actualizar documentación.
