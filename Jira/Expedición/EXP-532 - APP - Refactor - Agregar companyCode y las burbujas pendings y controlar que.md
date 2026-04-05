---
jira_key: "EXP-532"
aliases: ["EXP-532"]
summary: "APP - Refactor - Agregar companyCode y las burbujas pendings y controlar que quede alineado con las cantidades de las pestañas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-03-27 09:11"
updated: "2026-03-30 11:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-532"
---

# EXP-532: APP - Refactor - Agregar companyCode y las burbujas pendings y controlar que quede alineado con las cantidades de las pestañas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-27 09:11 |
| Actualizado | 2026-03-30 11:28 |
| Etiquetas | ninguna |
| Jira | [EXP-532](https://bluinc.atlassian.net/browse/EXP-532) |

## Relaciones

- **Padre:** [[EXP-108 - Feat - Burbujas|EXP-108]] Feat - Burbujas
- **action item from:** [[EXP-531 - API - Refactor - Agregar companyCode y las burbujas pendings y controlar que|EXP-531]] API - Refactor - Agregar companyCode y las burbujas pendings y controlar que quede alineado con las cantidades de las pestañas

## Descripcion

Segun el refactor [link](https://bluinc.atlassian.net/browse/EXP-531)  debemos filtrar para un usuario con `companyCode` 

```
GET /v1/pendings?companyCode=4
```

## Criterios de aceptación

- `GET /v1/pendings` sin `companyCode` sigue funcionando igual que hoy (backwards compatible)


- `GET /v1/pendings?companyCode=4` retorna el mismo número que el listado de pickUp filtrado por `companyCode=4`


- `GET /v1/pendings?companyCode=4` retorna el mismo número que el listado de shipments filtrado por `companyCode=4`


- `GET /v1/pendings?companyCode=4` retorna el mismo número que el listado de providersOrders filtrado por `companyCode=4`


- Asi para cada caso
