---
jira_key: LAW-70
status: REVISIÓN
assignee: Emanuel Jesus Ferreyra
assignee_email: null
reporter: Marbe Moreno
priority: Medium
issuetype: Subtarea
project: LAW
updated: "2026-05-19T15:25:38.142-0300"
created: "2026-05-15T16:48:49.430-0300"
url: "https://bluinc.atlassian.net/browse/LAW-70"
tags: [jira, LAW, revisión]
---

# LAW-70 · API - COB - Refactor -  Agregar el includeNull al recurso de bank-accounts como se hizo con PED

[LAW-70 en Jira](https://bluinc.atlassian.net/browse/LAW-70)

## Descripción

Sabiendo que en el user puede venir algo como   
`includeNull: `0  
  
es necesario incluir este campo en   
`'https://gamma.api.cashbox.lio.red/v1/bank-accounts?currentPage=1&itemsPerPage=100&available=true&includeNull=0'`

para msotrar correctamente los bancos en el selector  
de cobros

## Comentarios (1)

### @Emanuel Jesus Ferreyra — 2026-05-15 17:35:07

:check_mark:  https://github.com/New-Bytes/api-rest-cobros/pull/873

## Labels
esperandoDependencia

---
_Sincronizado por jira-sidecar el 2026-06-07 22:30:03 UTC._
