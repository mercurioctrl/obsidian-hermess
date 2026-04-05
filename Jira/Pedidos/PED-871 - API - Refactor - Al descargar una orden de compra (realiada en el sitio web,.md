---
jira_key: "PED-871"
aliases: ["PED-871"]
summary: "API - Refactor - Al descargar una orden de compra (realiada en el sitio web, etc) se debe guardar pedclil.internalTax si corresponde al producto"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-12 11:39"
updated: "2024-11-22 00:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-871"
---

# PED-871: API - Refactor - Al descargar una orden de compra (realiada en el sitio web, etc) se debe guardar pedclil.internalTax si corresponde al producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-12 11:39 |
| Actualizado | 2024-11-22 00:37 |
| Etiquetas | ninguna |
| Jira | [PED-871](https://bluinc.atlassian.net/browse/PED-871) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **has action item:** [[NBWEB-926 - API - Refactor - Incluir internalTax si corresponde al procesar un carrito|NBWEB-926]] API - Refactor - Incluir internalTax si corresponde al procesar un carrito (crear pedclil)

## Descripcion

Al descargar una orden de compra (realiada en el sitio web, etc) se debe guardar `pedclil.internalTax `si corresponde al producto.

Tal vez, podemos traerlo de un paso previo cuando se genera en la web

```
{API_URL}/v1/downloadOrder/{pedido}
```
