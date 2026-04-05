---
jira_key: "NBWEB-412"
aliases: ["NBWEB-412"]
summary: "API - CMS - Feat - Listar zonas de los baners"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-18 13:43"
updated: "2022-08-01 12:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-412"
---

# NBWEB-412: API - CMS - Feat - Listar zonas de los baners

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-18 13:43 |
| Actualizado | 2022-08-01 12:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-412](https://bluinc.atlassian.net/browse/NBWEB-412) |

## Relaciones

- **Padre:** [[NBWEB-73 - API - CMS - ABMS|NBWEB-73]] API - CMS - ABMS

## Descripcion

```
GET {{API_URL}}/v1/cms/banners/zones
```

Retorna

```json
[
  {
    "id": 3,
    "descroption": "Banner central"
  },
  {
    "id": 3,
    "descroption": "Banner central"
  },
  {
    "id": 3,
    "descroption": "Banner central"
  }
]
```

Se debe crear una tabla para almacenar la información del tipo `NB_WEB.dbo.bannersZones`
