# Capítulo 06: Estrategia Multi-Factor

> **Nivel**: Avanzado  
> **Prerrequisitos**: Capítulos 01-05  
> **Estrategia**: Multi-Factor con Score Compuesto  
> **Objetivo**: Combinar múltiples indicadores en un sistema de scoring, implementar ranking de activos y construcción de portfolio.

---

## 1. ¿Qué es Multi-Factor?

Las estrategias multi-factor combinan múltiples señales (factores) en una
puntuación compuesta para cada activo:

- **Factor Momentum**: RSI, rate of change, SMA cross.
- **Factor Valor**: P/E bajo, P/B bajo.
- **Factor Volatilidad**: ATR bajo, beta baja.
- **Factor Tendencia**: Precio > SMA(200), ADX alto.

### Ventaja

Diversificación de señales: cuando un indicador falla, otros pueden compensar.

---

## 2. Sistema de Scoring

Cada factor genera un score normalizado [0, 100]:

$$\text{Score Total} = w_1 \cdot S_{momentum} + w_2 \cdot S_{trend} + w_3 \cdot S_{volatility}$$

Donde $\sum w_i = 1$ (los pesos suman 1).

### Normalización

Para comparar factores en la misma escala:

$$S_{norm} = \frac{S - S_{min}}{S_{max} - S_{min}} \times 100$$

---

## 3. Ranking y Selección

Con N activos y sus scores:

1. **Calcular** score compuesto para cada activo.
2. **Rankear** de mayor a menor score.
3. **Seleccionar** los Top-K activos (ej. top 5).
4. **Asignar** capital equitativamente o proporcional al score.

---

## 4. Rebalanceo

Cada período de rebalanceo (ej. mensual):

1. Recalcular scores.
2. Determinar nuevo Top-K.
3. Vender posiciones que ya no están en Top-K.
4. Comprar nuevas posiciones del Top-K.

### Costes de Rebalanceo

- Comisiones de compra/venta.
- Impacto de mercado (slippage).
- Impuestos sobre plusvalías realizadas.

---

## 5. Construcción de Portfolio

Métodos de asignación de pesos:

| Método | Descripción |
|--------|-------------|
| Equal Weight | 1/K para cada posición |
| Score Weight | Proporcional al score |
| Risk Parity | Inversamente proporcional a la volatilidad |
| Min Variance | Optimización de varianza mínima |

Para este curso usamos **Equal Weight** por simplicidad y robustez.

---

## Siguiente paso

Revisa `spec.md` y luego implementa y evalúa la estrategia en los notebooks.

---

> ⚠️ **Disclaimer**: Este curso es exclusivamente educativo. No constituye asesoría financiera.
