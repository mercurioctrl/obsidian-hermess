---
jira_key: "PED-210"
aliases: ["PED-210"]
summary: "APP - Feat - Filtros de ordenes -> Filtrar por Vendedores en pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-11-02 11:14"
updated: "2023-11-13 22:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-210"
---

# PED-210: APP - Feat - Filtros de ordenes -> Filtrar por Vendedores en pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-02 11:14 |
| Actualizado | 2023-11-13 22:56 |
| Etiquetas | ninguna |
| Jira | [PED-210](https://bluinc.atlassian.net/browse/PED-210) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **is blocked by:** [[PED-23 - API - Repository - Vendedores|PED-23]] API - Repository - Vendedores
- **is blocked by:** [[PED-209 - API - Feat - Filtros de ordenes - Filtrar por Vendedores en pedido|PED-209]] API - Feat - Filtros de ordenes -> Filtrar por Vendedores en pedido
- **is blocked by:** [[PED-264 - APP - Filtrar por vendedores - Incidencias varias|PED-264]] APP - Filtrar por vendedores - Incidencias varias

## Descripcion

Basándonos en el recurso [https://lioteam.atlassian.net/browse/PED-178](https://lioteam.atlassian.net/browse/PED-178)  y en el repositorio [link](https://lioteam.atlassian.net/browse/PED-23)  agregaremos un select entre los filtros para lograr el filtrado por estado del pedido.

```
GET {API_URL}/v1/orders?sellerId=1
```
