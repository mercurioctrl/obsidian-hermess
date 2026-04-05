---
jira_key: "EXP-10"
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

## Descripción

Se realizaran recursos para listar y ver detalles de las compras a proveedores para poder ingresarlas al deposito.

Se trabajara mucho con seriales e ingreso de mercaderia.

**Criterios de aceptación**

- En el listado de ingresos, no debo ver marcados como serializados los despachos, si adentro están todos serializados. (Ver tambien en prod)


- Verificar el funcionamiento del filtro serializado:si/no/todos


- El filtro de proveedores debe funcionar y poder combinarse con los demas filtros


- El filtro de marca debe funcionar y combinarse con los demas filtros. Teoricamente lo que muestra tienen que ser compras (despachos o pedidos) que adentro tienen esa marca


- Debe haber un filtro por string, que busque en el contenido del pedido (los productos)
