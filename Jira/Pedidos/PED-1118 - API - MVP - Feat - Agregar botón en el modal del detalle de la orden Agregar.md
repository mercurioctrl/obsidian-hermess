---
jira_key: "PED-1118"
aliases: ["PED-1118"]
summary: "API  - MVP - Feat - Agregar botón en el modal del detalle de la orden \"Agregar etiqueta\" . Se abrirá otro modal con el nombre del producto y al lado un campo etiqueta por ejemplo :'Origen China' para poder incluir esto en la facturación"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-09-29 09:53"
updated: "2025-11-10 09:54"
labels: ["MVPLaset"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1118"
---

# PED-1118: API  - MVP - Feat - Agregar botón en el modal del detalle de la orden "Agregar etiqueta" . Se abrirá otro modal con el nombre del producto y al lado un campo etiqueta por ejemplo :'Origen China' para poder incluir esto en la facturación

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-09-29 09:53 |
| Actualizado | 2025-11-10 09:54 |
| Etiquetas | MVPLaset |
| Jira | [PED-1118](https://bluinc.atlassian.net/browse/PED-1118) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **has action item:** [[PED-1117 - APP - MVP - Feat - Agregar botón en el modal del detalle de la orden Agregar|PED-1117]] APP  - MVP - Feat - Agregar botón en el modal del detalle de la orden "Agregar etiqueta" . Se abrirá otro modal con el nombre del producto y al lado un campo etiqueta por ejemplo :'Origen China' para poder incluir esto en la facturación

## Descripcion

Se debe agregar un **parámetro de etiquetado especial** para los ítems.
Este etiquetado servirá para mostrar información adicional o distintiva sobre un producto puntual, visible **solo en contextos específicos**, como:

- El **detalle de una orden**


- El **comprobante tipo factura**



Cada etiqueta estará **directamente asociada a un ítem existente** de la tabla `[NewBytes_DBF].[dbo].[articulo]`.

### **Diseño técnico**

#### **1. Nueva tabla**

Crear la tabla `[NewBytes_DBF].[dbo].[articulo_label]` con la siguiente estructura:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `id` | INT IDENTITY(1,1) PRIMARY KEY | Identificador único de la etiqueta |
| `id_articulo` | INT NOT NULL | Relación con `[NewBytes_DBF].[dbo].[articulo].id_articulo` |
| `description` | VARCHAR(100) | Texto descriptivo de la etiqueta |
| `showInvocher` | BIT DEFAULT 0 | Indica si se muestra en comprobantes tipo factura |
| `showInOrder` | BIT DEFAULT 0 | Indica si se muestra en el detalle de la orden |
| `created_at` | DATETIME DEFAULT GETDATE() | Fecha de creación |
| `updated_at` | DATETIME DEFAULT GETDATE() | Fecha de última actualización |

Agregar los indices en la tabla correspondientes para su optimo funcionamiento

 **Relación:**
`FOREIGN KEY (id_articulo) REFERENCES [NewBytes_DBF].[dbo].[articulo](id_articulo)`



**Obtiene la etiqueta asociada a un ítem determinado**

```
POST {API_URL}/v1/items/labels
```

Payload

```
{
  "itemIds": [4532, 9981, 7777]
}
```

Devuelve

```
{
  "success": true,
  "message": "Se recuperaron las etiquetas solicitadas",
  "data": [
    {
      "id": 12,
      "itemId": 4532,
      "description": "Made In China",
      "showInvocher": true,
      "showInOrder": true
    },
    {
      "id": 44,
      "itemId": 9981,
      "description": "Caja dañada",
      "showInvocher": false,
      "showInOrder": true
    },
    {
      "id": 2,
      "itemId": 7777,
      "description": null,
      "showInvocher": null,
      "showInOrder": null,
    }
  ]
}
```

```
PATCH {API_URL}/v1/items/labels
```

Payload

```
{
  "updates": [
    {
      "itemId": 4532,
      "description": "Producto sin caja original",
      "showInvocher": false,
      "showInOrder": true
    },
    {
      "itemId": 9981,
      "description": "Equipo demo de showroom",
      "showInvocher": true,
      "showInOrder": false
    },
    {
      "itemId": 7777,
      "description": "Reacondicionado por servicio técnico interno",
      "showInvocher": true,
      "showInOrder": true
    }
  ]
}
```

Devuelve

```
{
  "success": true,
  "message": "Se procesaron las etiquetas para los productos",
  "data": [
    {
      "itemId": 4532,
      "status": "updated",
      "label": {
        "id": 12,
        "description": "Producto sin caja original",
        "showInvocher": false,
        "showInOrder": true
      }
    },
    {
      "itemId": 9981,
      "status": "created",
      "label": {
        "id": 91,
        "description": "Equipo demo de showroom",
        "showInvocher": true,
        "showInOrder": false
      }
    },
    {
      "itemId": 7777,
      "status": "error",
      "errorCode": "ITEM_NOT_FOUND",
      "message": "El item 7777 no existe en articulo"
    }
  ]
}

```

### **Criterios de aceptación**

- El endpoint `GET` debe devolver la etiqueta correspondiente al `itemId` si existe, o `404` si no está definida.


- El endpoint `PATCH` debe permitir crear la etiqueta si no existe o actualizarla si ya está creada.


- Los campos `showInvocher` y `showInOrder` deben ser opcionales en la actualización (mantener valores actuales si no se envían).


- La tabla `articulo_label` debe estar correctamente relacionada con `articulo` mediante `id_articulo`.


- El backend debe validar que el `itemId` exista en `articulo` antes de crear la etiqueta.


- Toda actualización debe registrar `updated_at` con la fecha/hora actual.
