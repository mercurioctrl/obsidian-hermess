---
jira_key: "EXP-316"
aliases: ["EXP-316"]
summary: "API - Feat - Filtro especifico por id, sku en parámetros separados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-21 07:14"
updated: "2023-06-27 08:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-316"
---

# EXP-316: API - Feat - Filtro especifico por id, sku en parámetros separados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-21 07:14 |
| Actualizado | 2023-06-27 08:50 |
| Etiquetas | ninguna |
| Jira | [EXP-316](https://bluinc.atlassian.net/browse/EXP-316) |

## Relaciones

- **Padre:** [[EXP-10 - Feat - Listar pedidos (despachos) proveedores|EXP-10]] Feat - Listar pedidos (despachos) proveedores
- **blocks:** [[SNB-838 - mejoras para el sistema|SNB-838]] mejoras para el sistema
- **blocks:** [[EXP-317 - APP - Feat - Filtro especifico por id, sku en parámetros separados|EXP-317]] APP - Feat - Filtro especifico por id, sku en parámetros separados

## Descripcion

Agregaremos al recurso 

```
GET {API_URL}/v1/providersOrders
```

los parámetros SKU y itemId para poder buscar (solo si esta alguno de los parámetros presentes) dentro del pedido

```
GET {API_URL}/v1/providersOrders?sku={sku}&itemId={itemId}
```
