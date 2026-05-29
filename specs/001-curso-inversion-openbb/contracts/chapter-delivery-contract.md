# Contrato de Entrega por Capítulo

**Tipo**: Contrato interno (curso → estudiante)

## Estructura obligatoria de entrega (capítulos 01+)

Cada capítulo de estrategia DEBE entregar los siguientes artefactos para
considerarse completado:

### 1. Especificación de Estrategia (`spec.md`)

Documento Markdown con la siguiente estructura mínima:

```markdown
# Estrategia: [Nombre]

## Objetivo
[Qué busca lograr]

## Hipótesis de Mercado
[Premisa que explota la estrategia]

## Reglas Operativas
- Entrada: [condiciones]
- Salida: [condiciones]
- Stop-loss: [condiciones]

## Gestión de Riesgo
- Posición máxima: [%]
- Drawdown tolerable: [%]

## Parámetros Optimizables
| Parámetro | Rango | Default |
|-----------|-------|---------|
| [nombre]  | [min-max] | [valor] |

## Supuestos
- [lista]

## Métricas de Evaluación
- [KPIs esperados]
```

### 2. Notebook de Implementación (`notebooks/<NN>_estrategia.ipynb`)

Jupyter notebook ejecutable que:

- Descarga datos desde OpenBB para el universo definido.
- Calcula los indicadores técnicos requeridos.
- Implementa la lógica de señales (entrada/salida).
- Produce al menos una visualización del comportamiento de señales.
- Es reproducible: otro estudiante puede ejecutarlo sin modificaciones.

### 3. Notebook de Backtesting (`notebooks/<NN>_backtesting.ipynb`)

Jupyter notebook ejecutable que:

- Ejecuta el backtest usando backtesting.py con la estrategia del capítulo.
- Reporta métricas estándar: Sharpe, Sortino, max drawdown, win rate, profit factor, CAGR.
- Incluye gráfico de equity curve y drawdown.
- Compara contra benchmark (buy & hold).
- Concluye con interpretación: aprobar / iterar / descartar + justificación.

## Criterios de aceptación

| Criterio | Obligatorio |
|----------|-------------|
| spec.md sin ambigüedades en reglas | ✅ |
| Notebook de implementación ejecuta sin errores | ✅ |
| Notebook de backtesting produce métricas completas | ✅ |
| Conclusiones incluyen limitaciones y riesgos | ✅ |
| Otro estudiante puede reproducir resultados | ✅ |
| Optimización documenta riesgo de sobreajuste | ✅ (cap 02+) |

## Capítulo 00 (Fundamentos) — Excepción

El capítulo introductorio NO requiere spec de estrategia ni backtesting.
Entrega:

- `README.md` con conceptos teóricos.
- `notebooks/00_intro_openbb.ipynb` demostrando descarga y exploración de datos.
- Cuestionario de autoevaluación de fundamentos.
