---
jira_key: "NBWEB-411"
aliases: ["NBWEB-411"]
summary: "API - Refactor - Esquema de zonas"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-18 12:55"
updated: "2022-08-01 12:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-411"
---

# NBWEB-411: API - Refactor - Esquema de zonas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-18 12:55 |
| Actualizado | 2022-08-01 12:37 |
| Etiquetas | ninguna |
| Jira | [NBWEB-411](https://bluinc.atlassian.net/browse/NBWEB-411) |

## Relaciones

- **Padre:** [[NBWEB-54]] Content Manager

## Descripcion

Refactor

```
POST {{API_URL}}/v1/cms/banner/{zoneId}
```

El uploader debe tener en cuenta la zona a la que se esta subiendo el banner, ademas de los demas parametros
