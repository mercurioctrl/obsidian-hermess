---
jira_key: "INV-238"
aliases: ["INV-238"]
summary: "API - Refactor - Agregar al repositorio de stock la cantidad de regularizaciones realizadas"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-11 08:46"
updated: "2025-12-16 15:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-238"
---

# INV-238: API - Refactor - Agregar al repositorio de stock la cantidad de regularizaciones realizadas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-11 08:46 |
| Actualizado | 2025-12-16 15:39 |
| Etiquetas | ninguna |
| Jira | [INV-238](https://bluinc.atlassian.net/browse/INV-238) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **relates to:** [[INV-275 - API - Review - Cantidad de regularizaciones realizadas - Cantidad no coincidente|INV-275]] API - Review - Cantidad de regularizaciones realizadas - Cantidad no coincidente
- **relates to:** [[INV-285 - API - Review - Se observan regularizaciones en cero, cuando deberían ser|INV-285]] API - Review - Se observan regularizaciones en cero, cuando deberían ser mayores a cero

## Descripcion

Incorporar un nuevo parámetro `regularizations` en el recurso `GET {API_URL}/itemsStocks` que refleje la cantidad total de regularizaciones o ajustes manuales de stock realizados históricamente para cada ítem.

### Contexto

Actualmente, no existe un modo eficiente de obtener la cantidad de regularizaciones realizadas sobre un ítem. La única forma de estimar este valor es mediante una consulta al histórico de registros de stock en `[NB_WEB].[dbo].[registro_stock]`, filtrando por los procesos manuales o scripts que históricamente modificaron stock:

```
SELECT SUM(cantidad) AS regu
FROM [NB_WEB].[dbo].[registro_stock]
INNER JOIN NewBytes_DBF.dbo.articulo 
    ON registro_stock.cref = articulo.cref
WHERE (fichero = 'controlDePrecios.nb' OR fichero = 'provDiosStock.php' OR fichero = 'regularizacion')
  AND articulo.ID_ARTICULO = ?
  AND (registro_stock.sPosterior <> registro_stock.sAnterior);

```

Esta consulta es poco eficiente y depende de nombres de ficheros o patrones de texto (`LIKE`) que ralentizan la lectura del repositorio y son frágiles ante cambios.

### Implementación

- **Nueva tabla:**
Crear una tabla específica para registrar todas las regularizaciones de stock manuales (los nombres son un ejemplo):

```
CREATE TABLE [NB_WEB].[dbo].[registro_stock_regularizaciones] (
    id INT IDENTITY(1,1) PRIMARY KEY,
    itemId INT NOT NULL,
    warehouseStockId INT NULL,
    amount DECIMAL(18,2) NOT NULL,
    date DATETIME DEFAULT GETDATE(),
    CONSTRAINT FK_reg_stock_item FOREIGN KEY (itemId) REFERENCES NewBytes_DBF.dbo.articulo(ID_ARTICULO)
);

```


- **Carga inicial de datos:**
Ejecutar una migración o query que precargue los datos históricos de regularizaciones usando la consulta previa.
Este proceso deberá ejecutarse **al momento del corte** entre sistemas para consolidar el histórico.


- **Actualización del recurso de regularización manual:**
Refactorizar el recurso definido en
🔗 [[[INV-230]]](https://bluinc.atlassian.net/browse/INV-230) (`PATCH {API_URL}/itemsStocks/aleter`)
para que, además de registrar el movimiento en `[NB_WEB].[dbo].[registro_stock]`, inserte también un registro correspondiente en `[NB_WEB].[dbo].[registro_stock_regularizaciones]`.


- **Nuevo parámetro en el listado de stock:**
Una vez poblada la tabla, agregar el campo `regularizations` al recurso de listado de stock:

```
GET {API_URL}/itemsStocks?&stock=1&companyCode=4&categoryId={categoryId}&brandId={brandId}&search={title|sku|id}
```

Ejemplo de respuesta:

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
            "regularizations": 2 <<-- SE AGREGA
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
            "creditNoteReturn": 4,
            "regularizations": 2 <<-- SE AGREGA 
        }
    ],
    "pagination": {
        "total": 427,
        "pageSize": 100,
        "current": 1
    }
}
```



---

### Beneficios

- Se elimina la dependencia de búsquedas por nombre de fichero.


- Mejora significativa en la performance de consultas sobre el histórico de stock.


- Facilita análisis contables y operativos sobre ajustes manuales.


- Permite visualizar la cantidad de regularizaciones directamente desde el listado de stock.



---

### Criterios de aceptación

- Debe existir la tabla `[NB_WEB].[dbo].[registro_stock_regularizaciones]` con los campos indicados.


- El recurso `PATCH /itemsStocks/aleter` debe registrar la operación tanto en `registro_stock` como en `registro_stock_regularizaciones`.


- El endpoint `GET /itemsStocks` debe devolver el nuevo parámetro `regularizations` correctamente calculado.


- La carga inicial de datos históricos debe completarse sin errores ni duplicados.


- Las consultas sobre stock deben mantener o mejorar los tiempos de respuesta actuales.
