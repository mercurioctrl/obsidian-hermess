---
jira_key: "NBWEB-940"
aliases: ["NBWEB-940"]
summary: "API - Refactor - Agregar Objetivo mensual de facturación para los vendedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-19 18:18"
updated: "2025-01-21 17:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-940"
---

# NBWEB-940: API - Refactor - Agregar Objetivo mensual de facturación para los vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-19 18:18 |
| Actualizado | 2025-01-21 17:03 |
| Etiquetas | ninguna |
| Jira | [NBWEB-940](https://bluinc.atlassian.net/browse/NBWEB-940) |

## Relaciones

- **Padre:** [[NBWEB-529 - CMS - Personal|NBWEB-529]] CMS -  Personal
- **has action item:** [[MKT-243 - NB_ INCENTIVO VENDEDORES CUOTA MENSUAL|MKT-243]] NB_ INCENTIVO VENDEDORES CUOTA MENSUAL
- **has action item:** [[NBWEB-941 - APP - Refactor - Agregar Objetivo mensual de facturación para los vendedores|NBWEB-941]] APP - Refactor - Agregar Objetivo mensual de facturación para los vendedores

## Descripcion

Este parámetro es para editar el monto que usaremos en [link](https://lioteam.atlassian.net/browse/PED-931) 

```
PATCH {API_URL}/v1/cms/staff
```

```
[
    {
      ...
      id: 36,
      monthlyTargetAmount : 2344344.33
      ...
    }
]
```

Este parámetro edita `NewBytes_DBF.dbo.agentes.monthlyTargetAmount`
