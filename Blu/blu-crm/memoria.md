# memoria

Memoria operativa del proyecto (gotchas y datos para retomar). Ver [[arquitectura]] · [[contexto]] · [[stack]].

## Acceso demo

- Panel: http://localhost:8840 — `admin@blu.test` / `password`
- Seeder demo idempotente (`DatabaseSeeder`): tenant "BLU Demo" (slug `blu-demo`), dominio, 1 plantilla, 3 contactos.

## Puertos (host muy poblado — elegidos para no chocar con otros proyectos)

- 8840 -> panel + API (8830 lo tiene blufixture-nginx)
- 8831 -> micro WhatsApp (QR en dev)
- 3312 -> MySQL (3310 gigaerp-db, 3311 ocupado)

## Gotchas de build (no repetir)

- Backend corre PHP 8.3, pero `composer require --ignore-platform-reqs` resolvía Symfony 8 (pide 8.4). Fix: `composer config platform.php 8.3.32` + regenerar lock con `--ignore-platform-req=ext-pcntl --ignore-platform-req=ext-posix`.
- `composer install` NO acepta `--no-audit` (solo `require`).
- Mirror bloquea por advisories: `composer config policy.advisories.block false`.
- `nuxi init` crashea en el host (Node 18, necesita 20+). El Nuxt se armó a mano; buildea en el contenedor node:20.
- Frontend: `npm install --legacy-peer-deps` (conflicto @nuxt/icon + @pinia/nuxt).
- Columna JSON de contacto: `custom_attributes`, NO `attributes` (choca con Eloquent).
- Rutas sanctum sin header `Accept: application/json` dan 500 (redirect a login inexistente) en vez de 401.
- `campaigns.sending_domain_id` es RESTRICT -> borrar un tenant necesita limpieza en orden o FK checks off.

## Gotchas de operación / dev (nuevos, 2026-08)

- **El código está *baked* en la imagen** (sin bind-mount del source). Editar en el host NO se refleja en el contenedor corriendo. Para aplicar: **rebuild** (`docker compose build backend frontend && up -d && restart nginx`) o `docker compose cp` (efímero).
- **La imagen es de producción (sin dev-deps):** phpunit/pint no vienen. Para tests: `docker compose exec backend composer install` (efímero) y luego `php vendor/bin/phpunit`. Repetir tras cada rebuild.
- **`MAIL_MAILER=ses` inyectado por Docker gana sobre el `<env>` de phpunit.** En tests que envían mail, forzar `config(['mail.default' => 'array'])`.
- **502 de nginx tras un rebuild:** los `upstream` cacheaban la IP. Ya arreglado con resolver Docker (`127.0.0.11`) + `proxy_pass` por variable. Si aparece transitorio: `docker compose restart nginx`.
- **SES real vs fake:** `SES_FAKE=false` usa AWS; `true` = gestores fake (dev/tests sin creds). Requiere `AWS_*` + `SES_SNS_TOPIC_ARN` en el `.env`.
- **Bug de audiencia por segmento (resuelto):** el `belongsToMany` hacía `select *` y la columna `id` del pivote `contact_segment` pisaba `contacts.id` -> se insertaba el id del pivote como `contact_id`. Fix: `->select('contacts.*')` en `SendCampaignService::audience()`.
- **URLs firmadas de baja usan `APP_URL`:** al deployar/replicar, setear `APP_URL` al público del cliente o los links de List-Unsubscribe salen mal.

## Convenciones

- Enums string en DB + cast PHP enum (patrón BLU).
- CRUD = controller resourceful + FormRequest + JsonResource + respuesta `{success,message,data}`. Invokable solo para acciones (send, verify, webhook, import, unsubscribe).
- Lógica de negocio en `app/Services/<Feature>/`. Servicios externos detrás de interfaz mockeable.
- `config()` en runtime (no `env()`, que falla con config cacheada). Pint: `new Clase` sin paréntesis si no hay args.
- Git: sin coautoría de IA en commits. `.claude/CLAUDE.md` no se versiona (uso interno).
