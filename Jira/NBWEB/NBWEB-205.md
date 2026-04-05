---
jira_key: "NBWEB-205"
summary: "API - Enviar mensaje a un messageChannel"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-26 11:25"
updated: "2022-06-26 21:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-205"
---

# NBWEB-205: API - Enviar mensaje a un messageChannel

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-26 11:25 |
| Actualizado | 2022-06-26 21:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-205](https://bluinc.atlassian.net/browse/NBWEB-205) |

## Descripción

```
POST {{API_URL}}/v1/postventa/{postsaleInboundId}/messageChannel/{token}
```

Se debe agregar un recurso que debe servir para enviar un mensaje o issue, para poder escribir un issue es necesario contar con el token correcto.

Para esto se puede modelar una tabla llamada `postsaleInboundMessageChanelIssue` o similar y en ella almacenar

- `id`


- `postsaleInboundMessageChanelId`


- `messege` (max 256)


- `userId`


- `clientId`


- `date` datetime completo


- otra informacion relevante de la conexion que envia el issue



Estos son los campos mínimos, aunque pueden surgir nuevos en el desarrollo.
