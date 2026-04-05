---
jira_key: "NBWEB-204"
aliases: ["NBWEB-204"]
summary: "API - Crear un message channel con permalink"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-26 11:24"
updated: "2022-06-26 21:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-204"
---

# NBWEB-204: API - Crear un message channel con permalink

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-26 11:24 |
| Actualizado | 2022-06-26 21:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-204](https://bluinc.atlassian.net/browse/NBWEB-204) |

## Relaciones

- **Padre:** [[NBWEB-99 - API - Precarga postventa|NBWEB-99]] API - Precarga postventa
- **blocks:** [[NBWEB-208 - APP - Feat - Maquetar y Conectar tickets|NBWEB-208]] APP - Feat - Maquetar y Conectar tickets

## Descripcion

```
POST {{API_URL}}/v1/postventa/messageChannel
```

Se debe agregar un recurso que debe crear un canal de mensajes para un determinado postsaleId

Para esto se puede  modelar una tabla llamada `postsaleInboundMessageChanel` o similar y en ella almacenar

- id


- Un token único para acceder al canal y enviar mensajes


- un `postsaleInboundId` para poder joinear con `postsaleInbound`



Estos son los campos mínimos, aunque pueden surgir nuevos en el desarrollo.

**Retorna el token**

Solo se puede crear un messageChannel por postsaleInboundId
