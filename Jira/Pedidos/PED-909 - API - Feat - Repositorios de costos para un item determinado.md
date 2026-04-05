---
jira_key: "PED-909"
aliases: ["PED-909"]
summary: "API - Feat - Repositorios de costos para un item determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-20 08:02"
updated: "2025-01-02 11:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-909"
---

# PED-909: API - Feat - Repositorios de costos para un item determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-20 08:02 |
| Actualizado | 2025-01-02 11:00 |
| Etiquetas | ninguna |
| Jira | [PED-909](https://bluinc.atlassian.net/browse/PED-909) |

## Relaciones

- **Padre:** [[PED-497]] Ver orden de compra
- **has action item:** [[PED-910]] APP - MVP - Refactor - Seleccionar costo para el item de una orden

## Descripcion

Lo que haremos sera traer para un item determinado (itemId) el costo de cada compra junto con la fecha de compra y el nombre del proveedor.

```
GET {API_URL}/v1/items/{itemId}/costHistory
```

```
...
{
  "cost": 1042.5,
  "purchaseDate": "01/01/2024",
  "providerDescription": "LASET"
},
{
  "cost": 1034.5,
  "purchaseDate": "01/09/2023",
  "providerDescription": "GIGABYTE"
}
...
```

Esta informacion la sacaremos de la siguiente tabla

```
SELECT ...
  FROM [NewBytes_DBF].[dbo].[albprot]
  LEFT JOIN [NewBytes_DBF].[dbo].[albprol]
  WHERE albprol.cref = ?
```
