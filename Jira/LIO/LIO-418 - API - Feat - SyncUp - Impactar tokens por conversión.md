---
jira_key: "LIO-418"
aliases: ["LIO-418"]
summary: "API - Feat - SyncUp - Impactar tokens por conversión"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-11 07:25"
updated: "2025-09-30 11:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-418"
---

# LIO-418: API - Feat - SyncUp - Impactar tokens por conversión

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-11 07:25 |
| Actualizado | 2025-09-30 11:20 |
| Etiquetas | ninguna |
| Jira | [LIO-418](https://bluinc.atlassian.net/browse/LIO-418) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos
- **relates to:** [[LIO-443 - API - Review - SyncUp - Impactar tokens por conversión - Tabla inexistente|LIO-443]] API - Review - SyncUp - Impactar tokens por conversión -> Tabla inexistente
- **has action item:** [[LIO-456 - API - Referrals - Agregar acreditación en billetera al procesar conversión de|LIO-456]] API - Referrals - Agregar acreditación en billetera al procesar conversión de referido
- **relates to:** [[LIO-464 - API - Review - SyncUp - Impactar tokens por conversión - Correos duplicados|LIO-464]] API - Review - SyncUp - Impactar tokens por conversión -> Correos duplicados

## Descripcion

**Parte 1: Conversión del referido**

La propuesta es un generar un recurso SyncUp que se ejecute cada x minutos y busque si los usuarios que tienen referidos sin extinguir ni expirar en la tabla `[LO].[dbo].user_referrals` y si alguno realizo una compra que aun no tiene procesado su referido.

Si el usuario tiene una compra finalizada (osea que la venta esta terminada con `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS].ID_STATUS > 2`) lo agregaremos a `LO.dbo.referral_conversions`y lo extinguiremos de la tabla `[LO].[dbo].user_referrals`

Tabla `LO.dbo.referral_conversions`

| Columna | Tipo | Descripción |
| --- | --- | --- |
| id | BIGINT (PK) | ID único del registro |
| usuarioID | BIGINT (FK referrals) | Referencia al referido |
| pedidoCabeceraId | BIGINT (FK orders) | Orden asociada a la conversión |
| fee | DECIMAL(10,2) | Comisión generada |
| created_at | TIMESTAMP | Fecha creación |
| updated_at | TIMESTAMP | Fecha actualización |

La comisión o `fee` la dejaremos en las variables de entorno como `REFERAL_FEE`


Si el usuario referido finalmente realiza una compra, el sistema verifica si existe un referido para el usuario que acaba de realizar una compra.

**Parte 2: Envío de correo al emisor del referido**

Asunto: 💰 Has generado un nuevo ingreso por tu referido!

```
¡Felicitaciones, {{nombre_usuario}}!

Uno de tus referidos ha realizado una compra en {{nombre_tienda}}.

Detalles de la conversión:
- Fecha: {{fecha_conversion}}
- Monto de la compra: {{monto_compra}}
- Tu comisión: {{monto_comision}}
- Productos: {{lista_productos}}

Sigue compartiendo tu enlace para acumular más comisiones:

Este es un mensaje automático. Si no deseas recibir más notificaciones de referidos, actualiza tus preferencias en tu perfil.

```
