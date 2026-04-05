---
jira_key: "COB-467"
aliases: ["COB-467"]
summary: "API - Feat - Obtener pedido completo para que el que lee la cuenta corriente lo pueda visualizar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-07-30 22:19"
updated: "2024-04-16 12:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-467"
---

# COB-467: API - Feat - Obtener pedido completo para que el que lee la cuenta corriente lo pueda visualizar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-30 22:19 |
| Actualizado | 2024-04-16 12:19 |
| Etiquetas | ninguna |
| Jira | [COB-467](https://bluinc.atlassian.net/browse/COB-467) |

## Relaciones

- **Padre:** [[COB-5 - API - Feat - Obtener cuenta corriente de un cliente|COB-5]] API - Feat - Obtener cuenta corriente de un cliente

## Descripcion

Asi como lo hacemos en la API de NB para mostrar el siguiente apartado

[adjunto]
Crearemos el mismo recurso pero en este caso para mostrar en las cuentas corrientes, el contenido de cada pedido que cobramos.

[adjunto]


```
GET {API_URL}/v1/miCuenta/ordenesDeCompra/{branch}/{oder}
```

```
[
    {
        "orderId": "10281922",
        "branch": "0002",
        "clientId": "019227",
        "description": "ACCESORIOS GENERICO CABLE MONITOR VGA",
        "itemId": "111770",
        "amount": "1.000",
        "status": "P",
        "value": "18.72000",
        "iva": "21.00",
        "price": {
            "value": 18.72,
            "iva": 21,
            "finalPrice": 22.6512
        }
    },
    {
        "orderId": "10281922",
        "branch": "0002",
        "clientId": "019227",
        "description": "SSD SATA 480GB 2.5 PNY",
        "itemId": "109455",
        "amount": "1.000",
        "status": "P",
        "value": "74.36000",
        "iva": "21.00",
        "price": {
            "value": 74.36,
            "iva": 21,
            "finalPrice": 89.9756
        }
    }
]
```



Crearemos entonces el recurso

```
GET {API_URL}/v1/orders/{branch}/{oder}
```

```
[
    {
        "orderId": "10281922",
        "branch": "0002",
        "clientId": "019227",
        "description": "ACCESORIOS GENERICO CABLE MONITOR VGA",
        "itemId": "111770",
        "amount": "1.000",
        "status": "P",
        "value": "18.72000",
        "iva": "21.00",
        "price": {
            "value": 18.72,
            "iva": 21,
            "finalPrice": 22.6512
        }
    },
    {
        "orderId": "10281922",
        "branch": "0002",
        "clientId": "019227",
        "description": "SSD SATA 480GB 2.5 PNY",
        "itemId": "109455",
        "amount": "1.000",
        "status": "P",
        "value": "74.36000",
        "iva": "21.00",
        "price": {
            "value": 74.36,
            "iva": 21,
            "finalPrice": 89.9756
        }
    }
]
```
