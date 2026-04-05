---
jira_key: "INV-30"
aliases: ["INV-30"]
summary: "API - Feat - Filtro para los que no tienen imangen"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-17 08:58"
updated: "2023-10-17 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-30"
---

# INV-30: API - Feat - Filtro para los que no tienen imangen

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-17 08:58 |
| Actualizado | 2023-10-17 10:31 |
| Etiquetas | ninguna |
| Jira | [INV-30](https://bluinc.atlassian.net/browse/INV-30) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **blocks:** [[INV-31 - APP - Feat- Agregar filtro tipo checbox para listar todos los que no tienen|INV-31]] APP - Feat- Agregar filtro tipo "checbox" para listar todos los que no tienen imagen

## Descripcion

Agregaremos un filtro para que nos permita saber los que no tienen imagen

```
GET {{API_URL}}/items?noImage=1
```
