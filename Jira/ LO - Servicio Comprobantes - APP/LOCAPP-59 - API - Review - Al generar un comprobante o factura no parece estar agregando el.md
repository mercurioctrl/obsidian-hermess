---
jira_key: "LOCAPP-59"
aliases: ["LOCAPP-59"]
summary: "API - Review - Al generar un comprobante o factura no parece estar agregando el internalTax, pese a ser una orden que si lo tiene"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2024-11-08 15:27"
updated: "2024-12-30 07:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-59"
---

# LOCAPP-59: API - Review - Al generar un comprobante o factura no parece estar agregando el internalTax, pese a ser una orden que si lo tiene

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-08 15:27 |
| Actualizado | 2024-12-30 07:04 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-59](https://bluinc.atlassian.net/browse/LOCAPP-59) |

## Relaciones

- **Padre:** [[LOCAPP-23 - Generar un comprobante|LOCAPP-23]] Generar un comprobante

## Descripcion

```
curl 'https://ms-comprobantes.lio.red/v2/F/555902/4d87f991497649f0bd70662537f192' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://comprobantes.lio.red' \
  -H 'Referer: https://comprobantes.lio.red/voucher/F/555902/4d87f991497649f0bd70662537f192?show=1' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```
