---
jira_key: "EXP-427"
aliases: ["EXP-427"]
summary: "API - Refactor - Agregar al detalle de la orden el parametro para saber si ese item tiene un control pendiente [IDEA RECHAZADA POR EXP]"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2024-08-05 16:54"
updated: "2024-08-05 17:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-427"
---

# EXP-427: API - Refactor - Agregar al detalle de la orden el parametro para saber si ese item tiene un control pendiente [IDEA RECHAZADA POR EXP]

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-05 16:54 |
| Actualizado | 2024-08-05 17:12 |
| Etiquetas | ninguna |
| Jira | [EXP-427](https://bluinc.atlassian.net/browse/EXP-427) |

## Relaciones

- **Padre:** [[EXP-424 - Controles de stock al despachar|EXP-424]] Controles de stock al despachar

## Descripcion

Haremos una refactorizacion sobre el recurso 

```
{API_URL}/v1/orders/{pedido}
```

```
[
    {
        "title": "FUENTE GAMER GIGABYTE 650W 80 PLUS BRONZE",
        "id": 101756,
        "sku": "GP-P650B",
        "category": "FUENTES     ",
        "idCategory": 38,
        "idBrand": 4,
        "brand": "GIGABYTE                                          ",
        "mainImage": "7ab86f5882d044f74fa0ada8bd63b1e3.jpeg",
        "notSerializable": 0,
        "incomingQuantity": 1,
        "serializedQuantity": 0,
        "fullSerialized": false,
        "acreditado": 0,
        "conIva": 89.4944919,
        "ivaTax": 21,
        "sinIva": 73.96239,
        "cotizacion": 953.5,
        "iibbPerceptions": 3.25.
        "pendingCount": true/false <--- NUEVO
    },
    {
        "title": "GABINETE GAMER AUREOX NEREID ARX 320G",
        "id": 103041,
        "sku": "NEREID ARX 320G",
        "category": "GABINETE GAMER",
        "idCategory": 18,
        "idBrand": 119,
        "brand": "AUREOX",
        "mainImage": "355715a3533fb0a125bf075475dfdcc6.jpeg",
        "notSerializable": 0,
        "incomingQuantity": 1,
        "serializedQuantity": 0,
        "fullSerialized": false,
        "acreditado": 0,
        "conIva": 58.98988355,
        "ivaTax": 10.5,
        "sinIva": 53.38451,
        "cotizacion": 953.5,
        "iibbPerceptions": 3.25
        "pendingCount": true/false <--- NUEVO
    },
    {
    
...
```

`[NewBytes_DBF].[dbo].[stocksControl] WHERE countedDate IS NULL and itemId = ?`
