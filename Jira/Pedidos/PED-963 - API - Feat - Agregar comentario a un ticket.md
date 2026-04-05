---
jira_key: "PED-963"
aliases: ["PED-963"]
summary: "API - Feat - Agregar comentario a un ticket"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-04 19:09"
updated: "2025-03-10 18:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-963"
---

# PED-963: API - Feat - Agregar comentario a un ticket

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-04 19:09 |
| Actualizado | 2025-03-10 18:34 |
| Etiquetas | ninguna |
| Jira | [PED-963](https://bluinc.atlassian.net/browse/PED-963) |

## Relaciones

- **Padre:** [[PED-960 - Tickets de pedido|PED-960]] Tickets de pedido
- **has action item:** [[PED-966 - APP - Feat - Agregar modal para visualizar y responder tickets al ejecutar el|PED-966]] APP - Feat - Agregar modal para visualizar y responder tickets al ejecutar el accionable en el indicador de ticket para una orden

## Descripcion

Este es el recurso para enviar mensajes al hilo, el cual puede tener una imagen adjunta y un máximo de 1000 caracteres


```
POST {API_URL}/v1/orders/{branch-order}/ticket/comment
```

**Carga útil: **

```
{
  branch: '0002',
  order: '10394337',
  message: esto es una prueba
  file: (binario) <<-- Esta imagen proviene del formulario,
  id: 27
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

Seguiremos ademas, lo realizado en el refactor [link](https://lioteam.atlassian.net/browse/LIO-244)  de tal forma que cada vez que generamos un comentario marcaremos 

`[NewBytes_DBF].[dbo].[pedclitTicket].pending=false`
