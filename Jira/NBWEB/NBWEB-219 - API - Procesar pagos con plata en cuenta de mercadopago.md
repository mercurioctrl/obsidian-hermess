---
jira_key: "NBWEB-219"
aliases: ["NBWEB-219"]
summary: "API - Procesar pagos con plata en cuenta de mercadopago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-01 16:46"
updated: "2022-06-26 21:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-219"
---

# NBWEB-219: API - Procesar pagos con plata en cuenta de mercadopago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-01 16:46 |
| Actualizado | 2022-06-26 21:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-219](https://bluinc.atlassian.net/browse/NBWEB-219) |

## Relaciones

- **Padre:** [[NBWEB-77 - Implementar Pagos|NBWEB-77]] Implementar Pagos
- **relates to:** [[NBWEB-221 - APP - Formulario para pagos MP tarjeta y plata en cuenta|NBWEB-221]] APP - Formulario para pagos MP tarjeta y plata en cuenta
- **blocks:** [[NBWEB-242 - APP - Procesar pago con tarjeta y plata en cuenta de mp|NBWEB-242]] APP - Procesar pago con tarjeta y plata en cuenta de mp

## Descripcion

```
POST {{API_URL}}/v1/carrito/processPreferenceMP
```

Recibe:

```
{
    "title": "00491810" // numero de Orden de Compra,
    "quantity": 1 // esto no se toca queda en 1,
    "unit_price": 1 // precio total de la compra,
    "clientId": 254335,
    "orderId": "00491810",
    "branch": "0002"
}
```

Retorna



```
{
    "preference_id": "237836675-7877471d-25fb-4530-b1c2-77a6fe507761"
}
```
