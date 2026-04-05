---
jira_key: "PEGA-133"
aliases: ["PEGA-133"]
summary: "API - Refactor - Si en una primera consulta, de una busqueda no logro matchear ningun resultado, hacer una segunda ejecucion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-10-04 16:48"
updated: "2024-10-15 11:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-133"
---

# PEGA-133: API - Refactor - Si en una primera consulta, de una busqueda no logro matchear ningun resultado, hacer una segunda ejecucion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-04 16:48 |
| Actualizado | 2024-10-15 11:08 |
| Etiquetas | ninguna |
| Jira | [PEGA-133](https://bluinc.atlassian.net/browse/PEGA-133) |

## Relaciones

- **Padre:** [[PEGA-6 - Feat - Listar productos|PEGA-6]] Feat - Listar productos

## Descripcion

Haremos una ejecución mas amplia del estilo 


```
 
  SELECT TOP (300) i.[id],
       i.[lastRepositoryid],
       i.[resellerId],
       i.[brandId],
       i.[description],
       i.[price],
       i.[lastPrice],
       i.[destinyUrl],
       i.[defaultImgUrl],
       i.[deleted],
       i.[hide],
       i.[originId],
       i.[featured],
       i.[firstPriceDifference],
       ft.[RANK] AS Relevance
FROM [PEGA].[dbo].[items] i
INNER JOIN FREETEXTTABLE([PEGA].[dbo].[items], [description], 'RAZER KAIRA X FOR PLAYSTATION 5') ft
    ON i.[id] = ft.[KEY]
ORDER BY   ft.[RANK] DESC

```

Es posible que necesitemos hacer una query dentro de otra para ordenar primero por semejanza como el ejemplo y otra para ordenar por precio según el filtro
