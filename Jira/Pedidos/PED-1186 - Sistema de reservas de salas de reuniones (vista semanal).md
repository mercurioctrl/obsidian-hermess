---
jira_key: "PED-1186"
aliases: ["PED-1186"]
summary: "Sistema de reservas de salas de reuniones (vista semanal)"
status: "Tareas por hacer"
type: "Epic"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2025-12-14 21:31"
updated: "2025-12-14 21:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1186"
---

# PED-1186: Sistema de reservas de salas de reuniones (vista semanal)

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Epic |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-14 21:31 |
| Actualizado | 2025-12-14 21:39 |
| Etiquetas | ninguna |
| Jira | [PED-1186](https://bluinc.atlassian.net/browse/PED-1186) |

## Relaciones

*Sin relaciones*

## Descripcion

Implementar un sistema de reservas de salas que permita visualizar la ocupación semanal de una sala, crear nuevas reservas y cancelarlas, garantizando que no existan solapamientos horarios.
El sistema debe exponer recursos HTTP para listar reservas en un rango semanal, crear reservas de forma transaccional y cancelar reservas existentes, utilizando la zona horaria [[GMT-3]] definida por la base de datos.
El front será responsable de navegar entre semanas y de calcular los espacios libres a partir de la información devuelta por la API.
