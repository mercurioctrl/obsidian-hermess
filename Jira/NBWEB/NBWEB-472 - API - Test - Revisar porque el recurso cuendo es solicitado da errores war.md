---
jira_key: "NBWEB-472"
aliases: ["NBWEB-472"]
summary: "API - Test - Revisar porque el recurso cuendo es solicitado da errores war"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-23 16:24"
updated: "2022-10-03 09:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-472"
---

# NBWEB-472: API - Test - Revisar porque el recurso cuendo es solicitado da errores war

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-23 16:24 |
| Actualizado | 2022-10-03 09:56 |
| Etiquetas | ninguna |
| Jira | [NBWEB-472](https://bluinc.atlassian.net/browse/NBWEB-472) |

## Relaciones

- **Padre:** [[NBWEB-206 - API - Leer mensajes de un meesageChannel|NBWEB-206]] API - Leer mensajes de un meesageChannel

## Descripcion

Al hacer

```
curl 'https://gamma.api.nb.com.ar/v1/postventa/32120/messageChannel' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjEyODY1NTUsImF1ZCI6ImE2NGRkZDdlNWVhMzQ1M2RhZWY1NTcwMTE4YTY2MmNmYWExZjJjMTYiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RpZ29GUCI6IjI1NDMzIiwicm9sZSI6MSwiY29ycmVvQ29uZmlybWFkbyI6MSwiY2Fycml0b0FjdGl2byI6ODEyMTQxOH0sImlhdCI6MTY2MTI3NTc1NSwibmJmIjoxNjYxMjc1NzU1fQ.hjUF6D6eiqeHKwFObPcywkmA_Rw80phwhnLZ1RMInzs' \
  -H 'Connection: keep-alive' \
  -H 'Origin: http://gamma.nb.com.ar' \
  -H 'Referer: http://gamma.nb.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

Se obtiene

```
<br />
<b>Warning</b>:  Attempt to read property "ID_RMACLIENTE" on bool in <b>/var/www/app/src/Repository/PostVentaRepository.php</b> on line <b>267</b><br />
<br />
<b>Warning</b>:  Undefined array key 0 in <b>/var/www/app/src/Service/PostVentaService.php</b> on line <b>177</b><br />
<br />
<b>Warning</b>:  Attempt to read property "rmaId" on null in <b>/var/www/app/src/Dto/PostVentaDto/PostVentaHeaderDto.php</b> on line <b>17</b><br />
<br />
<b>Warning</b>:  Attempt to read property "clientId" on null in <b>/var/www/app/src/Dto/PostVentaDto/PostVentaHeaderDto.php</b> on line <b>18</b><br />
<br />
<b>Warning</b>:  Attempt to read property "dateAdmission" on null in <b>/var/www/app/src/Dto/PostVentaDto/PostVentaHeaderDto.php</b> on line <b>19</b><br />
<br />
<b>Warning</b>:  Attempt to read property "status" on null in <b>/var/www/app/src/Dto/PostVentaDto/PostVentaHeaderDto.php</b> on line <b>20</b><br />
<br />
<b>Warning</b>:  Attempt to read property "agentId" on null in <b>/var/www/app/src/Dto/PostVentaDto/PostVentaHeaderDto.php</b> on line <b>21</b><br />
<br />
<b>Warning</b>:  Attempt to read property "outboundStatus" on null in <b>/var/www/app/src/Dto/PostVentaDto/PostVentaHeaderDto.php</b> on line <b>22</b><br />
{"isMessageChannelOpen":false,"messageChannel":[],"ticketHeader":{"rmaId":0,"clientId":0,"date":null,"status":"","agentId":"","outboundStatus":""},"ticketDetails":[]}
```
