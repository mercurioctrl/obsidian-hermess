---
jira_key: "LIO-519"
aliases: ["LIO-519"]
summary: "APP Mobile - Feat - Cambio de precio de un ítem determinado desde la vista de listado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-20 08:18"
updated: "2026-02-03 17:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-519"
---

# LIO-519: APP Mobile - Feat - Cambio de precio de un ítem determinado desde la vista de listado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-20 08:18 |
| Actualizado | 2026-02-03 17:52 |
| Etiquetas | ninguna |
| Jira | [LIO-519](https://bluinc.atlassian.net/browse/LIO-519) |

## Relaciones

- **Padre:** [[LIO-501]] Catálogo / Inventario de productos

## Descripcion

Se debe permitir la edición del precio directamente desde la lista de precios, sin necesidad de ingresar al detalle del ítem. Para ello se utilizará el nuevo recurso disponible en V4. En caso de utilizar un modal o caja de edición, el precio actual deberá mostrarse como placeholder para dar contexto al cambio.

El endpoint a utilizar es:

```
PUT {{API_URL}}/v4/inventories/products/{id}/list
```

Payload:

```
{
  "price": 4983297
}
```
