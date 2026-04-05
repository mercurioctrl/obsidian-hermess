---
jira_key: "NBWEB-974"
aliases: ["NBWEB-974"]
summary: "API - Refactor - Mis ordenes de compra - Revision de totales e incorporación de percepciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-24 09:41"
updated: "2025-07-08 10:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-974"
---

# NBWEB-974: API - Refactor - Mis ordenes de compra - Revision de totales e incorporación de percepciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-24 09:41 |
| Actualizado | 2025-07-08 10:40 |
| Etiquetas | ninguna |
| Jira | [NBWEB-974](https://bluinc.atlassian.net/browse/NBWEB-974) |

## Relaciones

- **Padre:** [[NBWEB-946]] Mi Cuenta
- **has action item:** [[SNB-3182]] la web no muestra percepçion
- **has action item:** [[NBWEB-975]] APP - Refactor - Agregar percepciones al modal de ordenes en mi cuenta

## Descripcion

Siguiendo lo relatado en [link](https://bluinc.atlassian.net/jira/servicedesk/projects/SNB/queues/custom/63/[[SNB-3182]])  vimos algunos refactor necesarios para mostrar bien la información en mi cuenta tanto en el listado de ordenes de compra, como en el detalle de las ordenes en si.

Refactorizaremos el siguiente recurso

```
GET {API_URL}/v1/miCuenta/ordenesDeCompra?limit=10&offset=0
```

## ¿Que debemos realizar?

Arreglar pequeño bug que multiplica los totalesAl ver el pedido `"orderNumber": "10414168"` de `Avincetto` notamos que el total, parece estar multiplicado x3. Es probable que algo de la query este molestando en la suma.

```
[
    {
        "status": 2,
        "branch": "0002",
        "orderNumber": "10414168",
        "clientName": "AVINCETTO LEONARDO OSCAR",
        "userName": "lylcomputacion",
        "clientId": 13151,
        "subtotal": {
            "currencyQuote": 1185,
            "subtotalDollar": 2816.22345,
            "subtotalDollarFinal": 3351.233343,
            "subTotalPesosAr": 3337224.7882499998,
            "subTotalPesosArFinal": 3971211.511455
        },
        "date": "21-06-2025",
        "trackingNumber": null,
        "secretKey": "ciruela",
        "deliveryMethodDescription": "Retiro de cliente en Local",
        "deliveryMethodId": 1,
        "paymentVoucher": true,
        "paymentMethodId": "3",
        "dropShipping": false
    },
    {
        "status": 2,
        "branch": "0002",
        ...
```

Agregar percepciones sumadas para el detalle de la orden tal cual lo hacemos en “pedidos” y tambien lo agregaremos a los totales `subtotalDollarFinal` y `subTotalPesosArFinal````
...
{
        "status": 2,
        "branch": "0002",
        "orderNumber": "10414168",
        "clientName": "AVINCETTO LEONARDO OSCAR",
        "userName": "lylcomputacion",
        "clientId": 13151,
        "subtotal": {
            "currencyQuote": 1185,
            "subtotalDollar": 2816.22345,
            "subtotalDollarFinal": 3351.233343, <-=-- SE SUMA PER
            "subTotalPesosAr": 3337224.7882499998,
            "subTotalPesosArFinal": 3971211.511455, <--- SE SUMA PER
            "perception": 37.549646 <-- NUEVO,
            "perceptionPesosAr": 44496.33 <-- NUEVO
        },
        "date": "21-06-2025",
        "trackingNumber": null,
        "secretKey": "ciruela",
        "deliveryMethodDescription": "
...        
```
