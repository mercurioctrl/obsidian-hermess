---
jira_key: "PED-401"
aliases: ["PED-401"]
summary: "API - Feat - Ver seriales tomados para un pedido determinado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-27 12:58"
updated: "2023-12-28 17:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-401"
---

# PED-401: API - Feat - Ver seriales tomados para un pedido determinado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-27 12:58 |
| Actualizado | 2023-12-28 17:52 |
| Etiquetas | ninguna |
| Jira | [PED-401](https://bluinc.atlassian.net/browse/PED-401) |

## Relaciones

- **Padre:** [[PED-400 - Ver serializacion|PED-400]] Ver serializacion
- **blocks:** [[PED-402 - APP - Feat - Ver seriales tomados para un pedido determinado|PED-402]] APP - Feat - Ver seriales tomados para un pedido determinado

## Descripcion

Este recurso se encarga de traer todos los seriales para un pedido determinado

```
GET {API_URL}/v1/orders/{PEDIDO}/serials
```

```
[
    {
        "id": "111453",
        "description": "PROCESADOR AMD (AM4) RYZEN 5 5600G",
        "serial": "9LU6433N30261",
        "outDate": "20231227.0",
        "inDate": "20231123.0",
        "exactTime": "27\/12\/2023, 10:46:56"
    },
    {
        "id": "111453",
        "description": "PROCESADOR AMD (AM4) RYZEN 5 5600G",
        "serial": "9LU6468N30079",
        "outDate": "20231227.0",
        "inDate": "20231123.0",
        "exactTime": "27\/12\/2023, 10:46:58"
    }
]

```

```
SELECT articulo.id_articulo
    , articulo.cdetalle
    , [ST_REMITOS_VENTA_DETALLE_SALIDA].SERIAL
    , albclit.cnumalb
    , FECHA_EGRESO
    , FECHA_INGRESO
    , FORMAT([ST_REMITOS_VENTA_DETALLE_SALIDA].HORA_EXACTA, 'dd/MM/yyyy, hh:mm:ss') AS HORA_EXACTA
FROM [NewBytes_DBF].[dbo].[albclit]
INNER JOIN [NewBytes_DBF].[dbo].[albclil]
    ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
INNER JOIN [NewBytes_DBF].[dbo].clientes
    ON clientes.ccodcli = albclit.ccodcli
INNER JOIN [NEW_BYTES].[dbo].[ST_REMITOS_VENTA_DETALLE_SALIDA]
    ON [ST_REMITOS_VENTA_DETALLE_SALIDA].REMITO_FP = albclit.cnumalb
        AND ST_REMITOS_VENTA_DETALLE_SALIDA.SUCURSAL_REMITO = ALBCLIT.cnumsuc
        AND ST_REMITOS_VENTA_DETALLE_SALIDA.CREF = albclil.cref
INNER JOIN [NEW_BYTES].[dbo].[ST_DETALLE_STOCK]
    ON ST_REMITOS_VENTA_DETALLE_SALIDA.ID_STOCK = ST_DETALLE_STOCK.ID_STOCK
LEFT JOIN [NewBytes_DBF].[dbo].articulo
    ON articulo.cref = albclil.cref
WHERE dfecalb > '20171130'
    AND albclit.ID_NROREMCLI_ENC = ?
ORDER BY cdetalle ASC

```
