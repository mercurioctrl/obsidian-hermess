---
jira_key: "EXP-10"
aliases: ["EXP-10"]
summary: "Feat - Listar pedidos (despachos) proveedores"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2022-10-31 14:04"
updated: "2023-03-09 10:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-10"
---

# EXP-10: Feat - Listar pedidos (despachos) proveedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2022-10-31 14:04 |
| Actualizado | 2023-03-09 10:52 |
| Etiquetas | ninguna |
| Jira | [EXP-10](https://bluinc.atlassian.net/browse/EXP-10) |

## Relaciones

- **Padre:** [[EXP-5]] Ingreso de mercaderia
- **Subtarea:** [[EXP-32]] API - Feat - Listar pedidos de proveedores
- **Subtarea:** [[EXP-34]] APP - Feat - Listar pedidos de proveedores (Pestaña ingresos)
- **Subtarea:** [[EXP-33]] API - Feat - Filtros al listar pedidos proveedor
- **Subtarea:** [[EXP-60]] API - Feat - Agregar filtro de marca al listado de pedidos proveedor
- **Subtarea:** [[EXP-62]] APP - Feat - Agregar filtro de marca al listado de pedidos proveedor
- **Subtarea:** [[EXP-40]] APP - Feat - Detalle pedido proveedor
- **Subtarea:** [[EXP-38]] API - Feat - Detalle pedido proveedor
- **Subtarea:** [[EXP-39]] API - Feat - Detalle seriales por ítem de pedido proveedor
- **Subtarea:** [[EXP-41]] APP - Feat - Detalle seriales por ítem de pedido proveedor
- **Subtarea:** [[EXP-37]] API - Feat - Determinar si están cumplida la serializacion completa de un ítem
- **Subtarea:** [[EXP-63]] APP - Feat - Herramienta borrar en modale Detalle de seriales por item
- **Subtarea:** [[EXP-79]] APP - Refactor - Detalle pedido proveedor, marcar en verde los completados
- **Subtarea:** [[EXP-94]] API - Refactor - Detalle item de pedido, agregar codigos unicos
- **Subtarea:** [[EXP-127]] APP - Refactor - Detalle de ingreso de mercadería, ampliar imagen 
- **Subtarea:** [[EXP-159]] API - Refactor - Agregar filtro de producto al listado pedidos proveedor
- **Subtarea:** [[EXP-247]] APP - Refactor - Ocultar ingresos segun permiso especifico 
- **Subtarea:** [[EXP-274]] API - Refactor - Solo mostrar resultados del ultimo año (ultimos 365 dias), en todos los casos a menos que la fecha se explicite
- **Subtarea:** [[EXP-287]] APP - Refactor - Se deben modificar los filtros de estado para ser mutliples
- **Subtarea:** [[EXP-288]] API - Refactor - Se deben modificar los filtros de estadO para ser mutliples
- **Subtarea:** [[EXP-316]] API - Feat - Filtro especifico por id, sku en parámetros separados
- **Subtarea:** [[EXP-317]] APP - Feat - Filtro especifico por id, sku en parámetros separados
- **Subtarea:** [[EXP-336]] API - Review - El listado de ingresos no busca bien por numero de ingreso
- **Subtarea:** [[EXP-386]] API - Review - Error al usar algunos filtros en el listado
- **is blocked by:** [[EXP-153]] Ingresos - Pedido completamente serializado
- **is blocked by:** [[EXP-155]] Ingresos - Filtro por proveedor sin resultados
- **is blocked by:** [[EXP-200]] Ingresos - Buscar id proveedor sin resultados

## Descripcion

Se realizaran recursos para listar y ver detalles de las compras a proveedores para poder ingresarlas al deposito.

Se trabajara mucho con seriales e ingreso de mercaderia.

**Criterios de aceptación**

- En el listado de ingresos, no debo ver marcados como serializados los despachos, si adentro están todos serializados. (Ver tambien en prod)


- Verificar el funcionamiento del filtro serializado:si/no/todos


- El filtro de proveedores debe funcionar y poder combinarse con los demas filtros


- El filtro de marca debe funcionar y combinarse con los demas filtros. Teoricamente lo que muestra tienen que ser compras (despachos o pedidos) que adentro tienen esa marca


- Debe haber un filtro por string, que busque en el contenido del pedido (los productos)
