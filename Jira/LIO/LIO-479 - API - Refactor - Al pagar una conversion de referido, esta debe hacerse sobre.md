---
jira_key: "LIO-479"
aliases: ["LIO-479"]
summary: "API - Refactor - Al pagar una conversion de referido, esta debe hacerse sobre el precio final (creo que se esta haciendo sobre el precio sin IVA)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-26 08:38"
updated: "2025-12-12 10:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-479"
---

# LIO-479: API - Refactor - Al pagar una conversion de referido, esta debe hacerse sobre el precio final (creo que se esta haciendo sobre el precio sin IVA)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-26 08:38 |
| Actualizado | 2025-12-12 10:54 |
| Etiquetas | ninguna |
| Jira | [LIO-479](https://bluinc.atlassian.net/browse/LIO-479) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos
- **has action item:** [[SNB-3525 - Queja referido lucas|SNB-3525]] Queja referido "lucas"

## Descripcion

```
POST {{API_URL}}/v4/syncUp/referralConversions
```

Por lo que estuve viendo, siempre me da un poco menos del 1% la comisión y creo que viene por el lado de que se hace sobre el precio sin iva.
