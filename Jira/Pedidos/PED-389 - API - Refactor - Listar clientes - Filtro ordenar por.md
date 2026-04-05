---
jira_key: "PED-389"
aliases: ["PED-389"]
summary: "API - Refactor - Listar clientes -> Filtro ordenar por"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-26 07:43"
updated: "2024-01-26 04:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-389"
---

# PED-389: API - Refactor - Listar clientes -> Filtro ordenar por

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-26 07:43 |
| Actualizado | 2024-01-26 04:39 |
| Etiquetas | ninguna |
| Jira | [PED-389](https://bluinc.atlassian.net/browse/PED-389) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **blocks:** [[PED-390 - APP - Feat - Listar clientes - Conjunto de filtros ordenar por y sentido del|PED-390]] APP - Feat - Listar clientes -> Conjunto de filtros ordenar por y sentido del orden
- **is blocked by:** [[PED-404 - API - Listar clientes - Filtrado - Incidencias varias|PED-404]]   API - Listar clientes -> Filtrado - Incidencias varias
- **relates to:** [[PED-463 - API - Refactor - Listar clientes - Filtro por ultima compra|PED-463]] API - Refactor - Listar clientes -> Filtro por ultima compra 
- **relates to:** [[PED-517 - API - Listar clientes - Filtrado - Error al enlazar columnas|PED-517]] API - Listar clientes -> Filtrado - Error al enlazar columnas

## Descripcion

Refactorizaremos el recurso para poder ordenar los resultados según los parámetros listados mas abajo. Adicionalmente agregaremos otro parámetro para darle dirección al orden.

```
GET {API_URL}/v1/clients?order={parametro}&direction=desc
```



```
[
    {
        "date": "2022-05-30 19:36:52",
        "ccodcli": "053669",
        "businessName": "Catriel Mercurio",
        "name": "Catriel Mercurio",
        "clientTaxNumber": "20000000002",
        "email": "defecto@nb.com.ar",
        "phone": "0000",
        "salespersonName": " ",
        "address": null,
        "id": 53669,
        "average_purchase_value": ,
        "purchase_frequency": ,
        "relationship_duration_month": ,
        "ltv": ,
        "lasPurchase": "21/05/2023", <---- Fecha de ultima compra
        "sinceLastPurchase": 186 <--- Dias desde la ultima compra
    },
    ...
```



Se debe poder ordenar por los siguientes parámetros

- `sinceLastPurchase`


- `ltv`


- `relationship_duration_month`


- `purchase_frequency`


- `average_purchase_value`


- `date`


- `businessName`


- `name`





Este filtro puede combinarse con todos los demas
