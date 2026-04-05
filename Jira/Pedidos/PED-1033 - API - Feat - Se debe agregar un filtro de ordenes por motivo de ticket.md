---
jira_key: "PED-1033"
aliases: ["PED-1033"]
summary: "API - Feat - Se debe agregar un filtro de ordenes por motivo de ticket"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-01 12:54"
updated: "2025-07-14 10:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1033"
---

# PED-1033: API - Feat - Se debe agregar un filtro de ordenes por motivo de ticket

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-01 12:54 |
| Actualizado | 2025-07-14 10:31 |
| Etiquetas | ninguna |
| Jira | [PED-1033](https://bluinc.atlassian.net/browse/PED-1033) |

## Relaciones

- **Padre:** [[PED-960]] Tickets de pedido
- **has action item:** [[PED-1035]] APP - Feat - Se deben poder filtrar las ordenes por tipo y motivo de ticket

## Descripcion

Agregaremos un filtro para ver las ordenes que cuenten con un ticket de un motivo determinado

```
GET {API_URL}/v1/orders?issueId={issueId}
```

Toda los joins y logica necesarios, solo se agregan  si esta el parámetro `issueId` presente de modo tal que el repositorio no vea afectada su performance por esta lógica a menos que sea necesario. Se debe buscar la forma mas performativa de realizarlo.
