---
jira_key: "LIO-184"
aliases: ["LIO-184"]
summary: "API - CMS - Refactor - Sección categorías en el CMS -> Adición de categoría hija"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-01-27 17:03"
updated: "2025-01-28 23:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-184"
---

# LIO-184: API - CMS - Refactor - Sección categorías en el CMS -> Adición de categoría hija

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-01-27 17:03 |
| Actualizado | 2025-01-28 23:23 |
| Etiquetas | ninguna |
| Jira | [LIO-184](https://bluinc.atlassian.net/browse/LIO-184) |

## Relaciones

- **action item from:** [[LIO-176 - API - CMS - Feat - Repositorio de Lectura Escritura para categorias en el CMS|LIO-176]] API - CMS - Feat - Repositorio de Lectura / Escritura para categorias en el CMS

## Descripcion

Tomando como referencia la siguiente historia [https://lioteam.atlassian.net/browse/LIO-183](https://lioteam.atlassian.net/browse/LIO-183) , procederemos con la refactorización necesaria para que, al crear una categoría, se pueda aceptar el parámetro `parentCategory=null`. Esto permitirá indicar que se trata de una categoría hija que aún no tiene asignada una categoría padre.

Es importante tener en cuenta que, además de la modificación en el recurso POST, el recurso GET también se verá afectado. Se deberá ajustar para que, en caso de ser necesario, devuelva `null` en el campo `parentCategory`.

```
POST/GET {{API_URL}}/v1/categories
```
