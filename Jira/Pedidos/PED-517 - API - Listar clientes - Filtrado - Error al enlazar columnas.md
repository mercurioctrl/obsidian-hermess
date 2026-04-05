---
jira_key: "PED-517"
aliases: ["PED-517"]
summary: "API - Listar clientes -> Filtrado - Error al enlazar columnas"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-01-26 04:38"
updated: "2024-01-30 07:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-517"
---

# PED-517: API - Listar clientes -> Filtrado - Error al enlazar columnas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-26 04:38 |
| Actualizado | 2024-01-30 07:08 |
| Etiquetas | ninguna |
| Jira | [PED-517](https://bluinc.atlassian.net/browse/PED-517) |

## Relaciones

- **Padre:** [[PED-15 - Clientes|PED-15]] Clientes
- **relates to:** [[PED-389 - API - Refactor - Listar clientes - Filtro ordenar por|PED-389]] API - Refactor - Listar clientes -> Filtro ordenar por

## Descripcion

Al momento de intentar filtrar por frecuencia de compra `purchaseFrequency`, promedio de compra `averagePurchaseValue`, permanencia `relationshipDurationMonth`, me aparecen errores como el siguiente

[adjunto]
Dato extra:

El nombre de la columna es `purchase_frequency` y no `purchaseFrecuency`, por lo que quizás el error es que no se está realizando correctamente la función `separator`

[adjunto]
