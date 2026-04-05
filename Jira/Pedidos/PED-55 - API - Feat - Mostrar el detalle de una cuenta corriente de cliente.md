---
jira_key: "PED-55"
aliases: ["PED-55"]
summary: "API - Feat - Mostrar el detalle de una cuenta corriente de cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-09-07 08:37"
updated: "2024-05-03 18:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-55"
---

# PED-55: API - Feat - Mostrar el detalle de una cuenta corriente de cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-07 08:37 |
| Actualizado | 2024-05-03 18:21 |
| Etiquetas | ninguna |
| Jira | [PED-55](https://bluinc.atlassian.net/browse/PED-55) |

## Relaciones

- **Padre:** [[PED-54 - Cuenta corriente de clientes|PED-54]] Cuenta corriente de clientes
- **is blocked by:** [[PED-53 - Migracion a Laravel|PED-53]] Migracion a Laravel
- **blocks:** [[PED-61 - APP - Feat - Mostrar cuenta corriente para un cliente determinado|PED-61]] APP - Feat - Mostrar cuenta corriente para un cliente determinado
- **relates to:** [[SNB-1872 - me toma el valor en pesos de nota de crédito en dolares.|SNB-1872]] me toma el valor en pesos de nota de crédito en dolares.

## Descripcion

Asi como lo hicimos en el sistema de caja ([link](https://lioteam.atlassian.net/browse/COB-5?jql=text%20~%20%22cuenta%20corriente%22%20AND%20project%20IN%20(10049)) ), necesitaremos el recurso para leer cuenta corriente

```
GET {API_URL}/v1/currentAccount/{clientId}
```

```json
[
 {
            "date": "2021-12-28",
            "albNumber": "00019696",
            "total": -47.770874,
            "currencyQuote": 107.5,
            "agent": "Seba",
            "agentDescription": "Web Sistema",
            "branch": "0010",
            "comment": "Se debe enviar a, Localidad: ACOSTILLA, Provincia: CATAMARCA, Telefono:, ",
            "currentBalance": -41.450874,
            "currencyQuoteDay": 395,
            "currencyQuoteDayCheck": 465.75,
            "subTotal": -47.770874,
            "totalPesos": -5135.368955,
            "id": 630013,
            "notFiscalId": null,
            "voucherId": null,
            "token": null,
            "availableBalance": -41.450874,
            "dollarQuote": null,
            "availableBalancePesos": -16165.84086,
            "trCode": 24,
            "trName": "Remitos - Ventas",
            "order": null
        },
        {
            "date": "2023-04-23",
            "albNumber": null,
            "total": 1,
            "currencyQuote": 226,
            "agent": "Seba",
            "agentDescription": "Web Sistema",
            "branch": null,
            "comment": "esto es una prueba de sistemas",
            "currentBalance": -41.450874,
            "currencyQuoteDay": 395,
            "currencyQuoteDayCheck": 465.75,
            "subTotal": -46.770874,
            "totalPesos": 226,
            "id": 708394,
            "notFiscalId": 708394,
            "voucherId": null,
            "token": null,
            "availableBalance": -41.450874,
            "dollarQuote": null,
            "availableBalancePesos": -16165.84086,
            "trCode": 42,
            "trName": "Cobro Efectivo Caja",
            "order": null
        }
]
```

Esto se pude hacer leyendo el recurso, o trayéndose el repositorio a a la nueva aplicaicon
