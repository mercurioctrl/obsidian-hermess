---
jira_key: "PED-131"
aliases: ["PED-131"]
summary: "API - Rpository - Medios de cobro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-09 16:07"
updated: "2023-10-10 09:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-131"
---

# PED-131: API - Rpository - Medios de cobro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-09 16:07 |
| Actualizado | 2023-10-10 09:17 |
| Etiquetas | ninguna |
| Jira | [PED-131](https://bluinc.atlassian.net/browse/PED-131) |

## Relaciones

- **Padre:** [[PED-7]] Repositorios y base del proyecto
- **blocks:** [[PED-125]] APP - Feat - Modal de liquidacion

## Descripcion

Asi como lo hicimos en cobros para poder componer la herramientas de “cobros” se deben poder obtener los medios de cobro.

```
GET {API_URL}/v1/receiveMethods
```

```
[
    {
        "id": 1,
        "description": "DOLARES",
        "increment": 0,
        "currencyAmount": 1,
        "isCheck": "NO",
        "paymentTolerance": 1,
        "dailyInterest": 0
    },
    {
        "id": 2,
        "description": "PESOS",
        "increment": 0,
        "currencyAmount": 395,
        "isCheck": "NO",
        "paymentTolerance": 10,
        "dailyInterest": 0
    },
    {
        "id": 14,
        "description": "CUENTA CORRIENTE",
        "increment": 0,
        "currencyAmount": 1,
        "isCheck": "NO",
        "paymentTolerance": 1,
        "dailyInterest": 0
    },
    {
        "id": 15,
        "description": "CHEQUE",
        "increment": 0,
        "currencyAmount": 465.75,
        "isCheck": "SI",
        "paymentTolerance": 10,
        "dailyInterest": 0.29
    },
    {
        "id": 13,
        "description": "RETENCION IIBB",
        "increment": 0,
        "currencyAmount": 395,
        "isCheck": "NO",
        "paymentTolerance": 10,
        "dailyInterest": 0
    },
    {
        "id": 17,
        "description": "RETENCION DE GANANCIAS",
        "increment": 0,
        "currencyAmount": 273.5,
        "isCheck": "NO",
        "paymentTolerance": 10,
        "dailyInterest": 0
    },
    {
        "id": 10,
        "description": "RETENCION IVA",
        "increment": 0,
        "currencyAmount": 273.5,
        "isCheck": "NO",
        "paymentTolerance": 10,
        "dailyInterest": 0
    },
    {
        "id": 11,
        "description": "RETENCION PATRONALES",
        "increment": 0,
        "currencyAmount": 273.5,
        "isCheck": "NO",
        "paymentTolerance": 10,
        "dailyInterest": 0
    }
]
```
