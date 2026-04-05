---
jira_key: "PED-614"
aliases: ["PED-614"]
summary: "Filtrar por request invoice LO "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2024-03-14 17:09"
updated: "2024-03-19 15:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-614"
---

# PED-614: Filtrar por request invoice LO 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2024-03-14 17:09 |
| Actualizado | 2024-03-19 15:37 |
| Etiquetas | ninguna |
| Jira | [PED-614](https://bluinc.atlassian.net/browse/PED-614) |

## Relaciones

- **Subtarea:** [[PED-616]] APP - Refactor - Agregar filtro para "Factura solicitada"
- **relates to:** [[SNB-1624]] FACTURACION

## Descripcion

Se agrego un parametro al filtrado de ordenes en pedidos que refiere a que pedidos tienen pendientes pedidos de facturacion.

```

```

[adjunto]
```
{{API_URL}}/v1/orders?itemsPerPage=20&currentPage=1&requestInvoice=1
```
