---
jira_key: "POS-82"
aliases: ["POS-82"]
summary: "API - Test - Revisar porque no carga correctamente la grilla (falla hace poco, antes funcionaba)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-23 16:38"
updated: "2022-10-11 10:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-82"
---

# POS-82: API - Test - Revisar porque no carga correctamente la grilla (falla hace poco, antes funcionaba)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-23 16:38 |
| Actualizado | 2022-10-11 10:20 |
| Etiquetas | ninguna |
| Jira | [POS-82](https://bluinc.atlassian.net/browse/POS-82) |

## Relaciones

- **Padre:** [[POS-33 - API - Feat - Listar postventas finalizadas|POS-33]] API - Feat - Listar postventas finalizadas

## Descripcion

Al hacer

```
curl 'https://gamma.api.aftersale.lio.red/v1/afterSalesFinalized?currentPage=1&itemsPerPage=15' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjEzNjczNDIsImF1ZCI6IjkyZjlhNmRhZTBhYzRkNDE1YTBjMzRhMTdjMjE1NjFjYmVhYTcxNDAiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjI1NDMzIiwicG9zdHZlbnRhIjoiMSIsInBvc3R2ZW50YV9jcmVkaXRvcyI6IjEiLCJhZ2VudElkIjoiMTIiLCJwb3N0dmVudGFfc29sdWNpb24iOiIwIiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIn0sImlhdCI6MTY2MTI4MDk0MiwibmJmIjoxNjYxMjgwOTQyfQ.2vPH0I9rZkJr_7L-XPqzo5V96CsXmFuJpSpkPYEldSE' \
  -H 'Connection: keep-alive' \
  -H 'Origin: http://gamma.postventa.saftel.com' \
  -H 'Referer: http://gamma.postventa.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

Retorna 

```
{
    "message": "Slim Application Error",
    "exception": [
        {
            "type": "Exception",
            "code": 0,
            "message": "SQLSTATE[42000]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]La columna 'NEW_BYTES.dbo.ST_RMACABECERA.ID_RMACLIENTE' de la lista de selecci\u00f3n no es v\u00e1lida, porque no est\u00e1 contenida en una funci\u00f3n de agregado ni en la cl\u00e1usula GROUP BY. SQL: SELECT C.ID_RMACLIENTE as aftersaleId, CAST(C.ID_CLIENTE AS INT) as clientId, rtrim(CL.cnomcli) as clientName, (SELECT FORMAT (CAST(C.FECHA_INGRESO as date),'dd-MM-yyyy') as date) as admissionDate, CAST(C.HORA AS TIME ) as dateTime, rtrim(C.ESTADO) as status, rtrim(C.ID_USUARIO) as agentId, CONCAT(rtrim(P.USU_NOMBRE),' ',rtrim(P.USU_APELLIDO)) as agentName , CASE WHEN rtrim(D.ENTREGADO) != '' THEN 1 ELSE 0 END as dispatched, (SELECT FORMAT (CAST(D.FECHA_ENTREGA as date),'dd-MM-yyyy') as date) as dispatchedDate, MAX(D.finishedTestingDate) as finishedTime, C.assignationDate as assignationDate FROM [NEW_BYTES].[dbo].[ST_RMACABECERA] C LEFT JOIN NEW_BYTES.dbo.ST_RMADETALLE D ON C.ID_RMACLIENTE = D.ID_RMACLIENTE LEFT JOIN NewBytes_DBF.dbo.articulo as Ar ON Ar.cRef = D.PRODUCTO_CREF LEFT JOIN [NewBytes_DBF].[dbo].[clientes] as CL ON CAST(CL.ccodcli AS INT) = CAST(C.ID_CLIENTE AS INT) left JOIN [NEW_BYTES].[dbo].[PGM_USUARIOS] AS P ON (RTRIM(C.ID_USUARIO) = RTRIM(P.ID_AGENTE)) OR (RTRIM(C.ID_USUARIO) = P.USU_IDENTIFICACION) WHERE C.REVISADO = 'SI' AND C.ESTADO = 'REVISADO' ORDER BY C.ID_RMACLIENTE DESC OFFSET 0 rows FETCH next 15 rows only",
            "file": "/var/www/app/src/App/Database.php",
            "line": 122
        }
    ]
}
```
