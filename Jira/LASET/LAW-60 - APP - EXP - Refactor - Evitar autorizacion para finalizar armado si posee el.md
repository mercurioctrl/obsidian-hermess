---
jira_key: "LAW-60"
aliases: ["LAW-60"]
summary: "APP - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockHand"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-03-31 08:07"
updated: "2026-04-01 10:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-60"
---

# LAW-60: APP - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockHand

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-31 08:07 |
| Actualizado | 2026-04-01 10:38 |
| Etiquetas | ninguna |
| Jira | [LAW-60](https://bluinc.atlassian.net/browse/LAW-60) |

## Relaciones

- **Padre:** [[LAW-43]] Onboarding producción
- **action item from:** [[LAW-59]] API - EXP - Refactor - Evitar autorizacion para finalizar armado si posee el permiso expUnlockHand

## Descripcion

Una vez realizado el refactor [link](https://bluinc.atlassian.net/browse/LAW-59)  tendremos dentro del objeto `user` el parametro `expUnlockHand` que de ser `true`

Habilita al boton “Entregar” a disparar directamente el recurso dispatch sin pasar por el modal de para ingresar

```
PATCH {API_URL}/v1/orders/{pedido}/hand  
```

[adjunto]
