---
jira_key: "EXP-85"
aliases: ["EXP-85"]
summary: "APP - Feat - Serializar salida de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-18 12:42"
updated: "2023-01-27 12:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-85"
---

# EXP-85: APP - Feat - Serializar salida de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-18 12:42 |
| Actualizado | 2023-01-27 12:01 |
| Etiquetas | ninguna |
| Jira | [EXP-85](https://bluinc.atlassian.net/browse/EXP-85) |

## Relaciones

- **Padre:** [[EXP-15 - Feat - Serializar salida|EXP-15]] Feat - Serializar salida
- **is blocked by:** [[EXP-66 - API - Feat - Serializar salida|EXP-66]] API - Feat - Serializar salida

## Descripcion

Al igual que en [link](https://lioteam.atlassian.net/browse/EXP-43) donde tomamos los seriales para la entrada, en este recurso haremos lo propio pero para la salida de mercaderia.

```
GET {API_URL}/v1/orders/{pedido}/serials/
```

Para esto utilizaremos [link](https://lioteam.atlassian.net/browse/EXP-66)
