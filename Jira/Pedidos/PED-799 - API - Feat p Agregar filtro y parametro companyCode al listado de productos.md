---
jira_key: "PED-799"
aliases: ["PED-799"]
summary: "API - Feat p Agregar filtro y parametro companyCode al listado de productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-19 08:58"
updated: "2024-08-25 23:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-799"
---

# PED-799: API - Feat p Agregar filtro y parametro companyCode al listado de productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-19 08:58 |
| Actualizado | 2024-08-25 23:57 |
| Etiquetas | ninguna |
| Jira | [PED-799](https://bluinc.atlassian.net/browse/PED-799) |

## Relaciones

- **Padre:** [[PED-65 - Listado de productos|PED-65]] Listado de productos

## Descripcion

Se filtra según el parámetro `[NewBytes_DBF].[dbo].[articulos].ccodemp`

```
GET {api_url}/v1/items?companyCode={companyCode}
```
