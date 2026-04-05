---
jira_key: "INV-211"
aliases: ["INV-211"]
summary: "API - MVP - Feat- Agregar repo con pestaña de producto por depósito"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-10-16 10:37"
updated: "2025-11-14 11:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-211"
---

# INV-211: API - MVP - Feat- Agregar repo con pestaña de producto por depósito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-16 10:37 |
| Actualizado | 2025-11-14 11:07 |
| Etiquetas | ninguna |
| Jira | [INV-211](https://bluinc.atlassian.net/browse/INV-211) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **Subtarea:** [[INV-213 - API - MVP - Feat- opción para cambiar el producto de depósito|INV-213]] API - MVP - Feat-  opción para cambiar el producto de depósito
- **Subtarea:** [[INV-214 - APP - MVP - Feat- opción para cambiar el producto de depósito|INV-214]]  APP  - MVP - Feat-  opción para cambiar el producto de depósito
- **Subtarea:** [[INV-259 - API - MVP - Refactor - Registro de stock - Agregar control de stock al snapshot|INV-259]] API - MVP - Refactor - Registro de stock -> Agregar control de stock al snapshot
- **action item from:** [[INV-212 - APP - MVP - Feat- Agregar repo con pestaña de producto por depósito|INV-212]] APP - MVP - Feat- Agregar repo con pestaña de producto por depósito
- **has action item:** [[INV-231 - API - Refactor - Repositorio de stock - Agregar cantidad de productos ingresando|INV-231]] API - Refactor - Repositorio de stock -> Agregar cantidad de productos ingresando

## Descripcion

Crearemos un nuevo repositorio desde el cual manejaremos y leeremos todos los datos referidos a los distintos stocks y movimientos de los mismos, la idea es tener control total y poder ubicar rápidamente cualquier diferencia o encontrar el stock .

Lo haremos sobre un repositorio distinto a items porque operaremos mucho sobre el y agregaremos mas parámetros específicos de cantidades

```
GET {API_URL}/itemsStocks?&stock=1&companyCode=4&categoryId={categoryId}&brandId={brandId}&search={title|sku|id}
```

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
