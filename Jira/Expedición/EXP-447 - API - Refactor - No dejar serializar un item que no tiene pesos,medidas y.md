---
jira_key: "EXP-447"
aliases: ["EXP-447"]
summary: "API - Refactor - No dejar serializar un item que no tiene pesos,medidas y cantidad por bulto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-18 09:00"
updated: "2024-09-24 12:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-447"
---

# EXP-447: API - Refactor - No dejar serializar un item que no tiene pesos,medidas y cantidad por bulto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-18 09:00 |
| Actualizado | 2024-09-24 12:42 |
| Etiquetas | ninguna |
| Jira | [EXP-447](https://bluinc.atlassian.net/browse/EXP-447) |

## Relaciones

- **Padre:** [[EXP-11]] Feat - Serializar entrada de mercadería
- **relates to:** [[EXP-92]] API - Refactor - No dejar serializar un item que no tiene cargado al menos uno de los codigos unicos
- **has action item:** [[EXP-448]] APP - Refactor - Cargar pesos y medidas del producto si no existen cuando se serializan y no los tienen

## Descripcion

Al igual que se hizo en [link](https://lioteam.atlassian.net/browse/EXP-92)  para los EAN o UPC haremos lo priopio para cuando le faltan los las medidas, pesos y cantidad por bulto en `[NewBytes_DBF].[dbo].[articulo]`

```
      ,[weightAverage]
      ,[lengthAverage]
      ,[widthAverage]
      ,[highAverage]
      ,[packagePerUnit]
```
