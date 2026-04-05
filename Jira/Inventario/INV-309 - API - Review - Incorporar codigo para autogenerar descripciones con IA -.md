---
jira_key: "INV-309"
aliases: ["INV-309"]
summary: "API - Review - Incorporar codigo para autogenerar descripciones con IA - getSuggestDecription no está definido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-12-29 15:22"
updated: "2026-01-09 15:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-309"
---

# INV-309: API - Review - Incorporar codigo para autogenerar descripciones con IA - getSuggestDecription no está definido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-29 15:22 |
| Actualizado | 2026-01-09 15:22 |
| Etiquetas | ninguna |
| Jira | [INV-309](https://bluinc.atlassian.net/browse/INV-309) |

## Relaciones

- **Padre:** [[INV-80 - Descripciones|INV-80]] Descripciones
- **clones:** [[INV-84 - API - Refactor - Incorporar codigo para autogenerar descripciones con IA|INV-84]] API - Refactor - Incorporar codigo para autogenerar descripciones con IA

## Descripcion

Al intentar consumir el recurso aparece el siguiente error.

[adjunto]
```
curl.exe ^"https://gamma.api.inventory.lio.red/suggestDescription^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Content-Type: application/json^" ^
  -H ^"Referer: https://gamma.inventario.saftel.com/^" ^
  -H ^"Origin: https://gamma.inventario.saftel.com^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjcxMDg0MjcsInVzdWFyaW8iOjY2MzY5fQ.ipSbh_H1sp4xRugcpbcN_8f7OwpZq-NNTAVihVZqhMQ^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"^{^\^"itemId^\^":121111,^\^"characteristics^\^":^\^"DISCO SSD PATRIOT P400 2TB M.2 2280 GEN4 PS001656^\^",^\^"temperature^\^":0.5^}^"
```
