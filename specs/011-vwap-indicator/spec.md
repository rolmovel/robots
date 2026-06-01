# Feature Specification: VWAP — Volume Weighted Average Price como Indicador de Trading

**Feature Branch**: `[011-vwap-indicator]`

**Created**: 2026-06-01

**Status**: Draft

**Input**: User description: "ahora quiero crear un capitulo en torno al VWAP con explicaciones y notebooks asociados"

## User Scenarios & Testing

### User Story 1 - Comprender el concepto y cálculo del VWAP (Priority: P1)

El usuario desea entender qué es el VWAP (Volume Weighted Average Price), por qué es un indicador institucional clave, y cómo se calcula paso a paso. Quiere ver la evolución del VWAP intradiario y diario, comparándolo con el precio y con otras medias móviles como la SMA.

**Why this priority**: Es el fundamento sin el cual no se puede aplicar ninguna estrategia basada en VWAP. Sin comprender que el VWAP pondera el volumen — y por tanto refleja el precio promedio real donde se ejecutó el volumen — el usuario no puede entender su valor como referencia institucional.

**Independent Test**: Puede ser probado completamente descargando datos históricos con volumen, calculando el VWAP acumulado desde el inicio de sesión/día, y generando visualizaciones claras que muestren precio vs. VWAP. Entrega valor educativo inmediato.

**Acceptance Scenarios**:

1. **Given** datos históricos de precios y volumen de un activo, **When** se calcula el VWAP como la suma acumulada de (precio típico × volumen) dividida por la suma acumulada de volumen, **Then** se obtiene una línea de VWAP que se mueve en conjunto con el precio pero con menor volatilidad.
2. **Given** el VWAP calculado, **When** se grafica junto al precio de cierre, **Then** se observa que el precio tiende a revertir hacia el VWAP cuando se aleja significativamente.
3. **Given** el VWAP diario, **When** se compara con una SMA del mismo período, **Then** el VWAP muestra un comportamiento más suave y reactivo a las zonas de alto volumen.

---

### User Story 2 - Identificar zonas de soporte/resistencia dinámicas con VWAP (Priority: P2)

El usuario quiere usar el VWAP como referencia dinámica de soporte y resistencia. Cuando el precio está por encima del VWAP, este actúa como soporte; cuando está por debajo, como resistencia. Quiere identificar oportunidades de entrada cuando el precio rebota en el VWAP.

**Why this priority**: Es la aplicación más directa y común del VWAP en trading institucional. Transforma un indicador de cálculo técnico en una herramienta de decisión con reglas de entrada/salida claras.

**Independent Test**: Puede ser probado completamente definiendo reglas de entrada (compra cuando el precio toca el VWAP en tendencia alcista, venta cuando lo toca en tendencia bajista) y ejecutando un backtest con métricas de rendimiento.

**Acceptance Scenarios**:

1. **Given** un activo en tendencia alcista (precio > SMA 200), **When** el precio desciende y toca el VWAP, **Then** se genera una señal de compra si el volumen en ese punto confirma la reacción.
2. **Given** un activo en tendencia bajista (precio < SMA 200), **When** el precio asciende y toca el VWAP, **Then** se genera una señal de venta si el volumen confirma la reacción.
3. **Given** las señales generadas, **When** se ejecuta el backtest, **Then** se obtienen métricas de rendimiento (Sharpe, drawdown, win rate) que pueden compararse contra buy & hold.

---

### User Story 3 - Construir estrategias multi-temporalidad con VWAP (Priority: P3)

El usuario desea combinar el VWAP intradiario con el VWAP acumulado a nivel diario y semanal para identificar confluciones de soporte/resistencia en múltiples temporalidades. Quiere estrategias que operen cuando las líneas de VWAP en diferentes horizontes temporales convergen.

**Why this priority**: Aporta una capa adicional de sofisticación que diferencia al curso de tutoriales básicos de VWAP. Permite al usuario desarrollar estrategias más robustas con señales de mayor confianza cuando múltiples temporalidades coinciden.

**Independent Test**: Puede ser probado calculando VWAP intradiario, diario y semanal sobre los mismos datos, identificando zonas de convergencia, y ejecutando backtests que usen estas confluciones como filtros de entrada.

**Acceptance Scenarios**:

1. **Given** datos intradiarios, diarios y semanales de un activo, **When** se calcula el VWAP en cada temporalidad, **Then** se pueden identificar zonas donde los VWAPs convergen (se superponen dentro de un margen de X%).
2. **Given** una zona de convergencia de VWAPs, **When** el precio llega a esa zona con volumen decreciente y luego repunta con volumen creciente, **Then** se genera una señal de trading de mayor confianza que una señal basada en un solo VWAP.
3. **Given** las señales multi-temporalidad, **When** se ejecuta el backtest, **Then** el win rate y el Sharpe Ratio mejoran respecto a la estrategia de un solo VWAP.

---

### Edge Cases

- ¿Qué sucede cuando un activo no tiene datos de volumen disponibles? (El VWAP no se puede calcular; se debe usar un fallback como SMA o mostrar un aviso).
- ¿Cómo se comporta el VWAP en días con volumen extremadamente bajo (feriados, apertura tardía)? (El VWAP puede ser menos representativo).
- ¿Qué pasa cuando hay gaps de precio al abrir? (El VWAP acumulado no se "recorta" en el gap, lo que puede crear una divergencia temporal).
- ¿Cómo se calcula el VWAP en mercados con sesiones fragmentadas? (Se necesita volumen total agregado de todas las sesiones).

## Requirements

### Functional Requirements

- **FR-001**: El sistema MUST calcular el VWAP diario como la suma acumulada de (precio típico × volumen) dividida por la suma acumulada de volumen, donde precio típico = (Alta + Baja + Cierre) / 3.
- **FR-002**: El sistema MUST permitir calcular VWAP en ventanas móviles (ej. VWAP de los últimos N días) además del VWAP acumulado desde el inicio.
- **FR-003**: El sistema MUST generar visualizaciones comparativas: precio vs. VWAP vs. SMA para que el usuario observe las diferencias de comportamiento.
- **FR-004**: El sistema MUST identificar y marcar visualmente las zonas donde el precio cruza o toca el VWAP, indicando si fue un rebote (soporte/resistencia) o un ruptura.
- **FR-005**: El sistema MUST implementar una estrategia de trading basada en rebotes al VWAP con reglas de entrada (contacto del VWAP en dirección de tendencia), salida (objetivo de beneficio o stop-loss), y filtro de tendencia (SMA 200).
- **FR-006**: El sistema MUST ejecutar backtests de la estrategia VWAP-reversión y calcular métricas de rendimiento estándar (Sharpe, Sortino, Max Drawdown, Win Rate, Profit Factor, duración promedio de trades).
- **FR-007**: El sistema MUST permitir comparar el rendimiento de la estrategia VWAP contra buy & hold y contra otras estrategias del curso (ej. SMA cross, RSI momentum).
- **FR-008**: El sistema MUST incluir visualizaciones claras: precio + VWAP + señales de trading, mapa de calor de contactos con VWAP, y resultados del backtest.
- **FR-009**: El sistema MUST documentar las limitaciones del VWAP (no disponible para activos sin volumen, sesgo en días con baja liquidez).

### Key Entities

- **Precio Típico (Typical Price)**: (Alta + Baja + Cierre) / 3. Representa el promedio del rango del período.
- **VWAP Acumulado**: Suma acumulada de (precio típico × volumen) / suma acumulada de volumen desde el inicio de la ventana.
- **VWAP Móvil**: VWAP calculado sobre una ventana deslizante de N períodos (ej. últimos 20 días).
- **Zona de Convergencia**: Rango de precios donde se superponen dos o más líneas de VWAP de diferentes temporalidades.
- **Señal de Rebote**: Señal de trading generada cuando el precio toca el VWAP y reacciona en la dirección de la tendencia.
- **Métricas de Backtest**: Métricas de rendimiento estándar para evaluar la estrategia.

## Assumptions

- Los datos descargados incluyen columnas de Volumen (O, H, L, C, V). Si un ticker no tiene volumen, se usará un fallback a SMA.
- El VWAP se calculará en base diario (no intradiario minuto a minuto) ya que los datos de `curso.lib.data` proporcionan velas diarias.
- La tendencia se filtrará usando SMA 200, consistente con los capítulos anteriores del curso.
- Se usarán los mismos activos de prueba que en capítulos anteriores (ej. AAPL, MSFT, SPY) para permitir comparaciones directas.

## Success Criteria

### Measurable Outcomes

- **SC-001**: El usuario puede calcular y visualizar el VWAP diario de cualquier activo con volumen en menos de 3 minutos.
- **SC-002**: La estrategia VWAP-reversión genera al menos un Sharpe Ratio comparable (±0.2) con las mejores estrategias del curso en los activos de prueba.
- **SC-003**: El usuario puede identificar al menos 5 zonas de contacto/rebote al VWAP en un gráfico de 1 año de datos.
- **SC-004**: El nuevo capítulo incluye notebooks autocontenidos que se ejecutan sin errores desde la celda de importación hasta los resultados del backtest.
- **SC-005**: Las visualizaciones de precio vs. VWAP son claras y comprensibles para un usuario sin conocimientos avanzados de análisis técnico.
