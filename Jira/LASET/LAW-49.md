---
jira_key: "LAW-49"
summary: "APP - PED - Feat- Filtro companyCode + includeNull en PaymentMethods"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-03-10 09:42"
updated: "2026-03-13 19:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-49"
---

# LAW-49: APP - PED - Feat- Filtro companyCode + includeNull en PaymentMethods

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-10 09:42 |
| Actualizado | 2026-03-13 19:05 |
| Etiquetas | ninguna |
| Jira | [LAW-49](https://bluinc.atlassian.net/browse/LAW-49) |

## Descripción

# 

## Descripción

Agregar soporte del parámetro `includeNull` en los llamados al endpoint `/paymentMethods`, tanto en la action del store como en los llamados directos por axios.

> **Prerequisito:** El permiso `includeNull` debe venir en el objeto `user` (ver instrucciones en `backend-permiso-includeNull-permisos-agente.md`). El getter asumido es `store.getters['auth/user']` — verificar el nombre exacto del getter en el store de autenticación del proyecto.
