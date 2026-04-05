---
jira_key: "PED-749"
aliases: ["PED-749"]
summary: "DATASET - Crear tabla aceleradores y agregar columna en pedclil"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-24 10:15"
updated: "2024-06-26 02:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-749"
---

# PED-749: DATASET - Crear tabla aceleradores y agregar columna en pedclil

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-24 10:15 |
| Actualizado | 2024-06-26 02:50 |
| Etiquetas | ninguna |
| Jira | [PED-749](https://bluinc.atlassian.net/browse/PED-749) |

## Relaciones

- **Padre:** [[PED-748]] Incentivo 25 años

## Descripcion

Crearemos una tabla nueva llamada `NB_WEB.dbo.acelerators` con las siguientes columnas

- id (int auto)


- txtMatch (string)


- acelerator (decimal/float)


- startDate (datetime)


- endDate (datetime)



Agregaremos una columna a la tabla `[NewBytes_DBF].[dbo].[pedclil]`

- acelerator (decimal/float)
