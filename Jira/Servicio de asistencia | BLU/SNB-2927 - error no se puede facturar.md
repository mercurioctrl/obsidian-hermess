---
jira_key: "SNB-2927"
aliases: ["SNB-2927"]
summary: "error no se puede facturar"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Pedidos Jira"
created: "2025-03-28 17:13"
updated: "2025-04-16 09:00"
labels: ["Facturación"]
jira_url: "https://bluinc.atlassian.net/browse/SNB-2927"
---

# SNB-2927: error no se puede facturar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Pedidos Jira |
| Creado | 2025-03-28 17:13 |
| Actualizado | 2025-04-16 09:00 |
| Etiquetas | Facturación |
| Jira | [SNB-2927](https://bluinc.atlassian.net/browse/SNB-2927) |

## Relaciones

*Sin relaciones*

## Descripcion

este pedido no se puede facturar tira error el sistema

Server error: `POST http://ms-comprobantes.lio.red/v2/CreateVoucher` resulted in a `500 Internal Server Error` response: "Campo Cmp.Importe_total debe ser igual a la suma del campo Items.Pro_total_item de todos los items declarados."

Información del pedido: 0002 - 10397191
Cliente: 20794 - VIVAS JULIO ALEJANDRO
Usuario: pat
