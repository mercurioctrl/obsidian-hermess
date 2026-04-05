---
jira_key: "PED-886"
aliases: ["PED-886"]
summary: "API - Refactor - Agregar filtro de empresa a las ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-27 11:53"
updated: "2024-11-29 02:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-886"
---

# PED-886: API - Refactor - Agregar filtro de empresa a las ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-27 11:53 |
| Actualizado | 2024-11-29 02:41 |
| Etiquetas | ninguna |
| Jira | [PED-886](https://bluinc.atlassian.net/browse/PED-886) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra

## Descripcion

Agregaremos para el repositorio de compras un filtro llamado 

```
GET {API_URL}/v1/orders?companyCode=5
```

Lo que hace este filtro es que cuando esta presente, filtrar 

`[NewBytes_DBF].[dbo].[pedclit].companyCode`

Si no esta presente o es `null`, trae todas las empresas
