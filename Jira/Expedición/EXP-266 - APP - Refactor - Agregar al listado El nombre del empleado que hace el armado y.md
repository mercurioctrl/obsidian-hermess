---
jira_key: "EXP-266"
aliases: ["EXP-266"]
summary: "APP - Refactor - Agregar al listado El nombre del empleado que hace el armado y del que hace la entrega segun el token"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-03-30 09:43"
updated: "2023-05-29 06:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-266"
---

# EXP-266: APP - Refactor - Agregar al listado El nombre del empleado que hace el armado y del que hace la entrega segun el token

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-30 09:43 |
| Actualizado | 2023-05-29 06:35 |
| Etiquetas | ninguna |
| Jira | [EXP-266](https://bluinc.atlassian.net/browse/EXP-266) |

## Relaciones

- **Padre:** [[EXP-12 - Feat - Listar pedidos para envio|EXP-12]] Feat - Listar pedidos para envio
- **is blocked by:** [[EXP-265 - API - Refactor - Agregar al listado El nombre del empleado que hace el armado y|EXP-265]] API - Refactor - Agregar al listado El nombre del empleado que hace el armado y del que hace la entrega segun el token

## Descripcion

Se deben agregar, para mostrar el nombre del empleado (basándonos en la tabla NewBytes_DBF.dbo.agentes) que hace un armado y una entrega, basándonos en el token.

```
GET {{API_URL}}/v1/shipments
```

```
GET {{API_URL}}/v1/pickUp
```

Agregaremos el objeto dos parámetros de la siguiente manera en dos columnas a la derecha de todo.

`whoBuild` y `whoAuthorizes`

Es decir “Armador” y “Entregador”
