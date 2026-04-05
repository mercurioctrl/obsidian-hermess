---
jira_key: "NBWEB-935"
aliases: ["NBWEB-935"]
summary: "APP - Feat - Agregar subtitulo a los items"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-12-16 16:05"
updated: "2024-12-26 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-935"
---

# NBWEB-935: APP - Feat - Agregar subtitulo a los items

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-16 16:05 |
| Actualizado | 2024-12-26 10:44 |
| Etiquetas | ninguna |
| Jira | [NBWEB-935](https://bluinc.atlassian.net/browse/NBWEB-935) |

## Relaciones

- **Padre:** [[NBWEB-682]] Productos
- **action item from:** [[NBWEB-934]] API - Feat - Agregar subtitulo a los items
- **has action item:** [[SNB-2642]] AGREGAR ITEM EN WEB POR PROMOCIÓN EN COMBO

## Descripcion

Agregaremos un subtitulos para algunos productos (la mayoria no lo tienen y se ve como hoy en dia) basándonos en el recuso (ver imagen)

```
GET {API_URL}/v1/subtitle/{itemId}
```



```
 {
    "description": "En combo con AMD 8600g obtenes un duescuento de 2 % sobre este producto",
}
```

En description puede venir código html para poder hacer enlaces o negritas. Por ejemplo:

En combo con  <a href=”sitio”>AMD 8600g</a> obtenes un duescuento de 2 % sobre este producto.

[adjunto]
