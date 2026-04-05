---
jira_key: "EXP-283"
aliases: ["EXP-283"]
summary: "API - Refactor - Permitir en el modal donde cargan los serial de \"Devoluciones\" los intervalos"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-16 09:39"
updated: "2023-05-16 15:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-283"
---

# EXP-283: API - Refactor - Permitir en el modal donde cargan los serial de "Devoluciones" los intervalos

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-16 09:39 |
| Actualizado | 2023-05-16 15:19 |
| Etiquetas | ninguna |
| Jira | [EXP-283](https://bluinc.atlassian.net/browse/EXP-283) |

## Relaciones

- **Padre:** [[EXP-119]] Feat - Acreditar un pedido parcial o totalmente

## Descripcion

Modificaremos el recurso 

```
POST {API_URL}/v1/ordersRefund/{pedido}
```

De modo tal que nos permita agregar un intervalo

Si quieren podemos charlar esto porque tiene una pequeña vuelta de tuerca de como se van agregando los seriales por front

Se agregara al modal

[adjunto]
La posibilidad de recibir intervalos como se hace en 

[adjunto]


Se trata de un recurso que nos permite dar de alta una lista de seriales a partir de dos string, uno de inicio y uno final.

**Ejemplo**:

Siendo` startSerial = MMFE8YT000095` y `endSerial = MMFE8YT000105`

Deberemos dar de alta los siguientes seriales:

```
MMFE8YT000095
MMFE8YT000096
MMFE8YT000097
MMFE8YT000098
MMFE8YT000099
MMFE8YT000100
MMFE8YT000101
MMFE8YT000102
MMFE8YT000103
MMFE8YT000104
MMFE8YT000105
```

A partir de dos input de entrada para un string se debe agregar el parametro `mode` al ejecutar el recurso [link](https://lioteam.atlassian.net/browse/EXP-125)  (de no estar presente, hacemos lo que hacemos hasta hoy)

```

    mode:interval, //indica el modo para la lista
    "serials": [
        'MMFE8YT000095',
        'MMFE8YT000105'
    ]

```
