# Capítulo 02: Cruce de Medias Móviles (SMA Cross)

> **Nivel**: Principiante-Intermedio  
> **Prerrequisitos**: Capítulo 01 (Media Móvil Simple)  
> **Estrategia**: Trend-following con cruce de dos SMAs  
> **Objetivo**: Implementar la estrategia SMA Cross, aprender optimización de parámetros y entender el riesgo de sobreajuste.

---

## 1. Cruce de Medias Móviles

El cruce de medias móviles es una de las estrategias más populares de trend-following.
Utiliza dos medias móviles de diferente período:

- **SMA rápida** (período corto, ej. 10): Sensible a cambios recientes.
- **SMA lenta** (período largo, ej. 20): Representa la tendencia general.

### Señales

- **Golden Cross** (cruce alcista): SMA rápida cruza POR ENCIMA de SMA lenta → Comprar.
- **Death Cross** (cruce bajista): SMA rápida cruza POR DEBAJO de SMA lenta → Vender.

---

## 2. Optimización de Parámetros

### ¿Qué es?

Encontrar la combinación de parámetros (n1, n2) que maximiza una métrica
(ej. Sharpe Ratio) sobre datos históricos.

### El Problema del Overfitting

> **PELIGRO**: Una estrategia que funciona perfectamente en datos históricos
> puede fallar completamente en datos futuros.

El sobreajuste ocurre cuando optimizamos demasiado para datos específicos:

- La estrategia "memoriza" patrones pasados en vez de capturar tendencias reales.
- Solución: Walk-forward testing, datos out-of-sample, validación cruzada temporal.

### Mitigación

1. **Dividir datos**: Train (70%) + Test (30%) temporal.
2. **Limitar parámetros**: Menos parámetros = menos overfitting.
3. **Robustez**: La estrategia debe funcionar en un RANGO de parámetros, no solo en uno.

---

## 3. Herramienta: Optimizador SAMBO

backtesting.py incluye un optimizador basado en SAMBO (Sequential Model-based
Algorithm Configuration) que permite barrer parámetros eficientemente:

```python
stats = bt.optimize(
    n1=range(5, 50, 5),
    n2=range(10, 100, 5),
    maximize='Sharpe Ratio'
)
```

---

## Siguiente paso

Revisa `spec.md` y luego implementa y evalúa la estrategia en los notebooks.

---

> ⚠️ **Disclaimer**: Este curso es exclusivamente educativo. No constituye asesoría financiera.
