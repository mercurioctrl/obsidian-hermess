---
jira_key: "LIO-361"
aliases: ["LIO-361"]
summary: "APP - Refactor - Conectar nuevo recurso de cacnelacion en las compras/ventas"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-05-22 09:25"
updated: "2025-05-29 18:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-361"
---

# LIO-361: APP - Refactor - Conectar nuevo recurso de cacnelacion en las compras/ventas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-22 09:25 |
| Actualizado | 2025-05-29 18:18 |
| Etiquetas | ninguna |
| Jira | [LIO-361](https://bluinc.atlassian.net/browse/LIO-361) |

## Relaciones

- **Padre:** [[LIO-359]] Cancelaciones
- **action item from:** [[LIO-360]] API - Feat - Cancelación de orden por comprador o vendedor autenticado

## Descripcion

Refactorizaremos todos los puntos del sistema donde actualmente se permite cancelar una compra o venta, para que utilicen el nuevo recurso de cancelación unificado desarrollado en [[[LIO-360]]](https://bluinc.atlassian.net/browse/LIO-360).

**Implementación:**

- Al presionar la opción de "Cancelar compra/venta", se deberá solicitar al usuario el **motivo de la cancelación**.


- Las opciones de motivo se obtendrán desde el repositorio ya existente:

```
GET /v4/ticket/issues/1
```


- Una vez seleccionado el motivo, se deberá invocar el nuevo endpoint:

```
PATCH {API_URL}/v4/purchase/{ID}/cancel
```

con el campo `motivoCancelacion` en el payload.



**Requisitos funcionales:**

- Si la cancelación es exitosa, la interfaz debe reflejar claramente que la compra o venta fue **cancelada**.


- Si ocurre un error o la operación no puede realizarse, el mensaje de error devuelto por la API debe mostrarse al usuario de forma **clara y comprensible**.



**Criterios de aceptación:**

- Todos los flujos de cancelación existentes deben migrarse al nuevo endpoint.


- El usuario debe seleccionar un motivo válido desde las opciones provistas.


- La operación debe ser transparente y clara tanto en éxito como en error.
