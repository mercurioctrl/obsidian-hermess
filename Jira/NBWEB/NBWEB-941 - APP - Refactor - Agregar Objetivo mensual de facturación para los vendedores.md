---
jira_key: "NBWEB-941"
aliases: ["NBWEB-941"]
summary: "APP - Refactor - Agregar Objetivo mensual de facturación para los vendedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-01-19 18:18"
updated: "2025-01-21 17:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-941"
---

# NBWEB-941: APP - Refactor - Agregar Objetivo mensual de facturación para los vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-19 18:18 |
| Actualizado | 2025-01-21 17:28 |
| Etiquetas | ninguna |
| Jira | [NBWEB-941](https://bluinc.atlassian.net/browse/NBWEB-941) |

## Relaciones

- **Padre:** [[NBWEB-529 - CMS - Personal|NBWEB-529]] CMS -  Personal
- **action item from:** [[NBWEB-940 - API - Refactor - Agregar Objetivo mensual de facturación para los vendedores|NBWEB-940]] API - Refactor - Agregar Objetivo mensual de facturación para los vendedores
- **has action item:** [[MKT-243 - NB_ INCENTIVO VENDEDORES CUOTA MENSUAL|MKT-243]] NB_ INCENTIVO VENDEDORES CUOTA MENSUAL

## Descripcion

Este parámetro es para editar el monto que usaremos en [link](https://lioteam.atlassian.net/browse/PED-932)  y proviene del refactor

[adjunto]


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
