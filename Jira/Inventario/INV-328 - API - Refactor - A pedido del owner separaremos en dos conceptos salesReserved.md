---
jira_key: "INV-328"
aliases: ["INV-328"]
summary: "API - Refactor - A pedido del owner separaremos en dos conceptos salesReserved"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-19 17:38"
updated: "2026-01-22 18:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-328"
---

# INV-328: API - Refactor - A pedido del owner separaremos en dos conceptos salesReserved

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-19 17:38 |
| Actualizado | 2026-01-22 18:53 |
| Etiquetas | ninguna |
| Jira | [INV-328](https://bluinc.atlassian.net/browse/INV-328) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-330]] APP - Refactor - Agregar nuevo parámetro sales a la resta y las columnas

## Descripcion

Diferenciaremos el concepto `salesReserved` segun su estado en dos métricas diferentes

- salesReserved (`AND albclit.ntipoalb = 1`)


- sales (`AND albclit.ntipoalb > 1`)



De esta forma obtendremos un objeto como el siguiente

```
GET /itemsStocks?currentPage=1&itemsPerPage=500&companyCode=4&brandId=43&search=121556
```

```
{
    "list": [
        {
            "title": "PROCESADOR AMD (AM5) RYZEN 7 8700G ",
            "sku": "100-100001236SBX",
            "id": 121556,
            "category": "PROCESADORES",
            "categoryId": 3,
            "brand": "AMD                                               ",
            "brandId": 43,
            "mainImage": "http://static.nb.com.ar/img/544669030ad7e000c9bf9bc789041283.png",
            "globalRegularization": 0.0,
            "stock": 115.0,
            "virtualStock": 0,
            "stockLio": 0,
            "stockInOrders": 0,
            "stockAfterSale": 0,
            "nstockHide": 250.0,
            "stockWarehouseId": null,
            "stockWarehouseDescription": null,
            "stockWarehouseCode": null,
            "WarehouseSensitive": false,
            "usedSerialNumbers": 34,
            "totalSerialNumbers": 400,
            "companyCode": 4,
            "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "notSerializable": 0,
            "distributorId": 1,
            "stockCtrl": 0,
            "stockLoQueue": 0,
            "inProviderOrder": 0,
            "inProviderOrderInbound": 400.0,
            "creditNoteReturn": 0,
            "aftersalesCreditNote": 0,
            "regularizations": 0,
            "salesReserved": 34.0,
            "salesReserved": 1.0,
            "stockDelta": 0.0
        }
    ],
    "pagination": {
        "total": 1,
        "pageSize": 500,
        "current": 1
    }
}
```

IMPORTANTE: El nuevo parametro `sales` tambien se resta para el `stockDelta`
