# Modulo Flota GSM

Administración de **líneas SIM prepagas**: dar de alta números, registrar cargas y seguir el vencimiento de cada línea (una prepaga se pierde si no se recarga cada X meses). Avisa por **email** a una lista de contactos por línea. **PR #54, migración `0109` (2026-08-29).**

Sección `/flota-gsm`, permiso `VER_SECCION_FLOTA_GSM` (grupo Operaciones del sidebar).

## Tablas (migración 0109)

- **`gsm_lineas`** — `nombre`, `numero`, `observaciones`, `meses_vigencia` (cada cuántos meses recargar, default 6), `activo`. Última carga **denormalizada**: `ultima_carga_fecha` / `ultima_carga_monto` / `ultima_carga_moneda`. `vence_el`, `alerta_15d_enviada_at` (marca anti-duplicado), `usuario_id`.
- **`gsm_cargas`** — historial: `gsm_linea_id` (cascade), `fecha`, `monto`, `moneda`, `notas`, `usuario_id`.
- **`gsm_contactos`** — a quién avisar: `gsm_linea_id` (cascade), `nombre` (nullable), `email`.

Ver [[Base de Datos]].

## Vencimiento

`vence_el = ultima_carga_fecha + meses_vigencia` (`GsmLinea::recalcularVencimiento()`, `addMonthsNoOverflow`). `diasRestantes()` = `Carbon::today()->diffInDays(vence_el, false)` (negativo = vencida, null si nunca se cargó).

## Backend

- **`GsmLineaController`** (`/api/gsm/lineas`, JSON directo, **sin** wrapper `data`):
  - `index` / `show` (incluye `cargas[]`) / `store` / `update` / `destroy`. Los **contactos** se sincronizan con un array `contactos[]` en store/update (delete + recreate).
  - **`registrarCarga`** (`POST /gsm/lineas/{linea}/cargas`): crea la carga, actualiza la última carga denormalizada, recalcula `vence_el`, resetea `alerta_15d_enviada_at = null` (nuevo ciclo) y **avisa a los contactos** por email. El aviso va fuera de la transacción (un fallo SMTP no revierte la carga).
- **`GsmAlertaService`** — `avisarCarga()` / `avisarVencimiento()` → `Mail::mailer('erp')->raw(...)` con `from` de `config('mail.erp_from')` a cada contacto (try/catch por contacto).
- **`gsm:alertas-vencimiento`** (comando `EnviarAlertasGsm`) — agendado en `routes/console.php` **`dailyAt('09:00')`**. Avisa cuando faltan ≤15 días (líneas activas, `vence_el` entre hoy y hoy+15, `alerta_15d_enviada_at` null), **una sola vez por ciclo** (se rearma al cargar). ⚠️ Corre en el contenedor **`minisaas-scheduler`** (`schedule:work`), no en `minisaas-backend`.

## Frontend

`pages/flota-gsm/index.vue` — tabla con **badge de vencimiento por color** (rojo ≤15 días / vencida, ámbar ≤30, verde), tarjetas de stats (activas / por vencer / vencidas), y modales: alta/edición (con contactos dinámicos), registrar carga e historial. NavItem `lucide:phone` en grupo Operaciones. Ver [[Frontend]].

## Decisiones

- Es un módulo de **seguimiento**: la carga **no** genera gasto ni movimiento de banco/caja (a diferencia de los pagos de sueldo del [[Modulo Personal]]). Si se quisiera imputar a finanzas, se agrega aparte.
- El aviso de "15 días antes" y el de "carga registrada" van **sólo por email** a la lista de contactos de la línea (pueden ser externos / no usuarios); no usa push ni notificación in-app.

## Deploy

`docker cp` a **`minisaas-backend` y `minisaas-scheduler`** + `php artisan migrate` + `optimize:clear` + `docker restart minisaas-scheduler` (para que el scheduler tome el comando). Frontend: rebuild. Ver [[Stack e Infraestructura]].

## Ver también

- [[Modulo Reservas Reuniones]] — mismo patrón de comando agendado + mailer `erp@` (recordatorios)
- [[Modulo Permisos]] — `VER_SECCION_FLOTA_GSM`
- [[Backend - API]] · [[Base de Datos]] · [[Reglas de Negocio]]
