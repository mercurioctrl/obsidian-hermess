---
jira_key: "INV-237"
aliases: ["INV-237"]
summary: "API - Refactor - Agregar al repositorio de stock la cantidad de NC realizadas desde postventa (solo cuando afectaron stock)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-10 17:03"
updated: "2025-12-05 04:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-237"
---

# INV-237: API - Refactor - Agregar al repositorio de stock la cantidad de NC realizadas desde postventa (solo cuando afectaron stock)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-10 17:03 |
| Actualizado | 2025-12-05 04:43 |
| Etiquetas | ninguna |
| Jira | [INV-237](https://bluinc.atlassian.net/browse/INV-237) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Agregaremos un nuevo parámetro que refleje aquellos casos, donde el credito de postventa afecto el stock.

Este caso, hasta donde entiendo solo se puede dar en dos variantes

- Cuando el producto falla, y se hace un crédito por cambio. En este caso se cuenta un crédito y ademas otro que es para hacer un remplazo.


- Cuando el producto falla y se hace un crédito para devolver el dinero. En este caso se cuenta un crédito.



Utilizaremos el parametro `aftersalesCreditNote`

```
GET {API_URL}/itemsStocks?&stock=1&companyCode=4&categoryId={categoryId}&brandId={brandId}&search={title|sku|id}
```

```
[
  ...
  {
            "title": "MEMORIA ADATA DIMM XPG LANCER DDR5 16GB 6000MHZ BLACK",
            "sku": "AX5U6000C3016G-CLARBK",
            "id": 118755,
            "category": "MEMORIAS",
            "categoryId": 1,
            "brand": "ADATA",
            "brandId": 91,
            "mainImage": "https://gamma.static.nb.com.ar/img/4929df4a8457158299d18c5baf93f1ed.png",
            "globalRegularization": 0,
            "stock": 0,
            "virtualStock": 0,
            "stockLio": 0,
            "stockInOrders": 0,
            "stockAfterSale": 0,
            "nstockHide": 0,
            "stockWarehouseId": 2,
            "stockWarehouseDescription": "SAFcom",
            "stockWarehouseCode": "SAF",
            "WarehouseSensitive": false,
            "usedSerialNumbers": 100,
            "totalSerialNumbers": 100,
            "companyCode": 4,
            "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "notSerializable": 0,
            "distributorId": 1,
            "stockCtrl": 0,
            "stockLoQueue": 0,
            "inProviderOrder": 10,
            "inProviderOrderInbound": 10,
            "creditNoteReturn": 4,
            "aftersalesCreditNote": 2 <<-- SE AGREGA
        },
        {
            "title": "MEMORIA ADATA DIMM XPG SPECTRIX 16GB (2x8) DDR4 3600 18I DCBKD45G",
            "sku": "AX4U36008G18I-DCBKD45G",
            "id": 118754,
            "category": "MEMORIAS",
            "categoryId": 1,
            "brand": "ADATA",
            "brandId": 91,
            "mainImage": "https://gamma.static.nb.com.ar/img/44e17db1dd144906eaf3813202f9ccee.png",
            "globalRegularization": 0,
            "stock": 0,
            "virtualStock": 0,
            "stockLio": 0,
            "stockInOrders": 0,
            "stockAfterSale": 0,
            "nstockHide": 0,
            "stockWarehouseId": 2,
            "stockWarehouseDescription": "SAFcom",
            "stockWarehouseCode": "SAF",
            "WarehouseSensitive": false,
            "usedSerialNumbers": 100,
            "totalSerialNumbers": 100,
            "companyCode": 4,
            "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "notSerializable": 0,
            "distributorId": 1,
            "stockCtrl": 0,
            "stockLoQueue": 0,
            "inProviderOrder": 10,
            "inProviderOrderInbound": 10,
            "creditNoteReturn": 4, <<-- SE AGREGA
            "aftersalesCreditNote": 2 <<-- SE AGREGA
        }
    ],
    "pagination": {
        "total": 427,
        "pageSize": 100,
        "current": 1
    }
}
```
