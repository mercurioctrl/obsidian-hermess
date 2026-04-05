---
jira_key: "EXP-14"
aliases: ["EXP-14"]
summary: "Feat - Listar pedidos para retiro"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2022-10-31 14:08"
updated: "2023-10-20 14:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-14"
---

# EXP-14: Feat - Listar pedidos para retiro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-31 14:08 |
| Actualizado | 2023-10-20 14:09 |
| Etiquetas | ninguna |
| Jira | [EXP-14](https://bluinc.atlassian.net/browse/EXP-14) |

## Relaciones

- **Padre:** [[EXP-7 - Despacho de retiros|EXP-7]] Despacho de retiros
- **Subtarea:** [[EXP-55 - API - Feat - Listar pedidos para retiro|EXP-55]] API - Feat - Listar pedidos para retiro
- **Subtarea:** [[EXP-68 - API - Feat - Detalle de pedido|EXP-68]] API - Feat - Detalle de pedido
- **Subtarea:** [[EXP-73 - API - Feat - Volanta operativa para armar el pedido|EXP-73]] API - Feat - Volanta operativa para armar el pedido
- **Subtarea:** [[EXP-74 - APP - Feat - Volanta operativa para armar el pedido|EXP-74]] APP - Feat - Volanta operativa para armar el pedido
- **Subtarea:** [[EXP-84 - APP - Listar pedido para retiro|EXP-84]] APP - Listar pedido para retiro
- **Subtarea:** [[EXP-114 - API - Refactor - hacer el campo fullSerialized dinámico según su estado real|EXP-114]] API - Refactor - hacer el campo fullSerialized dinámico según su estado real 
- **Subtarea:** [[EXP-115 - API - Refactor - hacer el campo fullSerialized PARA CADA ITEM en Detalle pedido|EXP-115]] API - Refactor - hacer el campo fullSerialized PARA CADA ITEM en "Detalle pedido" dinámico según su estado real 
- **Subtarea:** [[EXP-128 - APP - Review - Invertir bandera de notSerializable en el detalle del producto|EXP-128]] APP - Review - Invertir bandera de notSerializable en el detalle del producto
- **Subtarea:** [[EXP-149 - API - Feat - Alertar pedido para que lo preparen cuando un cliente se presenta|EXP-149]] API - Feat - Alertar pedido para que lo preparen cuando un cliente se presenta
- **Subtarea:** [[EXP-150 - APP - Feat - Alertar pedido para que lo preparen cuando un cliente se presenta|EXP-150]] APP - Feat - Alertar pedido para que lo preparen cuando un cliente se presenta
- **Subtarea:** [[EXP-151 - API - Feat - Leeer alertas de pedidos|EXP-151]] API - Feat - Leeer alertas de pedidos
- **Subtarea:** [[EXP-152 - APP - Feat - Mostrar alertas de pedidos|EXP-152]] APP - Feat - Mostrar alertas de pedidos
- **Subtarea:** [[EXP-188 - API - Refactor - Reordenar listado en pantalla para copiar el orden de la|EXP-188]] API - Refactor - Reordenar listado en pantalla para copiar el orden de la volanta
- **Subtarea:** [[EXP-273 - API - Refactor - Solo mostrar resultados del ultimo año (ultimos 365 dias), en|EXP-273]] API - Refactor - Solo mostrar resultados del ultimo año (ultimos 365 dias), en todos los casos a menos que la fecha se explicite
- **Subtarea:** [[EXP-339 - APP - Refactor - En el filtro multiple estados mostrar los que estan cargados|EXP-339]] APP - Refactor - En el filtro multiple "estados" mostrar los que estan cargados por defecto
- **Subtarea:** [[EXP-419 - API - Refactor - Cambiar del orden de la grilla retiros (solo retiros, no|EXP-419]] API - Refactor - Cambiar del orden de la grilla retiros (solo retiros, no envios)
- **Subtarea:** [[EXP-452 - API - Refactor - Agregar companyCode, sin afectar el tiempo de el repositorio|EXP-452]] API - Refactor - Agregar companyCode, sin afectar el tiempo de el repositorio
- **Subtarea:** [[EXP-453 - APP - Refactor - Agregar logo de NBe cuando el companyCode es el de esa empresa|EXP-453]] APP - Refactor - Agregar logo de NBe cuando el companyCode es el de esa empresa
- **Subtarea:** [[EXP-485 - APP - MVP - Feat - Agregar Filtro empresa según companyCode|EXP-485]] APP - MVP - Feat - Agregar Filtro empresa según companyCode
- **Subtarea:** [[EXP-489 - API - MVP - Feat - Agregar listado de companies|EXP-489]] API - MVP - Feat - Agregar listado de companies
- **is blocked by:** [[EXP-172 - Retiros - Filtro por fechas no coincidente|EXP-172]] Retiros - Filtro por fechas no coincidente
- **is blocked by:** [[EXP-174 - Retiros - Filtrado por texto número de cliente sin resultados|EXP-174]] Retiros - Filtrado por texto número de cliente sin resultados
- **is blocked by:** [[EXP-175 - Retiros - Filtrado por texto medio de retiro sin resultados|EXP-175]] Retiros - Filtrado por texto medio de retiro sin resultados
- **is blocked by:** [[EXP-173 - Retiros - Filtrado por texto número de orden sin resultados|EXP-173]] Retiros - Filtrado por texto número de orden sin resultados
- **is blocked by:** [[EXP-171 - Retiros - Combinación de filtros serializado y estado, resultados no|EXP-171]] Retiros - Combinación de filtros serializado y estado, resultados no coincidentes

## Descripcion

- Solo se puede ver este listado si estas logueado en el sistema


- Controlar filtro de Serializados si/no. 


- Controlar filtro de estado si/no. 


- Controlar filtro por fechas


- Controlar filtro por string



---

30-01-23

- Se debe respetar el mismo orden en la volanta que cuando veo el modal con el detalle del pedido
