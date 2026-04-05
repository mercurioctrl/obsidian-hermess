---
jira_key: "SNB-3392"
aliases: ["SNB-3392"]
summary: "Whaticket - LO - Error al intentar subir imagen de producto"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2025-09-11 15:42"
updated: "2025-11-07 17:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3392"
---

# SNB-3392: Whaticket - LO - Error al intentar subir imagen de producto

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2025-09-11 15:42 |
| Actualizado | 2025-11-07 17:07 |
| Etiquetas | ninguna |
| Jira | [SNB-3392](https://bluinc.atlassian.net/browse/SNB-3392) |

## Relaciones

*Sin relaciones*

## Descripcion

Por medio de Whaticket nos reportan que al intentar subir la imagen de un articulo les aparece un error. Al replicar el error de manera interna se recabo la siguiente información:



```
Internal Server Error: Signature verification failed
```

```
curl 'https://omega-api.libreopcion.com.ar/statics/upload-file/temp' \
  -X POST \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0' \
  -H 'Accept: application/json' \
  -H 'Accept-Language: es-MX' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Cache-Control: no-cache' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NzA1NTkyMzQsImF1ZCI6Ijc0ZDM5MGQ3NGQzZTg0NDE3MzFiMDc3MWYzNTUyNjZkOWNlNmRkODUiLCJ1c2VyIjp7ImlkIjo3NDI1MSwiZW1haWwiOiJjaGVueS5tc25AZ21haWwuY29tIiwibm9tYnJlIjoiRGVuaXMgTWFydGluZXoiLCJwZXJmaWwiOiJ2ZW5kZWRvciIsImRvY3VtZW50byI6IjM3OTc0MzUyIiwidGVsZWZvbm8iOiIzNzI1NTU4MzM0IiwiZGlyZWNjaW9uIjp7ImNhbGxlIjoiQ2hpbGUgMTIwIiwibnVtZXJvIjoiMTIwIiwicGlzbyI6IjEiLCJjYXNhQXB0byI6IjEifSwiY29kaWdvUG9zdGFsIjoiMzUwOSIsImF2YXRhciI6MywiY2l1ZGFkIjp7ImlkIjo4MDg0LCJub21icmUiOiJHRU5FUkFMIEpPU0UgREUgU0FOIE1BUlRJTiAgICAiLCJwcm92aW5jaWFJZCI6OH0sInByb3ZpbmNpYSI6eyJpZCI6OCwibm9tYnJlIjoiQ0hBQ08gICAgICAgICAgICAgICAgICAgICAgICAgIiwicGFpc0lkIjo3LCJjaXVkYWREZWZlY3RvSWQiOjgwODR9LCJwYWlzIjp7ImlkIjo3LCJub21icmUiOiJBUkdFTlRJTkEifSwidGllbmRhSWQiOjAsInZlbmRlZG9ySWQiOjU5ODE4LCJ0b2tlblYzIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjFjM1ZoY21sdklqcDdJbWxrSWpvM05ESTFNU3dpWlcxaGFXd2lPaUpqYUdWdWVTNXRjMjVBWjIxaGFXd3VZMjl0SWl3aWJtOXRZbkpsSWpvaVJHVnVhWE1nVFdGeWRHbHVaWG9pTENKd1pYSm1hV3dpT2lKMlpXNWtaV1J2Y2lJc0ltUnZZM1Z0Wlc1MGJ5STZJak0zT1RjME16VXlJaXdpZEdWc1pXWnZibThpT2lJek56STFOVFU0TXpNMElpd2laR2x5WldOamFXOXVJanA3SW1OaGJHeGxJam9pUTJocGJHVWdNVEl3SWl3aWJuVnRaWEp2SWpvaU1USXdJaXdpY0dsemJ5STZJakVpTENKallYTmhRWEIwYnlJNklqRWlmU3dpWTI5a2FXZHZYM0J2YzNSaGJDSTZJak0xTURraUxDSmhkbUYwWVhJaU9qTXNJbU5wZFdSaFpDSTZleUpwWkNJNk9EQTROQ3dpYm05dFluSmxJam9pUjBWT1JWSkJUQ0JLVDFORklFUkZJRk5CVGlCTlFWSlVTVTRpTENKd2NtOTJhVzVqYVdGZmFXUWlPamdzSW5SdmRHRnNJam93ZlN3aWNISnZkbWx1WTJsaElqcDdJbWxrSWpvNExDSnJaWGtpT2pnc0ltNXZiV0p5WlNJNklrTklRVU5QSWl3aWNHRnBjMTlwWkNJNk55d2lkRzkwWVd3aU9qQXNJbU5wZFdSaFpGOWtaV1psWTNSdlgybGtJam93ZlN3aWNHRnBjeUk2ZXlKcFpDSTZOeXdpYm05dFluSmxJam9pUVZKSFJVNVVTVTVCSWl3aWRHOTBZV3dpT2pCOUxDSjBhV1Z1WkdGZmFXUWlPakFzSW5abGJtUmxaRzl5WDJsa0lqbzFPVGd4T0N3aWRHOXJaVzVXTkNJNklqRXpSa1JETkRGRUxVRTJOalV0TkVFMFF5MDVNVU13TFRjNE5qZEdRVVpHUWpWRFF5SXNJbU52WkdsbmIxOXdiM04wWVd4ZlpHVm1ZWFZzZENJNk1USXlPU3dpWVdOMGFYWmxWMkZzYkdWMElqcG1ZV3h6Wlgwc0ltbHpjeUk2SW14cFluSmxiM0JqYVc5dUxtTnZiU0lzSW1GMVpDSTZJbXhwWW5KbGIzQmphVzl1TG1OdmJTSXNJbWxoZENJNk1UYzFOelU1T1RJek5Dd2libUptSWpveE56VTNOVGs1TWpNMGZRLlhyUUZVM2Rndnp0Wm8wMVVXRGIxYTJ0WHdGOUR5R1lEVC12MEM3Y3Rtc3MiLCJjb2RpZ29Qb3N0YWxEZWZhdWx0IjoxMjI5LCJhY3RpdmVXYWxsZXQiOmZhbHNlfSwiaWF0IjoxNzU3NTk5MjM0LCJuYmYiOjE3NTc1OTkyMzR9.X8QXesIicvW5Jl0iXAL17eFj673ls1N8cpTfexWb0uQ' \
  -H 'Content-Type: multipart/form-data; boundary=----geckoformboundary25d7e2f97c44a602b4801752f282f331' \
  -H 'Origin: https://libreopcion.com.ar' \
  -H 'Connection: keep-alive' \
  -H 'Referer: https://libreopcion.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  --data-binary \
  $'------geckoformboundary25d7e2f97c44a602b4801752f282f331\r\nContent-Disposition: form-data; name="file"; filename="gris.png"\r\nContent-Type: image/jpeg\r\n\r\n------geckoformboundary25d7e2f97c44a602b4801752f282f331--\r\n'
```

[adjunto]


---

Te comparto aquí información adicional del cliente:

```
cheny.msn@gmail.com
```

```
SELECT	
    usuarios.id,    	
    usuarios.nombre,
    usuarios.correo,
    clientes.ID_CLIENTE,
    clientes.cnomcli,
	usuarios.activo,
	email_verificado
FROM [LO].[dbo].[usuarios]
LEFT JOIN NewBytes_DBF.dbo.clientes ON usuarios.id = clientes.clientLo
WHERE id IN(74251)
```

[adjunto]
