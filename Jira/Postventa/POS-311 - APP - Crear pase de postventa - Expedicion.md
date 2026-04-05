---
jira_key: "POS-311"
aliases: ["POS-311"]
summary: "APP - Crear pase de postventa - Expedicion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Ezequiel manzano"
created: "2024-08-19 15:23"
updated: "2024-08-27 02:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-311"
---

# POS-311: APP - Crear pase de postventa - Expedicion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Ezequiel manzano |
| Creado | 2024-08-19 15:23 |
| Actualizado | 2024-08-27 02:51 |
| Etiquetas | ninguna |
| Jira | [POS-311](https://bluinc.atlassian.net/browse/POS-311) |

## Relaciones

- **Padre:** [[POS-310 - Refactor Refactorizar pases|POS-310]] Refactor: Refactorizar pases

## Descripcion

Al crear un pase de origin postventa con destino a expedicion. Se debe agregar un serial a la hora del crear el pase

SOLO SI EL ORIGEN ES PVENTA Y EL DESTINO EXPEDICION

para esto enviaremos una request POST donde incluiremos el serial a lo que ya veniamos haciendo.

[adjunto]


Por lo tanto deberiamos incluir en el modal el campo “serial” 

[adjunto]
