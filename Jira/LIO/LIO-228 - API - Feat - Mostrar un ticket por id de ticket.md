---
jira_key: "LIO-228"
aliases: ["LIO-228"]
summary: "API - Feat - Mostrar un ticket por id de ticket"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-02-17 18:19"
updated: "2025-07-29 16:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-228"
---

# LIO-228: API - Feat - Mostrar un ticket por id de ticket

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-02-17 18:19 |
| Actualizado | 2025-07-29 16:06 |
| Etiquetas | ninguna |
| Jira | [LIO-228](https://bluinc.atlassian.net/browse/LIO-228) |

## Relaciones

- **Padre:** [[LIO-21]] Migrar sistema de tickets para usar el de capa 1 (NB)
- **has action item:** [[LIO-226]] APP - Refactor - Conectar sistema de envio de ticket a v4
- **has action item:** [[PED-962]] API - Feat - Leer ticket por numero de orden
- **relates to:** [[SNB-3285]] Whaticket - LO - Orden de los mensajes del ticket

## Descripcion

```
GET {APIv4_URL}/v4/ticket/68031?id=85695
```

```
[{
    "id": 85695,
    "open": true,
    "description":"esto es una prueba",
    "startDate": "2025-02-12 14:26:36.360",
    "endDate": "",
    "pending": true,
    "type": {
        "id": 2,
        "description": "Tengo un problema"
    },
    "issue": {
        "id": 8,
        "description": "Con el vendedor"
    },
    "thread": [
        {
                "id": 4,
                "ticketId": 9,
                "senderUserId": 2,
                "message": "asdasda2",
                "date": "2025-02-18 10:52:02",
                "file": null,
                "sellerImage": "asdasdasdasd.png",
                "userAvatar":18,
                "userName":"BsAsPc"
            }
    ] 
}]
```
