---
jira_key: "INV-149"
aliases: ["INV-149"]
summary: "API - Refactor - Se debe poder buscar por match directo del sku"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-09 08:47"
updated: "2024-10-10 10:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-149"
---

# INV-149: API - Refactor - Se debe poder buscar por match directo del sku

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-09 08:47 |
| Actualizado | 2024-10-10 10:16 |
| Etiquetas | ninguna |
| Jira | [INV-149](https://bluinc.atlassian.net/browse/INV-149) |

## Relaciones

- **Padre:** [[INV-27]] Productos

## Descripcion

```
GET {api_url}/items?search=DUAL-RTX3050-O6G
```

Haremos un refactor para que en el parametro search no solo pueda buscar coincidencias en los titulos del producto sino tambien en los sku directamente. Esto funcionaria “matcheando” directamente es decir que solo si lo recibo completo y  sin diferencias traigo un resultado solo

```
 [NewBytes_DBF].[dbo].[articulo].ID_PRODUCTO
```
