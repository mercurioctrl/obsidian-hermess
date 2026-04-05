---
jira_key: "INV-240"
aliases: ["INV-240"]
summary: "API - Refactor - Agregar al repositorio de stock la cantidad de ventas / resesvas realizadas "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-12 09:05"
updated: "2025-12-22 14:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-240"
---

# INV-240: API - Refactor - Agregar al repositorio de stock la cantidad de ventas / resesvas realizadas 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-12 09:05 |
| Actualizado | 2025-12-22 14:00 |
| Etiquetas | ninguna |
| Jira | [INV-240](https://bluinc.atlassian.net/browse/INV-240) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-298 - API - Review - Debemos obtener salesReserved segun el siguiente concepto y|INV-298]] API - Review - Debemos obtener salesReserved segun el siguiente concepto y filtrando sucursal solo cuando se indica explicitamente

## Descripcion

Se incorporará un nuevo parámetro al recurso de listado de stock que muestre, para cada ítem, la cantidad total de unidades **reservadas en ventas activas**, bajo el nombre `salesReserved`.

Este valor representará la **suma de las cantidades de artículos reservadas** en pedidos de clientes (`albclil` y `albclit`) según su estado y tipo de comprobante, excluyendo los comprobantes anulados o finalizados.

---

### **Recurso afectado**

```
GET {API_URL}/itemsStocks?stock=1&companyCode=4&categoryId={categoryId}&brandId={brandId}&search={title|sku|id}
```

---

### **Implementación técnica**

El valor de `salesReserved` se obtendrá mediante una consulta a las tablas:

- `NewBytes_DBF.dbo.albclil`


- `NewBytes_DBF.dbo.albclit`



Ejemplo de SQL base:

```
SELECT 
    SUM(albclil.ncanent) AS RESERVAS
FROM NewBytes_DBF.dbo.albclil
LEFT OUTER JOIN NewBytes_DBF.dbo.albclit 
    ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
WHERE albclil.ID_Articulo = @itemId
  AND albclil.ID_ALMACEN = @warehouseId
  AND albclit.ntipoalb > 1

```

> `ntipoalb > 1`* representa un pedido que ya cambio de estado, y por ende se considera liquidado*


El resultado deberá sumarse y exponerse en el campo `salesReserved` de la respuesta principal.

---

### **Ejemplo de respuesta**

```
[
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
    "regularizations": 2,
    "salesReserved": 5
  }
]

```

---

### **Reglas y consideraciones**

- Si no existen reservas para un ítem, retornar `salesReserved = 0`.


- Debe respetarse el mismo `stockWarehouseId` que en el resto de los cálculos de stock.


- El cálculo debe realizarse de forma eficiente, preferentemente en una subquery o `JOIN` dentro del procedimiento que genera el listado.


- Asegurar que exista índice sobre `albclil.ID_Articulo` y `albclil.ID_ALMACEN` para evitar degradar la performance del endpoint, si es necesario agregar el indice compuesto.



---

### **Criterios de aceptación**

- Cada ítem del listado incluye un nuevo campo `salesReserved` con el total de unidades reservadas en ventas.


- Si el ítem no tiene reservas activas, el campo aparece con valor `0`.


- El valor se obtiene a partir de la suma de `albclil.ncanent` filtrando solo registros con `ntipoalb > 1`.


- El endpoint mantiene tiempos de respuesta similares al actual 200ms aprox.


- En caso de error en la consulta de reservas, el resto del listado debe seguir devolviéndose correctamente, asignando `salesReserved = 0` por defecto.
