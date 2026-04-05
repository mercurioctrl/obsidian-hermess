---
jira_key: "LIO-575"
aliases: ["LIO-575"]
summary: "API - Fet - Agregar campo description (título) al PATCH de productos del inventario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-03-17 13:19"
updated: "2026-03-20 10:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-575"
---

# LIO-575: API - Fet - Agregar campo description (título) al PATCH de productos del inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-17 13:19 |
| Actualizado | 2026-03-20 10:12 |
| Etiquetas | ninguna |
| Jira | [LIO-575](https://bluinc.atlassian.net/browse/LIO-575) |

## Relaciones

- **Padre:** [[LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-576]] APP - Feat - Habilitar edición inline del título en la grilla del catálogo

## Descripcion

## Contexto

El endpoint `PATCH /v4/inventories/products/{productId}/list` ya soporta `active` e `instantFlash`. Se necesita agregar soporte para modificar el título del producto (`titulo` en `[CS].[dbo].[productos]`) via el campo `description`.

A diferencia de `active` e `instantFlash` (que insertan `0` o `1` directamente en el SQL), el título es texto libre, por lo que **no puede interpolarse** en el string de query — necesita ir como parámetro bind para evitar SQL injection.

Esto requiere un cambio de arquitectura en `ProductsRepository::updateById()`: pasar valores adicionales como array de parámetros.

## Validación

```
# Cambiar título
curl -X PATCH 'https://gamma.api4.libreopcion.com/v4/inventories/products/{productId}/list' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"description": "Nuevo título del producto"}'
​
# Título vacío → debe devolver 400
curl -X PATCH 'https://gamma.api4.libreopcion.com/v4/inventories/products/{productId}/list' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"description": ""}'
​
# Combinado con active
curl -X PATCH '...' -d '{"description": "Nuevo título", "active": true}'
```

## Criterios de aceptación

- `PATCH` con `{"description": "Nuevo título"}` actualiza `titulo` en DB


- Si `description` es string vacío o solo espacios, devuelve 400


- Si `description` supera 255 caracteres, devuelve 400


- El título va como parámetro bind (no interpolado) — verificable en los logs de query


- La respuesta incluye el producto con el `description` actualizado


- Se puede combinar con `active`, `instantFlash`, `price` y `utility` en el mismo request


- Un vendedor no puede modificar el título de un producto ajeno
