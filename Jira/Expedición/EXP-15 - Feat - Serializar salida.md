---
jira_key: "EXP-15"
aliases: ["EXP-15"]
summary: "Feat - Serializar salida"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2022-10-31 14:08"
updated: "2023-12-11 15:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-15"
---

# EXP-15: Feat - Serializar salida

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-31 14:08 |
| Actualizado | 2023-12-11 15:20 |
| Etiquetas | ninguna |
| Jira | [EXP-15](https://bluinc.atlassian.net/browse/EXP-15) |

## Relaciones

- **Padre:** [[EXP-7 - Despacho de retiros|EXP-7]] Despacho de retiros
- **Subtarea:** [[EXP-66 - API - Feat - Serializar salida|EXP-66]] API - Feat - Serializar salida
- **Subtarea:** [[EXP-67 - API - Feat - Determinar si están cumplida la serializacion completa de un ítem|EXP-67]] API - Feat - Determinar si están cumplida la serializacion completa de un ítem para un pedido especifico
- **Subtarea:** [[EXP-85 - APP - Feat - Serializar salida de un pedido|EXP-85]] APP - Feat - Serializar salida de un pedido
- **Subtarea:** [[EXP-96 - API - Refactor - Serialziar salida|EXP-96]] API - Refactor - Serialziar salida
- **Subtarea:** [[EXP-98 - API - Feat - Confirmar despacho de mercaderia|EXP-98]] API - Feat - Confirmar despacho de mercaderia
- **Subtarea:** [[EXP-99 - APP - Feat - Confirmar despacho de mercaderia|EXP-99]] APP - Feat - Confirmar despacho de mercaderia
- **Subtarea:** [[EXP-106 - API - Feat - Eliminar serial de un pedido|EXP-106]] API - Feat - Eliminar serial de un pedido
- **Subtarea:** [[EXP-107 - APP - Feat - Eliminar serial de un pedido que aun no fue despachado|EXP-107]] APP - Feat - Eliminar serial de un pedido que aun no fue despachado
- **Subtarea:** [[EXP-158 - API - Review - Al serializar un pedido poniendo cualquier numero el error es|EXP-158]] API - Review - Al serializar un pedido poniendo cualquier numero el error es incierto
- **Subtarea:** [[EXP-184 - API - Feat - Agregar posibilidad de serial izar en intervalos, como se hizo|EXP-184]] API - Feat - Agregar posibilidad de serial izar en intervalos, como se hizo para la entrada, pero para la salida
- **Subtarea:** [[EXP-185 - API - Feat - Serializado automatico|EXP-185]] API - Feat - Serializado automatico
- **Subtarea:** [[EXP-186 - APP - Feat - Serializar salida por intervalos|EXP-186]] APP - Feat - Serializar salida por intervalos
- **Subtarea:** [[EXP-189 - APP- Feat - Serializado automatico|EXP-189]] APP- Feat - Serializado automatico
- **Subtarea:** [[EXP-190 - API - Refactor - Ocultar los anulados en listado de envios y listado de retiros|EXP-190]] API - Refactor - Ocultar los anulados en listado de envios y listado de retiros
- **Subtarea:** [[EXP-246 - API - Feat - Confirmar despacho de mercadería, validar que tenga transportista|EXP-246]] API - Feat - Confirmar despacho de mercadería, validar que tenga transportista en los casos siguientes
- **Subtarea:** [[EXP-264 - API - Refactor - Al eliminar, se duplica la subconsulta por no filtrar sucursal|EXP-264]] API - Refactor - Al eliminar, se duplica la subconsulta por no filtrar sucursal
- **Subtarea:** [[EXP-271 - API - Refactor - Confirmar despacho (siin factura) cuando es Libre Opcion|EXP-271]] API - Refactor - Confirmar despacho (siin factura) cuando es Libre Opcion

## Descripcion

- Se deben poder eliminar seriales de a uno, tomados en un pedido en la salida, pero solo si el mismo no fue “despachado”.


- Se deben poder eliminar seriales de a varios seleccionados, tomados en un pedido en la salida, pero solo si el mismo no fue “despachado”.


- Una vez que se despacha un pedido, se debe ir de la lista y de la burbuja.
