---
jira_key: "LAW-59"
summary: "API - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockHand"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-31 08:07"
updated: "2026-04-01 10:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-59"
---

# LAW-59: API - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockHand

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-31 08:07 |
| Actualizado | 2026-04-01 10:34 |
| Etiquetas | ninguna |
| Jira | [LAW-59](https://bluinc.atlassian.net/browse/LAW-59) |

## Descripción

Cuando el usuario tiene el permiso `[NB_WEB].[dbo].[permisos_agente].expUnlockHand`

Al realizar 

```
PATCH {API_URL}/v1/orders/{pedido}/dispatch
```

Actualmente solicita autorización; si tiene `expUnlockHand=true`, entrega directamente.

Adicionalmente agregaremos el permiso al objeto `user` para que el front sepa como interpretar el boton

[attachment]
