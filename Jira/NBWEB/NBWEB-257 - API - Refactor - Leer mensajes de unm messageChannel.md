---
jira_key: "NBWEB-257"
aliases: ["NBWEB-257"]
summary: "API - Refactor -  Leer mensajes de unm messageChannel"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-14 09:30"
updated: "2022-06-26 21:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-257"
---

# NBWEB-257: API - Refactor -  Leer mensajes de unm messageChannel

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-14 09:30 |
| Actualizado | 2022-06-26 21:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-257](https://bluinc.atlassian.net/browse/NBWEB-257) |

## Relaciones

- **Padre:** [[NBWEB-99]] API - Precarga postventa
- **relates to:** [[NBWEB-206]] API - Leer mensajes de un meesageChannel
- **blocks:** [[NBWEB-208]] APP - Feat - Maquetar y Conectar tickets

## Descripcion

Se debe agregar la informacion del ingreso de postventa que esta asociado al canal de mensajes de la siguiente forma



```
GET {{API_URL}}/v1/postventa/2026/messageChannel/{token}
```

```
GET {{API_URL}}/v1/postventa/2026/messageChannel
```

```json
[
    "ticketHeader": {
                    "ticketNumber": 19482,
                    "status": "REVISADO",
                    "userId": 0,
                    "finalized": null
                    },
      "ticketDetails": [{
                        "itemFinalized": "REVISADO",
                          "itemTicketNumber": 29597,
                          "serial": "SP650PCBUSEA004675",
                          "productId": 6201,
                          "warranty": "SI",
                          "failDescription": "DEJA FALLAS",
                          "testStatus": "REVISADO",
                          "technicalReport": "",
                          "deliveryDate": "08-05-2015",
                          "description": "FUENTE GAMER THERMALTAKE SMART 650W",
                          "sku": "SP-650P"                         
                        },
                        {
                        "itemFinalized": "REVISADO",
                        "itemTicketNumber": 29597,
                        "serial": "SP650PCBUSEA004675",
                        "productId": 6201,
                        "warranty": "SI",
                        "failDescription": "DEJA FALLAS",
                        "testStatus": "REVISADO",
                        "technicalReport": "",
                        "deliveryDate": "08-05-2015",
                        "description": "FUENTE GAMER THERMALTAKE SMART 650W",
                        "sku": "SP-650P",    
                      ],
           "messageChanel" : [{
                        "message": "Hola prueba mensaje2",
                        "date": "2022-05-30 10:42:48.477",
                        "usuario": "EzeTestLunes1233a"
                        },
                        {
                        "message": "Prueba sin token",
                        "date": "2022-05-30 10:44:38.063",
                        "usuario": "EzeTestLunes1233a"
                        }]
    }
   
]
```
