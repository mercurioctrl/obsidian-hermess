---
jira_key: "NBWEB-915"
summary: "API - Refactor - Agregar internalTax dentro del detalle de las ordenes, tanto al monto final como el parametro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-04 18:02"
updated: "2024-11-06 03:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-915"
---

# NBWEB-915: API - Refactor - Agregar internalTax dentro del detalle de las ordenes, tanto al monto final como el parametro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-04 18:02 |
| Actualizado | 2024-11-06 03:13 |
| Etiquetas | ninguna |
| Jira | [NBWEB-915](https://bluinc.atlassian.net/browse/NBWEB-915) |

## Descripción

```
GET {API_URL}/v1/miCuenta/ordenesDeCompra/{branch}/{order}
```

```
[
    {
        "orderId": "10337209",
        "branch": "0000",
        "clientId": 19227,
        "description": "MINI PC GIGABYTE BRIX BSRE-1505 (AMD Ryzen 1505G)",
        "itemId": 116741,
        "amount": 1,
        "status": 1,
        "price": {
            "value": 372.08481,
            "iva": 10.5,
            "internalTax": 23.43, <- SE AGREGA 
            "finalPrice": 411.15371505 <- SE SUMA EL MONTO SI EXISTE
        }
    }
]
```
