---
jira_key: "POS-291"
aliases: ["POS-291"]
summary: "API - Refactor - en logica al realizar nota de credito según sucursal asignada al pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-04-10 14:03"
updated: "2024-07-07 22:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-291"
---

# POS-291: API - Refactor - en logica al realizar nota de credito según sucursal asignada al pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-04-10 14:03 |
| Actualizado | 2024-07-07 22:10 |
| Etiquetas | ninguna |
| Jira | [POS-291](https://bluinc.atlassian.net/browse/POS-291) |

## Relaciones

- **Padre:** [[POS-123 - MS - Servicio de emision de comprobantes|POS-123]] MS - Servicio de emision de comprobantes
- **is blocked by:** [[POS-297 - API - Créditos pendientes - Error al acreditar|POS-297]] API - Créditos pendientes - Error al acreditar

## Descripcion

El el caso de que se intente realizar una nota de crédito en Postventa y este pertenezca a suc 10, no deberia realizar la petición de generar voucher a la afip. Si no internamente generar la acreditación a la cuenta del cliente.

siendo el recurso capaz de identificar si es Suc 10 o no.
