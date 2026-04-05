---
jira_key: "PED-116"
aliases: ["PED-116"]
summary: "API - Feat - Realizar seguimiento de una orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-03 10:17"
updated: "2023-10-05 13:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-116"
---

# PED-116: API - Feat - Realizar seguimiento de una orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-03 10:17 |
| Actualizado | 2023-10-05 13:41 |
| Etiquetas | ninguna |
| Jira | [PED-116](https://bluinc.atlassian.net/browse/PED-116) |

## Relaciones

- **Padre:** [[PED-58]] Agregar / Editar Envío en las ordenes de compra

## Descripcion

Este recurso sirve para poder hacer tracking del envio de una orden.

Por detrás, puede conectarse al servicio del mismo modo que se hace en exp

```
GET {{API_URL}}/order/{branch}-{order}/trackingShipping
```

Devuelve

```json
[
    {
        "state": "Entregado Cobrado",
        "brach": "New Bytes - CABA, CABA",
        "address": "Jujuy 1039, CABA, CABA",
        "date": "2023-09-22 12:00"
    },
    {
        "state": "En Proceso De Retiro - Centro De Operaciones Bs As",
        "branch": "OCA - Centro De Operaciones Bs As",
        "address": "Mariano Ferreyra 302, CABA, CABA",
        "date": "2023-09-26T09:33:54.047-03:00"
    },
    {
        "state": "En Proceso En Oca - Centro De Operaciones Bs As",
        "branch": "OCA - Centro De Operaciones Bs As",
        "address": "Mariano Ferreyra 302, CABA, CABA",
        "date": "2023-09-27T00:02:24.19-03:00"
    },
    {
        "state": "En Proceso En Oca - Centro De Operaciones Bs As",
        "branch": "OCA - Centro De Operaciones Bs As",
        "address": "Mariano Ferreyra 302, CABA, CABA",
        "date": "2023-09-27T00:02:36.61-03:00"
    },
    {
        "state": "Procesado En Oca - Centro De Operaciones Bs As",
        "branch": "OCA - Centro De Operaciones Bs As",
        "address": "Mariano Ferreyra 302, CABA, CABA",
        "date": "2023-09-27T00:03:35.007-03:00"
    },
    {
        "state": "Arribado A Centro De Distribuci\u00f3n De Destino - Luis Guillon",
        "branch": "OCA - Luis Guillon",
        "address": "Boulevard Bs. As. 1459, Bs As, Buenos Aires",
        "date": "2023-09-27T05:44:59.943-03:00"
    },
    {
        "state": "Programado Para Visita A Domicilio - Luis Guillon",
        "branch": "OCA - Luis Guillon",
        "address": "Boulevard Bs. As. 1459, Bs As, Buenos Aires",
        "date": "2023-09-27T06:25:09.47-03:00"
    },
    {
        "state": "Visita A Domicilio En Curso - Luis Guillon",
        "branch": "OCA - Luis Guillon",
        "address": "Boulevard Bs. As. 1459, Bs As, Buenos Aires",
        "date": "2023-09-27T08:19:35.713-03:00"
    },
    {
        "state": "Estado De Visita Online (sin Motivo) - Luis Guillon",
        "branch": "OCA - Luis Guillon",
        "address": "Boulevard Bs. As. 1459, Bs As, Buenos Aires",
        "date": "2023-09-27T14:46:57-03:00"
    },
    {
        "state": "Entregado - Luis Guillon",
        "branch": "OCA - Luis Guillon",
        "address": "Boulevard Bs. As. 1459, Bs As, Buenos Aires",
        "date": "2023-09-27T14:46:59-03:00"
    }
]
```
