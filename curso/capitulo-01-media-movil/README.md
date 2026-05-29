# Capítulo 01: Media Móvil Simple con Filtro Sectorial

> **Nivel**: Principiante  
> **Prerrequisitos**: Capítulo 00 (Fundamentos)  
> **Estrategia**: Trend-following con SMA y filtro de sector salud  
> **Objetivo**: Implementar y evaluar tu primera estrategia automatizada completa.

---

## 1. ¿Qué es una Media Móvil?

Una **media móvil** (Moving Average) es el promedio de los últimos N precios de
cierre de un activo. Suaviza el ruido del precio diario y revela la tendencia
subyacente.

### Media Móvil Simple (SMA)

$$SMA(N) = \frac{1}{N} \sum_{i=0}^{N-1} P_{t-i}$$

Donde $P_t$ es el precio de cierre en el día $t$ y $N$ es el período.

### Interpretación

- **Precio > SMA**: Tendencia alcista (el activo cotiza por encima de su promedio).
- **Precio < SMA**: Tendencia bajista (el activo cotiza por debajo de su promedio).

### Tipos de Media Móvil

| Tipo | Ventaja | Desventaja |
|------|---------|------------|
| SMA (Simple) | Fácil de entender y calcular | Reacciona lento a cambios |
| EMA (Exponencial) | Reacciona más rápido | Más sensible a ruido |

En este capítulo usamos **SMA** por su simplicidad.

---

## 2. La Estrategia: Filtro Sectorial + SMA

### Hipótesis de Mercado

> Las empresas del sector salud que cotizan por debajo de su media móvil
> de 30 días durante un período prolongado (1 mes) están experimentando
> una corrección temporal, y tienden a recuperarse hacia su media.

### Lógica de la Estrategia

1. **Universo**: Empresas del sector salud (JNJ, PFE, UNH, ABBV, MRK).
2. **Señal de entrada**: El precio de cierre está por debajo de la SMA(30) durante al menos 30 días consecutivos.
3. **Señal de salida**: El precio cruza por encima de la SMA(30).
4. **Gestión de riesgo**: Stop-loss al 10% por debajo del precio de entrada.

### ¿Por qué esta estrategia como primera?

- Usa un solo indicador (SMA) → fácil de entender.
- Tiene reglas claras y binarias → fácil de automatizar.
- El sector salud es relativamente estable → buenos datos históricos.
- Introduce el concepto de "filtro" → base para estrategias más complejas.

---

## 3. Conceptos de Backtesting

### ¿Cómo evaluamos la estrategia?

Aplicamos las reglas de la estrategia a datos históricos y medimos:

- **Rendimiento total**: ¿Cuánto habríamos ganado/perdido?
- **Sharpe Ratio**: ¿El rendimiento justifica el riesgo?
- **Max Drawdown**: ¿Cuánto habríamos perdido en el peor momento?
- **Win Rate**: ¿Qué porcentaje de operaciones fueron rentables?
- **Comparación vs Buy & Hold**: ¿Es mejor que simplemente mantener?

### Herramienta: backtesting.py

Usamos la librería `backtesting.py` que permite definir estrategias como
clases Python y ejecutarlas sobre datos OHLCV.

```python
from backtesting import Backtest, Strategy

class MiEstrategia(Strategy):
    def init(self):
        # Inicializar indicadores
        pass
    
    def next(self):
        # Lógica de trading en cada vela
        pass
```

---

## 4. Flujo de trabajo

1. ✅ Leer esta teoría
2. → Crear la especificación formal (`spec.md`)
3. → Implementar en notebook (`01_estrategia.ipynb`)
4. → Evaluar con backtesting (`01_backtesting.ipynb`)
5. → Documentar conclusiones

---

## Siguiente paso

Revisa el archivo `spec.md` de este capítulo para ver la especificación
formal de la estrategia, y luego abre los notebooks para implementarla.

---

> ⚠️ **Disclaimer**: Este curso es exclusivamente educativo. No constituye
> asesoría financiera. Las estrategias presentadas son para aprendizaje y
> no deben utilizarse como recomendación de inversión.
