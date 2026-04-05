---
jira_key: "LAW-52"
aliases: ["LAW-52"]
summary: "API - COB - Se debe agregar el companyCode al user, como en el resto de las apps (PED,INV...)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2026-03-11 18:05"
updated: "2026-03-25 14:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LAW-52"
---

# LAW-52: API - COB - Se debe agregar el companyCode al user, como en el resto de las apps (PED,INV...)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2026-03-11 18:05 |
| Actualizado | 2026-03-25 14:55 |
| Etiquetas | ninguna |
| Jira | [LAW-52](https://bluinc.atlassian.net/browse/LAW-52) |

## Relaciones

- **has action item:** [[LAW-53 - APP - COB - Se debe agregar el companyCode al user, como en el resto de las|LAW-53]] APP - COB - Se debe agregar el companyCode al user, como en el resto de las apps (PED,INV...)
- **is cloned by:** [[LAW-54 - API - COB - Review - Se debe agregar el companyCode al user - Parámetro|LAW-54]] API - COB - Review - Se debe agregar el companyCode al user -> Parámetro includeNull sin resultados

## Descripcion

- Ademas de agregar el companyCode al user, los recursos deben admitir el filtrado por companyCode

- [https://gamma.api.cashbox.lio.red/v1/boxBalance/Seba?itemsPerPage=15&currentPage=1](https://gamma.api.cashbox.lio.red/v1/boxBalance/Seba?itemsPerPage=15&currentPage=1)


- [https://gamma.api.cashbox.lio.red/v1/box/Seba?currentPage=1](https://gamma.api.cashbox.lio.red/v1/box/Seba?currentPage=1)


- [https://gamma.api.cashbox.lio.red/v1/tradableDispatchMethod](https://gamma.api.cashbox.lio.red/v1/tradableDispatchMethod)


- [https://gamma.api.cashbox.lio.red/v1/tradablePaymentMethod](https://gamma.api.cashbox.lio.red/v1/tradablePaymentMethod)


- [https://gamma.api.cashbox.lio.red/v1/paymentMethods](https://gamma.api.cashbox.lio.red/v1/paymentMethods)


- [https://gamma.api.cashbox.lio.red/v1/tradable?currentPage=1](https://gamma.api.cashbox.lio.red/v1/tradable?currentPage=1)


- [https://gamma.api.cashbox.lio.red/v1/pendingCashOut?currentPage=1&pending=true&agentId=12](https://gamma.api.cashbox.lio.red/v1/pendingCashOut?currentPage=1&pending=true&agentId=12)


- [https://gamma.api.cashbox.lio.red/v1/vouchers?currentPage=1](https://gamma.api.cashbox.lio.red/v1/vouchers?currentPage=1)


- [https://gamma.api.cashbox.lio.red/v1/passes?currentPage=1&status=abierto&destiny=Seba](https://gamma.api.cashbox.lio.red/v1/passes?currentPage=1&status=abierto&destiny=Seba) 




- Se debe agregar al obj user permisos para msotrar/ocultar pestañas: estos en NB deben tener los permisos porque actualmente ven todo pero los user de laset deben tenerlo deshabilitado

- Impuestos


-  cheques


- billetera LO


- `unlockedCompanyFilter`


- solicitudes 


- pases





Es importante tener en cuenta como en PED las tareas de [link](https://bluinc.atlassian.net/browse/LAW-44) 

por lo tanto includeNull debe ser para:
`paymentMethod`

`tradablePaymentMethod`

`tradableDispatchMethod`
