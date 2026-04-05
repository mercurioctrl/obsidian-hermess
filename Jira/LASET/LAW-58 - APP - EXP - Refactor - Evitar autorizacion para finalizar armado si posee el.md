---
jira_key: "LAW-58"
aliases: ["LAW-58"]
summary: "APP - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockDispatch"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-03-31 08:02"
updated: "2026-04-01 10:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-58"
---

# LAW-58: APP - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockDispatch

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-31 08:02 |
| Actualizado | 2026-04-01 10:57 |
| Etiquetas | ninguna |
| Jira | [LAW-58](https://bluinc.atlassian.net/browse/LAW-58) |

## Relaciones

- **Padre:** [[LAW-43 - Onboarding producción|LAW-43]] Onboarding producción

## Descripcion

Una vez realizado el refactor [link](https://bluinc.atlassian.net/browse/LAW-57)  tendremos dentro del objeto `user` el parametro `expUnlockDispatch` que de ser `true`

Habilita al boton “Finalizar Pedido” a disparar directamente el recurso dispatch sin pasar por el modal de para ingresar 

```
PATCH {API_URL}/v1/orders/{pedido}/dispatch  
```

[adjunto]
