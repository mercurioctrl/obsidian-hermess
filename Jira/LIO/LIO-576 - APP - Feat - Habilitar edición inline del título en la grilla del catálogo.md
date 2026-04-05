---
jira_key: "LIO-576"
aliases: ["LIO-576"]
summary: "APP - Feat - Habilitar edición inline del título en la grilla del catálogo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-17 13:22"
updated: "2026-03-20 10:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-576"
---

# LIO-576: APP - Feat - Habilitar edición inline del título en la grilla del catálogo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-17 13:22 |
| Actualizado | 2026-03-20 10:12 |
| Etiquetas | ninguna |
| Jira | [LIO-576](https://bluinc.atlassian.net/browse/LIO-576) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **action item from:** [[LIO-575]] API - Fet - Agregar campo description (título) al PATCH de productos del inventario

## Descripcion

# 

## Contexto

En la grilla del catálogo (`ProductoTienda.vue`), la celda del título ya tiene un `<input>` con `@blur="actualizarDatos('description')"`, pero está desactivado con `v-if="false"`. Solo muestra el texto plano.

Con el backend listo para recibir `PATCH /v4/inventories/products/{id}/list` con `{"description": "..."}`, hay que reactivar el input para que el vendedor pueda editar el título directamente desde la grilla.

## Comportamiento esperado

- El título es un `<input type="text">` editable directamente en la grilla


- Al hacer foco, o con un lapiz (`@focus`) se selecciona todo el texto para facilitar el reemplazo


- Al perder foco (`@blur`) se dispara el PATCH con `{"description": "nuevo título"}`


- Si el servidor responde OK, `itemModified` se actualiza desde `response.product` y aparece toast de éxito


- Si hay error (ej: título vacío), aparece toast de error y el campo queda con el valor previo



## Validación

- Abrir el catálogo en gamma


- Hacer click en el título de cualquier producto → debe volverse un input editable


- Cambiar el texto y hacer Tab o click afuera → debe guardar y mostrar "Campo actualizado exitosamente."


- Verificar en DevTools → Network → el PATCH lleva `{"description": "nuevo título"}` (string, no NaN)


- Recargar la página → el nuevo título debe persistir


- Borrar todo el texto y hacer blur → debe mostrar error del servidor (400 título vacío)



## Criterios de aceptación

- El título se puede editar directamente en la grilla (inline)


- Al hacer foco se selecciona todo el texto


- Al perder foco se guarda via PATCH


- El valor enviado al server es string, no número


- El título en la celda se actualiza desde la respuesta del servidor


- Se muestra toast de éxito o error según corresponda


- Si el server rechaza (vacío, muy largo), el campo no queda en blanco — el valor previo se restaura desde `this.item.description` (mismo patrón que `price`)
