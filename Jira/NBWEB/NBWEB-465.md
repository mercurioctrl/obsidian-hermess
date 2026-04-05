---
jira_key: "NBWEB-465"
summary: "QUE SERIA EL ERROR QUE LE MUESTRA?"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-18 16:33"
updated: "2022-08-22 09:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-465"
---

# NBWEB-465: QUE SERIA EL ERROR QUE LE MUESTRA?

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-18 16:33 |
| Actualizado | 2022-08-22 09:59 |
| Etiquetas | ninguna |
| Jira | [NBWEB-465](https://bluinc.atlassian.net/browse/NBWEB-465) |

## Descripción

ABAJO A LA DERECHA LE TIRA UN ERROR QUE NO LE DEJA CERRAR EL PEDIDO.   COMO LO RESUELVE?

```
curl 'https://omega.api.nb.com.ar/v1/carrito/calcularEnvioPara/3550' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjA4NjE2NTksImF1ZCI6IjVjZjg2MTk2MzM1Y2ZlZTBkODBmZGFjNTRiY2MyNTQ1MmU5NGQ5ZDkiLCJ1c2VyIjp7ImlkIjo0NzE1MCwiY29kaWdvRlAiOiIwMzI0MTkiLCJyb2xlIjoxLCJjb3JyZW9Db25maXJtYWRvIjoxLCJjYXJyaXRvQWN0aXZvIjo4MTE3OTM4fSwiaWF0IjoxNjYwODUwODU5LCJuYmYiOjE2NjA4NTA4NTl9.9nKlcA6mQ6vhePCACMuEM-wvg4xT9Fm-UPWVks6yhXA' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://www.nb.com.ar' \
  -H 'Referer: https://www.nb.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

[attachment]
