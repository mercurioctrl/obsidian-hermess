---
jira_key: "POS-56"
aliases: ["POS-56"]
summary: "API - Feat - Ver detalle ingreso"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-05 11:51"
updated: "2022-10-14 09:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-56"
---

# POS-56: API - Feat - Ver detalle ingreso

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-05 11:51 |
| Actualizado | 2022-10-14 09:29 |
| Etiquetas | ninguna |
| Jira | [POS-56](https://bluinc.atlassian.net/browse/POS-56) |

## Relaciones

- **Padre:** [[POS-19 - Ingresos|POS-19]] Ingresos
- **Subtarea:** [[POS-77 - API - Refactor - Agregar al recurso la descripción de la falla|POS-77]] API - Refactor - Agregar al recurso la descripción de la falla
- **Subtarea:** [[POS-80 - APP - Refactor - Mejorar la forma en la que se visualizan las descripciones|POS-80]] APP - Refactor - Mejorar la forma en la que se visualizan las descripciones largas en el modal
- **Subtarea:** [[POS-140 - API - Refactor - Agregar stocks disponibles|POS-140]] API - Refactor - Agregar stocks disponibles
- **Subtarea:** [[POS-141 - APP - Refactor - Agregar stocks disponibles|POS-141]] APP - Refactor - Agregar stocks disponibles
- **Subtarea:** [[POS-164 - API - Refactor - Agregar precios posibles del producto|POS-164]] API - Refactor - Agregar precios posibles del producto
- **Subtarea:** [[POS-202 - API - Review - Mostrar precios históricos completos y revisar precio de venta|POS-202]] API - Review - Mostrar precios históricos completos y revisar precio de venta
- **Subtarea:** [[POS-203 - APP - Review - Agregar fechas a los precios historico y de venta|POS-203]] APP - Review - Agregar fechas a los precios historico y de venta

## Descripcion

```
GET {API_URL}/v1/aftersales/{aftersaleId}
```
