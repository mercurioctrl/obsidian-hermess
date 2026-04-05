---
jira_key: "BULLY-11"
aliases: ["BULLY-11"]
summary: "APP - Feat - Mostrar velas para un ticker determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-06-22 09:13"
updated: "2023-07-26 13:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-11"
---

# BULLY-11: APP - Feat - Mostrar velas para un ticker determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-22 09:13 |
| Actualizado | 2023-07-26 13:37 |
| Etiquetas | ninguna |
| Jira | [BULLY-11](https://bluinc.atlassian.net/browse/BULLY-11) |

## Relaciones

- **Padre:** [[BULLY-9]] Grafico de velas / movimientos de precios
- **is blocked by:** [[BULLY-10]] API - Feat - Obtener velas para un ticker determinado

## Descripcion

Inspirados en el ejemplo que se encuentra en  [link](https://help.etnatrader.com/web-api/trading-api/code-samples/get-trading-data-for-charts)  crearemos un recurso similar, para poder dibujar un gráfico de velas.

Y para esto necesitaremos como mínimo los siguientes paramtros (mas adelante agregaremos otros para agregar informacion: time, low, high, open, close



```
PUT {API_URL}/v1/getCandlesAndIndicators
```

Carga útil:

```
{
    "Security": {
        "Symbol": "AAPL",
        "Exchange": "NGS",
        "Currency": "USD"
    },
    "SecurityHistorySettings": {
        "StartDate": 1688356800,
        "EndDate": 1688479282,
        "CandlesCount": -1,
        "Period": "5m",
        "Interval": -5,
        "IncludeNonMarketData": false
    },
    "IndicatorsHistorySettings": [
        {
            "Signature": "SMA|5m|false|1|0",
            "Interval": -5,
            "StartDate": 1688356800,
            "EndDate": 1688403540,
            "CandlesCount": -1,
            "Offset": 0
        }
    ]
}
```

Responde (algo similar, según los datos que necesitamos ahora) **Ver ejemplo en postman de como es la salida real ****[https://liodev.postman.co/workspace/Team-LO~75849ccd-cf9d-4bd6-8a70-d240478268d8/example/20349853-359210b6-8f94-4a70-b937-ab772fd68916](https://liodev.postman.co/workspace/Team-LO~75849ccd-cf9d-4bd6-8a70-d240478268d8/example/20349853-359210b6-8f94-4a70-b937-ab772fd68916)**

```
[{
    "time": 1514764800,
    "low": 192.463774876385,
    "high": 206.26996358990505,
    "open": 199.337469437104,
    "close": 200.55875981792926
},
{
    "time": 1514764800,
    "low": 192.463774876385,
    "high": 206.26996358990505,
    "open": 199.337469437104,
    "close": 200.55875981792926
}
,
{
    "time": 1514764800,
    "low": 192.463774876385,
    "high": 206.26996358990505,
    "open": 199.337469437104,
    "close": 200.55875981792926
}]
```

En la próxima historia agregaremos el tamaño de la vela (1min,2min,1 dia, etc) y el tiempo mostrado en el eje x. Mientras tanto usar 4 min / 7 dias

Referencias

- Tiempo (Time): Este atributo se refiere al período de tiempo en donde se encuentra la vela.


- Mínimo (Low): El atributo "Low" representa el precio más bajo alcanzado durante el período de tiempo especificado. En una vela alcista (verde o blanca), el extremo inferior de la vela muestra el precio más bajo alcanzado durante ese tiempo. En una vela bajista (roja o negra), el extremo superior de la vela representa el precio más bajo.


- Máximo (High): El atributo "High" indica el precio más alto alcanzado durante el período de tiempo considerado. En una vela alcista, el extremo superior de la vela representa el precio máximo, mientras que en una vela bajista, el extremo inferior muestra el precio máximo alcanzado.


- Apertura (Open): El atributo "Open" se refiere al precio de apertura de la vela, es decir, el primer precio registrado en el período de tiempo considerado. En una vela alcista, el precio de apertura se encuentra en la parte inferior del cuerpo de la vela, mientras que en una vela bajista, se encuentra en la parte superior.


- Cierre (Close): El atributo "Close" se refiere al precio de cierre de la vela, es decir, el último precio registrado en el período de tiempo considerado. En una vela alcista, el precio de cierre se encuentra en la parte superior del cuerpo de la vela, mientras que en una vela bajista, se encuentra en la parte inferior.
