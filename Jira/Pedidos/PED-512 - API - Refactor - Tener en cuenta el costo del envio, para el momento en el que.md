---
jira_key: "PED-512"
aliases: ["PED-512"]
summary: "API - Refactor - Tener en cuenta el costo del envio, para el momento en el que liquidemos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-24 08:18"
updated: "2024-01-30 05:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-512"
---

# PED-512: API - Refactor - Tener en cuenta el costo del envio, para el momento en el que liquidemos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-24 08:18 |
| Actualizado | 2024-01-30 05:39 |
| Etiquetas | ninguna |
| Jira | [PED-512](https://bluinc.atlassian.net/browse/PED-512) |

## Relaciones

- **Padre:** [[PED-58 - Agregar Editar Envío en las ordenes de compra|PED-58]] Agregar / Editar Envío en las ordenes de compra

## Descripcion

Dado que al cotizar un envió con el recurso 

```
{{API_URL}}/order/nb/{orde}/cp/{cp}
```

```
[
    {
        "id": 4069,
        "costo": 6954, <-----
        "descripcion": "A domicilio por Entregar",
        "precio": 8414,
        "plazoEntrega": "entre el lunes 29 y el miércoles 31",
        "plazoEntregaNumero": 5,
        "total": 6954
    },
    {
        "id": 4041,
        "costo": 541140.69, <-----
        "descripcion": "A domicilio por OCA",
        "precio": 541140.69,
        "plazoEntrega": "entre el viernes 26 y el martes 30",
        "plazoEntregaNumero": 2,
        "total": 541140.69
    }
]
```

Se tiene en cuenta el costo, quizás al momento de agregarlo en el pedido necesitemos guardarlo.

Para esto podemos usar `[NewBytes_DBF].[dbo].[pedclil].ncostoextra` donde podemos guardarlo incialmente.

Luego transmitirlo a `[NewBytes_DBF].[dbo].[albclil].ncostoextra`

Y Finalmente podremos setearlo de la forma correcta en `[NEW_BYTES].[dbo].[MS_REMITO_DETALLE_GANANCIA_ENLACE].COSTO` pudiendo hacer los calculos correctos en la misma tabla, pero teniendo en cuenta el costo real de cada envío y no el que esta cargado fijo en el sistema.
