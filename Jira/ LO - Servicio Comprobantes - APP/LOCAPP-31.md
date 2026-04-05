---
jira_key: "LOCAPP-31"
summary: "API - Feat - Agregar direccion secundaria al remito fiscal"
status: "codeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-25 14:46"
updated: "2024-03-25 17:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-31"
---

# LOCAPP-31: API - Feat - Agregar direccion secundaria al remito fiscal

| Campo | Valor |
|-------|-------|
| Estado | codeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-25 14:46 |
| Actualizado | 2024-03-25 17:09 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-31](https://bluinc.atlassian.net/browse/LOCAPP-31) |

## Descripción

Según el refactor realizado en [link](https://lioteam.atlassian.net/browse/PED-543) se debe modificar el recurso

```
GET {API_URL}/v2/dispatchVoucher/{remito}/{token}
```

para agregar los nuevos parámetros al objeto envío

```
.....

"iva105": "112,38",
"neto0": "0,00",
"iva0": "0,00",
"iibbPerception": "0,00"
},
"envio": {
"cp": "1437",
"direccion": "EXPRESO ÑANDUBAY.. Avda. Coronel Roca 3450.Nave C Módulos 64",
"localidad": "CIUDAD DE BUENOS AIRES",
"provincia": "CAPITAL FEDERAL ( CAP. FED. )",
"tel1": "(011) 3754 7220",
"addressFinal": "av. almafuerte 257", <---- NUEVO 
"postalCodeFinal": 3102, <---- NUEVO
"provinceNameFinal": "ENTRE RIOS", <---- NUEVO
"localityNameFinal": "PARANA" <---- NUEVO
},
"pie": {

.....
```

Si hay dudas de como se enlazan los nuevos datos ver recurso en la api de pedidos donde ya estan enlazados **cuando tiene una direccion y un destino final**

```
/v1/orders/{pedido}
```
