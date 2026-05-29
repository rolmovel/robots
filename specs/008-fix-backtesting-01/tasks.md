# Tasks: Fix Backtesting Notebook – Capítulo 01

**Input**: Design documents from `specs/008-fix-backtesting-01/`

**Feature branch**: `008-fix-backtesting-01`
**Target file**: `curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb`

**Tech stack**: Python 3.12, backtesting==0.3.3, bokeh==3.9.0, pandas, matplotlib
**Scope**: Two cell edits (cell 12 + cell 16). No new files, no helper changes.

---

## Phase 1: Setup

**Purpose**: Normalize the notebook to a clean baseline before making changes.

- [X] T001 Clear all cell outputs and reset execution counts in `curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb`

**Checkpoint**: Notebook is normalized — no stale outputs, execution_count is null on all code cells.

---

## Phase 2: User Story 1 – Notebook executes without errors (Priority: P1) 🎯 MVP

**Goal**: Cell 12 (`bt.plot()`) no longer raises an uncaught exception, allowing all subsequent cells to run.

**Independent Test**: Execute only cells 2, 4, 6, 8, 12 in order from a clean kernel and confirm no `error`-type output cell is produced.

### Implementation for User Story 1

- [X] T002 [US1] Wrap `bt.plot()` in `try/except ValueError` in cell 12 of `curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb`

  Replace the current cell source:
  ```python
  # Gráfico interactivo completo (Bokeh)
  bt.plot()
  ```
  With:
  ```python
  # Gráfico interactivo completo (Bokeh)
  # NOTA: backtesting 0.3.3 usa una API de Bokeh obsoleta (DatetimeTickFormatter.days
  # espera str, no list). El gráfico interactivo no está disponible con Bokeh 3.x.
  try:
      bt.plot()
  except ValueError as e:
      if "DatetimeTickFormatter" in str(e):
          print("⚠️  bt.plot() no disponible con Bokeh 3.x.")
          print("   Ver la Equity Curve matplotlib en la celda anterior.")
      else:
          raise
  ```

**Checkpoint**: Cell 12 executes cleanly. Running "Run All Cells" no longer halts at cell 12.

---

## Phase 3: User Story 2 – Comparación Estrategia vs Buy & Hold produce resultados (Priority: P2)

**Goal**: Cell 14 prints the numeric comparison table (retorno, B&H, diferencia, max DD).

**Independent Test**: Execute cells 2–14 in order from a clean kernel and confirm cell 14 prints three numeric values without error.

### Implementation for User Story 2

- [X] T003 [US2] Validate that cell 14 in `curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb` executes correctly after the US1 fix

  No code change is required for cell 14 — it was blocked only by the error in cell 12.
  Run cells 2, 4, 6, 8, 12 (fixed), 14 in order and confirm output shows:
  - `Retorno Estrategia: 2.85%`
  - `Retorno Buy & Hold: 39.43%`
  - `Diferencia: -36.58%`
  - `Max Drawdown Estrat.: -9.05%`
  - The `⚠️ Buy & Hold supera a la estrategia` branch is printed (expected given metrics).

**Checkpoint**: Cell 14 produces full numeric comparison output.

---

## Phase 4: User Story 3 – Conclusiones concretas y sin marcadores (Priority: P3)

**Goal**: Cell 16 prints concrete backtest values; no `[...]` placeholders remain.

**Independent Test**: Execute cell 16 in isolation (after cells 2, 4, 6, 8) and confirm no `[` or `]` characters appear in the output.

### Implementation for User Story 3

- [X] T004 [US3] Replace placeholder conclusion text in cell 16 of `curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb`

  Replace the current cell source with:
  ```python
  print("""
  CONCLUSIONES DEL BACKTEST
  ========================

  1. Rendimiento: La estrategia retornó un 2.85% total (CAGR ~0.57%) frente a un
     Buy & Hold de JNJ del 39.43% en el mismo período. La estrategia sub-rinde
     considerablemente en retorno bruto.

  2. Riesgo: Max Drawdown de -9.05%, por debajo del umbral tolerable del 15%.
     La estrategia protege mejor el capital en las caídas.

  3. Sharpe Ratio: 0.109 — por debajo del target de 0.5 definido en spec.md.
     El ratio riesgo/retorno es insuficiente para la configuración actual.

  4. Detalles operativos: 7 operaciones, Win Rate 57.14%, Profit Factor 1.501.
     La estrategia es altamente selectiva (pocas señales de entrada).

  5. Limitaciones observadas:
     - Muy pocas señales de entrada (requiere 30 días consecutivos bajo SMA)
     - Alta dependencia del período SMA y del umbral days_below
     - No considera costes de oportunidad mientras espera señal de entrada

  6. DECISIÓN: Iterar.
     Justificación: El Max Drawdown cumple el objetivo (-9.05% < 15%), pero el
     retorno total y el Sharpe están muy por debajo de los targets. Se recomienda
     reducir el parámetro days_below (p.ej. 10–15 días) y evaluar un universo más
     amplio antes de descartar la estrategia.
  """)
  ```

**Checkpoint**: Cell 16 prints concrete values. No `[...]` placeholders appear in output.

---

## Phase 5: Polish & Validación final

**Purpose**: Confirm the notebook passes the success criteria (SC-001..004) end-to-end.

- [X] T005 Execute `curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb` end-to-end from a clean kernel and confirm 0 error-type output cells (success criterion SC-001)

  Validation command:
  ```bash
  source .venv/bin/activate
  jupyter nbconvert --to notebook --execute \
    curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb \
    --output /tmp/01_backtesting_check.ipynb

  python -c "
  import json
  nb = json.load(open('/tmp/01_backtesting_check.ipynb'))
  errs = [i for i,c in enumerate(nb['cells'])
          if any(o.get('output_type')=='error' for o in c.get('outputs',[]))]
  print('Error cells:', errs if errs else 'None — all cells passed ✓')
  "
  ```

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **US1 (Phase 2)**: Depends on Phase 1 (normalized notebook)
- **US2 (Phase 3)**: Depends on US1 fix — cell 14 is unblocked by cell 12 fix
- **US3 (Phase 4)**: Independent of US1/US2 — cell 16 is a standalone print statement
- **Polish (Phase 5)**: Depends on US1, US2, US3 all complete

### User Story Dependencies

| Story | Depends on | Independently testable? |
|-------|-----------|------------------------|
| US1 (P1) | T001 | Yes — cells 2, 4, 6, 8, 12 only |
| US2 (P2) | T002 (US1 fix) | Yes — cells 2–14 |
| US3 (P3) | T001 only | Yes — cell 16 is independent |

### Parallel Opportunities

- **T003 (US2) and T004 (US3)** can execute in parallel once T002 is done (T003 requires the
  US1 fix in place; T004 is fully independent of T002/T003 and can run after T001).
- **T005** requires T002, T003, and T004 to be complete.

---

## Parallel Example: US1 → US2 + US3 → Polish

```
T001 (normalize)
  └── T002 [US1] (fix cell 12)
        └── T003 [US2] (validate cell 14)  ──┐
  └── T004 [US3] (fix cell 16)  ─────────────┤
                                              └── T005 (end-to-end validation)
```

---

## Implementation Strategy

**MVP = US1 only (T001 + T002)**

Completing US1 unblocks "Run All Cells" for the student and provides immediate value.
US2 and US3 are polish — they add precision and completeness without blocking the
core learning experience.

Suggested execution order for a single implementer:
1. T001 → T002 → T003 (verify) → T004 → T005
