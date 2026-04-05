---
jira_key: "PED-1009"
aliases: ["PED-1009"]
summary: "APP - Mostrar chat general para las ventas de libre opcion"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-06-01 21:20"
updated: "2025-06-10 10:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1009"
---

# PED-1009: APP - Mostrar chat general para las ventas de libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-01 21:20 |
| Actualizado | 2025-06-10 10:34 |
| Etiquetas | ninguna |
| Jira | [PED-1009](https://bluinc.atlassian.net/browse/PED-1009) |

## Relaciones

- **Padre:** [[PED-1005]] Chat General
- **action item from:** [[PED-1006]] API - Feat - Listar ultimos chats de compras en libreopcion (Cabeceras de los chats)
- **action item from:** [[PED-1007]] API - Feat - Crear endpoint para obtener historial completo del chat de un pedido libre opcion
- **action item from:** [[PED-1008]] API - Feat - Intervenir en el chat (responder) como libreopcion
- **relates to:** [[PED-1017]] APP - Refactor - Mostrar chat general para las ventas de libre opcion -> Agregar filtro por chats abiertos/cerrados

## Descripcion

Se debe implementar una interfaz visual de chat en el módulo de pedidos que permita:

- Visualizar todos los chats activos con clientes (lista de conversaciones).


- Ver y responder los mensajes de cada chat asociado a un `pedidoDetalleId`.



La experiencia debe emular la estructura de **WhatsApp Web**, mostrando:

- **Columna izquierda:** Lista de conversaciones con los clientes, donde cada ítem representa un pedido. Debe incluir:

- Avatar del cliente.


- Nombre del cliente.


- Último mensaje.


- Fecha del último mensaje.


- Estado de prioridad si aplica.


- Permitir scroll y paginación con `itemsPerPage` y `currentPage`.




- **Columna derecha:** Conversación activa con el cliente seleccionada:

- Mostrar todos los mensajes del pedido, con fechas y remitente.


- Estilos diferentes para mensajes enviados por vendedor, Libre Opción y por el cliente.


- Campo de entrada para escribir nuevos mensajes (solo desde Libre Opción).


- Botón de "Enviar" para enviar el mensaje al backend (`POST /chatLo/{pedidoDetalleId}/reply`).





### Endpoints a consumir

- **Lista de chats (columna izquierda):**



```
GET /v1/chatLo?currentPage=1&itemsPerPage=20&open=true&idLo={optional}
```

- **Mensajes de un pedido (columna derecha):**



```
GET /v1/chatLo/{pedidoDetalleId}
```

- **Enviar mensaje (Libre Opción):**



```
POST /v1/chatLo/{pedidoDetalleId}/reply
```

###  Criterios de aceptación

- Se muestran correctamente los chats en la columna izquierda con paginación.


- Al hacer clic sobre un chat, se carga y muestra el historial completo.


- Se puede enviar un mensaje si se ingresó texto válido.


- La interfaz se adapta correctamente a escritorio (modo similar a WhatsApp Web).


- Se muestran los avatares y nombres correctamente.


- Diferencia clara visualmente entre mensajes del cliente y del sistema.





---

###  Notas adicionales

- Usar componentes reutilizables para las burbujas de mensaje.


- Validar que el campo de texto no esté vacío antes de enviar.


- En caso de error, mostrar mensaje claro al usuario.
