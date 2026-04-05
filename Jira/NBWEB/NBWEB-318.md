---
jira_key: "NBWEB-318"
summary: "Modificacion de Tabla MediosEnvio"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-06-29 12:00"
updated: "2022-06-29 12:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-318"
---

# NBWEB-318: Modificacion de Tabla MediosEnvio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-06-29 12:00 |
| Actualizado | 2022-06-29 12:05 |
| Etiquetas | ninguna |
| Jira | [NBWEB-318](https://bluinc.atlassian.net/browse/NBWEB-318) |

## Descripción

Query para crear una columan que contendra la distancia maxima pertimida para un trasportista

```
ALTER TABLE [LO].[dbo].[mediosEnvio]
ADD maxDistance int NULL;
```



Query para asignar 100km como distancia maxima a Trasporte Camioneta

```
update [LO].[dbo].[mediosEnvio]
set maxDistance = 100
where id = 3031;
```
