---
jira_key: "NBWEB-917"
aliases: ["NBWEB-917"]
summary: "API - Refactor - Agregar internalTax dentro del detalle de PEDIDOS, tanto al monto final como el parametro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-04 18:06"
updated: "2024-11-06 03:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-917"
---

# NBWEB-917: API - Refactor - Agregar internalTax dentro del detalle de PEDIDOS, tanto al monto final como el parametro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-04 18:06 |
| Actualizado | 2024-11-06 03:21 |
| Etiquetas | ninguna |
| Jira | [NBWEB-917](https://bluinc.atlassian.net/browse/NBWEB-917) |

## Relaciones

- **Padre:** [[NBWEB-610 - API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro|NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta

## Descripcion

```
GET /v1/miCuenta/pedidos/{branch}/{order}
```

```
[
    {
        "branch": "0002",
        "albNumber": "00571746",
        "clientId": 19227,
        "productId": "102405",
        "description": "ANBYTE CABLE IMPRESORA USB A\/B 2.0 1.55M AZUL ICTC",
        "amount": "1.000",
        "price": {
            "value": 1.45991,
            "iva": 21,
            "internalTax": 32,34 <- Se agrega el parametro
            "finalPrice": 1.7664911 <- Se suma al monto final
        },
        "currencyQuote": 0,
        "perception": 0
    }
]
```
