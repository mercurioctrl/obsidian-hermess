---
jira_key: "PED-79"
aliases: ["PED-79"]
summary: "API - Repository - Cotizacion de medios de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-19 09:29"
updated: "2023-09-19 12:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-79"
---

# PED-79: API - Repository - Cotizacion de medios de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-19 09:29 |
| Actualizado | 2023-09-19 12:42 |
| Etiquetas | ninguna |
| Jira | [PED-79](https://bluinc.atlassian.net/browse/PED-79) |

## Relaciones

- **Padre:** [[PED-7]] Repositorios y base del proyecto

## Descripcion

```
GET {{API_URL}}/v1/currencyQuote
```

```
[
   {
    "description": "PESOS",
    "currency": 211.0,
    "CurrencyQuoteMax": 235.0,
    "minCurrencyQuotePesos": 211.0,
    "minCurrencyQuoteCheck": null,
    "id": 1,
    "dailyInterest":12
  },
  "description": "PESOSLO",
    "currency": 211.0,
    "CurrencyQuoteMax": 235.0,
    "minCurrencyQuotePesos": 211.0,
    "minCurrencyQuoteCheck": null,
    "id": 1,
    "dailyInterest":12
]
```

Adicionalmente agregaría un objeto extra para la taza de interés diaria

que surge de dividir por 365

el monto que sale de `SELECT TASAANUAL FROM NEW_BYTES.dbo.PV_PARAMETROS_VARIOS`

el parámetro se llamara `dailyInterest`
