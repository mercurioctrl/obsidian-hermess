---
jira_key: "COB-49"
aliases: ["COB-49"]
summary: "API - Feat - Filtrar comprobantes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-09 15:14"
updated: "2022-10-27 08:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-49"
---

# COB-49: API - Feat - Filtrar comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-09 15:14 |
| Actualizado | 2022-10-27 08:14 |
| Etiquetas | ninguna |
| Jira | [COB-49](https://bluinc.atlassian.net/browse/COB-49) |

## Relaciones

- **Padre:** [[COB-43 - API - Feat - Listar comprobantes de pago|COB-43]] API - Feat - Listar comprobantes de pago
- **blocks:** [[COB-51 - APP - Feat - Listar comprobantes de pago|COB-51]] APP - Feat - Listar comprobantes de pago

## Descripcion

```
GET {{API_URL}}/v1/vouchers/{terminos de busqueda}?between=01-01-202_101-01-2022&currency=pesos&voucherTypeTax=A&voucherTypeId=2
```

Los términos de búsqueda pueden incluir

- Pedido


- businessName


- voucherTypeTax


- currency


- voucherNumber


- clientName


- clientId


- voucherTypeId



Tener en cuenta que puedo filtrar, sin necesariamente hacer match, en este estilo:
