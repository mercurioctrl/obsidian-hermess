---
jira_key: "NBWEB-991"
aliases: ["NBWEB-991"]
summary: "API - Refactor - Alterar el ranking para contemplar los cuit para una cuenta puntera"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-28 14:43"
updated: "2025-08-06 10:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-991"
---

# NBWEB-991: API - Refactor - Alterar el ranking para contemplar los cuit para una cuenta puntera

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-28 14:43 |
| Actualizado | 2025-08-06 10:28 |
| Etiquetas | ninguna |
| Jira | [NBWEB-991](https://bluinc.atlassian.net/browse/NBWEB-991) |

## Relaciones

- **Padre:** [[NBWEB-978]] NB TRAVEL

## Descripcion

Refactorizaremos el recurso 


```
GET {API_URL}/v1/ranking
```


específicamente el metodo `getRankingAcelerator` para lograr vincular los distintos cuit a una cuenta puntera.

Según los datos de los inscritos en `[NB_WEB].[dbo].[travel]` debemos lograr que para los distintos CUIT, se asignen a una cuenta puntera (a la que pertenece el usuario)

```
SELECT TOP (1000) [id]
      ,[userId]
      ,[phone]
      ,[documents]
      ,[registrationDate]
  FROM [NB_WEB].[dbo].[travel]
```

```
SELECT 
    t.id,
    t.userId,
    t.phone,
    u.codigoFP, -- ejemplo si querés algo del join
    LTRIM(RTRIM(m.n.value('.', 'NVARCHAR(MAX)'))) AS document,
    t.registrationDate
FROM NB_WEB.dbo.travel t
CROSS APPLY (
    SELECT CAST('<x>' + 
                REPLACE(t.documents, ',', '</x><x>') + 
                '</x>' AS XML) AS xmlData
) d
CROSS APPLY d.xmlData.nodes('/x') AS m(n)
LEFT JOIN NB_WEB.dbo.usuarios_nb u ON u.userId = t.userId
ORDER BY u.codigoFP DESC
```
