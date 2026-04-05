---
jira_key: "INV-242"
aliases: ["INV-242"]
summary: "API - Refactor - Agregar indicador stockDelta para indicar la diferencia de stock que hay para un producto determinado y lo que debería haber según los movimientos realizados"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-12 16:36"
updated: "2025-12-05 04:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-242"
---

# INV-242: API - Refactor - Agregar indicador stockDelta para indicar la diferencia de stock que hay para un producto determinado y lo que debería haber según los movimientos realizados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-12 16:36 |
| Actualizado | 2025-12-05 04:54 |
| Etiquetas | ninguna |
| Jira | [INV-242](https://bluinc.atlassian.net/browse/INV-242) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios

## Descripcion

Se incorporará un nuevo parámetro llamado `stockDelta`, cuyo propósito es mostrar la **diferencia entre el stock teórico** (según todos los movimientos de ingreso y egreso) y el **stock real** que el sistema actualmente informa.
Este valor permitirá detectar inconsistencias de forma rápida y facilitar ajustes operativos o correcciones de datos.

Para obtenerlo, se aplicará la siguiente fórmula:

```
stockDelta =
   inProviderOrderInbound
 - aftersalesCreditNote
 - creditNoteReturn
 - nstockHide
 - stock
 - stockLio
 - stockCtrl
 - stockLoQueue
 - stockInOrders
 - salesReserved
 + globalRegularization

```

---

### **Endpoint afectado**

```
GET {API_URL}/itemsStocks?stock=1&companyCode=4&categoryId={categoryId}&brandId={brandId}&search={title|sku|id}
```

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
    "globalRegularization": 3,
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
    "salesReserved": 5,
    "stockDelta": 345
  }
]

```

### **Criterios de aceptación**

- **El parámetro **`stockDelta`** debe incluirse en la respuesta del endpoint**

y aparecer para cada ítem del listado cuando existan datos suficientes para calcularlo.


- **El cálculo de **`stockDelta`** debe aplicarse exactamente con la fórmula establecida**, respetando la suma y resta de cada parámetro, y validando que no se dupliquen valores 


- **El endpoint debe devolver **`stockDelta`** como número entero**, sin formateos adicionales, y debe poder ser negativo, cero o positivo según corresponda.


- **Si alguno de los parámetros utilizados en el cálculo no existe o es nulo**, debe considerarse como cero sin generar errores en el endpoint.


- **La performance del endpoint no debe degradarse**: cualquier ajuste en la query o en la fórmula debe ejecutarse dentro de los tiempos actuales de respuesta.
