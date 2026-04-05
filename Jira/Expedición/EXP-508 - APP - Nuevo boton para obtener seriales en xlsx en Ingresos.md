---
jira_key: "EXP-508"
aliases: ["EXP-508"]
summary: "APP - Nuevo boton para obtener seriales en xlsx en Ingresos "
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2025-09-04 13:27"
updated: "2025-09-15 20:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-508"
---

# EXP-508: APP - Nuevo boton para obtener seriales en xlsx en Ingresos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2025-09-04 13:27 |
| Actualizado | 2025-09-15 20:42 |
| Etiquetas | ninguna |
| Jira | [EXP-508](https://bluinc.atlassian.net/browse/EXP-508) |

## Relaciones

- **action item from:** [[EXP-507]] API - nuevo recurso para obtener seriales en xlsx

## Descripcion

Se debe utilizar el recurso para obtener los seriales en xlsx.


```powershell
curl --location 'https://gamma.api.warehouse.lio.red//v1/providersOrders/00010477/xlsx' \
--header 'Authorization: ••••••'
```

se puede enviar tmb el parametro ?itemId=121312  para obtener los seriales de ese item del ingreso correspondiente.
