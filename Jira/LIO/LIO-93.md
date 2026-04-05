---
jira_key: "LIO-93"
summary: "API - Refactor - Migrar recurso de seguimiento "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-09 08:38"
updated: "2025-03-21 07:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-93"
---

# LIO-93: API - Refactor - Migrar recurso de seguimiento 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-09 08:38 |
| Actualizado | 2025-03-21 07:47 |
| Etiquetas | ninguna |
| Jira | [LIO-93](https://bluinc.atlassian.net/browse/LIO-93) |

## Descripción

Migraremos el recurso de la API legacy a la API nuva de Libre Opcion

```
GET {API_LEGACY}/envios/paquete/602862/tracking/E000419650
```

El mismo actualmente funciona mal para algunos currier. 

Nosotros implementaremos una lógica nueva mucho mas simple, basada en lo que hacemos en la API de NB y de Pedidos para mostrar el tracking 

```
https://api.orders.lio.red/v1/orders/0002-10364760/trackingShipping
```

que devuelve algo como esto

```
[
    {
        "state": "Entregado Cobrado",
        "brach": "New Bytes - CABA, CABA",
        "address": "Jujuy 1039, CABA, CABA",
        "date": "2024-08-12 12:00"
    },
    {
        "state": "A\u00fan no recibimos tu env\u00edo. Suscribite al servicio de notificaciones y te enviaremos las novedades por e-mail",
        "brach": "Andreani  ",
        "address": "",
        "date": "13-08-2024 11:01"
    },
    {
        "state": "Ya tenemos tu env\u00edo. Lo estamos preparando para enviarlo a la sucursal a cargo de la entrega",
        "brach": "Andreani PROVEEDOR CALIFORNIA",
        "address": "",
        "date": "13-08-2024 18:31"
    },
    {
        "state": "El env\u00edo est\u00e1 viajando a la sucursal responsable de la entrega",
        "brach": "Andreani PROVEEDOR CALIFORNIA",
        "address": "",
        "date": "14-08-2024 04:57"
    },
    {
        "state": "Tu env\u00edo lleg\u00f3 a la sucursal a cargo de la entrega. Suscribite al servicio de notificaciones y te enviaremos novedades por e-mail",
        "brach": "Andreani SAN LORENZO (AV SAN MARTIN)",
        "address": "",
        "date": "15-08-2024 06:47"
    },
    {
        "state": "En el d\u00eda de hoy estaremos visitando el domicilio de entrega",
        "brach": "Andreani SAN LORENZO (AV SAN MARTIN)",
        "address": "",
        "date": "15-08-2024 09:22"
    },
    {
        "state": "El env\u00edo fue entregado",
        "brach": "Andreani SAN LORENZO (AV SAN MARTIN)",
        "address": "",
        "date": "15-08-2024 15:07"
    }
]
```
