---
jira_key: "NBWEB-611"
summary: "API - Review - Al intentar leer el recuro 'readToken' no me lo permite el middleware"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-16 09:15"
updated: "2024-01-26 02:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-611"
---

# NBWEB-611: API - Review - Al intentar leer el recuro 'readToken' no me lo permite el middleware

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-16 09:15 |
| Actualizado | 2024-01-26 02:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-611](https://bluinc.atlassian.net/browse/NBWEB-611) |

## Descripción

Al intentar leer el recuro 'readToken' no me lo permite el middleware

```
GET {{API_URL}}/v1/miCuenta/readToken
```

Devuelve

```
El usuario no está autorizado para realizar esta acción
```

Me gustaría saber la razón o si hay algún permiso especial, ya que debemos usar el recurso para poder mostrarlo.
