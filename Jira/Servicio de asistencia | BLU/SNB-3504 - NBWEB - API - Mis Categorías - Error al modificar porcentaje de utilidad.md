---
jira_key: "SNB-3504"
aliases: ["SNB-3504"]
summary: "NBWEB - API - Mis Categorías -> Error al modificar porcentaje de utilidad"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-10-31 09:54"
updated: "2025-11-10 13:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3504"
---

# SNB-3504: NBWEB - API - Mis Categorías -> Error al modificar porcentaje de utilidad

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-10-31 09:54 |
| Actualizado | 2025-11-10 13:26 |
| Etiquetas | ninguna |
| Jira | [SNB-3504](https://bluinc.atlassian.net/browse/SNB-3504) |

## Relaciones

- **relates to:** [[NBWEB-643]] API - Feat -Mis Categorias -> Agregar / Editar "Mi categoría"

## Descripcion

Como solución para este reporte, se propuso que si el producto/categoría se encuentran ocultos, no aparezcan más para estos recursos.

Por medio del correo de integraciones, se nos reporta que al modificar el porcentaje de utilidad de las categorías `REPRODUCTORES MULTIMEDIA` y `Mini PC`, se genera un error. Al realizar pruebas internas, se recopiló la siguiente información:

[adjunto]
```
curl.exe ^"https://api.nb.com.ar/v1/miCuenta/misCategorias^" ^
-X PATCH ^
-H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0^" ^
-H ^"Accept: application/json, text/plain, /^" ^
-H ^"Accept-Language: es-MX^" ^
-H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
-H ^"Content-Type: application/json^" ^
-H ^"Referer: https://nb.com.ar/^" ^
-H ^"Origin: https://nb.com.ar^" ^
-H ^"Sec-Fetch-Dest: empty^" ^
-H ^"Sec-Fetch-Mode: cors^" ^
-H ^"Sec-Fetch-Site: same-site^" ^
-H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjE5MjQ4NzMsImF1ZCI6IjhkYWY3NDk3MTkwOGExYzdkZWU4OTNiMDY5NWNkMGZmNzYyZTFiOTIiLCJ1c2VyIjp7ImlkIjo3NTY5NCwiY29kaWdvRlAiOiI4MjMzNCIsInJvbGUiOjEsImNvcnJlb0NvbmZpcm1hZG8iOjEsImNhcnJpdG9BY3Rpdm8iOjgzMjUyNjcsImJsYWNrVXNlciI6MCwic2hvd05hbWUiOm51bGwsIm1vZGUiOiJhcGkiLCJkb21haW4iOm51bGx9LCJpYXQiOjE3NjE5MTQwNzMsIm5iZiI6MTc2MTkxNDA3M30.RCLAZ2HWigVf6IlARgpFAXLAnPAXKyEvgM50gnse8Bs^" ^
-H ^"Connection: keep-alive^" ^
--data-raw ^"^{^\^"categoryId^\^":41,^\^"description^\^":^\^"REPRODUCTORES MULTIMEDIA^\^",^\^"utility^\^":11,^\^"hide^\^":false^}^"
```

[adjunto]
No se visualiza el mensaje de respuesta del Backend.
