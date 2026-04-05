---
jira_key: "EXP-243"
aliases: ["EXP-243"]
summary: "API - Feat - Listar transportistas/moto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-17 09:59"
updated: "2023-04-11 10:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-243"
---

# EXP-243: API - Feat - Listar transportistas/moto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-17 09:59 |
| Actualizado | 2023-04-11 10:26 |
| Etiquetas | ninguna |
| Jira | [EXP-243](https://bluinc.atlassian.net/browse/EXP-243) |

## Relaciones

- **Padre:** [[EXP-12 - Feat - Listar pedidos para envio|EXP-12]] Feat - Listar pedidos para envio
- **blocks:** [[EXP-245 - APP - Refactor - Agregar selector de transportista al modal para generar|EXP-245]] APP - Refactor - Agregar selector de transportista al modal para generar etiqueta generica

## Descripcion

Este recurso lista los transportistas para poder ser elegidos en el modal de generar etiqueta generica

```
GET {API_URL}/v1/shipper?description={cadena}
```

```
{
shipperDescription: 'Un nombre cualquier'
comment: 'Un texto cualquier'
},
{
shipperDescription: 'Un nombre cualquier'
comment: 'Un texto cualquier'
},
{
shipperDescription: 'Un nombre cualquier'
comment: 'Un texto cualquier'
}

```

Se debe poder filtrar por description con el parametro “description”
