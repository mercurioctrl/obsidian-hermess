---
jira_key: "NBWEB-540"
aliases: ["NBWEB-540"]
summary: "APP - Refactor - Agregar cupo disponible para cada agente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-04-28 13:23"
updated: "2023-05-08 07:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-540"
---

# NBWEB-540: APP - Refactor - Agregar cupo disponible para cada agente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-28 13:23 |
| Actualizado | 2023-05-08 07:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-540](https://bluinc.atlassian.net/browse/NBWEB-540) |

## Relaciones

- **Padre:** [[NBWEB-529 - CMS - Personal|NBWEB-529]] CMS -  Personal

## Descripcion

Se debe agregar a los recursos

```
GET {API_URL}/v1/cms/staff
```

```
PATCH {API_URL}/v1/cms/staff
```

El parámetro `nominalDailyLimit` de la tabla  `[NewBytes_DBF].[dbo].[agentes]`

Este parámetro es un decimal en dolares y se debe mostrar y poder editar para cada usuario
