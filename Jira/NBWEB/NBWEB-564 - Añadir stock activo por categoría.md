---
jira_key: "NBWEB-564"
aliases: ["NBWEB-564"]
summary: "Añadir stock activo por categoría"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2023-07-19 14:30"
updated: "2023-07-20 15:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-564"
---

# NBWEB-564: Añadir stock activo por categoría

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2023-07-19 14:30 |
| Actualizado | 2023-07-20 15:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-564](https://bluinc.atlassian.net/browse/NBWEB-564) |

## Relaciones

- **Padre:** [[NBWEB-158 - API - CMS - Categories|NBWEB-158]] API - CMS - Categories

## Descripcion

Basándonos en el recurso:

```
GET {{API_URL}}/v1/cms/Categories
```

Se le añadirá el siguiente parámetro `activeStock`

```
{
        "id": 20,
        "description": "ACCESORIOS",
        "show": 1,
        "initialB": 5,
        "initialC": 20
        "activeStock": 1 <----------- Se agrega
}
```

El cual cumplirá la función de mostrarle al usuario qué dentro de la categoría, por ejemplo, Dispositivos Ópticos tiene un producto en stock activo. 

[adjunto]
Esto surge de la necesidad de que cuando un administrador intente ocultar una categoría del sitio, este pueda ver si tal categoría tiene productos en stock activos.
