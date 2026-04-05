---
jira_key: "NBWEB-445"
aliases: ["NBWEB-445"]
summary: "API - Feat - Se tiene que poder descargar el archivo sin login, en caso de tener el token"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-05 13:58"
updated: "2022-08-23 10:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-445"
---

# NBWEB-445: API - Feat - Se tiene que poder descargar el archivo sin login, en caso de tener el token

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-05 13:58 |
| Actualizado | 2022-08-23 10:47 |
| Etiquetas | ninguna |
| Jira | [NBWEB-445](https://bluinc.atlassian.net/browse/NBWEB-445) |

## Relaciones

- **Padre:** [[NBWEB-432]] API - Feat - Descargar CSV
- **is blocked by:** [[NBWEB-443]] API - Feat - Generar hard token

## Descripcion

```
GET GET {{API_URL}}/v1/priceListCsv/{HARDTOKEN}
```

En el caso que el hardtoken coincida con alguna cuenta debo poder descargar el archivo.  No hace login, sino que solo genera y descarga el archivo.
