# Feature Specification: Fix Backtesting Notebook – Capítulo 01

**Feature Branch**: `008-fix-backtesting-01`

**Created**: 2026-05-29

**Status**: Draft

**Input**: User description: "revisar el backtesting del capitulo 01"

## User Scenarios & Testing *(mandatory)*

### User Story 1 – Notebook ejecuta sin errores de inicio a fin (Priority: P1)

Un estudiante del curso abre `01_backtesting.ipynb`, ejecuta todas las celdas en
orden con "Run All" y obtiene resultados completos sin ninguna excepción.

**Why this priority**: Sin ejecución limpia, el estudiante no puede aprender
ni verificar la estrategia. Es el requisito mínimo del capítulo.

**Independent Test**: Ejecutar `jupyter nbconvert --to notebook --execute 01_backtesting.ipynb`
y confirmar que el archivo resultante no contiene celdas con output type `error`.

**Acceptance Scenarios**:

1. **Given** el notebook con todas sus celdas en orden, **When** el estudiante
   ejecuta "Run All Cells", **Then** todas las celdas completan sin lanzar
   excepciones.
2. **Given** el entorno virtual del proyecto instalado, **When** se ejecuta
   la celda `bt.plot()`, **Then** se genera la visualización interactiva o,
   si el entorno Bokeh no es compatible, se muestra un aviso claro en lugar
   de un traceback inesperado.

---

### User Story 2 – Comparación Estrategia vs Buy & Hold produce resultados (Priority: P2)

El estudiante puede leer los valores numéricos de la comparación entre la
estrategia SMA y el Buy & Hold en la celda de resumen (actualmente celda 14).

**Why this priority**: Esta comparación es el núcleo pedagógico del capítulo:
el estudiante debe ver si la estrategia agrega valor respecto al benchmark.

**Independent Test**: Ejecutar sólo las celdas de setup, datos, estrategia,
backtest y comparación (celdas 2, 4, 6, 8, 14) y confirmar que los valores
numéricos `retorno_total_pct`, `buy_and_hold_pct` y `max_drawdown_pct` se
imprimen correctamente.

**Acceptance Scenarios**:

1. **Given** que el backtest ha completado (celda 8 con salida válida),
   **When** se ejecuta la celda de comparación, **Then** se muestran los tres
   valores numéricos (retorno estrategia, retorno B&H, diferencia).
2. **Given** que los resultados muestran que B&H supera a la estrategia,
   **When** se ejecuta la celda, **Then** el mensaje de advertencia `⚠️` se
   imprime indicando que el valor puede estar en menor drawdown o mejor Sharpe.

---

### User Story 3 – Conclusiones del backtest son legibles y representativas (Priority: P3)

El estudiante lee la sección de conclusiones (celda 16) y comprende el estado
actual de la estrategia: rendimiento, riesgo, Sharpe y decisión final, con
valores reales sustituidos en lugar de marcadores de posición.

**Why this priority**: Los marcadores `[Interpretar resultado...]` del
template dejan la celda incompleta y no aportan valor pedagógico.

**Independent Test**: Revisar la celda 16 y confirmar que no contiene
texto entre corchetes que no sea un valor concreto.

**Acceptance Scenarios**:

1. **Given** los resultados del backtest (retorno 2.85%, Sharpe 0.109,
   Max DD -9.05%, Win Rate 57.14%), **When** el estudiante lee las
   conclusiones, **Then** ve valores numéricos reales y una decisión
   explícita (aprobar / iterar / descartar) con justificación.

---

### Edge Cases

- ¿Qué ocurre si `bt.plot()` falla porque Bokeh no está instalado o su
  versión es incompatible? La celda debe capturar el error y mostrar un mensaje
  informativo en lugar de interrumpir la ejecución del resto del notebook.
- ¿Qué pasa si la variable `metrics` no está disponible al ejecutar la celda
  de comparación (p.ej. ejecución parcial)? El error debe ser descriptivo.
- ¿El notebook produce resultados deterministas? Los datos históricos de
  yfinance pueden variar; el notebook debe cargar datos con un rango de fechas
  fijo para garantizar reproducibilidad.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: La celda `bt.plot()` DEBE ejecutarse sin lanzar una excepción
  no controlada. Si Bokeh lanza un `ValueError` por incompatibilidad de versión,
  la celda DEBE capturar la excepción y mostrar un aviso explicativo.
- **FR-002**: La celda de comparación Estrategia vs Buy & Hold DEBE producir
  salida numérica visible al ser ejecutada después de la celda de backtest.
- **FR-003**: La celda de conclusiones DEBE reemplazar todos los marcadores
  de posición `[...]` con valores concretos derivados de los resultados
  del backtest (retorno 2.85%, Sharpe 0.109, Max DD -9.05%).
- **FR-004**: El notebook completo DEBE ejecutarse de inicio a fin sin
  errores al usar "Run All Cells" desde un entorno limpio con el `venv`
  del proyecto activado.
- **FR-005**: Cualquier cambio en la celda `bt.plot()` DEBE preservar la
  intención pedagógica: el estudiante debe poder ver o entender el gráfico
  interactivo de backtesting.py.

## Key Entities

- **Notebook `01_backtesting.ipynb`**: Archivo Jupyter con 18 celdas que
  implementa y evalúa la estrategia SMA con filtro sectorial del capítulo 01.
- **`bt.plot()`**: Llamada al método de visualización de `backtesting.py`
  que genera un gráfico interactivo en Bokeh. Actualmente falla por
  incompatibilidad entre la API de `DatetimeTickFormatter.days` y la
  versión de Bokeh instalada (espera `str`, recibe `list`).
- **`metrics`**: Objeto con los resultados del backtest (retorno, Sharpe,
  drawdown, etc.) calculado en la celda 8 y consumido en la celda 14.
- **Celda 16 (Conclusiones)**: Celda de código con texto fijo de conclusiones;
  actualmente contiene marcadores de posición sin valores concretos.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Al ejecutar "Run All Cells", el notebook completa con 0 celdas
  con output type `error` (actualmente 1 celda con error).
- **SC-002**: La celda de comparación muestra los tres valores numéricos
  esperados (retorno estrategia, retorno B&H, diferencia) en cada ejecución.
- **SC-003**: La celda de conclusiones no contiene ningún marcador entre
  corchetes `[...]` en su salida impresa.
- **SC-004**: El notebook se puede ejecutar de forma reproducible en el
  entorno del proyecto sin instalar dependencias adicionales más allá de
  las ya declaradas en `requirements.txt`.

## Assumptions

- El entorno virtual del proyecto tiene `backtesting.py` y `bokeh` instalados
  en versiones potencialmente incompatibles entre sí para `bt.plot()`.
- El fix preferido para `bt.plot()` es envolver la llamada en un bloque
  `try/except` que captura `ValueError` y muestra un aviso, manteniendo
  el resto del flujo de ejecución intacto.
- Los datos de yfinance para `JNJ` en el período usado por el notebook están
  disponibles y producen los resultados ya observados (retorno 2.85%,
  Sharpe 0.109, Max DD -9.05%).
- No se pide refactorizar la lógica de la estrategia ni cambiar parámetros;
  el alcance es únicamente corregir los errores de ejecución y completar
  el contenido de las celdas de conclusiones.
- El notebook `01_estrategia.ipynb` está fuera del alcance de este fix.

## Constitution Alignment *(mandatory)*

- **Spec-First Delivery**: Este documento define las historias de usuario,
  requisitos funcionales, supuestos, casos límite y criterios de éxito
  medibles para el fix del notebook de backtesting del capítulo 01.
- **Independent Value Slices**: Cada historia de usuario puede verificarse y
  entregarse de forma independiente (ejecución sin errores, comparación
  numérica, conclusiones concretas).
- **Verifiable Outcomes**: Cada historia incluye escenarios de aceptación
  con Given/When/Then y un método de test independiente.
- **Minimal, Explicit Change**: El alcance está acotado a tres celdas
  (12, 14, 16); no se modifica la lógica de la estrategia ni la estructura
  del notebook.
