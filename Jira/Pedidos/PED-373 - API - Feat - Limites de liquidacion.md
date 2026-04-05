---
jira_key: "PED-373"
aliases: ["PED-373"]
summary: "API - Feat - Limites de liquidacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-21 09:39"
updated: "2023-12-22 18:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-373"
---

# PED-373: API - Feat - Limites de liquidacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-21 09:39 |
| Actualizado | 2023-12-22 18:24 |
| Etiquetas | ninguna |
| Jira | [PED-373](https://bluinc.atlassian.net/browse/PED-373) |

## Relaciones

- **Padre:** [[PED-132]] Feat - Login / Re Login
- **relates to:** [[PED-381]] App -Feat : Limites de liquidacion
- **relates to:** [[PED-386]] API - Refactor - Limites de liquidación - Filtrar por vendedor

## Descripcion

Incluiremos un recurso que nos permita conocer los limites de facturación para cada sucursal.

```
{API_URL}/v1/closeSaleLimites
```

```
[
  {
  branch:10,
  limit: 10000,
  closeSales: 7400
  },
 {
  branch: 2,
  limit: 8000,
  closeSales: 2300
  },
]
```
