---
jira_key: "PED-80"
aliases: ["PED-80"]
summary: "API - Feat - Eliminar una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-20 09:17"
updated: "2023-09-20 15:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-80"
---

# PED-80: API - Feat - Eliminar una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-20 09:17 |
| Actualizado | 2023-09-20 15:53 |
| Etiquetas | ninguna |
| Jira | [PED-80](https://bluinc.atlassian.net/browse/PED-80) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **blocks:** [[PED-81 - APP - Feat - Eliminar una orden de compra|PED-81]] APP - Feat - Eliminar una orden de compra

## Descripcion

```
DELETE {API_URL}/v1/orders/{branch-order}
```

Este recurso hace un “Soft Delete” sobre las tablas

`[NewBytes_DBF].[dbo].[pedclit]`

`[NewBytes_DBF].[dbo].[pedclil]`

Solo es posible hacer esto cuando cestado = 'P'

Adicionalmente debo modificar el listado [link](https://lioteam.atlassian.net/browse/PED-9) para agregar un filtro (que esta siempre a menos que se indique lo contrario) que no me muestre estos pedidos.
