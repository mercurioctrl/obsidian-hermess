---
jira_key: "PED-19"
summary: "API - Feat - Editar cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-08 08:20"
updated: "2024-10-05 08:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-19"
---

# PED-19: API - Feat - Editar cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-08 08:20 |
| Actualizado | 2024-10-05 08:45 |
| Etiquetas | ninguna |
| Jira | [PED-19](https://bluinc.atlassian.net/browse/PED-19) |

## Descripción

```
PATCH {API_URL}/v1/clients/{id cliente}
```

Se deben poder editar los siguientes parámetros para el cliente 

- clientName


- commercialName


- clientAddress


- cityCode


- postalCode


- phone1


- phone2


- taxId


- contactName


- agentCode


- discount


- email


- groupCode


- currencyDivision


- inactive


- website


- countryId


- cityId


- clientGroupId


- salespersonId


- paymentMethodId


- currencyId


- web


- rmaEmail


- specialOfferDiscount


- generalDiscount


- manualPrice


- profile


- companyCode


- excludePerception


- specialPrice


- clientLo


- specialPriceFromCost


- productecaId



Siempre y cuando estén presentes en el payload como lo hacemos habitualmente.

Es posible que en el futuro este recurso pueda recibir mas parámetros para editar y que incluso algunos no estén directamente en la tabla clientes.
