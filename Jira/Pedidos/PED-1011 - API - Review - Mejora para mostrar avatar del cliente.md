---
jira_key: "PED-1011"
aliases: ["PED-1011"]
summary: "API - Review - Mejora para mostrar avatar del \"cliente\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-09 09:49"
updated: "2025-06-24 20:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1011"
---

# PED-1011: API - Review - Mejora para mostrar avatar del "cliente"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-09 09:49 |
| Actualizado | 2025-06-24 20:06 |
| Etiquetas | ninguna |
| Jira | [PED-1011](https://bluinc.atlassian.net/browse/PED-1011) |

## Relaciones

- **Padre:** [[PED-1005]] Chat General

## Descripcion

Siguiendo un ejemplo de la conversación #724219 - Leandro leon , aparece un mensaje del cliente como si fuese con avatar de Libre Opción. Si bien en la lista de conversaciones a la izquierda se obtiene correctamente el avatar, por eso utilizaremos el mismo metodo.

[adjunto]
```
[
    {
        "id": 760639,
        "message": "Gracias por elegirnos! Seguinos en nuestras redes para enterarte de los \u00faltimos ingresos y de los incre\u00edbles sorteos.",
        "sentAt": "2025-06-09 09:25:49",
        "seenAt": "2025-06-09 09:25:49",
        "user": {
            "id": 0,
            "avatar": -1,
            "logo": null,
            "name": null
        }
    },
    {
        "id": 760647,
        "message": "Hola! Me aparece pago rechazado, quer\u00eda saber si fue de su lado o la tarjeta?",
        "sentAt": "2025-06-09 09:37:53",
        "seenAt": "2025-06-09 09:39:34",
        "user": {
            "id": 105722,
            "avatar": -1, <---- este avatar es el generico para "cliente/comprador" en el caso del ejemplo "avatar": 0 como se muestra en el repo de cnversaciones (chatLo)
            "logo": null,
            "name": "Leandro leon"
        }
    },
    {
        "id": 760648,
        "message": "Hola seguramente tu tarjeta rechazo el pago por motivos de seguridad o por el monto , deberias ponerte en contactos con ellos para solicitar autorizacion",
        "sentAt": "2025-06-09 09:41:06",
        "seenAt": "2025-06-09 09:46:39",
        "user": {
            "id": 4845,
            "avatar": 45,
            "logo": "4cfdc491658a2956333ec3654f06dfe8.png",
            "name": "Gears Store"
        }
    }
]
```
