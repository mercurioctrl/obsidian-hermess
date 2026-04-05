---
jira_key: "PED-1291"
aliases: ["PED-1291"]
summary: "API - Review - Clientes nuevos Vs Clientes nuevos Objetivo -> Filtros no coincidentes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2026-01-28 12:41"
updated: "2026-01-29 13:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1291"
---

# PED-1291: API - Review - Clientes nuevos Vs Clientes nuevos Objetivo -> Filtros no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-28 12:41 |
| Actualizado | 2026-01-29 13:43 |
| Etiquetas | ninguna |
| Jira | [PED-1291](https://bluinc.atlassian.net/browse/PED-1291) |

## Relaciones

- **Padre:** [[PED-299 - Objetivos y Desafios|PED-299]] Objetivos y Desafios
- **clones:** [[PED-1285 - API - Feat - Clientes nuevos Vs Clientes nuevos Objetivo|PED-1285]] API - Feat - Clientes nuevos Vs Clientes nuevos Objetivo

## Descripcion

Aquí te comparto algunas observaciones y preguntas.



```
GET {API_URL}/v1/objectives/totalClients
```



### Criterios de aceptación

> Todos los vendedores con objetivo configurado deben estar incluidos en la respuesta.


- Se visualizan vendedores con `targetAmount` en cero



[adjunto]


> companyCode: Filtra vendedores por código de empresa


- No logro visualizar vendedores de otras empresas, ¿puede ser que sea necesario que configure algo para ellos?



[adjunto]
[adjunto]


> minTarget: Objetivo mínimo de clientes que debe tener configurado el vendedor


- Al filtrar por el mínimo objetivo, se visualizan objetivos menores al filtrado.



[adjunto]


> includeNoTarget: Incluye vendedores sin objetivo configurado (default: false)


- Al no incluir los que no tienen objetivos, se incluyen vendedores con objetivo.



[adjunto]


> sortBy: Campo por el cual ordenar (sellerId, amount, targetAmount, percentageAchieved, sellerDescription)


Al filtrar por porcentaje logrado descendente `?sortBy=percentageAchieved&sortOrder=desc&between=28-01-2025_28-01-2026` se visualiza primero un porcentaje mayor y luego uno menor.

[adjunto]
