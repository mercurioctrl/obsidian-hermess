---
jira_key: "EXP-242"
aliases: ["EXP-242"]
summary: "API - Feat - Crear un nuevo transportista/moto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-17 09:53"
updated: "2023-04-11 10:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-242"
---

# EXP-242: API - Feat - Crear un nuevo transportista/moto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-17 09:53 |
| Actualizado | 2023-04-11 10:26 |
| Etiquetas | ninguna |
| Jira | [EXP-242](https://bluinc.atlassian.net/browse/EXP-242) |

## Relaciones

- **Padre:** [[EXP-12 - Feat - Listar pedidos para envio|EXP-12]] Feat - Listar pedidos para envio

## Descripcion

Crearemos un recurso muy simple para poder dar de alta, al momento de la generación de etiqueta genérica, un nuevo transportista, en caso de no estar entre los listados.

```
POST {API_URL}/v1/shipper
```

```
{
shipperDescription: 'Un nombre cualquier'
comment: 'Un texto cualquier'
}
```

Para esto agregaremos una tabla llamada “`shipper`" que en principio solo tendrá

- id


- description


- comment
