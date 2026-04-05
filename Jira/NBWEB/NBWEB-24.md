---
jira_key: "NBWEB-24"
summary: "Detalle Ordenes de Compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-25 08:15"
updated: "2022-06-26 20:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-24"
---

# NBWEB-24: Detalle Ordenes de Compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-25 08:15 |
| Actualizado | 2022-06-26 20:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-24](https://bluinc.atlassian.net/browse/NBWEB-24) |

## Descripción

Se trata del recurso para obtener del detalle de una orden de compra

```
GET {{API_URL}}/v1/miCuenta/OrdenesDeCompra/{branch}/{orderNumber}
```

Retorna un array de objetos con los productos que contiene la orden de compra



```json
[
    {
        "branch": "0002",
        "orderId": "10264134",
        "clienId": "040687",
        "itemId": "103177",
        "description": "GABINETE THERMALTAKE H200 TG RGB BLACK",
        "amount": "3.000",
        "status": "P",
        "Price":{
          "value":"53.56365",
          "iva":10.5,
          "finalPrice":59.187833250000004
        } 
    },
   {
        "branch": "0002",
        "orderId": "10264134",
        "clienId": "040687",
        "itemId": "103177",
        "description": "GABINETE THERMALTAKE H200 TG RGB BLACK",
        "amount": "3.000",
        "status": "P",
        "Price":{
          "value":"53.56365",
          "iva":10.5,
          "finalPrice":59.187833250000004
        } 
    }
]
```
