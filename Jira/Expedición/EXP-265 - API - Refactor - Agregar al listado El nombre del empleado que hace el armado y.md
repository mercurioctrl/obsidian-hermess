---
jira_key: "EXP-265"
aliases: ["EXP-265"]
summary: "API - Refactor - Agregar al listado El nombre del empleado que hace el armado y del que hace la entrega segun el token"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-30 08:51"
updated: "2023-04-17 09:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-265"
---

# EXP-265: API - Refactor - Agregar al listado El nombre del empleado que hace el armado y del que hace la entrega segun el token

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-30 08:51 |
| Actualizado | 2023-04-17 09:45 |
| Etiquetas | ninguna |
| Jira | [EXP-265](https://bluinc.atlassian.net/browse/EXP-265) |

## Relaciones

- **Padre:** [[EXP-12 - Feat - Listar pedidos para envio|EXP-12]] Feat - Listar pedidos para envio
- **blocks:** [[EXP-266 - APP - Refactor - Agregar al listado El nombre del empleado que hace el armado y|EXP-266]] APP - Refactor - Agregar al listado El nombre del empleado que hace el armado y del que hace la entrega segun el token

## Descripcion

Se deben agregar, para mostrar el nombre del empleado (basándonos en la tabla NewBytes_DBF.dbo.agentes) que hace un armado y una entrega, basándonos en el token.

```
GET {{API_URL}}/v1/shipments
```

```
GET {{API_URL}}/v1/pickUp
```

Agregaremos el objeto dos parámetros de la siguiente manera

`whoBuild` y `whoAuthorizes`

```
{
    "response": [
        {
            
            -> "whoBuild": "Diego Bordon",
            -> "whoAuthorizes": "Valeria Vommaro"
            
            "date": "2023-03-29 17:49:44",
            "pedido": "X000200554739",
            "clientId": 56073,
            "clientName": "ONLINE COMPUTERS",
            "sellerId": 30,
            "sellerName": "Albarracin Julian",
            "paymentMethod": "Dep\u00f3sito en Banco",
            "dispatch": "Envio Moto                    ",
            "statusId": 2,
            "statusDescription": "Autorizados. Pendiente a despachar",
            "order": "10308854",
            "branch": "0002",
            "cfactura": null,
            "cnumalb": "00554739",
            "fullSerialized": false,
            "currierId": 3030,
            "currierName": "",
            "placeId": 0,
            "placeName": "",
            "provinceId": 0,
            "provinceName": null,
            "zipCode": 0,
            "shippingLabel": false,
            "token": null,
            "alert": false,
            "idDirCliNbWeb": 0,
            "paymentMethodId": 3,
            "shippingStatus": null
        },
...
]
```
