---
jira_key: "NBWEB-523"
summary: "API - Feat - Editar cotizacion"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-20 14:29"
updated: "2023-03-22 09:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-523"
---

# NBWEB-523: API - Feat - Editar cotizacion

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-20 14:29 |
| Actualizado | 2023-03-22 09:11 |
| Etiquetas | ninguna |
| Jira | [NBWEB-523](https://bluinc.atlassian.net/browse/NBWEB-523) |

## Descripción

Basándonos en la tabla `[NEW_BYTES].[dbo].[MS_COTIZACIONES]` generaremos el siguiente recurso

```
PATCH {{API_URL}}/v1/cms/currencyQuote 
```

```
[
   {
    "description": "PESOS",
    "currency": 211.0,
    "CurrencyQuoteMax": 235.0,
    "minCurrencyQuotePesos": 211.0,
    "minCurrencyQuoteCheck": null,
    "id": 1
  },
  "description": "PESOSLO",
    "currency": 211.0,
    "CurrencyQuoteMax": 235.0,
    "minCurrencyQuotePesos": 211.0,
    "minCurrencyQuoteCheck": null,
    "id": 1
]
```

Los recursos presentes se puden editer (menos id) si están en el objeto
