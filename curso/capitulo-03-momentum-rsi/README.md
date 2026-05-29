# Capítulo 03: Momentum y RSI

> **Nivel**: Intermedio  
> **Prerrequisitos**: Capítulo 02 (SMA Cross)  
> **Estrategia**: Momentum con oscilador RSI  
> **Objetivo**: Implementar una estrategia de momentum usando RSI, aprender sobre osciladores y combinación de indicadores.

---

## 1. Momentum en los Mercados

El momentum es la tendencia de un activo a continuar moviéndose en la misma dirección:

- **Momentum positivo**: Los activos que suben tienden a seguir subiendo.
- **Momentum negativo**: Los activos que bajan tienden a seguir bajando.

Este efecto está documentado académicamente y es la base de muchas estrategias cuantitativas.

---

## 2. El Índice de Fuerza Relativa (RSI)

El RSI (Relative Strength Index) es un oscilador que mide la velocidad y magnitud
de los cambios de precio:

$$RSI = 100 - \frac{100}{1 + RS}$$

Donde $RS = \frac{\text{Ganancia media}}{\text{Pérdida media}}$ sobre N períodos.

### Zonas

| Zona | RSI | Interpretación |
|------|-----|---------------|
| Sobrecompra | > 70 | Posible agotamiento alcista |
| Neutral | 30-70 | Sin señal clara |
| Sobreventa | < 30 | Posible agotamiento bajista |

---

## 3. Estrategia: RSI Mean-Reversion

La interpretación contrarian del RSI:

- **Comprar** cuando RSI < 30 (sobreventa → esperar rebote).
- **Vender** cuando RSI > 70 (sobrecompra → esperar corrección).

### Variación: RSI con Trend Filter

Combinar RSI con un filtro de tendencia (SMA 200) mejora resultados:

- Solo comprar en sobreventa SI el precio está por encima de SMA(200) (tendencia alcista).
- Solo vender en sobrecompra SI el precio está por debajo de SMA(200) (tendencia bajista).

---

## 4. Combinación de Indicadores

Regla fundamental: nunca tomar decisiones basadas en un solo indicador.

- Los indicadores de **tendencia** (SMA, EMA) confirman la dirección general.
- Los indicadores de **momentum** (RSI, MACD) señalan timing de entrada.
- Los indicadores de **volatilidad** (ATR, Bollinger) ajustan el tamaño de posición.

---

## Siguiente paso

Revisa `spec.md` y luego implementa y evalúa la estrategia en los notebooks.

---

> ⚠️ **Disclaimer**: Este curso es exclusivamente educativo. No constituye asesoría financiera.
