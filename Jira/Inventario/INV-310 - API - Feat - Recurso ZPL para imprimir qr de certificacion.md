---
jira_key: "INV-310"
aliases: ["INV-310"]
summary: "API - Feat - Recurso ZPL para imprimir qr de certificacion"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-02 08:01"
updated: "2026-01-09 09:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-310"
---

# INV-310: API - Feat - Recurso ZPL para imprimir qr de certificacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-02 08:01 |
| Actualizado | 2026-01-09 09:24 |
| Etiquetas | ninguna |
| Jira | [INV-310](https://bluinc.atlassian.net/browse/INV-310) |

## Relaciones

- **Padre:** [[INV-260 - Certificados eléctricos por Qr|INV-260]] Certificados eléctricos por Qr
- **has action item:** [[INV-311 - APP - Feat - Imprimir Recurso ZPL de qr de certificacion|INV-311]] APP - Feat - Imprimir Recurso ZPL de qr de certificacion
- **has action item:** [[INV-321 - API - Refactor - Recurso ZPL para imprimir qr de certificacion - Multiplicador|INV-321]] API - Refactor - Recurso ZPL para imprimir qr de certificacion -> Multiplicador de cantidad

## Descripcion

Según lo conversado ([link](https://blustudioinc.slack.com/archives/C03MPNS3N4W/p1767123600098879) ) dispondremos un recurso que nos permita imprimir el Qr por `ZPL` para cada uno de los casos

```
GET {API_URL}/electricalCertificate/{certificateId}/zpl
```

Esto devolverá el recurso con el código puro o texto plano, similar a como se realizo con las etiquetas de correo en otro momento (GET [https://api.warehouse.lio.red/v1/orders/zpl/360002849363940](https://api.warehouse.lio.red/v1/orders/zpl/360002849363940))

En cuanto el enlace que debe enrutarse en el Qr generado, siempre sera de esta forma

```
https://comprobantes.lio.red/voucher/certificate/{certificateId}
```

El mismo debe estar realizado de esta manera y entrar en la  etiqueta de 50ml de ancho x 25mm de ancho

[adjunto]
