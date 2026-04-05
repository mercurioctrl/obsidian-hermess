---
jira_key: "PED-1008"
aliases: ["PED-1008"]
summary: "API - Feat - Intervenir en el chat (responder) como libreopcion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-26 13:43"
updated: "2025-06-09 10:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1008"
---

# PED-1008: API - Feat - Intervenir en el chat (responder) como libreopcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-26 13:43 |
| Actualizado | 2025-06-09 10:34 |
| Etiquetas | ninguna |
| Jira | [PED-1008](https://bluinc.atlassian.net/browse/PED-1008) |

## Relaciones

- **Padre:** [[PED-1005 - Chat General|PED-1005]] Chat General
- **action item from:** [[PED-1007 - API - Feat - Crear endpoint para obtener historial completo del chat de un|PED-1007]] API - Feat - Crear endpoint para obtener historial completo del chat de un pedido libre opcion
- **has action item:** [[PED-1009 - APP - Mostrar chat general para las ventas de libre opcion|PED-1009]] APP - Mostrar chat general para las ventas de libre opcion

## Descripcion

Se debe desarrollar un recurso para permitir que el sistema de Libre Opción (usuario con ID `0`) pueda enviar mensajes a un chat de pedido específico, insertando registros en la tabla `LO.dbo.pedidosDetalleChat`.

```
POST {API_URL}/v1/chatLo/{pedidoDetalleId}/reply
```

```
{
  "message": "Gracias por tu compra. En breve te contactaremos para continuar con la gestión."
}
```

- `pedidoDetalleId`: se pasa en la URL.


- `message`: texto del mensaje enviado por Libre Opción.


- El mensaje siempre se guarda como enviado por el `usuarioRemitenteID = 0`.



### Comportamiento esperado:

- El mensaje se debe insertar con:

- `usuarioRemitenteID = 0`


- `fechaEnvio = NOW()` (fecha y hora actual)


- `fechaVisto = NULL`




- El endpoint debe validar que el `pedidoDetalleId` exista antes de insertar.


- Debe registrar el mensaje en la misma conversación ya iniciada.



```
{
  "id": 755401,
  "message": "Gracias por tu compra. En breve te contactaremos para continuar con la gestión.",
  "sentAt": "2025-05-26 09:33:45.312",
  "seenAt": null,
  "user": {
    "id": 0,
    "avatar": -1,
    "logo": ""
  }
}

```

### Criterios de aceptación:

-  Inserta correctamente el mensaje como usuario 0.


-  Devuelve la respuesta con los mismos campos que el historial (`id`, `message`, `sentAt`, `seenAt`, `user`).


-  Controla que el `pedidoDetalleId` exista.


-  Maneja errores si el campo `message` viene vacío o si el ID es inválido.
