---
jira_key: "NBWEB-691"
aliases: ["NBWEB-691"]
summary: "API - Agregar/Obtener comprobante de pago - No se visualiza el comprobante"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-09 02:14"
updated: "2024-04-15 00:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-691"
---

# NBWEB-691: API - Agregar/Obtener comprobante de pago - No se visualiza el comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-09 02:14 |
| Actualizado | 2024-04-15 00:35 |
| Etiquetas | ninguna |
| Jira | [NBWEB-691](https://bluinc.atlassian.net/browse/NBWEB-691) |

## Relaciones

- **Padre:** [[NBWEB-50]] Sitio Web
- **blocks:** [[NBWEB-674]] API - Feat -Agregar obtener comprobante de pago

## Descripcion

No se visualiza el comprobante, sin embargo, este si se encuentra en la base de datos.

```
https://gamma.api.nb.com.ar/v1/paymentVoucher/0002-10332635
```

[adjunto]
[adjunto]
Dato extra:

Quizás pueda deberse a la condición del `clientId`

[adjunto]
