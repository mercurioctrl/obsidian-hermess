---
jira_key: "NBWEB-873"
aliases: ["NBWEB-873"]
summary: "API - Refactor - Leer contenido sindicado en imagenes para un item determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-10 16:59"
updated: "2024-09-11 20:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-873"
---

# NBWEB-873: API - Refactor - Leer contenido sindicado en imagenes para un item determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-10 16:59 |
| Actualizado | 2024-09-11 20:54 |
| Etiquetas | ninguna |
| Jira | [NBWEB-873](https://bluinc.atlassian.net/browse/NBWEB-873) |

## Relaciones

- **Padre:** [[NBWEB-682]] Productos
- **blocks:** [[NBWEB-874]] APP - Refactor - Mostrar contenido sindicado en imagenes para un item determinado

## Descripcion

```
GET {API_URL}/v1/sindicateContentImg/{itemId}
```

```
{
    "sindicateContentImg": "https://i.imgur.com/bzJgKy9.jpeg"
}
```
