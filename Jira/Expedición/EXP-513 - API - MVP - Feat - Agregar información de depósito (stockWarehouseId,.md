---
jira_key: "EXP-513"
aliases: ["EXP-513"]
summary: "API - MVP - Feat - Agregar información de depósito (stockWarehouseId, stockWarehouseDescription, stockWarehouseCode) al recurso /v1/orders/{branch}-{order}"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-09 08:27"
updated: "2025-11-11 14:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-513"
---

# EXP-513: API - MVP - Feat - Agregar información de depósito (stockWarehouseId, stockWarehouseDescription, stockWarehouseCode) al recurso /v1/orders/{branch}-{order}

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-09 08:27 |
| Actualizado | 2025-11-11 14:02 |
| Etiquetas | ninguna |
| Jira | [EXP-513](https://bluinc.atlassian.net/browse/EXP-513) |

## Relaciones

- **Padre:** [[EXP-512]] Almacenes multiples
- **has action item:** [[EXP-515]] APP - MVP - Feat - Mostrar almacén cuando abrimos una orden para serializar 

## Descripcion

Actualmente, el recurso 

```
GET {API_URL}/v1/orders/{orderId}
```

devuelve el detalle de los ítems asociados a un pedido, incluyendo atributos del producto.
Para mejorar la trazabilidad del origen del stock, se debe agregar la información del depósito asociado a cada ítem.

Como en los otros casos, ahora es posible que vengan dos items del mismo id, pero para un almacén diferente

Adicionalmente agregaremos otro parámetro `WarehouseSensitive` en `[NewBytes_DBF].[dbo].[articulo]` con valor inicial `false`. El propósito es que cada item pueda ser sensible o no a la hora de serializar de que el serial debe estar en el almacén especifico que la orden pide o no.

### **Objetivo**

Incorporar los siguientes campos en la respuesta del recurso:

```
[
    {
        "title": "MEMORIA PATRIOT SIGNATURE LINE SODIMM DDR5 16GB 4800MT\/S PS001642",
        "id": 118933,
        "sku": "PSD516G480081S",
        "category": "MEMORIAS",
        "idCategory": 1,
        "idBrand": 36,
        "brand": "PATRIOT                                           ",
        "mainImage": "e45017f4a0a723f79d641664fc0f76e2.jpg",
        "notSerializable": 0,
        "incomingQuantity": 1,
        "serializedQuantity": 1,
        "fullSerialized": true,
        "acreditado": 0,
        "conIva": 39.971165,
        "ivaTax": 10.5,
        "sinIva": 36.173,
        "cotizacion": 1200,
        "iibbPerceptions": 0.9,
        "internalTax": 0,
        "stockWarehouseId": 2, <--
        "stockWarehouseDescription": "SAFcom", <--
        "stockWarehouseCode": "SAF", <--
        "WarehouseSensitive": false <--
    }
    ...
]
```

Estos valores deben corresponder `stockWarehouseId` para cada item, pudiendo darse el caso donde un mismo item, esta para dos depósitos distintos.

Un mismo 

- **stockWarehouseId** → `ID_ALMACEN`


- **stockWarehouseDescription** → `CDESCALM`


- **stockWarehouseCode** → `CCODALM`



Se crean índices si no existían, y **no** se degradan tiempos de respuesta del endpoint.

### **Criterios de aceptación** ✅

- El recurso `/v1/orders/{orderId}` debe incluir en cada ítem los campos:

- `stockWarehouseId`


- `stockWarehouseDescription`


- `stockWarehouseCode`




- Los valores deben provenir del mismo origen que en el repositorio de ítems (deben ser coherentes con `FP_Almacen`).


- La información debe ser coherente con la utilizada en otros recursos como `/v1/items` o `/v1/orders/{branch}-{order}` que ya realizamos en pedidos.


- No se modifican los nombres ni la estructura de los campos existentes.


- Se valida que, si el ítem no tiene depósito asignado, los tres valores se devuelvan como `null`.


- Si es necesario modificar estructuras de tablas para admitir la nueva clave única id_articulo + pedido + deposito se debe dejar la modificación en la historia


- Deben guardarse en la historia las ejecuciones sql necesarias
