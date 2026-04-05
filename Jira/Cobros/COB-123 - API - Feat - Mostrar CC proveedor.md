---
jira_key: "COB-123"
aliases: ["COB-123"]
summary: "API - Feat - Mostrar CC proveedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-28 22:07"
updated: "2024-02-13 03:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-123"
---

# COB-123: API - Feat - Mostrar CC proveedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-28 22:07 |
| Actualizado | 2024-02-13 03:48 |
| Etiquetas | ninguna |
| Jira | [COB-123](https://bluinc.atlassian.net/browse/COB-123) |

## Relaciones

- **Padre:** [[COB-114 - Feat - Ver cuentas proveedores|COB-114]] Feat - Ver cuentas proveedores

## Descripcion

Para desarrollar esta historia de intentara replicar la lógica existente en la vista de CC (cuenta corriente) de cliente, donde al hacer clic en el nombre de un cliente desplegamos un modal con los movimientos de la cuenta [link](https://lioteam.atlassian.net/browse/COB-5)

Para esto, tomaremos el valor inicial `SaldoInicialCTA` de [link](https://lioteam.atlassian.net/browse/COB-68) y lo utilizaremos como saldo inicial para empezar a calcular los subtotales.

Haremos un pequeño “research” sobre las bases de datos por si llegara a existir una estructura existente de esto (aunque parecer ser que no). De lo contrario replicaremos una estructura similar a la tabla `MC_CCORRIENTES_MOVIMIENTOS` de los clientes, pero para proveedores.

```
GET {API_RUL}/v1/currentAccountProvider/{providerId}
```

```
 [
        {
            "date": "20170315",
            "providersOrdersId": "00326440",
            "total": -921.25999999999999,
            "currencyQuote": 15.81,
            "agent": "VENTAS3",
            "comment": "Aca un texto o comentario",
            "currentBalance": 2.0800000000001546,
            "currencyQuoteDay": 136.0,
            "currencyQuoteDayCheck": 146.06,
            "subTotal": "-63146,01",
            "id": 300399   
        },
        {
            "date": "20170315",
            "providersOrdersId": "00326440",
            "total": -921.25999999999999,
            "currencyQuote": 15.81,
            "agent": "VENTAS3",
            "comment": "Aca un texto o comentario",
            "currentBalance": 2.0800000000001546,
            "currencyQuoteDay": 136.0,
            "currencyQuoteDayCheck": 146.06,
            "subTotal": "-63146,01",
            "id": 300399   
        }
  ]
```
