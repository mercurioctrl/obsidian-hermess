---
jira_key: "EXP-419"
aliases: ["EXP-419"]
summary: "API - Refactor - Cambiar del orden de la grilla retiros (solo retiros, no envios)"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-10 12:28"
updated: "2024-07-11 03:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-419"
---

# EXP-419: API - Refactor - Cambiar del orden de la grilla retiros (solo retiros, no envios)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-10 12:28 |
| Actualizado | 2024-07-11 03:17 |
| Etiquetas | ninguna |
| Jira | [EXP-419](https://bluinc.atlassian.net/browse/EXP-419) |

## Relaciones

- **Padre:** [[EXP-14 - Feat - Listar pedidos para retiro|EXP-14]] Feat - Listar pedidos para retiro

## Descripcion

```
GET /v1/pickUp
```

Cambiaremos el orden para que quede de la siguiente forma

-  Pedidos Alertados (Segunda prioridad fecha como esta ahora)


-  Pedidos de NewBytes  (Segunda prioridad fecha como esta ahora)


-  Pedidos de Libre Opcion  (Segunda prioridad fecha como esta ahora)
