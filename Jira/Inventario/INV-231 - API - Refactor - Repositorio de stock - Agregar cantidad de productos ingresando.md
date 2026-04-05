---
jira_key: "INV-231"
aliases: ["INV-231"]
summary: "API - Refactor - Repositorio de stock -> Agregar cantidad de productos ingresando"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-10 08:08"
updated: "2025-12-05 04:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-231"
---

# INV-231: API - Refactor - Repositorio de stock -> Agregar cantidad de productos ingresando

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-10 08:08 |
| Actualizado | 2025-12-05 04:39 |
| Etiquetas | ninguna |
| Jira | [INV-231](https://bluinc.atlassian.net/browse/INV-231) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **action item from:** [[INV-211 - API - MVP - Feat- Agregar repo con pestaña de producto por depósito|INV-211]] API - MVP - Feat- Agregar repo con pestaña de producto por depósito
- **action item from:** [[INV-223 - API - Refactor - Algunos cambios para el repositorio de stock|INV-223]] API - Refactor - Algunos cambios para el repositorio de stock
- **has action item:** [[INV-232 - API - Refactor - Repositorio de stock - Agregar cantidad de productos ingresados|INV-232]] API - Refactor - Repositorio de stock -> Agregar cantidad de productos ingresados

## Descripcion

Se agregará un nuevo parámetro al recurso de listado de stock llamado `inProviderOrder`, cuyo valor representa la **cantidad total del ítem que se encuentra actualmente en órdenes de compra de proveedor pendientes de ingreso**.

**Endpoint afectado:**

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
            "inProviderOrder": 10 <<-- SE AGREGA
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
            "inProviderOrder": 10 <<-- SE AGREGA
        }
    ],
    "pagination": {
        "total": 427,
        "pageSize": 100,
        "current": 1
    }
}
```

### Lógica de obtención del dato

El valor de `inProviderOrder` se obtendrá mediante una consulta que sume las cantidades (`ncanped`) de los ítems que se encuentran en órdenes de compra pendientes (`cEstado = 'p'`) y que aún no fueron ingresadas a stock.

**Ejemplo de query:**

```
SELECT 
    SUM(pedprol.ncanped) AS inProviderOrder
FROM 
    NewBytes_DBF.dbo.pedprol
    LEFT JOIN NewBytes_DBF.dbo.PedProT 
        ON pedprol.nNumPed = PedProT.nNumPed
WHERE 
    pedprol.id_articulo = ?
    AND pedprol.stockWarehouseId = 2
    AND PedProT.cEstado = 'p';
```

### Consideraciones de rendimiento

Para optimizar la ejecución de esta consulta —especialmente al invocarse dentro de listados masivos— se recomienda crear un **índice compuesto** en la tabla `[NewBytes_DBF].[dbo].[pedprol]` sobre las siguientes columnas:

```
CREATE INDEX IX_pedprol_idArticulo_StockWarehouse
ON NewBytes_DBF.dbo.pedprol (id_articulo, stockWarehouseId);

```

Y opcionalmente, si se prevé filtrar frecuentemente por estado, agregar un índice adicional en la tabla de cabecera:

```
CREATE INDEX IX_PedProT_cEstado
ON NewBytes_DBF.dbo.PedProT (cEstado);

```

#### **Criterios de aceptación**

- El parámetro `inProviderOrder` debe mostrarse correctamente en cada ítem del recurso `GET /itemsStocks`.


- El valor reflejado debe corresponder a la suma de `ncanped` de todas las órdenes de compra con `cEstado = 'p'` del ítem y depósito correspondiente.


- Si el ítem no tiene órdenes pendientes, el valor de `inProviderOrder` debe ser `0`.


- La query debe ejecutarse en un tiempo razonable (<200 ms por ítem individual), validado con los índices mencionados.


- El endpoint no debe verse afectado en su rendimiento ni estructura actual: el nuevo campo debe añadirse de forma no disruptiva.
