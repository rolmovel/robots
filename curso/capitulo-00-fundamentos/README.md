# Capítulo 00: Fundamentos de Inversión en Bolsa

> **Nivel**: Principiante  
> **Prerrequisitos**: Ninguno  
> **Objetivo**: Comprender los conceptos base de inversión en bolsa y familiarizarse con OpenBB como fuente de datos abiertos.

---

## 1. ¿Qué es la inversión en bolsa?

La inversión en bolsa consiste en comprar y vender instrumentos financieros
(acciones, ETFs, bonos, derivados) en mercados organizados con el objetivo
de obtener un rendimiento sobre el capital invertido.

### Tipos de mercados

- **Mercado primario**: Donde las empresas emiten nuevos valores (IPOs).
- **Mercado secundario**: Donde los inversores compran y venden valores ya emitidos.

### Tipos de activos

| Activo | Descripción | Riesgo típico |
|--------|-------------|---------------|
| Acciones | Participación en una empresa | Medio-Alto |
| ETFs | Fondos cotizados que replican índices | Medio |
| Bonos | Deuda emitida por gobiernos/empresas | Bajo-Medio |
| Derivados | Contratos basados en otros activos | Alto |

---

## 2. Conceptos fundamentales

### Riesgo y Rendimiento

- **Rendimiento**: Ganancia o pérdida obtenida sobre una inversión, expresada como porcentaje.
- **Riesgo**: Probabilidad de que el rendimiento real difiera del esperado.
- **Relación riesgo-rendimiento**: A mayor rendimiento esperado, mayor riesgo asumido.

### Horizonte temporal

| Horizonte | Plazo | Ejemplo de estrategia |
|-----------|-------|-----------------------|
| Intradía | Minutos a horas | Scalping, day trading |
| Corto plazo | Días a semanas | Swing trading |
| Medio plazo | Semanas a meses | Trend following |
| Largo plazo | Años | Buy & hold, value investing |

### Diversificación

No concentrar todo el capital en un solo activo o sector. La diversificación
reduce el riesgo específico (no sistemático) manteniendo un rendimiento esperado
razonable.

---

## 3. Métricas clave que usaremos en el curso

| Métrica | Qué mide | Fórmula simplificada |
|---------|----------|---------------------|
| Retorno total | Ganancia acumulada | (Valor final - Valor inicial) / Valor inicial |
| CAGR | Retorno anualizado compuesto | (Vf/Vi)^(1/años) - 1 |
| Sharpe Ratio | Rendimiento ajustado a riesgo | (Retorno - Tasa libre) / Volatilidad |
| Max Drawdown | Mayor caída desde un máximo | (Valle - Pico) / Pico |
| Win Rate | % de operaciones ganadoras | Ganadoras / Total operaciones |

---

## 4. Datos abiertos y OpenBB

### ¿Por qué datos abiertos?

Para diseñar y evaluar estrategias necesitamos datos históricos de precios.
OpenBB proporciona acceso unificado a múltiples fuentes de datos gratuitas
y de pago desde una única API Python.

### ¿Qué es OpenBB?

OpenBB es una plataforma open-source que actúa como capa de integración
de datos financieros. Con una sola línea de código puedes descargar datos
históricos de miles de activos.

```python
from openbb import obb

# Descargar 5 años de datos de Apple
data = obb.equity.price.historical("AAPL", provider="yfinance")
df = data.to_dataframe()
```

### Datos disponibles (gratuitos con yfinance)

- Precios históricos OHLCV (Open, High, Low, Close, Volume)
- Múltiples mercados: US, Europa, Asia
- Intervalos: diario, semanal, mensual
- ETFs y fondos indexados

---

## 5. ¿Qué es una estrategia de inversión?

Una estrategia de inversión es un conjunto de **reglas sistemáticas** que definen:

1. **Cuándo comprar** (señal de entrada)
2. **Cuándo vender** (señal de salida)
3. **Cuánto arriesgar** (gestión de riesgo)
4. **En qué invertir** (universo de activos)

Una estrategia bien definida elimina las decisiones emocionales y permite
ser **automatizada** y **evaluada** objetivamente mediante backtesting.

---

## 6. ¿Qué es el backtesting?

El backtesting consiste en aplicar una estrategia a datos históricos para
evaluar cómo habría funcionado en el pasado.

### Ventajas

- Evaluación objetiva basada en datos
- Identificación de debilidades antes de arriesgar capital real
- Comparación entre múltiples estrategias

### Limitaciones (IMPORTANTE)

- **El pasado no predice el futuro**: Rendimientos históricos no garantizan rendimientos futuros.
- **Sobreajuste (overfitting)**: Optimizar excesivamente para datos pasados puede crear estrategias que no funcionan en el futuro.
- **Costes no modelados**: Slippage, impacto de mercado, comisiones variables.
- **Survivorship bias**: Datos que solo incluyen empresas que sobrevivieron.

---

## 7. Flujo del curso

Cada capítulo a partir del 01 seguirá este flujo:

```
1. Teoría y fundamentos de la estrategia (README.md)
2. Especificación formal de la estrategia (spec.md)
3. Implementación automatizada (notebook de estrategia)
4. Evaluación con backtesting (notebook de backtesting)
5. Conclusiones y decisión (aprobar / iterar / descartar)
```

---

## Siguiente paso

Abre el notebook `notebooks/00_intro_openbb.ipynb` para practicar la descarga
y exploración de datos con OpenBB.

---

> ⚠️ **Disclaimer**: Este curso es exclusivamente educativo. No constituye
> asesoría financiera. Las estrategias presentadas son para aprendizaje y
> no deben utilizarse como recomendación de inversión.
