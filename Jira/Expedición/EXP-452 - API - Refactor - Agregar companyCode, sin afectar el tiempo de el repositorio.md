---
jira_key: "EXP-452"
aliases: ["EXP-452"]
summary: "API - Refactor - Agregar companyCode, sin afectar el tiempo de el repositorio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-30 06:42"
updated: "2024-10-09 22:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-452"
---

# EXP-452: API - Refactor - Agregar companyCode, sin afectar el tiempo de el repositorio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-30 06:42 |
| Actualizado | 2024-10-09 22:02 |
| Etiquetas | ninguna |
| Jira | [EXP-452](https://bluinc.atlassian.net/browse/EXP-452) |

## Relaciones

- **Padre:** [[EXP-14 - Feat - Listar pedidos para retiro|EXP-14]] Feat - Listar pedidos para retiro
- **has action item:** [[EXP-453 - APP - Refactor - Agregar logo de NBe cuando el companyCode es el de esa empresa|EXP-453]] APP - Refactor - Agregar logo de NBe cuando el companyCode es el de esa empresa

## Descripcion

```
GET {API_URL}/v1/pickUp
```

```
GET {API_URL}/v1/shipments
```

Agregaremos el parámetro `companyCode` con cuidado de no compromenter la performance del recurso
