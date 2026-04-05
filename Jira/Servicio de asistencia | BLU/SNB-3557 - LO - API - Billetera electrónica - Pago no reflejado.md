---
jira_key: "SNB-3557"
aliases: ["SNB-3557"]
summary: "LO - API - Billetera electrónica - Pago no reflejado"
status: "Resuelta"
type: "Support"
priority: "Highest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-12-12 19:29"
updated: "2025-12-15 11:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3557"
---

# SNB-3557: LO - API - Billetera electrónica - Pago no reflejado

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Highest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-12 19:29 |
| Actualizado | 2025-12-15 11:03 |
| Etiquetas | ninguna |
| Jira | [SNB-3557](https://bluinc.atlassian.net/browse/SNB-3557) |

## Relaciones

- **relates to:** [[LIO-240]] API - Feat - Obtener balance de billetera

## Descripcion

Al realizar una compra con dinero en la billetera:

- No se visualiza el movimiento.


- El saldo disponible ni el saldo pendiente parece verse afectado.



```
GET {API_V4}/wallet/balance
```

[adjunto]
[adjunto]
