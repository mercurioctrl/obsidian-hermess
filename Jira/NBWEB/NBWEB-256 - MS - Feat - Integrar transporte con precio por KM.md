---
jira_key: "NBWEB-256"
aliases: ["NBWEB-256"]
summary: "MS - Feat - Integrar transporte con precio por KM"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-14 09:07"
updated: "2022-06-26 20:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-256"
---

# NBWEB-256: MS - Feat - Integrar transporte con precio por KM

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-14 09:07 |
| Actualizado | 2022-06-26 20:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-256](https://bluinc.atlassian.net/browse/NBWEB-256) |

## Relaciones

- **Padre:** [[NBWEB-76]] API - Implementar MS envios
- **relates to:** [[NBWEB-250]] MS - Research - Obtener la distancia entre dos puntos

## Descripcion

```
{{API_URL}}/order/nb/{branch}-{order}/cp/{cp destino}
```

###### *Tambien debe volver con el resto de los recursos de cotizacion

Retorna algo similar a

```
[
{
        "costo": 2342,
        "descripcion": "Transporte Camioneta",
        "id": {nuevoId},
        "precio": "2342",
        "plazoEntrega": "",
        "plazoEntregaNumero": 0,
        "total": 2342
    },
    {
        "costo": 541.55,
        "descripcion": "Envio OCA a domicilio",
        "id": 4041,
        "precio": "541.5500",
        "plazoEntrega": "el viernes 17",
        "plazoEntregaNumero": 3,
        "total": 541.55
    },
    {
        "costo": 1545.81,
        "descripcion": "Andreani a domicilio",
        "id": 4065,
        "precio": 1545.81,
        "plazoEntrega": "hoy",
        "plazoEntregaNumero": 0,
        "total": 1545.81
    },
    {
        "costo": 300,
        "descripcion": "Moto (Capital Federal).",
        "precio": 300,
        "plazoEntrega": "hoy",
        "plazoEntregaNumero": 0,
        "total": 300
    }
]
```



Crearemos un nuevo repositorio de cotización de envíos (Logística Interna) en donde la cotización se realiza a partir de los km recorridos.

Para esto agregaremos una columna, dentro de la tabla de medios de envió (`kmPrice`).

Por otro lado se debe generar un metodo para poder obtener la distancia entre dos puntos (podemos verlo en la daily) y a su vez, una nueva tabla `distances` del lado del micro servicio con las siguientes columnas mínimas

- id


- cpHost


- cp


- distanceKm


- lastDate



Basados en la idea de que las distancias entre dos códigos postales no cambian, solo deberemos obtenerlas de una sola vez, ahorrando costos en caso de que consumamos un API que es paga.

Por esto, al momento de cotizar, debemos primero verificar que la relación entre `cpHost` y `cp` no se encuentra en la tabla.

Si no esta, se debe obtener.

Si esta, se debe utilizar multiplicando el precio por Km del medio de envío, por la cantidad de km para devolver un objeto del siguiente tipo

```
{
        "costo": 2342,
        "descripcion": "Transporte Camioneta",
        "id": {nuevoId},
        "precio": "2342",
        "plazoEntrega": "",
        "plazoEntregaNumero": 0,
        "total": 2342
    },
```
