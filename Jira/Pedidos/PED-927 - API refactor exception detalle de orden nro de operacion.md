---
jira_key: "PED-927"
aliases: ["PED-927"]
summary: "API refactor exception detalle de orden nro de operacion "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-01-07 18:01"
updated: "2025-01-27 17:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-927"
---

# PED-927: API refactor exception detalle de orden nro de operacion 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-01-07 18:01 |
| Actualizado | 2025-01-27 17:32 |
| Etiquetas | ninguna |
| Jira | [PED-927](https://bluinc.atlassian.net/browse/PED-927) |

## Relaciones

- **action item from:** [[SNB-2694]] numero de pago

## Descripcion

Se debe detallar las ordenes que tengan el mismo numero de operacion en caso de ser asi

POST /v1/paymentForBank

payload

```
{
    "pedido":"X000200534676",
...

}
```



Response:

```
{
   "errors": {
      "status": 400,
      "title": "Existen varias ordenes con el mismo nro de operación. Pedidos: (order:10273488, suc:0002), (order:10273488, suc:0002)",
    ...
   }
}
```
