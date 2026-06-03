# Historia práctica: Cómo usar indicadores en tu día a día (para informáticos)

Imagina que eres un programador al que le piden vigilar si conviene comprar o vender acciones. No tienes formación financiera; tienes lógica, automatización y curiosidad. Esta es una historia que te guía paso a paso, sin fórmulas, para que entiendas qué mirar y qué hacer.

1) Antes de encender el ordenador
- Mentalidad: piensa en reglas, no en corazonadas. Cada decisión sale de un conjunto de condiciones claras.
- Tiempo: destina 15–30 minutos al día para revisar señales y preparar cambios; reserva las horas de mayor volumen para ejecutar si decides hacerlo.

2) Preparar los datos (lo que necesitas)
- Precio: apertura, máximo, mínimo, cierre.
- Volumen: cuántas unidades se negociaron.
- Serie de tiempo limpia: sin saltos ni duplicados.
- Dónde buscarlo: los notebooks del curso y `curso/lib/indicators.py` contienen las funciones que necesitas. [curso/lib/indicators.py](curso/lib/indicators.py#L1)

3) Las herramientas (qué son los indicadores, en palabras simples)
- Medias (SMA/EMA): suavizan el ruido y muestran la dirección general. Piensa “promedio móvil” como el termómetro de tendencia.
- RSI (oscilador): te dice si algo está muy comprada o muy vendida — como si el mercado se hubiera cansado de subir o bajar.
- VWAP: precio medio ponderado por volumen — lo usan los grandes para saber si ejecutaron a buen precio.
- Bandas de Bollinger / ATR: te indican cuánta agitación tiene el precio; útil para stops y tamaño de posición.
- Donchian / Breakouts: detectan rupturas, momentos en que el precio “se escapa”.

4) Un día típico: checklist corto (lo que realmente harás)
- 1) Cargar datos recientes para tus activos de interés.
- 2) Ver el panorama general con una gráfica: precio + una media larga (ej. 200 periodos).
- 3) Mirar el filtro de tendencia: si el precio está por encima de la media larga, prioriza comprar; si está por debajo, prioriza vender o quedarse fuera.
- 4) Buscar señales de timing:
  - Cruce de medias (SMA rápida cruza SMA lenta): señal clara de entrada/salida.
  - RSI en extremo (muy bajo → posible compra; muy alto → posible venta).
  - Precio cerca del VWAP en una tendencia: buena zona para entrar a favor de la tendencia.
- 5) Revisa volatilidad (ATR/Bollinger): ajusta stop-loss y tamaño de posición.
- 6) Decide: si varias señales (tendencia + timing + volatilidad) apuntan en la misma dirección, se considera entrar; si están en conflicto, no operar.

5) Ejemplo narrativo corto
Te despiertas, cargas los datos y ves que el precio de XYZ está por encima de la media de 200 días: tendencia alcista. La SMA corta cruzó por encima de la SMA larga ayer (cruce alcista). Esta mañana, el RSI no está en sobrecompra y el precio ha hecho un pequeño pullback hacia el VWAP. La volatilidad es moderada.
Decisión: las señales (tendencia, cruce, pullback al VWAP) apuntan a comprar. Aplicas un stop conservador calculado por volatilidad y fijas un objetivo parcial para asegurar ganancias. Ejecutas la orden o la pones en la cola del agente automático.

6) Qué hacer cuando las señales no están de acuerdo
- Prioriza la tendencia (media larga) y el riesgo: si la tendencia es fuerte, un RSI extremo por sí solo no debería mandar vender.
- Si hay conflicto (ej. tendencia alcista pero cruce bajista), reduce tamaño de posición o espera confirmación (cierre de vela, volumen mayor).

7) Reglas prácticas para empezar (simplicidad primero)
- Usa una estrategia con 3 condiciones mínimas: filtro de tendencia + condición de timing + gestión de riesgo.
- Si encuentras una señal de entrada, anota por qué cumples cada condición. Esto evita operar por intuición.
- Automatiza la parte repetitiva: cálculos de indicadores y alertas; deja la decisión final para revisión humana al principio.

8) Gestión de riesgo (lo esencial)
- Nunca arriesgues más del 1–2% de tu capital total en una sola operación (ajusta según tu tolerancia).
- Define stop-loss y target antes de entrar; no improvises.
- Controla el tamaño de posición según volatilidad: si el activo es muy volátil, reduce tamaño.

9) Aprender haciendo: pequeñas prácticas diarias
- 1 semana: sigue 3 activos y registra señales y decisiones (sin poner dinero al principio).
- 1 mes: backtest rápido de la regla (aplica las mismas condiciones a datos históricos y mira resultados).
- Itera: ajusta parámetros con datos fuera de muestra; evita optimizar hasta que el sistema sea robusto.

10) Dónde mirar en este curso para profundizar
- Conceptos y notebooks por capítulo: [curso/](curso/)
- Implementaciones de indicadores: [curso/lib/indicators.py](curso/lib/indicators.py#L1)
- Backtesting y evaluación: revisa los notebooks de cada capítulo para ver ejemplos concretos.

11) Resumen para programadores — checklist corta
- Datos limpios → Indicadores calculados → Filtrado de tendencia → Señales de timing → Gestión de riesgo → Ejecutar/Simular.
- Regla: “Si dos de tres señales principales están alineadas, considerar entrada; si no, esperar.”

Si quieres, convierto este texto en un notebook interactivo con gráficos y ejemplos prácticos para 2 indicadores (SMA cross y VWAP) y algunos scripts de automatización. ¿Lo genero ahora?
