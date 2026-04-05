---
jira_key: "PED-1078"
aliases: ["PED-1078"]
summary: "API - Feat - Envio de plantilla con posicion y aceleradores"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-07 12:27"
updated: "2025-08-11 10:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1078"
---

# PED-1078: API - Feat - Envio de plantilla con posicion y aceleradores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-07 12:27 |
| Actualizado | 2025-08-11 10:46 |
| Etiquetas | ninguna |
| Jira | [PED-1078](https://bluinc.atlassian.net/browse/PED-1078) |

## Relaciones

- **Padre:** [[PED-1077]] NB Travel
- **has action item:** [[PED-1079]] APP - Feat - Envio de plantilla con posicion y aceleradores

## Descripcion

Utilizando la plantilla creada en [link](https://bluinc.atlassian.net/browse/PED-1079)  debemos enviar un correo semanal a los usuarios que tienen grupo asignado (y por ende participan de la acción)

- Grupo Asignado


- Posicion y candidad de millas del cliente


- Nombre del cliente


- Lista de aceleradores vigentes y próximos (los vencidos no importan)


- Lista de desafíos si hay vigentes (los vencidos no importan)



*Estaría bueno llevar el registro en una tabla de si se hizo el envío o no, de manera simple para que la tarea pueda tener un esquema de cola por si hay cualquier problema.*

*En modo debug, todos los correos se envían a forwarding*

*En modo normal, se envían todos los correos al cliente según su correo de la tabla usuarios, y en copia oculta se envía forwarding*
