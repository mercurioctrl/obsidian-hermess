---
jira_key: "NBWEB-446"
aliases: ["NBWEB-446"]
summary: "API - Feat Descargar XLSX"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-05 14:02"
updated: "2022-08-23 10:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-446"
---

# NBWEB-446: API - Feat Descargar XLSX

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-05 14:02 |
| Actualizado | 2022-08-23 10:49 |
| Etiquetas | ninguna |
| Jira | [NBWEB-446](https://bluinc.atlassian.net/browse/NBWEB-446) |

## Relaciones

- **Padre:** [[NBWEB-50 - Sitio Web|NBWEB-50]] Sitio Web
- **Subtarea:** [[NBWEB-447 - API - Feat - Descargar XLSX con el token|NBWEB-447]] API - Feat - Descargar XLSX con el token

## Descripcion

```
GET {{API_URL}}/v1/priceListExcel/{HARDTOKEN}
```

En el caso que el hardtoken coincida con alguna cuenta debo poder descargar el archivo.  No hace login, sino que solo genera y descarga el archivo.
