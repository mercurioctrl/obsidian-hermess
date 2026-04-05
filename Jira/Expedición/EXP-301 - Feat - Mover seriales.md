---
jira_key: "EXP-301"
aliases: ["EXP-301"]
summary: "Feat - Mover seriales"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2023-05-31 05:56"
updated: "2023-11-08 08:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-301"
---

# EXP-301: Feat - Mover seriales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-31 05:56 |
| Actualizado | 2023-11-08 08:49 |
| Etiquetas | ninguna |
| Jira | [EXP-301](https://bluinc.atlassian.net/browse/EXP-301) |

## Relaciones

- **Padre:** [[EXP-5]] Ingreso de mercaderia
- **Subtarea:** [[EXP-302]] API - Feat - Buscar seriales que son plausible de ser movidos 
- **Subtarea:** [[EXP-303]] API - Feat - Mover seriales seleccionados
- **Subtarea:** [[EXP-304]] APP - Feat - Modal "Mover Seriales"
- **Subtarea:** [[EXP-313]] API - Refactor - Buscar seriales, parece no ser reactivo a los seriales, o encuentra demasiados.
- **Subtarea:** [[EXP-314]] API - Refactor - Agregar el recurso que trae los seriles buscados: Nombre de producto, id de producto, Pedido "donde se ingreso, pero ya no existe"
- **is blocked by:** [[EXP-346]] APP - Mover seriales - Incidencias varias
- **is blocked by:** [[EXP-367]] API - Mover seriales - Incidencias varias

## Descripcion

Esta feature es una respuesta a uno de los pedidos de asistencia mas frecuente, que aun hasta hoy es inevitable y realmente ocupa mucho tiempo de sistemas, porque se da muy seguido hace muchos años.

Se trata de el momento en el cual se equvocan y toman mercaderia en un despacho incorrecto, o bien borran una orden proveedor por error (o corrección) y se pierden seriales.

Intetaremos poder encontrar cuales son esos seriales, verificar si es posible moverlos y finalmente darles un nuevo destino.

De esta forma estaremos cambiando constantes pedidos de asistencia por la autogestion del error.
