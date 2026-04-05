---
jira_key: "NBWEB-914"
aliases: ["NBWEB-914"]
summary: "API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-04 18:00"
updated: "2024-11-06 03:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-914"
---

# NBWEB-914: API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-04 18:00 |
| Actualizado | 2024-11-06 03:07 |
| Etiquetas | ninguna |
| Jira | [NBWEB-914](https://bluinc.atlassian.net/browse/NBWEB-914) |

## Relaciones

- **Padre:** [[NBWEB-610 - API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro|NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta

## Descripcion

```
GET {API_URL}/v1/miCuenta/ordenesDeCompra
```

```
[
    {
        "status": "1",
        "branch": "0002",
        "albNumber": "00571746",
        "clientName": "Catriel (no usar)",
        "clientId": 19227,
        "subtotal": {
            "currencyQuote": 1013,
            "subtotalDollar": 1.45991,
            "subtotalDollarFinal": 1.7664911, <--- lo sumaremos al monto final si existe
            "subTotalPesosAr": 1478.88883,
            "subTotalPesosArFinal": 1789.4554843 <--- lo sumaremos al monto final si existe
        },
        "date": "24-01-2024"
    },
    {
        "status": "3",
        "branch": "0002",
```
