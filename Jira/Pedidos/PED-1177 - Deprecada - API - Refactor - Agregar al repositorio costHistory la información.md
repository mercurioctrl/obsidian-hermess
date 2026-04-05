---
jira_key: "PED-1177"
aliases: ["PED-1177"]
summary: "Deprecada - API - Refactor - Agregar al repositorio costHistory la información de \"cantidad\" para esa compra"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-12-10 07:13"
updated: "2025-12-10 09:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1177"
---

# PED-1177: Deprecada - API - Refactor - Agregar al repositorio costHistory la información de "cantidad" para esa compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-10 07:13 |
| Actualizado | 2025-12-10 09:32 |
| Etiquetas | ninguna |
| Jira | [PED-1177](https://bluinc.atlassian.net/browse/PED-1177) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **duplicates:** [[PED-1176 - API - MVP- Refactor - Modificar recurso de costHistory|PED-1176]] API - MVP- Refactor - Modificar recurso de costHistory

## Descripcion

Agregaremos `amount` a cada uno de los costos por compra.

La idea es agregar la cantidad que se compro en cada compra, para posteriormente que el front pueda hacer promedios entre las cantidades.

```
GET /v1/items/{itemId}/costHistory
```

```
[
    {
        "cost": 84,
        "currencyQuote": 103.75,
        "invoiceDate": "2021-10-20 14:56:37",
        "cnompro": "LASET S.A.",
        "warehouseId": 2,
        "warehouseName": "SAFcom",
        "warehouseCode": "SAF",
        "countryId": 5,
        "countryDescription": "Estados Unidos De AMERICA",
        "countryCode": "US ",
        "amount": 34 <---- Se agrega
    },
    {
        "cost": 83,
        "currencyQuote": 88.5,
        "invoiceDate": "2021-01-08 12:34:38",
        "cnompro": "LASET S.A.",
        "warehouseId": 2,
        "warehouseName": "SAFcom",
        "warehouseCode": "SAF",
        "countryId": 5,
        "countryDescription": "Estados Unidos De AMERICA",
        "countryCode": "US ",
        "amount": 23 <-- Se agrega
    },
    {
        "cost": 90,
        "currencyQuote": 75.5,
        "invoiceDate": "2020-07-30 08:19:40",
        "cnompro": "LASET S.A.",
        "warehouseId": 2,
        "warehouseName": "SAFcom",
        "warehouseCode": "SAF",
        "countryId": 5,
        "countryDescription": "Estados Unidos De AMERICA",
        "countryCode": "US ",
        "amount": 12 <-- Se agrega
    }
]
```
