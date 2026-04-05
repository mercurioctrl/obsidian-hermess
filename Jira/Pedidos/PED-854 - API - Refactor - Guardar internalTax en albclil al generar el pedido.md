---
jira_key: "PED-854"
aliases: ["PED-854"]
summary: "API - Refactor - Guardar internalTax en albclil al generar el pedido"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-29 07:29"
updated: "2024-11-01 04:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-854"
---

# PED-854: API - Refactor - Guardar internalTax en albclil al generar el pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-29 07:29 |
| Actualizado | 2024-11-01 04:25 |
| Etiquetas | ninguna |
| Jira | [PED-854](https://bluinc.atlassian.net/browse/PED-854) |

## Relaciones

- **Padre:** [[PED-4]] Pedidos
- **action item from:** [[PED-853]] API - Refactor - Al crear/editar una orden se debe agregar el internalTax si corresponde en pedclil

## Descripcion

Así como se realizo en pedclil, propagaremos el dato al resto de la cadena  de compra, para esto debemos agregare el parámetro a la tabla en la base de datos `[NewBytes_DBF].[dbo].[albclil].internalTax` para poder plasmar el dato en etapas mas avanzadas de la compra.

Esto se realiza al ejecutar el recurso

```
POST {API_URL}/v1/makeSale
```
