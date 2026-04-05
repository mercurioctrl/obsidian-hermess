---
jira_key: "LIO-75"
aliases: ["LIO-75"]
summary: "API - Refactor - Ver productos del vendedor - Error al buscar atributo "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-07-23 13:49"
updated: "2024-07-24 11:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-75"
---

# LIO-75: API - Refactor - Ver productos del vendedor - Error al buscar atributo 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-07-23 13:49 |
| Actualizado | 2024-07-24 11:08 |
| Etiquetas | ninguna |
| Jira | [LIO-75](https://bluinc.atlassian.net/browse/LIO-75) |

## Relaciones

- **Padre:** [[LIO-2]] Variedad y Calidad de Productos/Catalogos
- **blocks:** [[LIO-73]] API - Refactor - Ver productos del vendedor - Añadir atributos

## Descripcion

Después de buscar por reseller y seleccionar alguno de sus atributos listados, me aparece el siguiente error. Cabe mencionar que esto sucede al buscar también cualquier articulo y seleccionar alguno de sus atributos.

[adjunto]
[adjunto]
```
curl "https://omega.api4.libreopcion.com/v4/search?search=bitbayres&offset=0&o=rel&color=rojo" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Referer: https://gamma.libreopcion.com/bitbayres?o=rel&ver_mas_vendedores=1&color=rojo" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjoyMzkzNzgsImVtYWlsIjoiZ2F2aWxhQG5iLmNvbS5hciIsIm5vbWJyZSI6IkdwcnVlYmEgTE8iLCJwZXJmaWwiOiJ2ZW5kZWRvciIsImRvY3VtZW50byI6Ik4wMDEyMzQ1NjciLCJ0ZWxlZm9ubyI6IjU0MTEgMjE2Mi03Mjg4IiwiZGlyZWNjaW9uIjp7ImNhbGxlIjoiQ0FMTEUgTUVYSUNPIiwibnVtZXJvIjoiNTAwIiwicGlzbyI6IjEiLCJjYXNhQXB0byI6IkNBU0EifSwiY29kaWdvX3Bvc3RhbCI6IjEyMDAiLCJhdmF0YXIiOjQsImNpdWRhZCI6eyJpZCI6MTQxOTAsIm5vbWJyZSI6IjkgREUgQUJSSUwiLCJwcm92aW5jaWFfaWQiOjIsInRvdGFsIjowfSwicHJvdmluY2lhIjp7ImlkIjoyLCJrZXkiOjIsIm5vbWJyZSI6IkJVRU5PUyBBSVJFUyIsInBhaXNfaWQiOjcsInRvdGFsIjowLCJjaXVkYWRfZGVmZWN0b19pZCI6MH0sInBhaXMiOnsiaWQiOjcsIm5vbWJyZSI6IkFSR0VOVElOQSIsInRvdGFsIjowfSwidGllbmRhX2lkIjowLCJ2ZW5kZWRvcl9pZCI6MjA3NjU0LCJ0b2tlblY0IjoiQ0Y0OUZEOEUtNDczQS00Q0M5LUJBNDgtOUU2MUQ2MkI0ODYzIn0sImlzcyI6ImxpYnJlb3BjaW9uLmNvbSIsImF1ZCI6ImxpYnJlb3BjaW9uLmNvbSIsImlhdCI6MTcyMTM5NTQyNywibmJmIjoxNzIxMzk1NDI3fQ.IODH0ARz6RYYPci9nVXgKKldl6d-ysiTc_yQR-F30lA" -H "Origin: https://gamma.libreopcion.com" -H "Connection: keep-alive" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-site" -H "Priority: u=0"
```

```
Object { status: 500, title: `SQLSTATE[HY000]: General error: 20018 The multi-part identifier "AV.value" could not be bound. [20018] (severity 16) [SELECT tbl.internal_id,tbl.product_picture,tbl.brand_picture,tbl.free_shipping,tbl.instant_flash,tbl.id_brand,tbl.brand_name,tbl.discount,tbl.finalPrice,tbl.listPrice,tbl.id_lo,tbl.category_id_lo,tbl.category_name,tbl.[description],tbl.keywords,tbl.mayconversion , MAX(tbl.rank) as ranking , tbl.sellerId, tbl.sellerName,tbl.sku,tbl.gtin FROM ( SELECT DISTINCT\n [internal_id]\n …E Latin1_general_CI_AI AND AV.value IN ( 'rojo'))\n as tbl\n \n GROUP BY tbl.internal_id,tbl.product_picture,tbl.brand_picture,tbl.free_shipping,tbl.instant_flash,tbl.id_brand,tbl.brand_name,tbl.discount,tbl.finalPrice,tbl.listPrice,tbl.id_lo,tbl.category_id_lo,tbl.category_name,tbl.[description],tbl.keywords,tbl.mayconversion , tbl.sellerId, tbl.sellerName,tbl.sku,tbl.gtin \n ORDER BY ranking DESC, mayConversion DESC OFFSET 0 rows FETCH next 30 rows only)`, file: "/var/www/app/vendor/laravel/framework/src/Illuminate/Database/Connection.php", … }
```
