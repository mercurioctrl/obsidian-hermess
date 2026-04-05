---
jira_key: "EXP-369"
aliases: ["EXP-369"]
summary: "API - Refactor - Agrear filtro tipo de pedido"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-11 13:12"
updated: "2023-10-11 15:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-369"
---

# EXP-369: API - Refactor - Agrear filtro tipo de pedido

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-11 13:12 |
| Actualizado | 2023-10-11 15:53 |
| Etiquetas | ninguna |
| Jira | [EXP-369](https://bluinc.atlassian.net/browse/EXP-369) |

## Relaciones

- **Padre:** [[EXP-12 - Feat - Listar pedidos para envio|EXP-12]] Feat - Listar pedidos para envio
- **is blocked by:** [[EXP-371 - API - Repository - Tipos de orden|EXP-371]] API - Repository - Tipos de orden
- **blocks:** [[EXP-370 - APP - Refactor - Agregar filtro y columna tipo de pedido|EXP-370]] APP - Refactor - Agregar filtro y columna tipo de pedido

## Descripcion

Agregaremos a 

```
GET {API_URL}/v1/shipments
```

La columna

`orderTypeId y orderTypeDescription`

Así como el filtro 

```
GET {API_URL}/v1/shipments?orderTypeId=1
```

Parecido a lo que se realizo en [link](https://lioteam.atlassian.net/browse/PED-137) 

 APLICA TANTO A RETIROS COMO ENVIOS
