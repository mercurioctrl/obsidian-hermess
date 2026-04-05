---
jira_key: "PED-1015"
aliases: ["PED-1015"]
summary: "API - Refactor - Agregaremos el parámetro lastId para saber si es necesario recargar el chat"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-09 15:32"
updated: "2025-06-24 20:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1015"
---

# PED-1015: API - Refactor - Agregaremos el parámetro lastId para saber si es necesario recargar el chat

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-09 15:32 |
| Actualizado | 2025-06-24 20:34 |
| Etiquetas | ninguna |
| Jira | [PED-1015](https://bluinc.atlassian.net/browse/PED-1015) |

## Relaciones

- **Padre:** [[PED-1005]] Chat General
- **blocks:** [[PED-1016]] APP - Refactor - Agregaremos el parámetro lastId para saber si es necesario recargar el chat

## Descripcion

Agregaremos el parámetro `lastId` para permitir la sincronización incremental del chat para que el front pueda entender si ya lo tiene en pantalla y desde que `id`para adelante, debe cargar los mensajes

```
POST {API_URL}/v1/chatLo/{chatId}/reply
```

Respuesta al enviar un mensaje:

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

---

En la misma linea de idea, refactorizaremos tambien el recurso 

```
GET /v1/chatLo/677013?lastId=661984
```

para recibir el ultimo `id del mensaje` que tiene cargado en pantalla lo que permite una sincronización incremental basada en ese parametro, en lugar de cargar toda la conversación solo me envié a partir de ese mensaje haciendo mucho mas rápida la carga de conversaciones largas, con mucho texto.
