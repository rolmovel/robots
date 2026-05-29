# Capítulo 05: Breakout con Canales de Donchian

> **Nivel**: Intermedio-Avanzado  
> **Prerrequisitos**: Capítulo 04 (Mean Reversion/Bollinger)  
> **Estrategia**: Breakout con Donchian Channels + Trailing Stop  
> **Objetivo**: Implementar una estrategia de ruptura de canales, aprender sobre volatilidad, ATR para sizing y trailing stops.

---

## 1. Breakout: Filosofía de Trading

El breakout (ruptura) se basa en la premisa opuesta a la reversión a la media:

- Los precios que rompen niveles de resistencia/soporte tienden a **continuar** moviéndose.
- Los períodos de baja volatilidad (compresión) preceden a movimientos explosivos.

### Turtle Trading

Los famosos "Turtle Traders" de Richard Dennis usaban un sistema de breakout
basado en canales de Donchian:

- **Comprar** cuando el precio supera el máximo de N días.
- **Vender** cuando el precio cae por debajo del mínimo de M días.

---

## 2. Canales de Donchian

$$\text{Canal Superior} = \max(\text{High}, N)$$
$$\text{Canal Inferior} = \min(\text{Low}, N)$$
$$\text{Canal Medio} = \frac{\text{Superior} + \text{Inferior}}{2}$$

A diferencia de Bollinger (que usa desviación estándar), Donchian usa
máximos/mínimos absolutos, haciéndolo más robusto ante outliers.

---

## 3. Trailing Stop con ATR

El trailing stop sigue al precio a una distancia fija (en unidades de ATR):

$$\text{Trailing Stop} = \text{Max Precio desde entrada} - K \cdot ATR(N)$$

**Ventaja**: Deja correr las ganancias mientras protege contra reversiones.

---

## 4. Position Sizing basado en Volatilidad

Método de asignación de capital basado en ATR (sistema Turtle):

$$\text{Tamaño Posición} = \frac{\text{Riesgo por Trade}}{\text{ATR} \times \text{Multiplicador}}$$

Esto normaliza el riesgo: activos más volátiles → posiciones más pequeñas.

---

## Siguiente paso

Revisa `spec.md` y luego implementa y evalúa la estrategia en los notebooks.

---

> ⚠️ **Disclaimer**: Este curso es exclusivamente educativo. No constituye asesoría financiera.
