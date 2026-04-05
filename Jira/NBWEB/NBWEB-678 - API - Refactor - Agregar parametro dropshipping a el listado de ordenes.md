---
jira_key: "NBWEB-678"
aliases: ["NBWEB-678"]
summary: "API - Refactor - Agregar parametro dropshipping a el listado de ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-03 09:10"
updated: "2024-04-15 02:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-678"
---

# NBWEB-678: API - Refactor - Agregar parametro dropshipping a el listado de ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-03 09:10 |
| Actualizado | 2024-04-15 02:14 |
| Etiquetas | ninguna |
| Jira | [NBWEB-678](https://bluinc.atlassian.net/browse/NBWEB-678) |

## Relaciones

- **Padre:** [[NBWEB-610 - API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro|NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta
- **blocks:** [[NBWEB-679 - APP - Refactor - Agregar parámetro dropshipping a el listado de ordenes|NBWEB-679]] APP - Refactor - Agregar parámetro dropshipping a el listado de ordenes

## Descripcion

```
GET {API_URL}/v1/miCuenta/ordenesDeCompra
```

```
...

      "paymentMethodId": null
    },
    {
        "status": 1,
        "branch": "0002",
        "orderNumber": "10336733",
        "clientName": "Catriel (no usar)",
        "userName": "catriel",
        "clientId": 19227,
        "subtotal": {
            "currencyQuote": 877,
            "subtotalDollar": 4.66289,
            "subtotalDollarFinal": 5.6420969,
            "subTotalPesosAr": 4089.35453,
            "subTotalPesosArFinal": 4948.1189813
        },
        "date": "25-01-2024",
        "trackingNumber": null,
        "secretKey": "molusco",
        "paymentVoucher": false,
        "paymentMethodId": null,
        "dropShipping": true/false <-- nuevo parametro
        
    }
]
```

```
SELECT 
      [dropShipping]
  FROM [NewBytes_DBF].[dbo].[pedclit]
```
