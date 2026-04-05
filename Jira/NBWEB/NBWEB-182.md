---
jira_key: "NBWEB-182"
summary: "MS - Envios - Leer datos de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-13 09:02"
updated: "2022-08-01 12:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-182"
---

# NBWEB-182: MS - Envios - Leer datos de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-13 09:02 |
| Actualizado | 2022-08-01 12:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-182](https://bluinc.atlassian.net/browse/NBWEB-182) |

## Descripción

```
GET {{API_URL}}/v1/shipping/{idEnvio or Clave Publica}
```

Retorna todos los datos de la tabla envios, menos la clave privada
