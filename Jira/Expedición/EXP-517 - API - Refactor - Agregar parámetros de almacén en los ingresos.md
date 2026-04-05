---
jira_key: "EXP-517"
aliases: ["EXP-517"]
summary: "API - Refactor - Agregar parámetros de almacén en los ingresos "
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2025-10-13 07:15"
updated: "2025-10-13 07:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-517"
---

# EXP-517: API - Refactor - Agregar parámetros de almacén en los ingresos 

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-13 07:15 |
| Actualizado | 2025-10-13 07:36 |
| Etiquetas | ninguna |
| Jira | [EXP-517](https://bluinc.atlassian.net/browse/EXP-517) |

## Relaciones

- **Padre:** [[EXP-486 - Ver ingreso|EXP-486]] Ver ingreso

## Descripcion

Al igual que lo realizado anteriormente se agrega 


- stockWarehouseId


- stockWarehouseDescription


- stockWarehouseCode


- warehouseSensitive




Para esto agregaremos `stockWarehouseId` a `[NewBytes_DBF].[dbo].[pedprol].stockWarehouseId` y `[NewBytes_DBF].[dbo].[albprol].stockWarehouseId`

```
GET {API_URL}/v1/providersOrders/{providerOrder}
```

```
[
    {
        "title": "TECLA HUNNOX SMART TACTIL 1 CANAL BLANCO",
        "id": "120248",
        "sku": "DM-TL1WF-BLA",
        "category": "CASA INTELIGENTE",
        "categoryId": "64",
        "brand": "HUNNOX",
        "brandId": "89",
        "mainImage": "b37352ff0ba9b4a65af69d129b35dfab.jpg",
        "notSerializable": "0",
        "incomingQuantity": "2000",
        "serializedQuantity": "0",
        "fullySerialized": "0",
        "ean": null,
        "upc": "000000120248",
        "gtin": null,
        "isbn": null,
        "stockWarehouseId": 2,
        "stockWarehouseDescription": "SAFcom",
        "stockWarehouseCode": "SAF",
        "warehouseSensitive": false        
    },
    {
        "title": "TECLA HUNNOX SMART TACTIL 2 CANALES BLANCO",
        "id": "120249",
        "sku": "DM-TL2WF-BLA",
        "category": "CASA INTELIGENTE",
        "categoryId": "64",
        "brand": "HUNNOX",
        "brandId": "89",
        "mainImage": "e2e1316b4f8c95982a21a617c7473479.jpg",
        "notSerializable": "0",
        "incomingQuantity": "2400",
        "serializedQuantity": "0",
        "fullySerialized": "0",
        "ean": null,
        "upc": "000000120249",
        "gtin": null,
        "isbn": null,
        "stockWarehouseId": 2,
        "stockWarehouseDescription": "SAFcom",
        "stockWarehouseCode": "SAF",
        "warehouseSensitive": false        
    },
```
