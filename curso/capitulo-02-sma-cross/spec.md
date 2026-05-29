# Estrategia: Cruce de Medias Móviles (SMA Cross)

## Objetivo

Capturar tendencias mediante señales de cruce entre dos medias móviles simples
de diferente período, operando long en cruces alcistas y cerrando en cruces bajistas.

## Hipótesis de Mercado

Cuando la media móvil de corto plazo cruza por encima de la de largo plazo,
indica el inicio de una tendencia alcista. El cruce inverso señala el fin de
la tendencia o el inicio de una bajista.

## Reglas Operativas

- **Universo**: Índices/ETFs de alta liquidez (SPY, QQQ) o acciones large-cap.
- **Indicadores**: SMA(n1) rápida, SMA(n2) lenta (n1 < n2).
- **Entrada (Long)**: SMA(n1) cruza por encima de SMA(n2).
- **Salida**: SMA(n1) cruza por debajo de SMA(n2).
- **Short (opcional)**: Abrir posición corta en death cross.

## Gestión de Riesgo

- Posición máxima: 100% del capital.
- Drawdown tolerable: 20%.
- Sin stop-loss fijo (la señal de cruce inverso actúa como salida).

## Parámetros Optimizables

| Parámetro | Rango | Default | Descripción |
|-----------|-------|---------|-------------|
| n1 | 5-50 | 10 | Período SMA rápida |
| n2 | 10-100 | 20 | Período SMA lenta |

## Supuestos

- El activo presenta tendencias claras y sostenidas.
- Las comisiones son ~0.2% por operación.
- No hay restricciones de short-selling.

## Métricas de Evaluación

- Retorno total (%) y CAGR
- Sharpe Ratio (target > 0.7)
- Max Drawdown (target < 20%)
- Número de operaciones (menos = menor coste por comisiones)
- Heatmap de optimización (n1 vs n2)
- Comparación train vs test (detección de overfitting)
