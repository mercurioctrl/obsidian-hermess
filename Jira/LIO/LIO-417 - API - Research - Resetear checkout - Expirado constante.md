---
jira_key: "LIO-417"
aliases: ["LIO-417"]
summary: "API - Research - Resetear checkout -> Expirado constante"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-08-08 18:28"
updated: "2025-08-13 15:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-417"
---

# LIO-417: API - Research - Resetear checkout -> Expirado constante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-08-08 18:28 |
| Actualizado | 2025-08-13 15:27 |
| Etiquetas | ninguna |
| Jira | [LIO-417](https://bluinc.atlassian.net/browse/LIO-417) |

## Relaciones

- **relates to:** [[LIO-381 - API - Feat - Resetear checkout|LIO-381]] API - Feat - Resetear checkout

## Descripcion

Realizaremos una investigación para determinar por qué, en algunos casos, la respuesta del backend incluye constantemente el parámetro `expired = true`, incluso después de realizar la petición PATCH para efectuar el reinicio.

Para reproducir el error, es necesario iniciar el proceso de pago desde el carrito y, en la sección de selección de envío o retiro, permanecer el tiempo suficiente hasta que el checkout expire.

```
PATCH {API_URL}/pedidos/checkout/{idPedido}/reset
```

[adjunto]
