---
jira_key: "PED-175"
aliases: ["PED-175"]
summary: "API - Feat - Listar comisiones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-10-26 10:14"
updated: "2024-02-02 08:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-175"
---

# PED-175: API - Feat - Listar comisiones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-26 10:14 |
| Actualizado | 2024-02-02 08:47 |
| Etiquetas | ninguna |
| Jira | [PED-175](https://bluinc.atlassian.net/browse/PED-175) |

## Relaciones

- **Padre:** [[PED-174]] Listar comisiones
- **blocks:** [[PED-176]] APP - Feat - Listar comisiones
- **blocks:** [[PED-526]] API - Refactor - Agregar comisiones de sucursal 10, que no se ven

## Descripcion

Crearemos una feature para poder mostrar las comisiones agrupadas por tipo de comisión y remito  pudiendo obtener y procesar información sobre comisiones basadas en fechas y agentes específicos. Las comisiones se calculan según diferentes condiciones y luego se estructuran en un formato específico.

Los filtros son 

- Vendedor


- Fecha





```
GET {API_URL}/v1/commissions?date{datre}&sellerId=8
```



Devuelve

```
{  {
    "date": "2023-10-02 16:07:30",
    "clientId": 6601,
    "order": "10329826",
    "clientName": "Eximb SRL                          ",
    "sellersName": "Altamiranda",
    "sellersName": "Andrea",
    "branch": "0002",
    "cnumalb": "00567208",
    "ID_NROREMCLI_ENC": "X000200567208",
    "credit": 0,
    "totalAmount": 4986.17,
    "priceList": "D",
    "commission": 10.97,
    "commissionSubtotal": 10.97,
    "totalShipped": 4986.17
  },
  {
    "date": "2023-10-02 16:12:54",
    "clientId": 26199,
    "order": "10329915",
    "clientName": "SUPPA NICOLAS HERNAN",
    "sellersName": "Altamiranda",
    "sellersName": "Andrea",
    "branch": "0002",
    "cnumalb": "00567207",
    "ID_NROREMCLI_ENC": "X000200567207",,
    "credit": 0,
    "totalAmount":2308.655,
    "priceList": "A",
    "commission": 11.543,
    "commissionSubtotal": 22.513,
    "totalShipped": 7294.825
  }
```



Usando la siguiente consulta(`$value`) y logica, podremos obtener los datos necesarios

```
if ($value->cnumalb) {

    switch ($value->listaPrecio) {

        case 'A':
            $coefComi = 0.5;
            break;
        case 'B':
            $coefComi = 0.35;
            break;
        case 'C':
            $coefComi = 0.35;
            break;
        default:
            $coefComi = 0.22;
            break;

    }

    $comision_operacion = $value->total * $coefComi / 100;
    $comision_subtotal  = $comision_operacion + $comision_subtotal;
    $total_remitido     = $total_remitido + $value->total;

```



```
(
        SELECT CONVERT(VARCHAR, E.FECHA_LIQUIDACION, 20) AS date
            , D.ID_CLIENTE as clientId
            , B.cnumped as 'order'
            , D.cnomcli as clientName
            , C.capeage as sellersName
            , C.cnbrage  as sellersName
            , A.cnumsuc as branch
            , A.cnumalb as cnumalb
            , B.ID_NROREMCLI_ENC
            , (SUM((A.ncanent * A.npreunit - A.ncanent * A.npreunit * A.ndto / 100))) AS total
            , A.listaPrecio
            , 0 AS credit
        FROM [NewBytes_DBF].[dbo].[albclil] A
        LEFT JOIN NewBytes_DBF.dbo.albclit B
            ON A.cnumalb = B.cnumalb
                AND A.cnumsuc = B.cnumsuc
        LEFT JOIN NewBytes_DBF.dbo.agentes C
            ON C.ID_VENDEDOR = B.ID_VENDEDOR
        LEFT JOIN NewBytes_DBF.dbo.clientes D
            ON D.ID_CLIENTE = B.ID_CLIENTE
        LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA E
            ON E.REMITO_FP = B.cnumalb
                AND E.SUCURSAL_REMITO = B.cnumsuc
        LEFT JOIN NewBytes_DBF.dbo.FP_FactWebCliEncabezado F
            ON F.ID_NROREMCLI_ENC = B.ID_NROREMCLI_ENC
                AND LANULADA <> 1
                AND CAE IS NOT NULL
        WHERE B.ccodage = 08
            AND F.DFECFAC BETWEEN '01-10-2023  00:00' AND '26-10-2023 23:59'
            AND B.ntipoalb > 1
            AND lfacturado = 1
            AND B.cnumsuc = '0002'
        --AND LANULADA <> 1 AND CAE IS NOT NULL
        GROUP BY E.FECHA_LIQUIDACION
            , D.ID_CLIENTE
            , B.cnumped
            , D.cnomcli
            , C.capeage
            , C.cnbrage
            , A.cnumsuc
            , A.cnumalb
            , B.ID_NROREMCLI_ENC
            , A.listaPrecio
        )

UNION

(
    SELECT CONVERT(VARCHAR, E.FECHA_LIQUIDACION, 20) AS dfecalb
        , D.ID_CLIENTE
        , B.cnumped
        , D.cnomcli
        , C.capeage
        , C.cnbrage
        , A.cnumsuc
        , A.cnumalb
        , B.ID_NROREMCLI_ENC
        , (SUM((A.ncanent * A.npreunit - A.ncanent * A.npreunit * A.ndto / 100))) AS total
        , A.listaPrecio
        , 0 AS credito
    FROM [NewBytes_DBF].[dbo].[albclil] A
    LEFT JOIN NewBytes_DBF.dbo.albclit B
        ON A.cnumalb = B.cnumalb
            AND A.cnumsuc = B.cnumsuc
    LEFT JOIN NewBytes_DBF.dbo.agentes C
        ON C.ID_VENDEDOR = B.ID_VENDEDOR
    LEFT JOIN NewBytes_DBF.dbo.clientes D
        ON D.ID_CLIENTE = B.ID_CLIENTE
    LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA E
        ON E.REMITO_FP = B.cnumalb
            AND E.SUCURSAL_REMITO = B.cnumsuc
    --LEFT JOIN NewBytes_DBF.dbo.FP_FactWebCliEncabezado F ON F.ID_NROREMCLI_ENC = B.ID_NROREMCLI_ENC AND LANULADA <> 1 AND CAE IS NOT NULL
    WHERE B.ccodage = 08
        AND E.FECHA_LIQUIDACION BETWEEN '01-10-2023 00:00' AND '26-10-2023 23:59'
        AND B.ntipoalb > 1
        AND lfacturado = 1
        AND B.cnumsuc = '0010'
    --AND LANULADA <> 1 AND CAE IS NOT NULL
    GROUP BY E.FECHA_LIQUIDACION
        , D.ID_CLIENTE
        , B.cnumped
        , D.cnomcli
        , C.capeage
        , C.cnbrage
        , A.cnumsuc
        , A.cnumalb
        , B.ID_NROREMCLI_ENC
        , A.listaPrecio
    )

UNION

(
    SELECT CONVERT(VARCHAR, E.FECHA_LIQUIDACION, 20) AS dfecalb
        , D.ID_CLIENTE
        , B.cnumped
        , D.cnomcli
        , C.capeage
        , C.cnbrage
        , A.cnumsuc
        , A.cnumalb
        , B.ID_NROREMCLI_ENC
        , (SUM((A.npreunit - A.npreunit * A.ndto / 100) * A.ACREDITADO) * - 1) AS total
        , A.listaPrecio
        , 1 AS credito
    FROM [NewBytes_DBF].[dbo].[albclil] A
    LEFT JOIN NewBytes_DBF.dbo.albclit B
        ON A.cnumalb = B.cnumalb
            AND A.cnumsuc = B.cnumsuc
    LEFT JOIN NewBytes_DBF.dbo.agentes C
        ON C.ID_VENDEDOR = B.ID_VENDEDOR
    LEFT JOIN NewBytes_DBF.dbo.clientes D
        ON D.ID_CLIENTE = B.ID_CLIENTE
    LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA E
        ON E.REMITO_FP = B.cnumalb
            AND E.SUCURSAL_REMITO = B.cnumsuc
    WHERE B.ccodage = 08
        AND E.FECHA_LIQUIDACION BETWEEN '01-10-2023  00:00' AND '26-10-2023 23:59'
                --AND B.cnumalb = '00514544'
        AND B.CNUMSUC = '0010'
        AND B.ntipoalb > 1
        AND A.ACREDITADO > 0
    GROUP BY E.FECHA_LIQUIDACION
        , D.ID_CLIENTE
        , B.cnumped
        , D.cnomcli
        , C.capeage
        , C.cnbrage
        , A.cnumsuc
        , A.cnumalb
        , B.ID_NROREMCLI_ENC
        , A.listaPrecio
    )

UNION

(
    SELECT CONVERT(VARCHAR, E.FECHA_LIQUIDACION, 20) AS dfecalb
        , D.ID_CLIENTE
        , B.cnumped
        , D.cnomcli
        , C.capeage
        , C.cnbrage
        , A.cnumsuc
        , A.cnumalb
        , B.ID_NROREMCLI_ENC
        , (SUM((A.npreunit - A.npreunit * A.ndto / 100) * A.ACREDITADO) * - 1) AS total
        , A.listaPrecio
        , 1 AS credito
    FROM [NewBytes_DBF].[dbo].[albclil] A
    LEFT JOIN NewBytes_DBF.dbo.albclit B
        ON A.cnumalb = B.cnumalb
            AND A.cnumsuc = B.cnumsuc
    LEFT JOIN NewBytes_DBF.dbo.agentes C
        ON C.ID_VENDEDOR = B.ID_VENDEDOR
    LEFT JOIN NewBytes_DBF.dbo.clientes D
        ON D.ID_CLIENTE = B.ID_CLIENTE
    LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA E
        ON E.REMITO_FP = B.cnumalb
            AND E.SUCURSAL_REMITO = B.cnumsuc
    WHERE B.ccodage = 41
        --AND E.FECHA_LIQUIDACION   BETWEEN '01-10-2022  00:00' AND '07-10-2022 23:59'
        AND B.ID_NROREMCLI_ENC IN (
            SELECT ID_NROREMCLI_ENC
            FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado F
            WHERE F.ccodage = 08
                AND F.DFECFAC BETWEEN '01-10-2023  00:00' AND '26-10-2023 23:59'
                AND NTIPODOCU = 2
            )
        --AND B.cnumalb = '00514544'
        AND B.ntipoalb > 1
        AND A.ACREDITADO > 0
    GROUP BY E.FECHA_LIQUIDACION
        , D.ID_CLIENTE
        , B.cnumped
        , D.cnomcli
        , C.capeage
        , C.cnbrage
        , A.cnumsuc
        , A.cnumalb
        , B.ID_NROREMCLI_ENC
        , A.listaPrecio
    )


```
