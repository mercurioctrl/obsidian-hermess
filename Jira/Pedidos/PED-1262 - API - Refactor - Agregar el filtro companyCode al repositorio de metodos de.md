---
jira_key: "PED-1262"
aliases: ["PED-1262"]
summary: "API - Refactor - Agregar el filtro companyCode  al repositorio de metodos de pago y parámetro que indica si es o no un banco"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-14 08:29"
updated: "2026-01-14 14:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1262"
---

# PED-1262: API - Refactor - Agregar el filtro companyCode  al repositorio de metodos de pago y parámetro que indica si es o no un banco

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-14 08:29 |
| Actualizado | 2026-01-14 14:01 |
| Etiquetas | ninguna |
| Jira | [PED-1262](https://bluinc.atlassian.net/browse/PED-1262) |

## Relaciones

- **Padre:** [[PED-1257]] Repositorio Bancos y medios de pago
- **has action item:** [[PED-1264]] APP - Refactor - Mostrar selector de bancos solo cuando se indica para el metodo de pago seleccionado
- **has action item:** [[PED-1263]] APP - Refactor - En el modal de liquidacion, filtrar los medios de pago según el companyCode definido para el pedido

## Descripcion

Agregaremos el filtro `companyCode` al repositorio de paymentMethods, de tal modo que podamos recortar el listado que ve cada uno, según la empresa, para si mismos.

Si el parámetro esta definido, filtramos por el. Si no esta definido o es `NULL` mostraremos todos.

```
GET {API_URL}/v1/paymentMethods?companyCode{companyCode}
```

Adicionalmente tambien lo agregaremos al objeto `companyCode` y `requiresBank` que proviene de la misma tabla y sirven para asignar la empresa, y para saber si es un banco o no  (`requiresBank`) lo cual despliega la lista de bancos (hoy esto esta harcodeado en el front)

```
[
    {
        "id": 1,
        "description": "Cta. Cte Cliente",
        "authorizedExit": "SI",
        "mustInformBank": "NO",
        "directCurrentAccount": "SI",
        "idInPaymentMethods": 5,
        "visible": false,
        "interest": 0,
        "successStatus": "",
        "successStatusDetailConvert": "",
        "companyCode": 4,
        "requiresBank": false <-- Se agrega
    },
    {
        "id": 2,
        "description": "Efectivo Moto",
        "authorizedExit": "SI",
        "mustInformBank": "NO",
        "directCurrentAccount": "NO",
        "idInPaymentMethods": 1,
        "visible": false,
        "interest": 0,
        "successStatus": "",
        "successStatusDetailConvert": "",
        "companyCode": 4,
        "requiresBank": false <-- Se agrega
    },
    {
        "id": 3,
        "description": "Dep\u00f3sito en Banco",
        "authorizedExit": "NO",
        "mustInformBank": "SI",
        "directCurrentAccount": "NO",
        "idInPaymentMethods": 7,
        "visible": true,
        "interest": 0,
        "successStatus": "",
        "successStatusDetailConvert": "",
        "companyCode": 4,
        "requiresBank": true <-- Se agrega
    },
...
]
```
