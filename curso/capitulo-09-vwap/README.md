# Capítulo 09: VWAP — Volume Weighted Average Price como Indicador de Trading

> **Nivel**: Intermedio  
> **Prerrequisitos**: Capítulos 00-03 (Fundamentos, Media Móvil, SMA Cross, RSI Momentum)  
> **Estrategia**: Reversión a la media con VWAP como referencia institucional  
> **Objetivo**: Usar el VWAP como zona dinámica de soporte/resistencia para generar señales de trading.

---

## 1. ¿Qué es el VWAP?

El **VWAP (Volume Weighted Average Price)** es el precio promedio ponderado por volumen de un activo durante un período determinado. Es el indicador más utilizado por traders institucionales para evaluar si ejecutaron órdenes por encima o por debajo del "precio justo" del mercado.

### La Fórmula del VWAP

$$VWAP = \frac{\sum (\text{Precio Típico} \times \text{Volumen})}{\sum \text{Volumen}}$$

Donde el **Precio Típico** (Typical Price) es:

$$\text{Precio Típico} = \frac{\text{Alta} + \text{Baja} + \text{Cierre}}{3}$$

### ¿Por qué es importante?

A diferencia de una media móvil simple (SMA) que trata cada período por igual, el VWAP **pondera cada período por su volumen**. Esto significa que:

- Los períodos con alto volumen tienen mayor influencia en el VWAP
- Los períodos con bajo volumen tienen menor influencia
- El VWAP refleja el **precio promedio real** donde se ejecutó el volumen

### VWAP Acumulado vs. VWAP Móvil

| Tipo | Descripción | Uso |
|------|-------------|-----|
| **VWAP Acumulado** | Suma desde el inicio del período de análisis | Referencia institucional estándar |
| **VWAP Móvil** | Calculado sobre una ventana deslizante (ej. 20 días) | Análisis de corto plazo |

---

## 2. VWAP como Soporte/Resistencia Dinámico

### Hipótesis de Mercado

> El VWAP actúa como un **imán** para el precio. Cuando el precio se aleja significativamente del VWAP, tiende a revertir hacia él. Los traders institucionales usan el VWAP como referencia para ejecutar órdenes grandes: compran cuando el precio está por debajo (precio "barato") y venden cuando está por encima (precio "caro").

### Comportamiento en Diferentes Regímenes

| Régimen de Mercado | Precio vs. VWAP | Comportamiento Esperado |
|--------------------|-----------------|------------------------|
| **Tendencia alcista** | Precio > VWAP | VWAP actúa como soporte |
| **Tendencia bajista** | Precio < VWAP | VWAP actúa como resistencia |
| **Mercado lateral** | Precio cerca de VWAP | Reversiones frecuentes al VWAP |

### Diferencia con la SMA

| Característica | VWAP | SMA |
|----------------|------|-----|
| **Ponderación** | Por volumen | Igual para todos los períodos |
| **Sensibilidad** | Reacciona a zonas de alto volumen | Reacciona igual a todos los períodos |
| **Uso institucional** | Referencia estándar para ejecución | Menos usado para ejecución |
| **Suavidad** | Más suave en días de alto volumen | Suavidad constante |

---

## 3. La Estrategia: Reversión al VWAP

### Hipótesis de Mercado

> Los activos en tendencia (filtrada por SMA 200) que se acercan al VWAP tienden a rebotar en la dirección de la tendencia. El VWAP actúa como un "precio justo" al que los traders institucionales están dispuestos a operar.

### Lógica de la Estrategia

1. **Universo**: Acciones líquidas (AAPL, MSFT, SPY)
2. **Filtro de tendencia**: 
   - Alcista: Precio > SMA(200) → buscar compras en VWAP
   - Bajista: Precio < SMA(200) → buscar ventas en VWAP
3. **Señal de entrada**: El precio se acerca al VWAP (dentro de 0.5% de tolerancia)
4. **Salida**: 
   - Take-profit: +2% desde entrada
   - Stop-loss: -2% desde entrada
   - Timeout: cerrar a los 10 días si no se alcanzó salida

### Parámetros de la Estrategia

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| VWAP_TOLERANCE_PCT | 0.5% | Tolerancia para considerar "contacto" con VWAP |
| TAKE_PROFIT_PCT | 2% | Objetivo de beneficio |
| STOP_LOSS_PCT | 2% | Límite de pérdida |
| TIMEOUT_DAYS | 10 | Días máximos sin salida |
| SMA_TREND | 200 | Período SMA para filtro de tendencia |

---

## 4. VWAP Multi-Temporal (P3)

### Concepto de Confluencia

Cuando el VWAP calculado en diferentes temporalidades (diario, semanal, mensual) convergen en un rango de precios cercano, se crea una **zona de confluencia** más fuerte que cualquier VWAP individual.

### VWAP por Temporalidad

| Temporalidad | Ventana | Sensibilidad | Uso |
|--------------|---------|-------------|-----|
| **Diario** | Todo el dataset | Alta | Señales rápidas |
| **Semanal** | Resampleado a semanal | Media | Tendencias intermedias |
| **Mensual** | Resampleado a mensual | Baja | Soportes/resistencias fuertes |

### Detección de Confluencia

Una zona de confluencia se detecta cuando **2 o más VWAPs** están dentro del **1%** entre sí:

$$\text{Confluencia} = \frac{|VWAP_1 - VWAP_2|}{VWAP_1} < 1\%$$

Las señales basadas en confluencia tienen mayor confianza que las basadas en un solo VWAP.

---

## 5. Limitaciones del VWAP

| Limitación | Descripción | Mitigación |
|------------|-------------|------------|
| **Requiere volumen** | No se puede calcular sin datos de volumen | Fallback a SMA con advertencia |
| **Mercados sin liquidez** | VWAP poco representativo en días de bajo volumen | Filtrar por volumen mínimo |
| **Gaps de precio** | Los gaps no se reflejan en el VWAP acumulado | Interpretar divergencias temporales |
| **Tendencias fuertes** | El VWAP pierde efectividad en tendencias sostenidas | Usar filtro de tendencia (SMA 200) |
| **Cambio de régimen** | El VWAP acumulado "envejece" con el tiempo | Complementar con VWAP móvil |
