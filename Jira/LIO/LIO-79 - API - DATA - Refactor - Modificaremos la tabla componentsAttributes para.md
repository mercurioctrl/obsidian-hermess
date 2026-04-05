---
jira_key: "LIO-79"
aliases: ["LIO-79"]
summary: "API - DATA - Refactor - Modificaremos la tabla componentsAttributes para enlazarlo a la cateogoria interna (capa 1) y a partir de ella, a la cateogria de libre opción"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-30 09:26"
updated: "2024-10-04 07:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-79"
---

# LIO-79: API - DATA - Refactor - Modificaremos la tabla componentsAttributes para enlazarlo a la cateogoria interna (capa 1) y a partir de ella, a la cateogria de libre opción

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-30 09:26 |
| Actualizado | 2024-10-04 07:34 |
| Etiquetas | ninguna |
| Jira | [LIO-79](https://bluinc.atlassian.net/browse/LIO-79) |

## Relaciones

- **Padre:** [[LIO-71]] Armador de equipos
- **is blocked by:** [[LIO-81]] API - DATA - Columna para enlazar componentsAttributes a la cateogoria interna (capa 1) - Categorías no coincidentes

## Descripcion

Basándonos en el repositorio de LO 

```
  SELECT *
  FROM [LO].[dbo].[categorias]
  where activa = 1 AND eliminada = 0 AND id_nb IS NOT NULL
```

Tomaremos las categorías que vamos  utilizar `componentsAttributes`

Adicionalmente agregaremos el parámetro `[LO].[dbo].[componentsAttributes].categoriaNbId` el cual podremos completar con `[LO].[dbo].[categorias].id_nb`
