---
jira_key: "BULLY-25"
aliases: ["BULLY-25"]
summary: "API - Feat - Repositorio de tickers"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-13 16:27"
updated: "2023-07-17 09:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-25"
---

# BULLY-25: API - Feat - Repositorio de tickers

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-13 16:27 |
| Actualizado | 2023-07-17 09:17 |
| Etiquetas | ninguna |
| Jira | [BULLY-25](https://bluinc.atlassian.net/browse/BULLY-25) |

## Relaciones

- **Padre:** [[BULLY-24]] Tickers

## Descripcion

Según lo documentado en [link](https://help.etnatrader.com/web-api/trading-api/securities/get-filtered-equities) , crearemos un repositorio que nos permita obtener los distintos tickers y sus parámetros para poder utilizar en el front en cada uno de las pestañas para seleccionar un ticker diferente.

Solo realizaremos la búsqueda cuando tengamos 2 caracteres o mas

```
GET {{API_URL}}/tickers?search={string de texto}
```

```
[
        {
            "Id": 681777,
            "Symbol": "INDY",
            "Description": "iShares S&P India Nifty 50 Index Fund",
            "Exchange": "XNAS",
            "Currency": "USD",
            "AddedDate": "2012-11-30T07:22:20.667Z",
            "ModifyDate": "2018-03-26T07:00:05.944571Z",
            "Type": "ETF",
            "Precision": 2,
            "VolumePrecision": 0,
            "TickSize": 0.01,
            "Enabled": true,
            "AllowTrade": true,
            "AllowMargin": true,
            "AllowShort": true
        },
        {
            "Id": 684344,
            "Symbol": "QQQ",
            "Description": "Invesco QQQ Trust, Series 1",
            "Exchange": "XNAS",
            "Currency": "USD",
            "AddedDate": "2012-11-30T07:22:20.67Z",
            "ModifyDate": "2018-05-29T07:00:05.8792207Z",
            "Type": "ETF",
            "Precision": 2,
            "VolumePrecision": 0,
            "TickSize": 0.01,
            "Enabled": true,
            "AllowTrade": true,
            "AllowMargin": true,
            "AllowShort": true
        }
    ]
```
