---
jira_key: "PED-962"
aliases: ["PED-962"]
summary: "API - Feat - Leer ticket por numero de orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-04 19:02"
updated: "2026-01-29 12:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-962"
---

# PED-962: API - Feat - Leer ticket por numero de orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-04 19:02 |
| Actualizado | 2026-01-29 12:48 |
| Etiquetas | ninguna |
| Jira | [PED-962](https://bluinc.atlassian.net/browse/PED-962) |

## Relaciones

- **Padre:** [[PED-960 - Tickets de pedido|PED-960]] Tickets de pedido
- **action item from:** [[LIO-228 - API - Feat - Mostrar un ticket por id de ticket|LIO-228]] API - Feat - Mostrar un ticket por id de ticket
- **has action item:** [[PED-966 - APP - Feat - Agregar modal para visualizar y responder tickets al ejecutar el|PED-966]] APP - Feat - Agregar modal para visualizar y responder tickets al ejecutar el accionable en el indicador de ticket para una orden
- **relates to:** [[PED-967 - API - Leer ticket por numero de orden - Error en la columna createdAt|PED-967]] API - Leer ticket por numero de orden - Error en la columna createdAt
- **relates to:** [[SNB-3635 - PED - Leer ticket por número de orden - Respuesta sin contenido|SNB-3635]] PED - Leer ticket por número de orden -> Respuesta sin contenido

## Descripcion

```
GET {API_URL}/v1/orders/{branch-order}/ticket
```

```
[{
    "id": 85695,
    "open": true,
    "description":"esto es una prueba",
    "startDate": "2025-02-12 14:26:36.360",
    "endDate": "",
    "pending" true,
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

Esta historia es similar a [link](https://lioteam.atlassian.net/browse/LIO-228)
