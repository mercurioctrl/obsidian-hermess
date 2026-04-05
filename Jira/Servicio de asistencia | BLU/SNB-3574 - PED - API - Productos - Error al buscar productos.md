---
jira_key: "SNB-3574"
aliases: ["SNB-3574"]
summary: "PED - API - Productos -> Error al buscar productos"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-12-22 17:32"
updated: "2025-12-22 17:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3574"
---

# SNB-3574: PED - API - Productos -> Error al buscar productos

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-22 17:32 |
| Actualizado | 2025-12-22 17:41 |
| Etiquetas | ninguna |
| Jira | [SNB-3574](https://bluinc.atlassian.net/browse/SNB-3574) |

## Relaciones

*Sin relaciones*

## Descripcion

Al buscar un producto me aparece el siguiente error:

[adjunto]
```
curl.exe ^"https://gamma.api.orders.lio.red/v1/items?order=10426406^&branch=0002^&between=07-12-2025_22-12-2025^&companyCode=4^&stockWarehouseId=2^&currentPage=1^&stock=1^&search=gabinete^&itemsPerPage=35^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjY0Mzg3ODUsImF1ZCI6ImVjYTJjNWI0MDExZDA3YTExNzE3NGFkYjZiMjliZjIxNzA5OTQ1MmIiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYWRvciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjEsImlzUG0iOjEsImlzR2VyZW5jaWEiOjEsImVkaXRDb3N0Rm9yU2FsZSI6MSwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjoxLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsLCJjcmVhdGVNYW51YWxWb3VjaGVyIjoxLCJiYW5MaXN0UHJpY2UiOiJDIiwidW5sb2NrZWRTZWxsZXJGaWx0ZXIiOjEsInVzZVN0b2NrSW5jb21pbmciOjF9LCJpYXQiOjE3NjY0MzUxODUsIm5iZiI6MTc2NjQzNTE4NX0.DqpxfxpW1TC8QE-_QzhZc3TVYnS_vIufGSoisv-rSgg^" ^
  -H ^"Origin: https://gamma.pedidos.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.pedidos.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^"
```

```
{ status: 500, title: "SQLSTATE[HY000]: General error: 20018 Column 'NewBytes_DBF.dbo.articulo.kit' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause. [20018] (severity 16) [SELECT\n A.ID_ARTICULO,\n A.CDETALLE,\n M.referencia AS MARCA,\n A.Id_marca as brandId,\n F.cnomfam AS FAMILIA,\n F.ID_FAMILIA,\n A.ID_PRODUCTO,\n A.ivaVenta,\n A…ILIA,\n M.imagen,\n C.niva,\n S.nstock_reserva_pedidos,\n M.referencia,\n NUC.utility,\n UI.utility,\n A.companyCode,\n S.nstock_postventa,\n S.ID_ALMACEN,\n ALM.CNOMBRE,\n ALM.CCODALM,\n S.nstock_ingresando\n ORDER BY\n F.cnomfam ASC,\n M.referencia ASC,\n A.CDETALLE ASC )", file: "/var/www/app/vendor/laravel/framework/src/Illuminate/Database/Connection.php", … }
```
