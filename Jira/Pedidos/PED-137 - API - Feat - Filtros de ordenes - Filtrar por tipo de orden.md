---
jira_key: "PED-137"
aliases: ["PED-137"]
summary: "API - Feat - Filtros de ordenes -> Filtrar por tipo de orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-10 09:26"
updated: "2023-10-10 14:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-137"
---

# PED-137: API - Feat - Filtros de ordenes -> Filtrar por tipo de orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-10 09:26 |
| Actualizado | 2023-10-10 14:23 |
| Etiquetas | ninguna |
| Jira | [PED-137](https://bluinc.atlassian.net/browse/PED-137) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-136]] APP - Feat - Filtros de ordenes -> Filtrar por tipo de orden

## Descripcion

Basándonos en [link](https://lioteam.atlassian.net/browse/PED-135) agregaremos el filtro para recibir por id

```
GET {API_URL}/v1/orders?orderTypeId=3
```
