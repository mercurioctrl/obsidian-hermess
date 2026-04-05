---
jira_key: "POS-284"
aliases: ["POS-284"]
summary: "API - Feat - Ver serializacion de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-21 13:44"
updated: "2024-02-27 15:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-284"
---

# POS-284: API - Feat - Ver serializacion de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-21 13:44 |
| Actualizado | 2024-02-27 15:40 |
| Etiquetas | ninguna |
| Jira | [POS-284](https://bluinc.atlassian.net/browse/POS-284) |

## Relaciones

- **Padre:** [[POS-281]] Listar pedidos
- **blocks:** [[POS-285]] APP - Feat - Vers serializacion de un pedido

## Descripcion

Este recurso es idéntico al que hemos utilizado en otras aplicaciones como la de pedidos

```
GET {API_URL}/v1/orders/{pedido}/serials
```

```
[
    {
        "id": 102894,
        "description": "GABINETE SFX KIT 782 BLACK",
        "serial": "S\/N:1368900727",
        "order": "00573245",
        "outDate": "2024-02-20 00:00:00",
        "inDate": "2022-12-27 00:00:00",
        "exactTime": "2024-02-20, 04:48:45"
    },
    {
        "id": 102894,
        "description": "GABINETE SFX KIT 782 BLACK",
        "serial": "S\/N:1368901169",
        "order": "00573245",
        "outDate": "2024-02-20 00:00:00",
        "inDate": "2022-12-27 00:00:00",
        "exactTime": "2024-02-20, 04:48:47"
    },
    {
        "id": 117992,
        "description": "MOTHER GIGABYTE N5105I H + MICRO CELERON",
        "serial": "SN222360006570",
        "order": "00573245",
        "outDate": "2024-02-20 00:00:00",
        "inDate": "2023-03-28 00:00:00",
        "exactTime": "2024-02-20, 04:44:32"
    },
    {
        "id": 117992,
        "description": "MOTHER GIGABYTE N5105I H + MICRO CELERON",
        "serial": "SN222360006568",
        "order": "00573245",
        "outDate": "2024-02-20 00:00:00",
        "inDate": "2023-03-28 00:00:00",
        "exactTime": "2024-02-20, 04:44:31"
    }
]
```
