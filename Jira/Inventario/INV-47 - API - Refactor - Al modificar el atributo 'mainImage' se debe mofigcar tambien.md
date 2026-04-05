---
jira_key: "INV-47"
aliases: ["INV-47"]
summary: "API - Refactor - Al modificar el atributo 'mainImage' se debe mofigcar tambien la portada de lo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-09 10:15"
updated: "2024-01-26 19:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-47"
---

# INV-47: API - Refactor - Al modificar el atributo 'mainImage' se debe mofigcar tambien la portada de lo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-09 10:15 |
| Actualizado | 2024-01-26 19:37 |
| Etiquetas | ninguna |
| Jira | [INV-47](https://bluinc.atlassian.net/browse/INV-47) |

## Relaciones

- **Padre:** [[INV-27]] Productos

## Descripcion

Se debe alterar el recurso para que a su vez que se edite cual es la imagen de portada, tambien lo haga para la tabla

```
PATCH /item/{ITEM}
```

```
{
"mainImage":"http://static.nb.com.ar/img/f9a7b5344ac785f75c2978d05f572184.jpg"
}
```

`[CS].[dbo].[productosFotos]` que utiliza la aplicacion Legacy para mostrar la portada.

Si queres pensalo y vemos si hay una forma mas simple de hacerlo
