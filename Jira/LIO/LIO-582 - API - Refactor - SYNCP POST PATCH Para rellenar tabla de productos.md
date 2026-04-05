---
jira_key: "LIO-582"
aliases: ["LIO-582"]
summary: "API - Refactor - SYNCP POST / PATCH Para rellenar tabla de productos"
status: "Ready for QA"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-25 13:09"
updated: "2026-03-30 16:43"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/LIO-582"
---

# LIO-582: API - Refactor - SYNCP POST / PATCH Para rellenar tabla de productos

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-25 13:09 |
| Actualizado | 2026-03-30 16:43 |
| Etiquetas | esperandoDependencia |
| Jira | [LIO-582](https://bluinc.atlassian.net/browse/LIO-582) |

## Relaciones

- **Padre:** [[LIO-2 - Variedad y Calidad de ProductosCatalogos|LIO-2]] Variedad y Calidad de Productos/Catalogos
- **is cloned by:** [[LIO-589 - API - Review - SYNCP POST PATCH Para rellenar tabla de productos - Error SQL|LIO-589]] API - Review - SYNCP POST / PATCH Para rellenar tabla de productos - Error SQL Server 

## Descripcion

Segun lo conversado, buscaremos la forma de actualizar el catalogo teniendo en cuenta el cambio de nombre por parte del vendedor.

Es decir que para un item donde todos tienen el mismo titulo en `[CS].[dbo].[productos].titulo` menos 1 o mas, generaremos una fila por cada titulo diferente, con el mismo id interno, pero su propio id de lo, precio, reseller y demas

```
POST {{API_URL}}/v4/syncUp/items
```

```
PATCH {{API_URL}}/v4/syncUp/items
```
