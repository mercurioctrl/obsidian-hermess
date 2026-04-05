---
jira_key: "LIO-192"
aliases: ["LIO-192"]
summary: "API - Refactor - Faltan atributos del vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-01-29 15:54"
updated: "2025-02-05 18:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-192"
---

# LIO-192: API - Refactor - Faltan atributos del vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-01-29 15:54 |
| Actualizado | 2025-02-05 18:42 |
| Etiquetas | ninguna |
| Jira | [LIO-192](https://bluinc.atlassian.net/browse/LIO-192) |

## Relaciones

- **Padre:** [[LIO-119 - Inventario|LIO-119]] Inventario

## Descripcion

Faltan los siguientes atributos que se mencionaron en [link](https://lioteam.atlassian.net/browse/LIO-120)



[adjunto]


```
{
    vendedor:{
    ...,
    reputacion:{
        ...,
        ventasConcretadas: 2152, //FALTA
        productosDisponibles: 1509, //FALTA
        puntajeGlobal: 5, //falta
    }
    }
}
```

Ejemplo:
[https://gamma.api4.libreopcion.com/v4/item/246108](https://gamma.api4.libreopcion.com/v4/item/246108)


[adjunto]
