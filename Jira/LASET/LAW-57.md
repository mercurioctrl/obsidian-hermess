---
jira_key: "LAW-57"
summary: "API - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockDispatch"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-31 07:57"
updated: "2026-04-01 10:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-57"
---

# LAW-57: API - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockDispatch

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-31 07:57 |
| Actualizado | 2026-04-01 10:33 |
| Etiquetas | ninguna |
| Jira | [LAW-57](https://bluinc.atlassian.net/browse/LAW-57) |

## Descripción

Cuando el usuario tiene el permiso `[NB_WEB].[dbo].[permisos_agente].expUnlockDispatch`

Al realizar 

```
PATCH {API_URL}/v1/orders/{pedido}/dispatch
```

Actualmente solicita autorización; si tiene `expUnlockDispatch=true`, despacha directamente.

[attachment]
Adicionalmente agregaremos el permiso al objeto `user` para que el front sepa como interpretar el boton
