---
jira_key: "LIO-223"
aliases: ["LIO-223"]
summary: "API - Feat - Actualizar ticket (agregar comentario)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-17 13:05"
updated: "2025-03-05 09:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-223"
---

# LIO-223: API - Feat - Actualizar ticket (agregar comentario)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-17 13:05 |
| Actualizado | 2025-03-05 09:59 |
| Etiquetas | ninguna |
| Jira | [LIO-223](https://bluinc.atlassian.net/browse/LIO-223) |

## Relaciones

- **Padre:** [[LIO-21 - Migrar sistema de tickets para usar el de capa 1 (NB)|LIO-21]] Migrar sistema de tickets para usar el de capa 1 (NB)
- **has action item:** [[LIO-226 - APP - Refactor - Conectar sistema de envio de ticket a v4|LIO-226]] APP - Refactor - Conectar sistema de envio de ticket a v4

## Descripcion

Este es el recurso para enviar mensajes al hilo, el cual puede tener una imagen adjunta y un maximo de 1000 caracteres

```
POST {APIv4_URL}/v4/ticket/680312/comment
```

**Carga útil: **

```
{
  id: 680312
  message: esto es una prueba
  file: (binario) <<-- Esta imagen proviene del formulario
}
```

**Crearemos la tabla:**

```
SELECT [id]
      ,[ticketId]
      ,[senderUserId]
      ,[message]
      ,[date]
      ,[file]
  FROM [NewBytes_DBF].[dbo].[pedclitTicketThread]
```
