---
jira_key: "LIO-568"
aliases: ["LIO-568"]
summary: "API - Feat - Agregar campo instantFlash al PATCH de productos del inventario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-09 08:34"
updated: "2026-03-16 15:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-568"
---

# LIO-568: API - Feat - Agregar campo instantFlash al PATCH de productos del inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-09 08:34 |
| Actualizado | 2026-03-16 15:55 |
| Etiquetas | ninguna |
| Jira | [LIO-568](https://bluinc.atlassian.net/browse/LIO-568) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-573 - APP - Feat - Activar toggle de InstantFlash en la grilla del catálogo|LIO-573]] APP - Feat - Activar toggle de InstantFlash en la grilla del catálogo

## Descripcion

## Contexto

El endpoint `PATCH /v4/inventories/products/{productId}/list` ya permite activar/desactivar un producto via `{"active": false}`, actualizando la columna `activo_vendedor` en `[CS].[dbo].[productos]`.

Se necesita el mismo comportamiento para el campo `instantFlash` (columna `instant_flash_vendedor`), para que el vendedor pueda activar o desactivar el modo flash de sus productos desde el catálogo.

## Qué hay que hacer

Agregar soporte para el parámetro `instantFlash` (bool) en `ProductsService::parametrizeUpdate()`, de modo que al hacer:

```
PATCH /v4/inventories/products/{productId}/list
{"instantFlash": true}
```

se actualice `instant_flash_vendedor` en la tabla `[CS].[dbo].[productos]`.

## Validación

```
# Activar flash
curl -X PATCH 'https://gamma.api4.libreopcion.com/v4/inventories/products/{productId}/list' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"instantFlash": true}'
​
# Desactivar flash
curl -X PATCH 'https://gamma.api4.libreopcion.com/v4/inventories/products/{productId}/list' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"instantFlash": false}'
```

Verificar que la respuesta incluye `"instantFlash": true/false` en el objeto `product`.

Se puede combinar con `active` en el mismo request:

```
{"active": false, "instantFlash": true}
```

## Criterios de aceptación

- `PATCH` con `{"instantFlash": true}` setea `instant_flash_vendedor = 1` en DB


- `PATCH` con `{"instantFlash": false}` setea `instant_flash_vendedor = 0` en DB


- Si `instantFlash` no es bool, devuelve 400 con mensaje de error claro


- La respuesta incluye el producto actualizado con el campo `instantFlash` correcto


- Un vendedor no puede modificar el `instantFlash` de un producto de otro vendedor (garantizado por el `WHERE vendedorID = ?` existente)


- Se puede actualizar `active` e `instantFlash` en el mismo request sin conflicto
