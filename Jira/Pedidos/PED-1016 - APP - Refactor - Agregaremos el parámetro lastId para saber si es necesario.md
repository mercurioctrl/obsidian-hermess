---
jira_key: "PED-1016"
aliases: ["PED-1016"]
summary: "APP - Refactor - Agregaremos el parámetro lastId para saber si es necesario recargar el chat"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-06-09 15:50"
updated: "2025-06-24 20:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1016"
---

# PED-1016: APP - Refactor - Agregaremos el parámetro lastId para saber si es necesario recargar el chat

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-09 15:50 |
| Actualizado | 2025-06-24 20:35 |
| Etiquetas | ninguna |
| Jira | [PED-1016](https://bluinc.atlassian.net/browse/PED-1016) |

## Relaciones

- **Padre:** [[PED-1005]] Chat General
- **is blocked by:** [[PED-1015]] API - Refactor - Agregaremos el parámetro lastId para saber si es necesario recargar el chat

## Descripcion

Actualmente el chat carga todos los mensajes de una conversación mediante

```
GET /v1/chatLo/{chatId}
```

Para evitar recargar toda la conversación cada vez que se escribe o se espera una respuesta, se implementará un sistema de sincronización incremental mediante `lastId`

De esta forma cada vez que enviemos un mensaje con

```
POST {API_URL}/v1/chatLo/{chatId}/reply
```

Recibiremos algo como esto

```
{
    "id": 661987,
    "lastId": 661984, <-- Se agrega el ultimo ID, que no es el del mensaje actual para que el front sepa si ya lo tiene en pantalla
    "message": "test",
    "sentAt": "2025-06-09 15:31:19",
    "seenAt": null,
    "user": {
        "id": 0,
        "avatar": -1,
        "logo": null,
        "name": null
    }
}
```

La idea es basarse en el parámetro `lastId` para saber si ya tenemos ese mensaje cargado en pantalla y si no es así, pediremos el recurso nuevamente para cargar el contenido faltante. Si ya esta en pantalla, entonces no pedimos el recurso dado que podemos cargar nuestro mensaje sin solicitar el recurso.

En la misma linea de idea, se refactorizo tambien el recurso

```
GET /v1/chatLo/677013?lastId={lastId}
```

es decir que ahora podemos enviarle `lastId` de modo tal que podremos cargar los mensajes de ese punto en adelante dando versatilidad a la carga de contenido y pueindo cargar en partes o parcialmente los mensajes según el contenido de pantalla.
