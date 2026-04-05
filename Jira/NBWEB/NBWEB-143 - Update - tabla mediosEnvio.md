---
jira_key: "NBWEB-143"
aliases: ["NBWEB-143"]
summary: "Update -  tabla mediosEnvio"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-04-26 12:17"
updated: "2022-06-26 21:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-143"
---

# NBWEB-143: Update -  tabla mediosEnvio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-04-26 12:17 |
| Actualizado | 2022-06-26 21:32 |
| Etiquetas | ninguna |
| Jira | [NBWEB-143](https://bluinc.atlassian.net/browse/NBWEB-143) |

## Relaciones

*Sin relaciones*

## Descripcion

```
-- sql para actualizar la tabla mediosEnvio, hablitando miniflete en recurso /medios-de-envio
UPDATE
    TOP(1) "LO"."dbo"."mediosEnvio"
SET
    "tipo" = '2'
WHERE
    "id" = 4056;
```
