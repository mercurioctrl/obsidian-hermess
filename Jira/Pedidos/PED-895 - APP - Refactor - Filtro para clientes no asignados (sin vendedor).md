---
jira_key: "PED-895"
aliases: ["PED-895"]
summary: "APP - Refactor - Filtro para clientes no asignados (sin vendedor)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-12-04 07:51"
updated: "2024-12-18 11:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-895"
---

# PED-895: APP - Refactor - Filtro para clientes no asignados (sin vendedor)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-04 07:51 |
| Actualizado | 2024-12-18 11:14 |
| Etiquetas | ninguna |
| Jira | [PED-895](https://bluinc.atlassian.net/browse/PED-895) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes

## Descripcion

Basandonos en [link](https://lioteam.atlassian.net/browse/PED-894)  le agregaremos a la ficha de clientes un filtro para mostrar aquellos clientes que fueron desvinculados de su vendedor

```
GET {API_URL}/v1/clients?unassignedClients={unassignedClients}
```

Si `unassignedClients=1` entonces muestro solo los que NO tienen vendedor asignado

Si `unassignedClients=0` entonces muestro solo los que SI tienen vendedor asignado

Si `unassignedClients=null (o no esta disponible)` entonces muestro todos los clientes
