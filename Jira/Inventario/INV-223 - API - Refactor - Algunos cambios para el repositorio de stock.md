---
jira_key: "INV-223"
aliases: ["INV-223"]
summary: "API - Refactor - Algunos cambios para el repositorio de stock"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-04 08:50"
updated: "2025-12-05 04:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-223"
---

# INV-223: API - Refactor - Algunos cambios para el repositorio de stock

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-04 08:50 |
| Actualizado | 2025-12-05 04:18 |
| Etiquetas | ninguna |
| Jira | [INV-223](https://bluinc.atlassian.net/browse/INV-223) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-222 - APP - MVP - Mover stock entre distintos stocks (columnas)|INV-222]] APP - MVP - Mover stock entre distintos stocks (columnas)
- **has action item:** [[INV-231 - API - Refactor - Repositorio de stock - Agregar cantidad de productos ingresando|INV-231]] API - Refactor - Repositorio de stock -> Agregar cantidad de productos ingresando

## Descripcion

Haremos un refactor del repositorio

```
GET {API_URL}/itemsStocks?&stock=1&companyCode=4&categoryId={categoryId}&brandId={brandId}&search={title|sku|id}
```

1 - Lo primero sera evitar que traiga todo el stock si no tengo ningún filtro. Para esto simplemente ejecutaremos la consulta cuando tengo al menos uno de los filtros, de modo tal que siempre lo traiga delimitado.

2 - Agregaremos nuevas columnas de stock como ser

- stockControl (`[NewBytes_DBF].[dbo].[stocks].nstock_ctrl`)


- stockLoQueue (`[NewBytes_DBF].[dbo].[stocks].nstock_en_cola`)







```
{
    "list": [
        {
            "title": "PLACA DE VIDEO ZOTAC RTX 5050 8GB TWIN EDGE",
            "sku": "ZT-B50500H-10M",
            "id": 121438,
            "category": "PLACA DE VIDEO               ",
            "categoryId": 23,
            "brand": "ZOTAC",
            "brandId": 104,
            "mainImage": null,
            "globalRegularization: 0,  <--regularizacion_global
            "stock": 200.0, <-- nstock
            "stockControl": 2,
            "stockLoQueue": 1,
            "virtualStock": 200.0, <-- nstock_virtual
            "stockLio": 0, <-- nstock_lo
            "stockInOrders": 0, <-- nstock_reserva_pedidos
            "stockAfterSale": 0, <-- nstock_postventa
            "nstockHide": 0, <--nstock_d1
            "stockWarehouseId": 2, 
            "stockWarehouseDescription": "SAFcom", 
            "stockWarehouseCode": "SAF", 
            "WarehouseSensitive": false,
            "usedSerialNumbers": 5, <-- Cantidad de serials utilizados (filtra por id, comany_code y stockWarehouseId)
            "totalSerialNumbers": 10 <-- Cantidad de seriales usados para este item (filtra por id, comany_code y stockWarehouseId)
            "companyCode": 4,
            "companyName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "notSerializable": 0,
            "distributorId": 1
        },
...        
```
