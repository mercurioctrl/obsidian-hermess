---
jira_key: LAW-69
status: REVISIÓN
assignee: Emanuel Jesus Ferreyra
assignee_email: null
reporter: Marbe Moreno
priority: Medium
issuetype: Subtarea
project: LAW
updated: "2026-05-20T09:52:07.629-0300"
created: "2026-05-14T13:24:46.125-0300"
url: "https://bluinc.atlassian.net/browse/LAW-69"
tags: [jira, LAW, revisión]
---

# LAW-69 · API - PED- Refactor - Agregar includeNull al recurso de los bancos como se hizo en paymentMethods

[LAW-69 en Jira](https://bluinc.atlassian.net/browse/LAW-69)

## Descripción

[https://api.orders.lio.red/v1/banks?currentPage=1&itemsPerPage=100&positiveBalance=1&companyCode=11&available=1](https://api.orders.lio.red/v1/banks?currentPage=1&itemsPerPage=100&positiveBalance=1&companyCode=11&available=1)  
  
agregar `includeNull`



Se refactorizó el endpoint GET /banks para alinear  con el comportamiento ya existente.

  Cambio: Cuando se filtra por companyCode, el parámetro includeNull controla si se incluyen registros con companyCode IS NULL.



**Origen del valor (por precedencia):**

1. Query param ?includeNull=true/false — si se envía explícitamente, tiene prioridad.
2. Campo includeNull del usuario autenticado (JWT) — se usa como fallback.



**  Impacto en la consulta:**

- includeNull=true → WHERE companyCode = X OR companyCode IS NULL
- includeNull=false → WHERE companyCode = X

---
_Sincronizado por jira-sidecar el 2026-06-07 22:24:52 UTC._
