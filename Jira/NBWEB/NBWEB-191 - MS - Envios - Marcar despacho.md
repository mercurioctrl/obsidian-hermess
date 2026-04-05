---
jira_key: "NBWEB-191"
aliases: ["NBWEB-191"]
summary: "MS - Envios - Marcar despacho"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-17 16:11"
updated: "2022-11-09 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-191"
---

# NBWEB-191: MS - Envios - Marcar despacho

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-17 16:11 |
| Actualizado | 2022-11-09 11:31 |
| Etiquetas | ninguna |
| Jira | [NBWEB-191](https://bluinc.atlassian.net/browse/NBWEB-191) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios

## Descripcion

Solo administradores

```
PUT {{API_URL}}/v1/shipping/{idEnvio or Clave Publica}/dispatch
```
