---
jira_key: "NBWEB-521"
aliases: ["NBWEB-521"]
summary: "API - Feat - Listar Cotizaciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-20 14:03"
updated: "2023-04-11 09:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-521"
---

# NBWEB-521: API - Feat - Listar Cotizaciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-20 14:03 |
| Actualizado | 2023-04-11 09:35 |
| Etiquetas | ninguna |
| Jira | [NBWEB-521](https://bluinc.atlassian.net/browse/NBWEB-521) |

## Relaciones

- **Padre:** [[NBWEB-73 - API - CMS - ABMS|NBWEB-73]] API - CMS - ABMS
- **blocks:** [[NBWEB-522 - APP - Feat - Cotizaciones|NBWEB-522]] APP - Feat - Cotizaciones

## Descripcion

Basándonos en la tabla `[NEW_BYTES].[dbo].[MS_COTIZACIONES]` generaremos el siguiente recurso

```
GET {{API_URL}}/v1/cms/currencyQuote 
```

```
[
  {
    "description": "PESOS",
    "currency": 211.0,
    "CurrencyQuoteMax": 235.0,
    "dateModify": "2023-03-17T12:43:20",
    "user": "andrea",
    "minCurrencyQuotePesos": 211.0,
    "minCurrencyQuoteCheck": null,
    "id": 1
  },
  {
    "description": "DOLARES",
    "currency": 206.78,
    "CurrencyQuoteMax": 235.0,
    "dateModify": "2023-03-17T12:43:20",
    "user": "andrea",
    "minCurrencyQuotePesos": null,
    "minCurrencyQuoteCheck": null,
    "id": 2
  },
  {
    "NOMBRE": "PESOSLO",
    "COTIZACION": 210.0,
    "COTIZACION_MAXIMA": 210.0,
    "FECMODIF": null,
    "USUARIO": "Catriel",
    "COTIZACION_MINIMA_PESOS": 210.0,
    "COTIZACION_MINIMA_CHEQUE": null,
    "IDFORMAPAGO": 1,
    "id": 3
  },
  {
    "NOMBRE": "CHEQUES",
    "COTIZACION": 228.34,
    "COTIZACION_MAXIMA": 235.0,
    "FECMODIF": "2023-03-17T12:43:20",
    "USUARIO": "andrea",
    "COTIZACION_MINIMA_PESOS": null,
    "COTIZACION_MINIMA_CHEQUE": 228.34,
    "IDFORMAPAGO": 3,
    "id": 4
  }
]
```
