---
jira_key: "NBWEB-571"
summary: "API - Refactor -  Cambio de las rutas para poder ver comprobantes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2023-08-02 10:12"
updated: "2023-08-02 11:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-571"
---

# NBWEB-571: API - Refactor -  Cambio de las rutas para poder ver comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2023-08-02 10:12 |
| Actualizado | 2023-08-02 11:15 |
| Etiquetas | ninguna |
| Jira | [NBWEB-571](https://bluinc.atlassian.net/browse/NBWEB-571) |

## Descripción

Al estar dentro de mi cuenta y querer obtener los comprobantes
`https://webapi.nb.com.ar/v1/miCuenta/comprobantes?limit=10&offset=0`
{
    "cae": 71508481965231,
    "branch": "0003",
    "invoiceNumber": "00030421",
    "invoiceType": "B",
    "invoiceDate": "2021-12-16",
    "invoiceLabel": "FACTURA",
    "clientName": "marbe moreno",
    "clientId": 46930,
    "subtotal": {
        "currencyQuote": 103.5,
        "subTotal": 122.96000000000001,
        "subTotalIva": 148.7816,
        "perceptionsIIBB": 0,
        "subTotalFinal": 148.7816,
        "currency": "DOL"
    },
    "voucherId": 464327,
  **  "voucherUrl": "****[https://comprobantes.lio.red/?F=464327&show=1&token=2e6d4d09609283308b316f4e68a7fd95%22](https://comprobantes.lio.red/?F=464327&show=1&token=2e6d4d09609283308b316f4e68a7fd95%22)**** **
}

Debe modificarse la url devuelta en voucherUrl por algo como


```
voucher/F/{Id}/{token}
```

[https://omega.comprobantes.lio.red/voucher/F/510648/4cfd384be3b640189362af099de8bb?show=1](https://omega.comprobantes.lio.red/voucher/F/510648/4cfd384be3b640189362af099de8bb?show=1)
