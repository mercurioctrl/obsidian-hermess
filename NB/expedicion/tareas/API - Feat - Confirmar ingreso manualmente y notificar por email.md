# API - Feat - Confirmar ingreso manualmente y notificar por email

**Proyecto:** [[NB/expedicion/expedicion|Expedición]]
**Estado:** Pendiente
**Fecha:** 2026-04-07

Agregar un mecanismo para que los operarios del depósito puedan confirmar explícitamente que un ingreso (provider order) fue recibido completamente, independientemente de si todos los serials están cargados. Esto resuelve el problema de que a veces la mercadería llega incompleta y la marca automática de `serialized` nunca se activa, dejando ingresos en un limbo.

El flujo es:
1. El operario abre el detalle del ingreso y presiona un botón "Confirmar ingreso"
2. Se marca el ingreso con un flag separado (`confirmed_by_operator` o similar) distinto del campo `serialized` existente
3. Se envía un email de notificación a una dirección configurada por `companyCode`

---

### Endpoint

`PATCH /v1/providersOrders/{providerOrderId}/confirmEntry`

### Tabla de definición del recurso

| Campo | Detalle |
|---|---|
| **Método** | PATCH |
| **Autenticación** | Requerida (JWT, permiso `exp_ingreso`) |
| **Path param** | `providerOrderId` (int) — ID del ingreso a confirmar |
| **Query params** | Ninguno |
| **Request body** | Ninguno (la acción es implícita) |

### Ejemplo de llamada

`PATCH /v1/providersOrders/10207/confirmEntry`

---

## Respuesta esperada

### Status y Content-Type

`200 OK Content-Type: application/json`

### Estructura de respuesta

Objeto con el resultado de la confirmación y el envío de email.

### Ejemplo de respuesta (copiar/pegar)

```json
{
  "success": true,
  "data": {
    "confirmed": true,
    "emailSent": true,
    "confirmedAt": "2026-04-07 14:30:00",
    "confirmedBy": "jperez"
  }
}
```

### Casos especiales

- **Ingreso ya confirmado:** Retornar éxito pero indicar que ya estaba confirmado, sin reenviar email
- **Email no configurado para el companyCode:** Confirmar el ingreso pero indicar `emailSent: false`
- **Ingreso no encontrado:** `404 Not Found`

---

## Modelo de datos

### Nueva tabla: `ST_INGRESO_EMAILS_NOTIFICACION`

Tabla para almacenar las direcciones de email de notificación por empresa.

| Campo | Tipo | Descripción |
|---|---|---|
| `ID` | int (PK, identity) | ID autoincremental |
| `COMPANY_CODE` | varchar(10) | Código de empresa |
| `EMAIL` | varchar(255) | Dirección de email destino |
| `ACTIVO` | bit | Si la configuración está activa |

### Modificación tabla existente: `PedProT` (header del pedido proveedor)

Agregar campos para la confirmación manual:

| Campo | Tipo | Descripción |
|---|---|---|
| `confirmed_by_operator` | bit (default 0) | Flag de confirmación manual del operario |
| `confirmed_at` | datetime (nullable) | Fecha/hora de confirmación |
| `confirmed_by` | varchar(100) (nullable) | Usuario que confirmó |

---

## Queries SQL

El endpoint ejecuta **3 queries secuenciales**.

### Query 1 — Verificar que el ingreso existe y obtener datos

```sql
SELECT p.NroPed, p.serialized, p.confirmed_by_operator, p.companyCode
FROM [NewBytes_DBF].[dbo].[PedProT] p
WHERE p.NroPed = :providerOrderId
```

### Query 2 — Marcar como confirmado

```sql
UPDATE [NewBytes_DBF].[dbo].[PedProT]
SET confirmed_by_operator = 1,
    confirmed_at = GETDATE(),
    confirmed_by = :username
WHERE NroPed = :providerOrderId
```

### Query 3 — Obtener email de notificación

```sql
SELECT EMAIL
FROM ST_INGRESO_EMAILS_NOTIFICACION
WHERE COMPANY_CODE = :companyCode
  AND ACTIVO = 1
```

---

## Archivos a modificar/crear

### Backend (API)

| Archivo | Acción |
|---|---|
| `app/src/App/Routes/ProvidersRoute.php` | Agregar ruta PATCH `confirmEntry` |
| `app/src/Controller/Providers/ProvidersOrderConfirm.php` | **Crear** — Controller para confirmar ingreso |
| `app/src/Service/Providers/ProvidersService.php` | Agregar método `confirmEntry()` |
| `app/src/Repository/Providers/ProvidersRepository.php` | Agregar queries de confirmación y lookup de email |
| `app/src/Support/Email/IngresoConfirmEmail.php` | **Crear** — Clase de email para notificación de confirmación |
| `app/database/migrations/` | **Crear** — Migración para nueva tabla y campos en PedProT |

### Frontend (APP) — tarea separada

| Archivo | Acción |
|---|---|
| Componente de detalle de ingreso | Agregar botón "Confirmar ingreso" |
| `plugins/api.js` | Agregar método `confirmEntry()` en providers |
| Store de providers | Agregar action para confirmar |

---

## Notas técnicas

- El campo `confirmed_by_operator` es **independiente** de `serialized`. Un ingreso puede estar `serialized = 0` (serials incompletos) pero `confirmed_by_operator = 1` (el operario dice que terminó). Esto cubre el caso de mercadería que llega incompleta.
- El email se envía usando PHPMailer (ya existe en `Support/Email/CreditoEmail.php` como referencia).
- La tabla `ST_INGRESO_EMAILS_NOTIFICACION` permite configurar múltiples emails por empresa si en el futuro se necesita. Por ahora con uno alcanza.
- El endpoint existente `fullSerializerCheck` no se modifica — sigue funcionando como está para la marca automática.
- Considerar agregar un filtro en el listado de ingresos para distinguir "confirmados por operario" vs "no confirmados".

## Ver también

- [[NB/expedicion/expedicion|Expedición]]
- [[NB/expedicion/arquitectura|Arquitectura]]
- [[NB/expedicion/documentacion|Documentación]]
