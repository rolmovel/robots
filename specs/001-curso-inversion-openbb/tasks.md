# Tasks: Curso de Inversión en Bolsa (Principiante → Experto) con OpenBB

**Input**: Design documents from `/specs/001-curso-inversion-openbb/`

**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Automated tests are not applicable — validation is manual (reproducible notebooks).
Each chapter MUST include a reproducible validation task.

**Organization**: Tasks are grouped by chapter to enable independent implementation and validation of each increment.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[US1]**: All tasks belong to User Story 1 (single consolidated story)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Project Infrastructure)

**Purpose**: Create project structure, dependencies, and shared configuration

- [X] T001 Create project directory structure per plan in curso/
- [X] T002 [P] Create curso/requirements.txt with pinned dependencies (openbb>=4.0, backtesting>=0.3.3, pandas-ta>=0.3.14, pandas>=2.0, numpy>=1.24, matplotlib>=3.7, plotly>=5.0, jupyterlab>=4.0)
- [X] T003 [P] Create curso/lib/__init__.py with package initialization

---

## Phase 2: Foundational (Shared Libraries)

**Purpose**: Core utilities that ALL chapters depend on — MUST complete before chapter content

**⚠️ CRITICAL**: No chapter content can begin until this phase is complete

- [X] T004 [P] [US1] Create curso/lib/data.py — OpenBB wrapper with download, local CSV/Parquet cache, gap detection and interpolation
- [X] T005 [P] [US1] Create curso/lib/indicators.py — pandas-ta wrappers for SMA, EMA, RSI, MACD, Bollinger Bands with course defaults
- [X] T006 [P] [US1] Create curso/lib/backtest.py — Helper to run backtesting.py, extract standard metrics (BacktestMetrics from data-model), compare strategies
- [X] T007 [P] [US1] Create curso/lib/reporting.py — Standard visualizations: equity curve, drawdown chart, metrics summary table

**Checkpoint**: Foundation ready — chapter creation can now proceed sequentially

---

## Phase 3: Capítulo 00 — Fundamentos (Nivel: principiante)

**Goal**: Estudiante entiende conceptos base de inversión y puede descargar/explorar datos con OpenBB

**Independent Test**: Estudiante completa cuestionario de fundamentos y ejecuta notebook de exploración sin errores

- [X] T008 [US1] Write curso/capitulo-00-fundamentos/README.md — Teoría: mercados, activos, riesgo/rendimiento, horizonte temporal, diversificación, rol de datos abiertos
- [X] T009 [US1] Create curso/capitulo-00-fundamentos/notebooks/00_intro_openbb.ipynb — Notebook demostrando: instalación, descarga de datos históricos (equity), exploración con pandas, visualización básica de precios
- [X] T010 [US1] Create curso/capitulo-00-fundamentos/cuestionario.md — Autoevaluación de 10 preguntas sobre fundamentos cubiertos en README

**Checkpoint**: Capítulo 00 completado — estudiante listo para estrategias

---

## Phase 4: Capítulo 01 — Media Móvil Simple con Filtro Sectorial (Nivel: principiante)

**Goal**: Primera estrategia automatizada completa — filtrar empresas de un sector (salud) cuyo precio está por debajo de MA(30) durante 1 mes

**Independent Test**: Notebook de backtesting produce métricas completas; spec.md es revisable por otro estudiante sin ambigüedades

- [X] T011 [US1] Write curso/capitulo-01-media-movil/README.md — Teoría: qué es una media móvil, tipos (SMA/EMA), uso como filtro de tendencia, concepto de señales entry/exit, introducción al backtesting
- [X] T012 [US1] Write curso/capitulo-01-media-movil/spec.md — Especificación SDD de la estrategia: filtro sector salud + MA(30) por debajo 1 mes, reglas entrada/salida, gestión riesgo, parámetros optimizables, métricas
- [X] T013 [US1] Create curso/capitulo-01-media-movil/notebooks/01_estrategia.ipynb — Implementación: descarga datos sector salud vía OpenBB, cálculo SMA(30), detección de señal (precio < SMA durante 30 días), visualización de señales sobre gráfico de precios
- [X] T014 [US1] Create curso/capitulo-01-media-movil/notebooks/01_backtesting.ipynb — Backtesting: ejecutar estrategia con backtesting.py, reportar métricas estándar, equity curve, comparar vs buy&hold, conclusiones + decisión

**Checkpoint**: Capítulo 01 completado — primera entrega completa (spec + implementación + backtesting)

---

## Phase 5: Capítulo 02 — Cruce de Medias Móviles (Nivel: principiante-intermedio)

**Goal**: Estrategia SMA Cross con señales long/short y optimización de períodos

**Independent Test**: Notebook ejecuta optimización de parámetros y documenta riesgo de sobreajuste

- [X] T015 [US1] Write curso/capitulo-02-sma-cross/README.md — Teoría: cruce de medias, señales golden/death cross, optimización de períodos, peligros del overfitting
- [X] T016 [US1] Write curso/capitulo-02-sma-cross/spec.md — Especificación SDD: SMA(n1) y SMA(n2) cross, reglas long/short, parámetros optimizables (n1, n2), restricciones
- [X] T017 [US1] Create curso/capitulo-02-sma-cross/notebooks/02_estrategia.ipynb — Implementación: descarga datos, cálculo dual SMA, señales de cruce, visualización
- [X] T018 [US1] Create curso/capitulo-02-sma-cross/notebooks/02_backtesting.ipynb — Backtesting + optimización: barrido de parámetros n1/n2 con optimizador SAMBO, heatmap, análisis de sobreajuste, métricas, conclusiones

**Checkpoint**: Capítulo 02 completado — estudiante entiende optimización y sus riesgos

---

## Phase 6: Capítulo 03 — Momentum / RSI (Nivel: intermedio)

**Goal**: Introducir osciladores (RSI) y combinación con filtros de tendencia

**Independent Test**: Estrategia combina RSI con filtro de tendencia; backtesting incluye análisis de zonas sobrecompra/sobreventa

- [X] T019 [US1] Write curso/capitulo-03-momentum-rsi/README.md — Teoría: momentum, osciladores, RSI (cálculo, interpretación), zonas sobrecompra/sobreventa, combinación con filtros
- [X] T020 [US1] Write curso/capitulo-03-momentum-rsi/spec.md — Especificación SDD: RSI(14) + SMA(50) filtro, reglas de entrada (RSI < 30 + precio > SMA), salida (RSI > 70), gestión riesgo
- [X] T021 [US1] Create curso/capitulo-03-momentum-rsi/notebooks/03_estrategia.ipynb — Implementación: cálculo RSI con pandas-ta, combinación con SMA, señales, visualización dual (precio + RSI panel)
- [X] T022 [US1] Create curso/capitulo-03-momentum-rsi/notebooks/03_backtesting.ipynb — Backtesting: evaluación multi-ticker, métricas, comparación con estrategia de cap-01/02, conclusiones

**Checkpoint**: Capítulo 03 completado — estudiante domina osciladores y combinación de indicadores

---

## Phase 7: Capítulo 04 — Mean Reversion / Bollinger Bands (Nivel: intermedio)

**Goal**: Estrategia de reversión a la media con Bollinger Bands y stop-loss dinámico

**Independent Test**: Backtesting demuestra comportamiento en mercado lateral vs tendencial

- [X] T023 [US1] Write curso/capitulo-04-mean-reversion/README.md — Teoría: reversión a la media, estadística, Bollinger Bands (cálculo, interpretación), stop-loss dinámico, mercados laterales
- [X] T024 [US1] Write curso/capitulo-04-mean-reversion/spec.md — Especificación SDD: entrada en banda inferior, salida en banda media/superior, stop-loss a X% bajo entrada, parámetros (período, desviaciones)
- [X] T025 [US1] Create curso/capitulo-04-mean-reversion/notebooks/04_estrategia.ipynb — Implementación: Bollinger Bands con pandas-ta, detección de toques, lógica de entrada/salida, visualización con bandas
- [X] T026 [US1] Create curso/capitulo-04-mean-reversion/notebooks/04_backtesting.ipynb — Backtesting: evaluación en distintos regímenes de mercado, métricas, análisis lateral vs tendencial, conclusiones

**Checkpoint**: Capítulo 04 completado — estudiante comprende reversión a la media y sus limitaciones

---

## Phase 8: Capítulo 05 — Breakout / Donchian Channels (Nivel: intermedio-avanzado)

**Goal**: Estrategia de breakout con trailing stop y gestión de volatilidad

**Independent Test**: Backtesting implementa trailing stop y compara con stop fijo

- [X] T027 [US1] Write curso/capitulo-05-breakout/README.md — Teoría: breakouts, Donchian Channels, ATR, trailing stop, gestión de posición basada en volatilidad
- [X] T028 [US1] Write curso/capitulo-05-breakout/spec.md — Especificación SDD: entrada en ruptura de canal superior(20), salida en canal inferior(10), trailing stop con ATR, position sizing por volatilidad
- [X] T029 [US1] Create curso/capitulo-05-breakout/notebooks/05_estrategia.ipynb — Implementación: Donchian con pandas-ta, ATR, lógica de breakout + trailing stop, visualización canales
- [X] T030 [US1] Create curso/capitulo-05-breakout/notebooks/05_backtesting.ipynb — Backtesting: comparar trailing stop vs stop fijo, métricas, análisis por régimen de volatilidad, conclusiones

**Checkpoint**: Capítulo 05 completado — estudiante domina gestión de posición y volatilidad

---

## Phase 9: Capítulo 06 — Multi-Factor (Nivel: avanzado)

**Goal**: Combinar múltiples señales con scoring y construir un portfolio simple

**Independent Test**: Sistema multi-factor genera ranking de activos y backtest de portfolio

- [X] T031 [US1] Write curso/capitulo-06-multi-factor/README.md — Teoría: sistemas multi-factor, scoring/ranking, ponderación de señales, diversificación de portfolio, correlación
- [X] T032 [US1] Write curso/capitulo-06-multi-factor/spec.md — Especificación SDD: combinar RSI + Momentum + Volatilidad, scoring normalizado, selección top-N, rebalanceo periódico, métricas de portfolio
- [X] T033 [US1] Create curso/capitulo-06-multi-factor/notebooks/06_estrategia.ipynb — Implementación: cálculo multi-indicador sobre universo de activos, scoring, ranking, selección, visualización
- [X] T034 [US1] Create curso/capitulo-06-multi-factor/notebooks/06_backtesting.ipynb — Backtesting: backtest de portfolio (simulación de rebalanceo), métricas (Sharpe portfolio, diversificación), comparación vs individual, conclusiones

**Checkpoint**: Capítulo 06 completado — estudiante sabe construir sistemas combinados

---

## Phase 10: Capítulo 07 — Agente Autónomo Integrador (Nivel: avanzado)

**Goal**: Sintetizar aprendizajes en un agente completo con orquestación, scheduling y evaluación holística

**Independent Test**: El agente ejecuta de forma autónoma múltiples estrategias y produce un reporte consolidado de rendimiento

- [X] T035 [US1] Write curso/capitulo-07-agente-autonomo/README.md — Teoría: arquitectura de agentes, orquestación de estrategias, scheduling, reporting de producción, walk-forward testing
- [X] T036 [US1] Write curso/capitulo-07-agente-autonomo/spec.md — Especificación SDD: agente que ejecuta N estrategias seleccionadas, criterios de activación/desactivación, reporting diario, métricas agregadas
- [X] T037 [US1] Create curso/capitulo-07-agente-autonomo/notebooks/07_agente.ipynb — Implementación: orquestador que carga specs de capítulos anteriores, ejecuta señales, consolida decisiones, genera reporte
- [X] T038 [US1] Create curso/capitulo-07-agente-autonomo/notebooks/07_backtesting_integral.ipynb — Backtesting integral: walk-forward sobre todo el período, métricas consolidadas multi-estrategia, análisis de correlación entre estrategias, reporte final del curso

**Checkpoint**: Capítulo 07 completado — estudiante tiene un agente funcional y evaluado

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Mejoras transversales a todos los capítulos

- [X] T039 [P] [US1] Create curso/README.md — Índice general del curso con descripción, prerrequisitos, instrucciones de setup y mapa de capítulos
- [X] T040 [P] [US1] Add disclaimer financiero estándar en cada README de capítulo (template en curso/lib/disclaimer.md)
- [X] T041 [US1] Validate quickstart.md instructions by running setup from scratch in clean environment
- [X] T042 [US1] Review all spec.md files for compliance with contracts/chapter-delivery-contract.md
- [X] T043 [P] [US1] Add .gitignore entries for datos descargados (*.csv, *.parquet en curso/data/), notebooks checkpoints (.ipynb_checkpoints/)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup (T001-T003)
- **Capítulo 00 (Phase 3)**: Depends on Foundational (Phase 2) — uses lib/data.py
- **Capítulo 01 (Phase 4)**: Depends on Phase 3 (conceptual prerequisite)
- **Capítulo 02 (Phase 5)**: Depends on Phase 4
- **Capítulo 03 (Phase 6)**: Depends on Phase 5
- **Capítulo 04 (Phase 7)**: Depends on Phase 6
- **Capítulo 05 (Phase 8)**: Depends on Phase 7
- **Capítulo 06 (Phase 9)**: Depends on Phase 8
- **Capítulo 07 (Phase 10)**: Depends on ALL previous chapters (integrator)
- **Polish (Phase 11)**: Can start after Phase 4 (partial), fully after Phase 10

### Within Each Chapter

- README.md first (theory)
- spec.md second (specification before code)
- Notebook de estrategia third (implementation)
- Notebook de backtesting fourth (evaluation)

### Parallel Opportunities

- All Phase 2 tasks (T004-T007) can run in parallel (different files)
- Phase 11 polish tasks marked [P] can run in parallel
- Within each chapter, README and spec can be written in parallel only if theory is already clear

---

## Parallel Example: Foundational Phase

```bash
# Launch all lib modules together (no interdependencies):
Task: "Create curso/lib/data.py"
Task: "Create curso/lib/indicators.py"
Task: "Create curso/lib/backtest.py"
Task: "Create curso/lib/reporting.py"
```

---

## Implementation Strategy

### MVP First (Capítulos 00 + 01 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (lib/)
3. Complete Phase 3: Capítulo 00 (fundamentos)
4. Complete Phase 4: Capítulo 01 (primera estrategia completa)
5. **STOP and VALIDATE**: Verificar que la entrega cumple el contrato (spec + notebook + backtesting)
6. Demo: estudiante reproduce notebook y obtiene resultados concordantes

### Incremental Delivery

1. Setup + Foundational → Infrastructure ready
2. Capítulo 00 → Fundamentos cubiertos
3. Capítulo 01 → Primera automatización completa (MVP!)
4. Capítulo 02 → Optimización de parámetros
5. Capítulo 03 → Osciladores y combinación
6. Capítulo 04 → Mean reversion
7. Capítulo 05 → Breakout y volatilidad
8. Capítulo 06 → Multi-factor
9. Capítulo 07 → Agente integrador (capstone)
10. Polish → Refinamiento transversal

Each chapter adds an independently valuable strategy to the student's toolkit.

---

## Notes

- [P] tasks = different files, no dependencies
- [US1] label maps all tasks to the single consolidated user story
- Each chapter is independently completable and verifiable per contracts/chapter-delivery-contract.md
- Include at least one validation task per chapter (the backtesting notebook IS the validation)
- Commit after each chapter or logical group
- Stop at any checkpoint to validate chapter independently
- Avoid: vague tasks, same file conflicts, cross-chapter dependencies that break independence (except sequential learning path)
