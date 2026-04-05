---
jira_key: "PED-880"
aliases: ["PED-880"]
summary: "API - Refactor - Agregar al repositorio del cliente el filtro \"Dias Inactividad\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-25 07:24"
updated: "2024-11-30 04:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-880"
---

# PED-880: API - Refactor - Agregar al repositorio del cliente el filtro "Dias Inactividad"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-25 07:24 |
| Actualizado | 2024-11-30 04:29 |
| Etiquetas | ninguna |
| Jira | [PED-880](https://bluinc.atlassian.net/browse/PED-880) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes
- **has action item:** [[PED-881 - APP - Refactor - Agregar al repositorio del cliente el filtro Dias Inactividad|PED-881]] APP - Refactor - Agregar al repositorio del cliente el filtro "Dias Inactividad"

## Descripcion

Agregaremos le filtro `InactiveDays` para utilizar, basándonos en la fecha de “ultima compra”.

Lo que hace es recibir una cantidad de días (por ej: 60 dias) y mostrar todos aquellos que tienen mas de 60 días sin compras.

Esto, combinado por alguno de los parámetros  ordenadores como el de “ultima compra” nos permite ordenar los clientes para buscar aquellos inactivos x días y podes rastrillarlos para contactarlos, re asignarlos, etc.

```
GET {API_URL}/v1/clients?InactiveDays=90
```
