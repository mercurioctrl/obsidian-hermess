---
jira_key: "MKT-210"
aliases: ["MKT-210"]
summary: "API - Feat - Agregar repositorio de objtetivo genius por ventas/vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-27 09:27"
updated: "2024-08-27 14:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/MKT-210"
---

# MKT-210: API - Feat - Agregar repositorio de objtetivo genius por ventas/vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-27 09:27 |
| Actualizado | 2024-08-27 14:25 |
| Etiquetas | ninguna |
| Jira | [MKT-210](https://bluinc.atlassian.net/browse/MKT-210) |

## Relaciones

- **Padre:** [[MKT-208 - NB_ Incentivo GENIUS|MKT-208]] NB_ Incentivo GENIUS
- **blocks:** [[MKT-211 - APP - Feat - Agregar tabla de posiciones por vendedor|MKT-211]] APP - Feat - Agregar tabla de posiciones por vendedor

## Descripcion

Agregaremos el recurso

```
GET {{API_URL}}/v1/objectives/capillarityIncentive/sellers
```

Utilizaremos un repositorio similar a este para devolver un objeto determinado en la historia principal

```sql
SELECT 
    pedclit.ID_VENDEDOR as sellerId,
    agentes.cnbrage sellerLName,
    agentes.capeage as sellerFName,
    SUM(pedclil.npreunit * ncanped) AS TotalSales,
    COUNT(DISTINCT pedclit.cnumped) AS UniqueOrders
FROM 
    [NewBytes_DBF].[dbo].[pedclit]
LEFT JOIN 
    NewBytes_DBF.dbo.pedclil ON pedclit.cnumped = pedclil.cnumped 
    AND pedclit.cnumsuc = pedclil.cnumsuc
INNER JOIN 
    NewBytes_DBF.dbo.agentes ON agentes.ID_VENDEDOR = pedclit.ID_VENDEDOR
INNER JOIN
    NewBytes_DBF.dbo.albclit ON albclit.cnumped = pedclit.cnumped AND albclit.cnumsuc = pedclit.cnumsuc    
WHERE 
    dfecped BETWEEN '26-08-2024 00:00' AND '06-09-2024 23:59'
    AND pedclil.cdetalle LIKE '%GENIUS%'
    AND pedclit.lanula <> 1 AND cestado = 's' AND albclit.ntipoalb > 1
    AND (
        SELECT SUM(npreunit * ncanped)
        FROM NewBytes_DBF.dbo.pedclil P2
        WHERE P2.cnumsuc = pedclit.cnumsuc
        AND P2.cnumped = pedclit.cnumped
    ) > 300
GROUP BY 
    pedclit.ID_VENDEDOR,
    agentes.cnbrage,
    agentes.capeage
ORDER BY 
    COUNT(pedclit.id) DESC;


```

```json
[
  {
    "sellerId": 41,
    "sellerLName": "Sheridaim",
    "sellerFName": "Natalia",
    "TotalSales": 511294938000.0,
    "UniqueOrders": 8
  },
  {
    "sellerId": 8,
    "sellerLName": "Andrea",
    "sellerFName": "Altamiranda",
    "TotalSales": 622729185000.0,
    "UniqueOrders": 11
  },
  
  ...
  ]
```
