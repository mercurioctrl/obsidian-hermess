---
jira_key: "PED-209"
aliases: ["PED-209"]
summary: "API - Feat - Filtros de ordenes -> Filtrar por Vendedores en pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-02 11:12"
updated: "2023-11-13 22:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-209"
---

# PED-209: API - Feat - Filtros de ordenes -> Filtrar por Vendedores en pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-02 11:12 |
| Actualizado | 2023-11-13 22:57 |
| Etiquetas | ninguna |
| Jira | [PED-209](https://bluinc.atlassian.net/browse/PED-209) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-210]] APP - Feat - Filtros de ordenes -> Filtrar por Vendedores en pedido

## Descripcion

Basándonos en el recurso [link](https://lioteam.atlassian.net/browse/PED-178) agregaremos filtrado por estado del pedido.

```
GET {API_URL}/v1/orders?sellerId=1
```
