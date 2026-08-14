# Módulo Notificaciones (in-app + email + push FCM)

Centro de notificaciones disparado por los eventos de [[modulos/tareas]] (asignación, cambio de estado, comentario, mención, deadline). Tres canales: **in-app**, **email** y **push** (Firebase Cloud Messaging). Migs `0079` (notificaciones), `0080` (dispositivos_push).

## Backend

- Motor **`App\Services\TareaNotificador`** (~220 líneas): decide destinatarios (asignados, seguidores, mencionados) y despacha por los tres canales.
- Enum **`App\Enums\TipoNotificacion`**: `ASIGNACION`, `CAMBIO_ESTADO`, `COMENTARIO`, `DEADLINE_PROXIMO`, `DEADLINE_VENCIDO`, `MENCION`.
- Rutas in-app: `GET /notificaciones`, `GET /notificaciones/contador`, `PATCH /notificaciones/leer-todas`, `PATCH /notificaciones/{n}/leida`.
- Push: `POST|DELETE /dispositivos-push` (registrar/borrar token FCM del dispositivo). `App\Services\FcmSender` es **defensivo** — resuelve Firebase en runtime y hace no-op si falta el paquete, la credencial o no hay tokens.
- Config `config/notificaciones.php`: `deadline_dias_previos=3`, `estados_excluidos_deadline=['LISTO']`, `permitir_autonotificacion` (env `NOTIFICACIONES_PERMITIR_AUTONOTIFICACION`, default false — para testear el circuito con una sola cuenta).
- **Scheduler**: `routes/console.php` agenda el comando `tareas:notificar-deadlines` **diario 09:00 America/Argentina/Buenos_Aires**, corriendo en el container `gigaerp-scheduler` (`schedule:work`). Ver [[memoria]].

## Frontend

- `NotificacionesCampana.vue` (campana en el topbar) + composable `useCentroNotificaciones`.
- Push: `useFirebasePush` (pide permiso **solo por acción explícita** del usuario, nunca al cargar), plugin `firebase.client.ts`, service worker `public/firebase-messaging-sw.js`. Config web de Firebase con defaults en `nuxt.config.ts` (proyecto `giga-erp-9ca67`).

## ⚠️ Estado del push

Push **aún NO operativo**. Falta:
- Frontend: `NUXT_PUBLIC_FIREBASE_VAPID_KEY` (Firebase Console → Cloud Messaging → Web Push certificates).
- Backend: `storage/app/firebase/service-account.json` + `FIREBASE_PROJECT_ID`.

El resto del sistema (in-app + email) funciona sin eso; el paquete PHP nuevo es `kreait/laravel-firebase` (ver [[troubleshooting]] para cómo se instaló sin rebuild).

## Ver también

- [[modulos/tareas]] · [[modulos/solicitudes]] — fuentes de los eventos
- [[memoria]] · [[troubleshooting]] — deploy de la dep, scheduler
- [[changelog#2026-08-14 — Deploy release colaboración (Tareas 2.0, Solicitudes, Minutas, Notificaciones+Push, Campañas)|changelog]]
