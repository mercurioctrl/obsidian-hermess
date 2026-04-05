---
jira_key: "PED-994"
aliases: ["PED-994"]
summary: "API - Refactor - Agregar percepciones ARBA al \"pedido + INFO\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-25 08:17"
updated: "2025-05-07 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-994"
---

# PED-994: API - Refactor - Agregar percepciones ARBA al "pedido + INFO"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-25 08:17 |
| Actualizado | 2025-05-07 10:42 |
| Etiquetas | ninguna |
| Jira | [PED-994](https://bluinc.atlassian.net/browse/PED-994) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **action item from:** [[PED-992 - API - Refactor - Agregar percepciones ARBA como un atributo diferenciado al|PED-992]] API - Refactor - Agregar percepciones ARBA como un atributo diferenciado al momento de ver el detalle de una orden
- **has action item:** [[PED-995 - APP - Refactor - Agregar percepciones ARBA al pedido + INFO|PED-995]] APP - Refactor - Agregar percepciones ARBA al "pedido + INFO"

## Descripcion

Así como lo hicimos en el detalle de la orden, agregaremos tambien el parámetro en el recurso para construir el pedido mas info y los presupuestos

Para esto agregaremos un nuevo atributo llamado `percepcion_arba`que funciona como `percepcion` pero para el caso de ARBA. Si no tiene, es cero.

```
GET {API_URL}/v1/aboutOrder/{branch-order}
```

```
{
    "info": {
        "clientId": 25584,
        "clientDescription": "MARCOMP S.R.L.",
        "seller": "Lautaro Soto",
        "order": "10403641",
        "branch": "0002",
        "remit": "X000200614857",
        "niva": null,
        "telephone": ""
    },
    "shipping": {
        "province": "",
        "city": "",
        "codePostal": 0,
        "carrierName": "",
        "address": "",
        "addressFinal": "",
        "postalCodeFinal": "",
        "provinceNameFinal": "",
        "localityNameFinal": ""
    },
    "items": [
        {
            "count": 1,
            "description": "MEMORIA ADATA SODIMM DDR4 16GB 3200 G22 SGN",
            "price": 26.9516,
            "iva": 10.5,
            "quote": 1215,
            "perception": 3,
            "perceptionArba": 6,  <-- Se agrega porcentual
            "internalTax": 0
        },
        {
            "count": 2,
            "description": "MEMORIA ADATA DIMM XPG 16GB 16A DDR4 3200 D35",
            "price": 30.0504,
            "iva": 10.5,
            "quote": 1215,
            "perception": 3,
            "perceptionArba": 6,  <-- Se agrega porcentual
            "internalTax": 0
        },
        {
            "count": 3,
            "description": "DISCO SSD ADATA LEGEND 710 512GB M2 Gen3 x4 2.400\/1.800MB\/s",
            "price": 32.3272,
            "iva": 10.5,
            "quote": 1215,
            "perception": 3,
            "perceptionArba": 6, <-- Se agrega porcentual
            "internalTax": 0
        }
    ]
}
```
