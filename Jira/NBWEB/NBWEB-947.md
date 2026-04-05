---
jira_key: "NBWEB-947"
summary: "API - Refactor - Agregar a la lista de pedidos el estado del mismo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-05 16:58"
updated: "2025-02-11 04:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-947"
---

# NBWEB-947: API - Refactor - Agregar a la lista de pedidos el estado del mismo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-05 16:58 |
| Actualizado | 2025-02-11 04:06 |
| Etiquetas | ninguna |
| Jira | [NBWEB-947](https://bluinc.atlassian.net/browse/NBWEB-947) |

## Descripción

```
GET {API_URL}/v1/miCuenta/pedidos
```

```
[
    {
        "status": "1",
        "branch": "0002",
        "albNumber": "00600152",
        "clientName": "Catriel (no usar)",
        "clientId": 19227,
        "statusId": 2, <<--- SE AGREGA
        "statusDescription": "Autorizados. Pendiente a despachar",  <<--- SE AGREGA
        "subtotal": {
            "currencyQuote": 1073.5,
            "subtotalDollar": 9.17073,
            "subtotalDollarFinal": 11.096583,
            "subTotalPesosAr": 9844.778655,
            "subTotalPesosArFinal": 11912.181850500001
        },
        "date": "04-12-2024"
    },
    {
        "status": "1",
        "branch": "0002",
        "albNumber": "00599099",
        "clientName": "Catriel (no usar)",
        "clientId": 19227,
        "statusId": 2, <<--- SE AGREGA
        "statusDescription": "Autorizados. Pendiente a despachar",  <<--- SE AGREGA
```
