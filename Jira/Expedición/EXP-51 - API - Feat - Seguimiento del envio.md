---
jira_key: "EXP-51"
aliases: ["EXP-51"]
summary: "API - Feat - Seguimiento del envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-09 09:01"
updated: "2023-05-29 06:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-51"
---

# EXP-51: API - Feat - Seguimiento del envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-09 09:01 |
| Actualizado | 2023-05-29 06:34 |
| Etiquetas | ninguna |
| Jira | [EXP-51](https://bluinc.atlassian.net/browse/EXP-51) |

## Relaciones

- **Padre:** [[EXP-13]] Feat - Etiquetas y seguimiento

## Descripcion

Este recurso trata sobre reutilizar recursos en el micro servicio de envíos para mostrar la ubicación y el estado actual sobre un pedido respecto al envió

```
GET {API_URL}/v1/shipments/{pedido}/tracking
```

Lo que hace es consumir el recurso en ms-envios de 

```
GET {{API_URL}}/trackingOrder/nb/0002-10296705
```

Devuelve algo así:

```
[
    {
        "state": "Finalizado",
        "brach": "New Bytes - CABA, CABA",
        "address": "Jujuy 1039, CABA, CABA",
        "date": "2022-10-31 12:00"
    },
    {
        "state": "En Proceso De Retiro - Centro De Operaciones Bs As",
        "branch": "OCA - Centro De Operaciones Bs As",
        "address": "Mariano Ferreyra 302, CABA, CABA",
        "date": "2022-11-01T14:49:25.813-03:00"
    },
    {
        "state": "Retirado En Origen - Centro De Operaciones Bs As",
        "branch": "OCA - Centro De Operaciones Bs As",
        "address": "Mariano Ferreyra 302, CABA, CABA",
        "date": "2022-11-02T14:36:17-03:00"
    },
    {
        "state": "En Proceso En Oca - Centro De Operaciones Bs As",
        "branch": "OCA - Centro De Operaciones Bs As",
        "address": "Mariano Ferreyra 302, CABA, CABA",
        "date": "2022-11-03T08:38:38.68-03:00"
    },
    {
        "state": "Procesado En Oca - Centro De Operaciones Bs As",
        "branch": "OCA - Centro De Operaciones Bs As",
        "address": "Mariano Ferreyra 302, CABA, CABA",
        "date": "2022-11-03T08:38:54.283-03:00"
    },
    {
        "state": "Arribado A Sucursal De Destino - Ushuaia",
        "branch": "OCA - Ushuaia",
        "address": "Maipu 790, Ushuaia, Tierra Del Fuego",
        "date": "2022-11-09T17:07:32.71-03:00"
    }
]
```

Entiendo que este recurso se encuentra detrás de un login. De ser así es necesario primero loguearse.

Todos los parámetros para autenticarse, así como dominios de los servicios deben estar en el archivo de variables de entorno.
