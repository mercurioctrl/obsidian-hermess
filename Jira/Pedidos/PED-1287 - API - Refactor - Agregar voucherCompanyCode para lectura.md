---
jira_key: "PED-1287"
aliases: ["PED-1287"]
summary: "API - Refactor - Agregar voucherCompanyCode para lectura"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Catriel Mercurio"
created: "2026-01-26 15:22"
updated: "2026-01-27 09:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1287"
---

# PED-1287: API - Refactor - Agregar voucherCompanyCode para lectura

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-26 15:22 |
| Actualizado | 2026-01-27 09:33 |
| Etiquetas | ninguna |
| Jira | [PED-1287](https://bluinc.atlassian.net/browse/PED-1287) |

## Relaciones

- **Padre:** [[PED-600 - EdicionAlta de cliente|PED-600]] Edicion/Alta de cliente
- **action item from:** [[PED-1283 - API - Refactor - Agregar nuevo parámetro voucherCompanyCode|PED-1283]] API - Refactor - Agregar nuevo parámetro voucherCompanyCode
- **action item from:** [[PED-1284 - APP - Refactor - Agregar selector de empresa de facturación con nuevo parámetro|PED-1284]] APP - Refactor - Agregar selector de empresa de facturación con nuevo parámetro

## Descripcion

Agregaremos el parámetro para poder el nuevo valor

```
GET {API_URL}/v1/clients/{id}/params
```

```
{
...
  "voucherCompanyCode": 9,
...
}

```
