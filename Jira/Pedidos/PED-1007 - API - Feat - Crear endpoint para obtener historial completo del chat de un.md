---
jira_key: "PED-1007"
aliases: ["PED-1007"]
summary: "API - Feat - Crear endpoint para obtener historial completo del chat de un pedido libre opcion"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-26 09:04"
updated: "2025-06-10 10:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1007"
---

# PED-1007: API - Feat - Crear endpoint para obtener historial completo del chat de un pedido libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-26 09:04 |
| Actualizado | 2025-06-10 10:22 |
| Etiquetas | ninguna |
| Jira | [PED-1007](https://bluinc.atlassian.net/browse/PED-1007) |

## Relaciones

- **Padre:** [[PED-1005 - Chat General|PED-1005]] Chat General
- **action item from:** [[PED-1006 - API - Feat - Listar ultimos chats de compras en libreopcion (Cabeceras de los|PED-1006]] API - Feat - Listar ultimos chats de compras en libreopcion (Cabeceras de los chats)
- **has action item:** [[PED-1008 - API - Feat - Intervenir en el chat (responder) como libreopcion|PED-1008]] API - Feat - Intervenir en el chat (responder) como libreopcion
- **has action item:** [[PED-1009 - APP - Mostrar chat general para las ventas de libre opcion|PED-1009]] APP - Mostrar chat general para las ventas de libre opcion

## Descripcion

Se debe desarrollar un nuevo recurso en el módulo de pedidos, que permita consultar todos los mensajes del chat asociados a un `pedidoDetalleID`, utilizando la tabla `LO.dbo.pedidosDetalleChat`.
Se trata del recurso que nos permite construir todo el chat completo una vez que hacemos clic en su cabecera [link](https://bluinc.atlassian.net/browse/PED-1006) 

```
GET {API_URL}/v1/chatLo/{pedidoDetalleId}
```

### Funcionalidad:

- El endpoint debe devolver todos los mensajes del chat correspondientes al `pedidoDetalleId` recibido como parámetro.


- Los mensajes deben estar ordenados cronológicamente por `fechaEnvio`.


- Cada mensaje debe incluir información del remitente, mensaje, fechas y datos del usuario.



### Formato de respuesta:

El resultado será similar a este array de objetos con el siguiente formato  

```
[
  {
    "id": 755301,                         // ID del mensaje
    "message": "Texto del mensaje",       // Contenido del mensaje
    "sentAt": "2025-05-25 20:58:13.743",  // Fecha y hora de envío
    "seenAt": "2025-05-25 20:58:13.743",  // Fecha y hora en que fue visto (puede ser null)
    "user": {
      "id": 4845,                         // ID del usuario que envió el mensaje
      "avatar": 45,                       // ID o hash del avatar (puede ser -1 si no tiene)
      "logo": "logo.png"                  // Archivo/logo asociado al usuario (vacío si no hay)
    }
  }
]

```

### Notas adicionales:

- Si el usuario no tiene avatar o logo, devolver `-1` y string vacío respectivamente.


- La información del usuario puede provenir de diferentes orígenes según el tipo, por ejemplo cuando es cero, ya sabemos que es libreOpcion.



**Criterios de aceptación:**

-  Devuelve todos los mensajes del `pedidoDetalleId` correctamente ordenados por fecha.


-  Todos los campos están traducidos a inglés y en formato camelCase.


-  Maneja correctamente usuarios del sistema y usuarios registrados.


-  Controla errores si el `pedidoDetalleId` no existe o no tiene mensajes.
