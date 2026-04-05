---
jira_key: "NBWEB-976"
aliases: ["NBWEB-976"]
summary: "API - Refactor - Agregar percepciones en pedidos dentro de mi cuenta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-06-24 10:05"
updated: "2025-07-04 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-976"
---

# NBWEB-976: API - Refactor - Agregar percepciones en pedidos dentro de mi cuenta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-06-24 10:05 |
| Actualizado | 2025-07-04 10:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-976](https://bluinc.atlassian.net/browse/NBWEB-976) |

## Relaciones

- **Padre:** [[NBWEB-946 - Mi Cuenta|NBWEB-946]] Mi Cuenta
- **has action item:** [[NBWEB-977 - APP - Refactor - Agregar percepciones en pedidos dentro de mi cuenta|NBWEB-977]] APP - Refactor - Agregar percepciones en pedidos dentro de mi cuenta
- **has action item:** [[SNB-3182 - la web no muestra percepçion|SNB-3182]] la web no muestra percepçion

## Descripcion

Siguiendo la linea de lo realizado para ordenes, agregaremos el parámetro tambien en los pedidos

```
GET {API_URL}/v1/miCuenta/pedidos?limit=10&offset=0
```

```
[
    {
        "status": "1",
        "branch": "0002",
        "albNumber": "00621976",
        "clientName": "AVINCETTO LEONARDO OSCAR",
        "clientId": 13151,
        "subtotal": {
            "currencyQuote": 1185,
            "subtotalDollar": 938.74115,
            "subtotalDollarFinal": 1117.077781, <-- SE SUMA PER
            "subTotalPesosAr": 1112408.26275,
            "subTotalPesosArFinal": 1323737.170485, <-- SE SUMA PER
            "perception": 37.549646 <-- NUEVO,
            "perceptionPesosAr": 44496.33 <-- NUEVO
        },
        "date": "23-06-2025",
        "statusId": 4,
        "statusDescription": "Armado Finalizado"
    },
    {
        "status": "1",
        "branch": "0002",
        "albNumber": "00621635",
        "clientName": "AVINCETTO LEONARDO OSCAR",
        "clientId": 13151,
        "subtotal": {
            "currencyQuote": 1170,
            "subtotalDollar": 385.9658,
            "subtotalDollarFinal": 437.787689,
            "subTotalPesosAr": 451579.986,
            "subTotalPesosArFinal": 512211.59613
        },
        "date": "19-06-2025",
        "statusId": 13,
        "statusDescription": "Entregado Cobrado"
    },
    {
    
    ....
```
