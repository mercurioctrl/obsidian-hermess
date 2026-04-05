---
jira_key: "EXP-124"
aliases: ["EXP-124"]
summary: "API - Feat - Ver detalle para acreditar"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-22 09:39"
updated: "2022-12-22 11:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-124"
---

# EXP-124: API - Feat - Ver detalle para acreditar

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-22 09:39 |
| Actualizado | 2022-12-22 11:38 |
| Etiquetas | ninguna |
| Jira | [EXP-124](https://bluinc.atlassian.net/browse/EXP-124) |

## Relaciones

- **Padre:** [[EXP-119]] Feat - Acreditar un pedido parcial o totalmente
- **blocks:** [[EXP-123]] APP - Feat - Ver detalle para acreditar

## Descripcion

Este recurso esta basado en la serie que son similares a toda la serie [link](https://lioteam.atlassian.net/browse/EXP-68) ya que solo agregaremos la informacion necesaria para realizar el credito:

- Cantidad acreditada del mismo producto para el mismo pedido


- Precio del producto para ese pedido


- Iva del producto



En este sentido puede hacerse un refactor o bien un recurso nuevo

```
GET {API_URL}/v1/refund/{pedido}
```
