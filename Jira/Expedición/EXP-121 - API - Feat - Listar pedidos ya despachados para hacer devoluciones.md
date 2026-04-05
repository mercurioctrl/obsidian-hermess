---
jira_key: "EXP-121"
aliases: ["EXP-121"]
summary: "API - Feat - Listar pedidos ya despachados para hacer devoluciones"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-22 09:15"
updated: "2023-01-27 12:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-121"
---

# EXP-121: API - Feat - Listar pedidos ya despachados para hacer devoluciones

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-22 09:15 |
| Actualizado | 2023-01-27 12:24 |
| Etiquetas | ninguna |
| Jira | [EXP-121](https://bluinc.atlassian.net/browse/EXP-121) |

## Relaciones

- **Padre:** [[EXP-117 - Feat - Listar pedidos despachados para hacer devoluciones|EXP-117]] Feat - Listar pedidos despachados para hacer devoluciones
- **blocks:** [[EXP-122 - APP - Feat - Listar pedidos para realizar devoluciones|EXP-122]] APP - Feat - Listar pedidos para realizar devoluciones

## Descripcion

Crearemos el recurso 

```
GET {API_URL}/v1/orders/
```

Que en principio sera al menos igual a [link](https://lioteam.atlassian.net/browse/EXP-55) , pero solo mostrara aquellos que ya fueron despachados (no aquellos que figuran en las otras dos pantallas) y tendrá filtros para

- Nombre y numero de cliente


- Numero de pedido / Numero de orden



La finalidad de este recurso, es buscar un pedido que ya fue despachado para poder acreditarlo parcialmente o totalmente
