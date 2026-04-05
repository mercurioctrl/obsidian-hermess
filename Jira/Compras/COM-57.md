---
jira_key: "COM-57"
summary: "API - Listar ingresos -> Referencia a tabla distinta"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-02-20 11:37"
updated: "2024-02-22 15:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-57"
---

# COM-57: API - Listar ingresos -> Referencia a tabla distinta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-02-20 11:37 |
| Actualizado | 2024-02-22 15:41 |
| Etiquetas | ninguna |
| Jira | [COM-57](https://bluinc.atlassian.net/browse/COM-57) |

## Descripción

Tomando en cuenta las tareas [link](https://lioteam.atlassian.net/browse/COM-29), [link](https://lioteam.atlassian.net/browse/COM-34) 

Parece ser que el recurso

```
GET {API_URL}/v1/providerOrderInbound
```

Está haciendo referencia a una tabla diferente a la que debería `Newbytes_DBF.dbo.albprol`

[attachment]
