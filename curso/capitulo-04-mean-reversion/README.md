# Capítulo 04: Reversión a la Media con Bandas de Bollinger

> **Nivel**: Intermedio  
> **Prerrequisitos**: Capítulo 03 (Momentum/RSI)  
> **Estrategia**: Mean Reversion con Bollinger Bands  
> **Objetivo**: Implementar una estrategia de reversión a la media, aprender sobre volatilidad dinámica, stop-loss dinámicos y regímenes de mercado.

---

## 1. Reversión a la Media

La hipótesis de reversión a la media establece que los precios tienden a volver
a su media histórica después de desviaciones significativas:

- **Precio muy por encima de la media**: Probable corrección a la baja.
- **Precio muy por debajo de la media**: Probable rebote al alza.

---

## 2. Bandas de Bollinger

John Bollinger creó este indicador en los años 80. Consiste en tres líneas:

$$\text{Banda Superior} = SMA(N) + K \cdot \sigma(N)$$
$$\text{Banda Media} = SMA(N)$$
$$\text{Banda Inferior} = SMA(N) - K \cdot \sigma(N)$$

Donde:
- $N$: Período (típicamente 20)
- $K$: Factor de desviación (típicamente 2)
- $\sigma$: Desviación estándar del precio

### Interpretación

- Precio toca **banda inferior**: Posible sobreventa → oportunidad de compra.
- Precio toca **banda superior**: Posible sobrecompra → oportunidad de venta.
- **Contracción** (bandas estrechas): Baja volatilidad → posible expansión inminente.
- **Expansión** (bandas anchas): Alta volatilidad → cautela.

---

## 3. Stop-Loss Dinámico

En lugar de un stop fijo (ej. -10%), usamos la volatilidad para ajustar:

$$\text{Stop Loss} = \text{Precio Entrada} - K_{stop} \cdot ATR(N)$$

**Ventaja**: En mercados volátiles, el stop es más amplio (evita salidas prematuras).
En mercados calmados, el stop es más ajustado (protege beneficios).

---

## 4. Regímenes de Mercado

Las estrategias de mean reversion funcionan mejor en mercados laterales (range-bound).
En tendencias fuertes, pueden generar señales falsas.

**Detección de régimen**:
- **Trending**: ADX > 25 o BB Width creciente sostenida.
- **Range-bound**: ADX < 20 o BB Width estable/decreciente.

---

## Siguiente paso

Revisa `spec.md` y luego implementa y evalúa la estrategia en los notebooks.

---

> ⚠️ **Disclaimer**: Este curso es exclusivamente educativo. No constituye asesoría financiera.
