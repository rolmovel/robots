# Feature Specification: Transformadas de Fourier como Indicadores de Trading

**Feature Branch**: `[010-fourier-transform-indicators]`

**Created**: 2026-06-01

**Status**: Draft

**Input**: User description: "quisiera analizar las transformadas de fourier como indicadores para la estrategia de inversion. Añade un nuevo capitulo con los notebooks"

## User Scenarios & Testing

### User Story 1 - Comprender la descomposición espectral de precios (Priority: P1)

El usuario desea entender cómo se descomponen las series temporales de precios en sus componentes de frecuencia usando la Transformada Rápida de Fourier (FFT). Quiere visualizar el espectro de potencias para identificar los ciclos dominantes en los datos de mercado.

**Why this priority**: Es el fundamento teórico y práctico sin el cual las estrategias de trading basadas en Fourier no tienen sentido. Sin comprender qué frecuencias dominan el precio, no se puede filtrar ni construir señales.

**Independent Test**: Puede ser probado completamente descargando datos históricos de un activo, calculando su FFT, generando un gráfico de espectro de potencias y extrayendo los ciclos dominantes. Entrega valor educativo inmediato al usuario.

**Acceptance Scenarios**:

1. **Given** datos históricos de precios de un activo, **When** se aplica la transformada FFT, **Then** se obtiene un espectro de potencias que muestra las frecuencias dominantes del activo.
2. **Given** el espectro de potencias, **When** se identifican los picos de frecuencia, **Then** se pueden extraer los períodos de los ciclos dominantes (ej. ciclo de 20 días, ciclo de 60 días).
3. **Given** los ciclos dominantes identificados, **When** se reconstruye la señal filtrada, **Then** la serie resultante suaviza el precio original conservando las oscilaciones cíclicas principales.

---

### User Story 2 - Filtrar señales de trading basadas en ciclos dominantes (Priority: P2)

El usuario quiere construir una estrategia de trading que utilice la descomposición de Fourier para filtrar el "ruido" de alta frecuencia de los precios y generar señales de entrada/salida basadas en los componentes cíclicos de baja frecuencia. La idea es operar las oscilaciones cíclicas identificadas.

**Why this priority**: Es el núcleo de la estrategia. Transforma el análisis espectral en decisiones de trading accionables con reglas de entrada y salida claras.

**Independent Test**: Puede ser probado completamente construyendo un filtro paso bajo/banda basado en FFT, generando señales de compra/venta sobre la señal filtrada, y ejecutando un backtest con métricas de rendimiento comparadas contra buy & hold.

**Acceptance Scenarios**:

1. **Given** los ciclos dominantes identificados de un activo, **When** se construye un filtro de Fourier que retiene solo esas frecuencias, **Then** se obtiene una señal filtrada que elimina el ruido de alta frecuencia.
2. **Given** la señal filtrada, **When** el precio cruza por encima de la señal filtrada, **Then** se genera una señal de compra.
3. **Given** la señal filtrada, **When** el precio cruza por debajo de la señal filtrada, **Then** se genera una señal de venta.
4. **Given** las señales generadas, **When** se ejecuta el backtest, **Then** se obtienen métricas de rendimiento (Sharpe, drawdown, win rate) comparables con estrategias tradicionales.

---

### User Story 3 - Comparar múltiples activos con análisis espectral (Priority: P3)

El usuario desea comparar el comportamiento espectral de múltiples activos simultáneamente para identificar qué activos tienen ciclos más estables o predecibles, y seleccionar aquellos con mejores propiedades cíclicas para la estrategia.

**Why this priority**: Permite optimizar la selección de universo de activos basado en propiedades espectrales objetivas, no solo en rendimiento histórico.

**Independent Test**: Puede ser probado descargando datos de múltiples tickers, calculando el espectro de cada uno, y generando un ranking basado en la estabilidad y amplitud de sus ciclos dominantes.

**Acceptance Scenarios**:

1. **Given** un universo de activos, **When** se calcula el espectro de potencias de cada uno, **Then** se puede comparar la estabilidad de sus ciclos dominantes a lo largo del tiempo.
2. **Given** los espectros comparados, **When** se filtran activos por estabilidad cíclica, **Then** se obtiene un subconjunto de activos con ciclos más predecibles para operar.

---

### Edge Cases

- ¿Qué sucede cuando la serie temporal tiene longitud no potencia de 2? (La FFT requiere padding o truncamiento).
- ¿Cómo se manean los gaps en los datos antes de aplicar FFT? (Los gaps introducen artefactos espectrales).
- ¿Qué pasa cuando un activo tiene múltiples ciclos con amplitudes similares? (El filtro puede ser ambiguo).
- ¿Cómo se comporta el filtro en regímenes de mercado cambiantes (tendencia fuerte vs. rango)? (Los ciclos pueden cambiar de frecuencia).

## Requirements

### Functional Requirements

- **FR-001**: El sistema MUST calcular la Transformada Rápida de Fourier (FFT) sobre series temporales de precios históricos.
- **FR-002**: El sistema MUST generar gráficos de espectro de potencias que muestren las frecuencias dominantes de un activo.
- **FR-003**: El sistema MUST permitir identificar y extraer los ciclos dominantes (períodos en días) desde el espectro.
- **FR-004**: El sistema MUST construir un filtro en el dominio de frecuencia que retenga solo las frecuencias seleccionadas y reconstruya la señal en el dominio del tiempo.
- **FR-005**: El sistema MUST generar señales de trading basadas en cruces entre el precio original y la señal filtrada por Fourier.
- **FR-006**: El sistema MUST ejecutar backtests de la estrategia Fourier-based y calcular métricas de rendimiento estándar (Sharpe, Sortino, Max Drawdown, Win Rate, Profit Factor).
- **FR-007**: El sistema MUST permitir comparar el rendimiento de la estrategia Fourier-based contra buy & hold del mismo activo.
- **FR-008**: El sistema MUST permitir comparar el análisis espectral de múltiples activos para selección de universo.
- **FR-009**: El sistema MUST incluir visualizaciones claras: precio vs. señal filtrada, espectro de potencias, y resultados del backtest.

### Key Entities

- **Serie de Precios**: Serie temporal diaria de precios (Open, High, Low, Close, Volume) de un activo financiero.
- **Espectro de Potencias**: Representación de la distribución de energía/varianza del precio en función de la frecuencia.
- **Ciclo Dominante**: Frecuencia con mayor amplitud en el espectro, expresada como período en días de trading.
- **Señal Filtrada**: Serie temporal reconstruida a partir de un subconjunto seleccionado de frecuencias del espectro.
- **Señal de Trading**: Señal binaria (compra/venta) generada por cruces entre precio y señal filtrada.
- **Métricas de Backtest**: Métricas de rendimiento estándar para evaluar la estrategia.

## Success Criteria

### Measurable Outcomes

- **SC-001**: El usuario puede calcular y visualizar el espectro de potencias de cualquier activo con datos históricos en menos de 5 minutos.
- **SC-002**: La estrategia Fourier-based genera al menos un Sharpe Ratio comparable (±0.2) con las mejores estrategias del curso en los activos de prueba.
- **SC-003**: El usuario puede comparar el análisis espectral de al menos 5 activos simultáneamente en un solo notebook.
- **SC-004**: El nuevo capítulo incluye notebooks autocontenidos que se ejecutan sin errores desde la celda de importación hasta los resultados del backtest.
- **SC-005**: Las visualizaciones del espectro y la señal filtrada son claras y comprensibles para un usuario con conocimientos básicos de procesamiento de señales.

## Assumptions

- Los datos históricos se obtienen del mismo proveedor que el resto del curso (yfinance vía OpenBB).
- Se asume que el usuario tiene conocimientos básicos de procesamiento de señales (qué es una frecuencia, qué es un filtro).
- La FFT se aplicará sobre precios de cierre diarios, con padding automático para longitudes no potencia de 2.
- Los gaps en los datos se interpolan antes de aplicar FFT para evitar artefactos espectrales.
- Se utilizarán las bibliotecas estándar de Python: numpy, scipy.signal, pandas, y matplotlib/plotly para visualización.
- El nuevo capítulo sigue la misma estructura que los capítulos existentes (capitulo-XX): README.md, spec.md, y directorio notebooks/.
- Las estrategias Fourier se enfocan en datos diarios, no intradiarios.

## Constitution Alignment

- **Spec-First Delivery**: Este documento define historias de usuario, requisitos funcionales, supuestos, casos límite y criterios medibles.
- **Independent Value Slices**: Cada historia de usuario es entregable independientemente — la comprensión espectral (P1) ya entrega valor educativo; la estrategia con filtros (P2) entrega valor de trading; la comparación multi-activo (P3) entrega valor de selección.
- **Verifiable Outcomes**: Cada historia incluye escenarios de aceptación y un método de prueba independiente.
- **Minimal, Explicit Change**: Se añade un nuevo capítulo siguiendo la convención existente `capitulo-08-fourier-transform`. No se modifican capítulos existentes. La infraestructura de datos y backtesting existente se reutiliza.
