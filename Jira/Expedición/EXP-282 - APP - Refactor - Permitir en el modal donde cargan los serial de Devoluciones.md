---
jira_key: "EXP-282"
aliases: ["EXP-282"]
summary: "APP - Refactor - Permitir en el modal donde cargan los serial de \"Devoluciones\" los intervalos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-05-16 09:34"
updated: "2023-06-05 08:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-282"
---

# EXP-282: APP - Refactor - Permitir en el modal donde cargan los serial de "Devoluciones" los intervalos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-16 09:34 |
| Actualizado | 2023-06-05 08:57 |
| Etiquetas | ninguna |
| Jira | [EXP-282](https://bluinc.atlassian.net/browse/EXP-282) |

## Relaciones

- **Padre:** [[EXP-119]] Feat - Acreditar un pedido parcial o totalmente

## Descripcion

Si quieren podemos charlar esto porque tiene una pequeña vuelta de tuerca de como se van agregando los seriales por front

Agregaremos al modal 

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
