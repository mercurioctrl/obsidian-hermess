---
jira_key: "LIO-571"
aliases: ["LIO-571"]
summary: "APP - Feat - Editar estado activo/inactivo de producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-10 12:29"
updated: "2026-04-01 12:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-571"
---

# LIO-571: APP - Feat - Editar estado activo/inactivo de producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-10 12:29 |
| Actualizado | 2026-04-01 12:49 |
| Etiquetas | ninguna |
| Jira | [LIO-571](https://bluinc.atlassian.net/browse/LIO-571) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **action item from:** [[LIO-569 - API - Feat - Editar estado activoinactivo de producto|LIO-569]] API - Feat - Editar estado activo/inactivo de producto
- **has action item:** [[LIO-590 - APP Mobile - Feat - Editar estado activoinactivo de producto|LIO-590]] APP Mobile - Feat - Editar estado activo/inactivo de producto

## Descripcion

Como vendedor, quiero poder activar o desactivar un producto directamente desde mi panel de inventario, para controlar qué productos están publicados sin tener que eliminarlos.

---

## Contexto

El backend ya soporta el campo `active` en el endpoint:

```
PATCH /v4/inventories/products/{productId}/list
Body: { "active": true | false }
```

La respuesta devuelve el producto actualizado con el campo `active` reflejando el nuevo estado. El backend actualiza `activo_vendedor` en `[CS].[dbo].[productos]`.

---

## Cambios requeridos en el frontend

Al hacer clic en el ojo de activo/inactivo, este debe ejecutar el cambio de visibilidad, el  recibir la respuesta si active:false, apaga el ojo a gris. Si es true, lo pone verde.

### Ubicación

[adjunto]
---

## Criterios de aceptación

- El toggle muestra el estado actual (`active`) al cargar el listado y el ojo esta gris o verde en consecuencia.


- Al hacer click, dispara `PATCH /v4/inventories/products/{id}/list` con `{ "active": true/false }`


- El cambio visual es inmediato si el request falla, se muestra toast de error


- La respuesta del PATCH actualiza `itemModified` con el objeto `product` devuelto por el backend


- El campo `active` en el GET del listado refleja el estado real guardado


- No resetea la paginación ni los filtros activos en la tabla



---

## Notas

- No requiere modal de confirmación; el cambio es liviano y reversible desde el mismo toggle.


- El diseño sigue exactamente el patrón del toggle `hide` ya existente en el componente (clase `.input-checkbox-2` con modificador `activo`).


- El store action ya existe; no hay que crear ni modificar `inventory/product.js`.
