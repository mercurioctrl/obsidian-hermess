---
jira_key: "SNB-2954"
aliases: ["SNB-2954"]
summary: "Sucede alguna cosa respecto a la API de mercadolibre, pese a tener token actualizado parece generar un error"
status: "Cerrada"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-03 08:56"
updated: "2025-04-08 09:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2954"
---

# SNB-2954: Sucede alguna cosa respecto a la API de mercadolibre, pese a tener token actualizado parece generar un error

| Campo | Valor |
|-------|-------|
| Estado | Cerrada (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-03 08:56 |
| Actualizado | 2025-04-08 09:26 |
| Etiquetas | ninguna |
| Jira | [SNB-2954](https://bluinc.atlassian.net/browse/SNB-2954) |

## Relaciones

*Sin relaciones*

## Descripcion

Recién me acabo de dar cuenta que pasa esto, pero no parece indicar un problema de autorización ¿me podras ayudar a debuguearlo para ver si cambio algo en la api?

```
curl 'https://api.inventory.lio.red/getImages/string?title=amd' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDM3MTEyMTcsInVzdWFyaW8iOjc0NjN9.NHUCJ2u3IWVL1dBqcSEGQIz7204_kCnF46mzpIi8uks' \
  -H 'Referer: https://inventario.saftel.com/' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"' \
  -H 'sec-ch-ua-mobile: ?0'
```
