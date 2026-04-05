---
jira_key: "POS-244"
aliases: ["POS-244"]
summary: "API - Feat - Enviar items al proveedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-15 13:06"
updated: "2023-04-11 10:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-244"
---

# POS-244: API - Feat - Enviar items al proveedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-15 13:06 |
| Actualizado | 2023-04-11 10:26 |
| Etiquetas | ninguna |
| Jira | [POS-244](https://bluinc.atlassian.net/browse/POS-244) |

## Relaciones

- **Padre:** [[POS-235 - Postventa Proveedores Recepcion|POS-235]] Postventa Proveedores Recepcion

## Descripcion

Crearemos un recurso para poder enviarle la mercadería a los proveedores

```
POST {API_URL}/v1/sendToProvider
```

```
{
providerId: 4, // este es el proveedor a donde llega la mercaderia
comment: "Cualquier comentario",
incomeAfterSaleIds: [
 3433,34234,23467,765,3434,6565
],
shippingOnProvider: true
}
```



Para esto utilizaremos `[NEW_BYTES].[dbo].[ST_RMA_PROVEEDORES_CABECERA]` a la cual le agregaremos la columna `providerId` y `comment` como dos parámetros extra que agregaremos.

La descripción seguiremos manteniendo “Mercadería para envio a proveedores”.

Y luego, de los items seleccionados, completaremos `[NEW_BYTES].[dbo].[ST_RMA_PROVEEDORES_DETALLE]` con la informacion proveniente de `[NEW_BYTES].[dbo].[ST_RMADETALLE]` y `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`
