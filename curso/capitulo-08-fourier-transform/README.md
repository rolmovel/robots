# Capítulo 08: Transformadas de Fourier como Indicadores de Trading

> **Nivel**: Intermedio-Avanzado  
> **Prerrequisitos**: Capítulos 00-02 (Fundamentos, Media Móvil, SMA Cross)  
> **Estrategia**: Análisis espectral + Filtrado de Fourier + Crossover  
> **Objetivo**: Descomponer precios en ciclos dominantes y construir señales de trading basadas en componentes frecuenciales.

---

## 1. ¿Qué es una Transformada de Fourier?

La **Transformada de Fourier** es una herramienta matemática que descompone una señal temporal en sus componentes de frecuencia. En lugar de ver el precio como una serie de valores a lo largo del tiempo, la FFT nos muestra qué frecuencias (ciclos) están presentes y con qué intensidad.

### La Transformada Discreta de Fourier (DFT)

$$X_k = \sum_{n=0}^{N-1} x_n \cdot e^{-i 2\pi k n / N}$$

Donde $x_n$ son los precios y $X_k$ son los coeficientes de Fourier en el dominio de frecuencia.

### Transformada Rápida de Fourier (FFT)

La FFT es un algoritmo eficiente para calcular la DFT:

$$O(N \log N) \quad \text{vs.} \quad O(N^2) \text{ para la DFT directa}$$

Esto hace posible analizar series de miles de puntos en milisegundos.

---

## 2. El Espectro de Potencias

El **espectro de potencias** muestra la contribución de cada frecuencia a la varianza total de la serie:

$$P(f_k) = \frac{|X_k|^2}{N}$$

Los picos en el espectro corresponden a **ciclos dominantes** — oscilaciones que se repiten con mayor regularidad y amplitud.

### Interpretación en Trading

| Período Detectado | Interpretación | Oportunidad Potencial |
|-------------------|----------------|----------------------|
| 5-15 días | Ciclo a corto plazo (ruido estructurado) | Swing trading rápido |
| 20-60 días | Ciclo mensual/trimestral | Posicionamiento medio plazo |
| 60-120 días | Ciclo semestral | Tendencia cíclica principal |

---

## 3. Filtrado en el Dominio de Frecuencia

La idea clave: **seleccionar solo las frecuencias que nos interesan** y descartar el resto.

### Proceso de Filtrado

1. **FFT**: Transformar precios al dominio de frecuencia
2. **Selección**: Identificar y conservar los picos dominantes
3. **Máscara**: Cero fuera de las bandas de frecuencia seleccionadas
4. **IFFT**: Transformada inversa para obtener la señal filtrada

$$x_{\text{filtered}}(t) = \mathcal{F}^{-1}\{X_k \cdot M_k\}$$

Donde $M_k$ es la máscara que selecciona las frecuencias deseadas.

---

## 4. La Estrategia: Crossover de Señal Filtrada

### Hipótesis de Mercado

> Los precios contienen una mezcla de señal cíclica (señal) y ruido aleatorio.  
> Al filtrar las frecuencias dominantes, obtenemos una señal suavizada que  
> revela el ciclo subyacente. Los cruces entre precio y señal filtrada  
> generan señales de entrada/salida con menor ruido que las medias móviles.

### Lógica de la Estrategia

1. **Universo**: Acciones líquidas (AAPL, MSFT, GOOGL, AMZN, META)
2. **FFT**: Descomponer el precio de cierre en componentes frecuenciales
3. **Filtrado**: Retener solo los 2-3 ciclos dominantes más fuertes
4. **Señal**: Comprar cuando el precio cruza por encima de la señal filtrada
5. **Salida**: Vender cuando el precio cruza por debajo de la señal filtrada
6. **Stop-loss**: -8% desde precio de entrada
7. **Timeout**: Cerrar posición si no se alcanza salida en 30 días

### Ventajas vs. Medias Móviles

| Característica | SMA | Fourier Filter |
|----------------|-----|----------------|
| Peso de observaciones | Uniforme | Basado en amplitud |
| Retardo (lag) | Proporcional a N | Depende del ciclo |
| Ajuste a cambios | Lento | Adaptable (recalcular) |
| Complejidad | O(1) por punto | O(N log N) total |

---

## 5. Limitaciones y Consideraciones

- **No estacionariedad**: Los ciclos financieros cambian con el tiempo → recalcular periódicamente
- **Fuga espectral**: Los bordes de la serie pueden introducir artefactos → usar ventanas (windowing)
- **Padding**: FFT requiere longitud potencia de 2 → rellenar con ceros
- **Interpolación**: Los gaps en datos financieros deben interpolarse antes de FFT

---

## 6. Arquitectura del Capítulo

```
01_fft_analysis.ipynb
├── Descarga de datos
├── FFT y espectro de potencias
├── Identificación de ciclos dominantes
└── Reconstrucción de señal filtrada

02_fourier_strategy.ipynb
├── Reutilización de componentes FFT (US1)
├── Construcción del filtro de Fourier
├── Generación de señales de crossover
├── Backtesting con backtesting.py
├── Métricas de rendimiento vs. Buy & Hold
└── Comparación multi-activo (US3)
```
