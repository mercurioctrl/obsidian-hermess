---
jira_key: "PED-1161"
aliases: ["PED-1161"]
summary: "API - MVP - Repositorio incoterms"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-10-21 11:21"
updated: "2025-11-25 12:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1161"
---

# PED-1161: API - MVP - Repositorio incoterms

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-21 11:21 |
| Actualizado | 2025-11-25 12:57 |
| Etiquetas | ninguna |
| Jira | [PED-1161](https://bluinc.atlassian.net/browse/PED-1161) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **has action item:** [[PED-1122]] API - MVP -Feat - Agregar condición de venta (Incoterms) como un selector en el detalle de la orden
- **has action item:** [[PED-1121]] APP - MVP -Feat - Agregar condición de venta (Incoterms) como un selector en el detalle de la orden
- **has action item:** [[PED-1164]] API - Refactor - Al crear una orden, esta debe tener un incoterm pedeterminado 

## Descripcion

Basándonos en `[NewBytes_DBF].[dbo].[FP_Incoterms]` agregaremos

```
GET {API_URL}/v1/incoterms
```

```
[
  {
    "id": 1,
    "code": "CFR",
    "description": "CFR"
  },
  {
    "id": 2,
    "code": "CIF",
    "description": "CIF"
  },
  {
    "id": 3,
    "description": "CIP",
```
