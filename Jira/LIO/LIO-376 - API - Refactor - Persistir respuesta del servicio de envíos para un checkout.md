---
jira_key: "LIO-376"
aliases: ["LIO-376"]
summary: "API - Refactor - Persistir respuesta del servicio de envíos para un checkout determinado dentro de la base de datos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-07-06 19:32"
updated: "2025-07-16 10:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-376"
---

# LIO-376: API - Refactor - Persistir respuesta del servicio de envíos para un checkout determinado dentro de la base de datos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-06 19:32 |
| Actualizado | 2025-07-16 10:38 |
| Etiquetas | ninguna |
| Jira | [LIO-376](https://bluinc.atlassian.net/browse/LIO-376) |

## Relaciones

- **Padre:** [[LIO-373]] Seguridad del checkout y protección de transacciones

## Descripcion

El refactor se debe realizar en V4.

```php
Route::post('envios/checkout/cotizacion', CheckoutQuote::class);
```
