---
jira_key: "INV-313"
aliases: ["INV-313"]
summary: "API - Feat - Repositorio de stock por deposito para un item determinado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-06 09:11"
updated: "2026-01-20 17:51"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/INV-313"
---

# INV-313: API - Feat - Repositorio de stock por deposito para un item determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-06 09:11 |
| Actualizado | 2026-01-20 17:51 |
| Etiquetas | esperandoDependencia |
| Jira | [INV-313](https://bluinc.atlassian.net/browse/INV-313) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-317 - APP - Feat - Repositorio de stock por deposito para un item determinado|INV-317]] APP - Feat - Repositorio de stock por deposito para un item determinado

## Descripcion

Crearemos un recurso para consultar disponibilidad para un item determinado en los distintos almacenes

```
GET /itemsStocksWarehouse/{itemId}?currentPage=1&itemsPerPage=500&companyCode=11
```



```
{
    "list": [
        {
            "stockWarehouseId": 15,
            "stockWarehouseCode": "BPR",
            "stockWarehouseCode": "BONDED PROVEEDOR",
            "address": "Miami",
            "default": true,
            "countryDescription": "Estados Unidos De AMERICA",
            "countryId": 5,
            "prefixFlag": "US",
            "companyCode": 11,
            "stockLio": 0,
            "stock": 0,
            "nstockHide" 0,
            "stockInOrders" 0,
            "virtualStock" 0,
            "stockCtrl": 0,
            "stockAfterSale" 0
        },
        {
            "stockWarehouseId": 16,
            "stockWarehouseCode": "BFA",
            "stockWarehouseCode": "BONDED-FASTMARK",
            "address": "miami",
            "default": true,
            "countryDescription": "Estados Unidos De AMERICA",
            "countryId": 5,
            "prefixFlag": "US",
            "companyCode": 11,
            "stockLio": 0,
            "stock": 0,
            "nstockHide" 0,
            "stockInOrders" 0,
            "virtualStock" 0,
            "stockCtrl": 0,
            "stockAfterSale" 0         
        },
   ...
    ],
    "pagination": {
        "total": 3,
        "pageSize": 500,
        "current": 1
    }
}
```
