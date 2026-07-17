# memoria

Memoria operativa del proyecto (gotchas y datos para retomar). Ver [[arquitectura]] · [[contexto]].

## Acceso demo

- Panel: http://localhost:8840 — `admin@blu.test` / `password`
- Seeder demo idempotente (`DatabaseSeeder`): tenant "BLU Demo", dominio verificado, 1 plantilla, 3 contactos.

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

## Convenciones

- Enums string en DB + cast PHP enum (patrón BLU).
- CRUD = controller resourceful + FormRequest + JsonResource + respuesta `{success,message,data}`. Invokable solo para acciones (send, webhook, import).
