---
jira_key: "INV-232"
aliases: ["INV-232"]
summary: "API - Refactor - Repositorio de stock -> Agregar cantidad de productos ingresados"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-10 08:24"
updated: "2025-12-05 04:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-232"
---

# INV-232: API - Refactor - Repositorio de stock -> Agregar cantidad de productos ingresados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-10 08:24 |
| Actualizado | 2025-12-05 04:40 |
| Etiquetas | ninguna |
| Jira | [INV-232](https://bluinc.atlassian.net/browse/INV-232) |

## Relaciones

- **Padre:** [[INV-199]] Control de Stock / Stock en general  / Control de Precios
- **action item from:** [[INV-231]] API - Refactor - Repositorio de stock -> Agregar cantidad de productos ingresando

## Descripcion

Se agregará un nuevo parámetro al recurso de listado de stock llamado `inProviderOrderInbound`, cuyo valor representa la **cantidad total del ítem que se encuentra actualmente en órdenes de compra de proveedor que ya ingresaron**.

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
            "inProviderOrder": 10,
            "inProviderOrderInbound": 10 <<-- SE AGREGA
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
            "inProviderOrderInbound": 10 <<-- SE AGREGA
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

El valor de `inProviderOrderInbound` se obtendrá mediante una consulta que sume las cantidades (`ncanped`) de los ítems que se encuentran en órdenes de compra pendientes (`cEstado = 'p'`) y que aún no fueron ingresadas a stock.

**Ejemplo de query:**

```
SELECT 
  sum(albprol.ncanent) AS inProviderOrderInbound
     FROM NewBytes_DBF.dbo.albprol
     LEFT OUTER JOIN NewBytes_DBF.dbo.albprot ON NewBytes_DBF.dbo.albprol.nnumalb = NewBytes_DBF.dbo.albprot.nnumalb
WHERE 
    albprol.id_articulo = ?
    AND albprol.stockWarehouseId = 2
```

### Consideraciones de rendimiento

Para optimizar la ejecución de esta consulta —especialmente al invocarse dentro de listados masivos— se recomienda crear un **índice compuesto** en la tabla `[NewBytes_DBF].[dbo].[albprol]` sobre las siguientes columnas:

```
CREATE INDEX IX_albprol_idArticulo_StockWarehouse
ON NewBytes_DBF.dbo.albprol (id_articulo, stockWarehouseId);

```



#### **Criterios de aceptación**

- El recurso `GET /itemsStocks` debe incluir en cada ítem el nuevo campo `inProviderOrderInbound`, mostrando un valor numérico correspondiente a la cantidad total del artículo en órdenes de compra de proveedor ya ingresadas.


- El cálculo de `inProviderOrderInbound` debe realizarse mediante la suma de `albprol.ncanent` filtrando por `id_articulo` y `stockWarehouseId`.


- Debe garantizarse un rendimiento adecuado del endpoint mediante la creación del índice compuesto `IX_albprol_idArticulo_StockWarehouse` en `[NewBytes_DBF].[dbo].[albprol]`.


- El nuevo campo no debe afectar ni modificar los valores existentes en otros atributos del listado (`stock`, `virtualStock`, `inProviderOrder`, etc.).


- La query debe ejecutarse en un tiempo razonable (<200 ms por ítem individual), validado con los índices mencionados.
