---
jira_key: "PED-342"
aliases: ["PED-342"]
summary: "API - Listar ordenes de compra - Discrepancia en los totales finales"
status: "Tareas por hacer"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2023-12-15 12:10"
updated: "2024-01-02 16:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-342"
---

# PED-342: API - Listar ordenes de compra - Discrepancia en los totales finales

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2023-12-15 12:10 |
| Actualizado | 2024-01-02 16:57 |
| Etiquetas | ninguna |
| Jira | [PED-342](https://bluinc.atlassian.net/browse/PED-342) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **relates to:** [[PED-333]] API - Refactor - En el total final no parece estar considerando las percpeciones, solo el iva
- **blocks:** [[PED-8]] Listar ordenes de compra

## Descripcion

En el listado de ordenes pareciera que no está considerando la nueva cotización (cuando está fue modificada) por lo que el total final del listado es incorrecto al compararlo con el total del detalle de la orden.

```
1.317,10 * 800 = 1.053.680,82
```

[adjunto]
Este es otro caso diferente en un pedido con sucursal 10 en el cual no se muestra el IVA y el total final del listado es menor al total final del detalle de la orden, puede ser que en el total final del listado no esté considerando todos los elementos necesarios.

[adjunto]
