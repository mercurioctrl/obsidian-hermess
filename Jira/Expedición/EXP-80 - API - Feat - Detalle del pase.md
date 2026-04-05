---
jira_key: "EXP-80"
aliases: ["EXP-80"]
summary: "API - Feat - Detalle del pase"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-17 09:18"
updated: "2022-11-17 10:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-80"
---

# EXP-80: API - Feat - Detalle del pase

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-17 09:18 |
| Actualizado | 2022-11-17 10:03 |
| Etiquetas | ninguna |
| Jira | [EXP-80](https://bluinc.atlassian.net/browse/EXP-80) |

## Relaciones

- **Padre:** [[EXP-18 - Feat - Listar pases|EXP-18]] Feat - Listar pases
- **blocks:** [[EXP-81 - APP - Feat - Detalle del pase|EXP-81]] APP - Feat - Detalle del pase

## Descripcion

Se trata de mostrar el detalle del pase, es la misma pantalla que ya desarrollamos para postventa pero desde este lado.

```
{API_URL}/v1/passes/{ID PASE}
```

Devuelve 

```
[
    {
        "id": "63",
        "itemId": "104653",
        "itemDescription": "MEMORIA PATRIOT SIGNATURE LINE DDR4 16 GB 3200 MHZ PS001558",
        "serial": "9DS240-05093",
        "afterSaleDetailId": "50250",
        "sku": "PSD416G32002"
    }
]
```

[adjunto]
