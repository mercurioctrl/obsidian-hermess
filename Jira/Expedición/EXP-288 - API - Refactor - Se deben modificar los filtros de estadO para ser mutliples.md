---
jira_key: "EXP-288"
aliases: ["EXP-288"]
summary: "API - Refactor - Se deben modificar los filtros de estadO para ser mutliples"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-18 08:45"
updated: "2023-06-08 06:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-288"
---

# EXP-288: API - Refactor - Se deben modificar los filtros de estadO para ser mutliples

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-18 08:45 |
| Actualizado | 2023-06-08 06:16 |
| Etiquetas | ninguna |
| Jira | [EXP-288](https://bluinc.atlassian.net/browse/EXP-288) |

## Relaciones

- **Padre:** [[EXP-10 - Feat - Listar pedidos (despachos) proveedores|EXP-10]] Feat - Listar pedidos (despachos) proveedores
- **is blocked by:** [[EXP-287 - APP - Refactor - Se deben modificar los filtros de estado para ser mutliples|EXP-287]] APP - Refactor - Se deben modificar los filtros de estado para ser mutliples

## Descripcion

Refactorizaremos el recurso

```
GET {{API_URL}}/v1/pickUp?itemsPerPage=15&currentPage=1
```

para poder enviar en lugar de un solo valor del atributo `status` de la siguiente manera: `status=1,4,3`

Se desea obtener la siguiente feature de front

[adjunto]
para convertir en 

[adjunto]
