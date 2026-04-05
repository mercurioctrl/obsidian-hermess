---
jira_key: "NBWEB-168"
summary: "APP - Carrito - Agregar ítem al carrito"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-05-05 08:53"
updated: "2022-06-26 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-168"
---

# NBWEB-168: APP - Carrito - Agregar ítem al carrito

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-05 08:53 |
| Actualizado | 2022-06-26 21:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-168](https://bluinc.atlassian.net/browse/NBWEB-168) |

## Descripción

```
POST /v1/carrito/item
```

Request

```
[{
"productId":86,
"amount":14,
"type":0
}]
```

[attachment]
