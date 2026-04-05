---
jira_key: "LOCAPP-44"
aliases: ["LOCAPP-44"]
summary: "MS - Volanta - Intento fallido al leer la variable token"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2024-05-02 21:44"
updated: "2024-07-24 18:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-44"
---

# LOCAPP-44: MS - Volanta - Intento fallido al leer la variable token

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-02 21:44 |
| Actualizado | 2024-07-24 18:04 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-44](https://bluinc.atlassian.net/browse/LOCAPP-44) |

## Relaciones

- **blocks:** [[LOCAPP-37]] MS - Refactor - Trasladar ambos parametros de dropshipping y join shipping al ms de comprobantes

## Descripcion

Al intentar visualizar la volanta desde Expedición, me aparece la siguiente advertencia. 

[adjunto]
```
curl 'https://gamma.ms-comprobantes.lio.red/v2/operationalOrder/X000200569130' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.comprobantes.lio.red' \
  -H 'Referer: https://gamma.comprobantes.lio.red/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

Dato extra:
Es posible que esté fallando el inicio de sesión en Expedición desde el MS de comprobantes.

Como sugerencia, me gustaría agregar una validación para verificar si la variable `token` está definida. Dejo esto a tu consideración.
