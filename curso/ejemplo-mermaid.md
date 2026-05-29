# Ejemplo de Diagramas Mermaid

Este archivo demuestra la capacidad de renderizado de diagramas Mermaid en JupyterLab
con la extensión `jupyterlab-myst`.

## Diagrama de Flujo: Estrategia de Trading

```mermaid
flowchart TD
    A[Obtener datos OHLCV] --> B[Calcular indicadores]
    B --> C{Señal de entrada?}
    C -->|Sí| D[Abrir posición]
    C -->|No| E[Esperar]
    D --> F{Señal de salida?}
    F -->|Sí| G[Cerrar posición]
    F -->|No| H[Mantener]
    G --> A
    H --> F
    E --> A
```

## Diagrama de Secuencia: Descarga de Datos con OpenBB

```mermaid
sequenceDiagram
    participant U as Usuario
    participant OBB as OpenBB SDK
    participant YF as Yahoo Finance

    U->>OBB: obb.equity.price.historical("AAPL")
    OBB->>YF: GET /v8/finance/chart/AAPL
    YF-->>OBB: JSON (OHLCV)
    OBB-->>U: OBBject con DataFrame
    U->>U: Aplicar pandas-ta indicadores
```

## Diagrama de Clases: Estructura del Curso

```mermaid
classDiagram
    class Capitulo {
        +String nombre
        +String README
        +List~Notebook~ notebooks
    }
    class Notebook {
        +String titulo
        +String tipo
        +ejecutar()
    }
    class Estrategia {
        +String nombre
        +calcular_senales()
        +backtest()
    }
    Capitulo "1" --> "*" Notebook
    Notebook "1" --> "1" Estrategia
```

## Verificación

Si ves los diagramas renderizados como gráficos SVG (no como texto plano),
la extensión `jupyterlab-myst` está funcionando correctamente.
