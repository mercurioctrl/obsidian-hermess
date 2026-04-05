---
jira_key: "PED-9"
aliases: ["PED-9"]
summary: "API - Feat - Repositorio de ordenes de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-30 23:20"
updated: "2025-05-15 17:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-9"
---

# PED-9: API - Feat - Repositorio de ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-30 23:20 |
| Actualizado | 2025-05-15 17:52 |
| Etiquetas | ninguna |
| Jira | [PED-9](https://bluinc.atlassian.net/browse/PED-9) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra

## Descripcion

```
GET {API_URL}/v1/orders
```

```json
[
    {
        "date": "2023-05-22 09:33:56",
        "orderNumber": "10314626",
        "branchNumber": "0010",
        "albumNumber": "X001000021371",
        "realAlbumNumber": "00021371",
        "clientDescription": "MERCURIO CATRIEL EDUARDO",
        "clientID": 26806,
        "observation": "INTERNO",
        "status": "s",
        "invoice": "B000400038173",
        "token": "25d899a4e9d147f1ace0ab982d4e9b",
        "voucherId": 502911,
        "seller": "Sin dendedor",
        "totalInPesos": 198044,
        "finalTotalInPesos": 198044,
        "total": 643,
        "finalTotal": 643
    },
    {
        "date": "2023-07-30 21:28:06",
        "orderNumber": "10322757",
        "branchNumber": "0002",
        "albumNumber": null,
        "realAlbumNumber": null,
        "clientDescription": "Libre Opcion",
        "clientDescription_ID": 32103,
        "observation": "PEDIDO LIBRE OPCION",
        "status": "P",
        "invoice": null,
        "token": null,
        "voucherId": null,
        "seller": "Libre Opcion",
        "totalInPesos": 141303.55,
        "finalTotalInPesos": 156140.43,
        "total": 458.78,
        "finalTotal": 506.95
    },
    {
        "date": "2023-07-30 21:20:10",
        "orderNumber": "10322756",
        "branchNumber": "0002",
        "albumNumber": null,
        "realAlbumNumber": null,
        "clientDescription": "OLIVER JUAN GABRIEL",
        "clientDescription_ID": 56642,
        "observation": "PEDIDO DE INTERNET",
        "status": "P",
        "invoice": null,
        "token": null,
        "voucherId": null,
        "seller": "Altamiranda Andrea",
        "totalInPesos": 113356.22,
        "finalTotalInPesos": 132409.69,
        "total": 368.04,
        "finalTotal": 429.9
    }
]

```

## Repositorios de ejemplo

```
SELECT TOP(120)
    CONVERT(VARCHAR,pedclit.dfecped, 20) AS dfecped,
    pedclit.cnumped,
    pedclit.cnumsuc,
    cnomcli,
    capeage,
    cnbrage,
    SUM(ncanped*npreunit-ncanped*npreunit*pedclil.ndto/100) AS total,
    SUM((ncanped*npreunit-ncanped*npreunit*pedclil.ndto/100)+(ncanped*npreunit-ncanped*npreunit*pedclil.ndto/100)*pedclil.niva/100) AS totalFinal,
    [MS_COTIZACIONES].COTIZACION as cotizacionDiaria,
    pedclit.cestado,
    albclit.cnumalb,
    albclit.ID_NROREMCLI_ENC,
    clientes.ID_CLIENTE,
    FP_FactWebCliEncabezado.cfactura,
    FP_FactWebCliEncabezado.ID_NROFACCLI_ENC,
    pedclit.cobserv,
    FP_FactWebCliEncabezado.token
FROM 
    [NewBytes_DBF].[dbo].[pedclit]
    LEFT JOIN NewBytes_DBF.dbo.clientes on clientes.ID_CLIENTE = pedclit.ccodcli
    LEFT JOIN NewBytes_DBF.dbo.agentes on agentes.ID_VENDEDOR = pedclit.ccodage
    LEFT JOIN NewBytes_DBF.dbo.pedclil ON pedclil.cnumped = pedclit.cnumped and pedclil.cnumsuc = pedclit.cnumsuc
    LEFT JOIN NEW_BYTES.dbo.MS_COTIZACIONES ON MS_COTIZACIONES.NOMBRE = 'PESOS'
    LEFT JOIN NewBytes_DBF.dbo.albclit ON albclit.cnumped = pedclit.cnumped and albclit.cnumsuc = pedclit.cnumsuc
    LEFT JOIN NewBytes_DBF.dbo.articulo ON articulo.cRef = pedclil.cref
    LEFT JOIN [NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado] ON FP_FactWebCliEncabezado.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
WHERE 
    pedclit.cnumped IS NOT NULL      
    AND pedclit.dfecped BETWEEN '30-07-2023 00:01' AND '30-07-2023 23:59'  
GROUP BY
    pedclit.cnumped,
    pedclit.cnumsuc,
    dfecped,
    cnomcli,
    capeage,
    cnbrage,
    [MS_COTIZACIONES].COTIZACION,
    pedclit.cestado,
    albclit.cnumalb,
    albclit.ID_NROREMCLI_ENC,
    clientes.ID_CLIENTE,
    FP_FactWebCliEncabezado.cfactura,
    FP_FactWebCliEncabezado.ID_NROFACCLI_ENC,
    pedclit.cobserv,
    FP_FactWebCliEncabezado.token
ORDER BY 
    pedclit.dfecped DESC

```
