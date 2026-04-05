---
jira_key: "LIO-573"
aliases: ["LIO-573"]
summary: "APP - Feat - Activar toggle de InstantFlash en la grilla del catálogo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-13 14:17"
updated: "2026-03-17 16:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-573"
---

# LIO-573: APP - Feat - Activar toggle de InstantFlash en la grilla del catálogo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-13 14:17 |
| Actualizado | 2026-03-17 16:18 |
| Etiquetas | ninguna |
| Jira | [LIO-573](https://bluinc.atlassian.net/browse/LIO-573) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **action item from:** [[LIO-568 - API - Feat - Agregar campo instantFlash al PATCH de productos del inventario|LIO-568]] API - Feat - Agregar campo instantFlash al PATCH de productos del inventario

## Descripcion

## Contexto

En la grilla del catálogo (`ProductoTienda.vue`) ya existe la celda del rayito de InstantFlash, pero está completamente desactivada (`v-if="false"` en el input). El ícono ya se renderiza con las clases `.activo` / `.inactivo` que aplican color o grayscale según `itemModified.instantFlash`, pero no es clickeable.

Con el backend listo para recibir `PATCH /v4/inventories/products/{id}/list` con `{"instantFlash": true/false}`, hay que reactivar la celda para que el vendedor pueda toggelear el flash desde la grilla.

## Qué hay que hacer

Hacer el rayito clickeable: al hacer click debe llamar al PATCH, actualizar el estado local y reflejar visualmente el cambio (color = activo, gris = inactivo).

## Comportamiento esperado

| Estado actual | Click | Resultado visual | Lo que va a DB |
| --- | --- | --- | --- |
| `instantFlash: false` | → | Rayito en color (`$InstantFlashSolid`) | `instant_flash_vendedor = 1` |
| `instantFlash: true` | → | Rayito en gris (grayscale 0.5) | `instant_flash_vendedor = 0` |

El estado se actualiza desde la respuesta del servidor (`response.product`), no optimistamente, para evitar desincronías.

## Validación

- Abrir el catálogo en gamma con un producto que tenga `instantFlash: false`


- Hacer click en el rayito → debe cambiar a color y mostrarse toast "Flash actualizado."


- Recargar la página → el rayito debe mantener el estado


- Repetir en sentido inverso (desactivar)


- Verificar en DevTools → Network → el PATCH lleva `{"instantFlash": true}` (boolean, no número)



## Criterios de aceptación

- Click en el rayito activa/desactiva el flash (toggle)


- El rayito en color indica `instantFlash: true`; en gris indica `instantFlash: false`


- El PATCH se llama con `instantFlash` como booleano (`true`/`false`, no `1`/`0`)


- El estado se refleja desde la respuesta del server, no localmente antes de la llamada


- Se muestra toast de éxito o error según corresponda


- El rayito es clickeable visualmente (`cursor: pointer`)
