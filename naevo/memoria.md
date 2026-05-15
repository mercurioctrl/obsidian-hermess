# Memoria

Consolidación de la memoria auto-guardada del proyecto (`~/.claude/projects/-var-www-naevo/memory/`). Son patterns, gotchas y decisiones que NO son obvias leyendo el código — cosas que aprendimos del camino.

## Feedback — workflow

Reglas de trabajo aprendidas durante sesiones previas.

- **Nunca adjudicar autoría** — sin Co-Authored-By, sin AI attribution en commits.
- **Rebuild frontend obligatorio** — después de cualquier cambio en Nuxt: `docker compose build --no-cache frontend && docker compose up -d frontend`. SSR requiere rebuild.
- **Backend también necesita rebuild** — tras cambios en Laravel, mismo patrón con `--no-cache backend`.
- **Verificar API antes de crear componentes** — siempre hacer `curl` al endpoint antes de inventar campos en un componente Vue. Los field names deben coincidir con la serialización Eloquent exacta, no asumir.
- **Laravel .env pisa docker-compose env** — `backend/.env` tiene precedencia sobre variables de `docker-compose.yml`. Si algo no funciona, revisar `backend/.env`.
- **Redis port interno vs host** — dentro de containers usar `REDIS_PORT=6379` (interno). El host-mapping (`6382`) es solo para conexiones desde el host Mac, no entre containers. El error se manifiesta como `Connection refused` en el log de Laravel durante login/session.
- **Curl API primero en bugs de display** — antes de investigar componentes, storage o nginx, hacer `curl` al endpoint y confirmar qué devuelve. 80% de los bugs de "no muestra" son field mismatches.
- **Revisar auth middleware antes de asumir** — las rutas de carrito NO tienen `auth:sanctum`. Resuelven el user manualmente via `PersonalAccessToken`.
- **Match route params con controller signature** — el número y orden de `{params}` en la ruta debe coincidir con los argumentos del método del controller.
- **Nuxt component auto-import prefix** — este proyecto usa `pathPrefix: false` para `ui/`, así que registra como `X` directo (no `UiX`).
- **No hardcodear contenido del CMS** — si algo debería ser editable, actualizar DB + seeder, no inlineear en Vue.
- **Controles del editor SIEMPRE visibles** — en `/home/edit`, los botones y controles de acción deben tener `opacity: 1` por defecto, NUNCA `opacity: 0` solo visible en hover. El usuario no puede saber que hay controles si no los ve.
- **"Volvelo como estaba" = versión anterior en la sesión** — NO el estado pre-sesión ni el último commit. Ante un revert, aclarar explícitamente a qué versión: "¿La versión con X o con Y?".
- **Pivot tables devuelven la join row, no el modelo real** — al iterar `related_products`, el modelo real está anidado (ej. `rp.related_product`).
- **CMS banner tiene dos campos de imagen** — `image_url` (modo text+image) vs `slider_image_url` (modo slider).
- **`apiResource` y rutas custom** — declarar la ruta custom (`POST upload-image`) **antes** del `apiResource` para que no se interprete como `{id}`.
- **macOS TCC bloquea Documents** — si el user pasa un path bajo `~/Documents/`, `~/Desktop/`, `~/Downloads/`, pedirle que mueva el archivo a `/tmp/` con `! mv ...`.
- **Python PIL en el host** para procesar imágenes — no hay ImageMagick instalado. `python3 -c "from PIL import Image"` funciona out of the box.

## Project — arquitectura y estructura

- **Container names, ports, paths, nginx** — backend=8000, frontend=3000, nginx=80 (host `APP_PORT=8088`), db=3306 (host `DB_PORT=3309`), redis=6379 (host port `6382`).
- **Volúmenes nombrados, no bind mounts** — usar `docker compose cp` para copiar archivos al container.
- **Home usa `layout: false`** — maneja su propia estructura completa. Otras páginas usan `default.vue`.
- **Branding** — NÆVO (con Æ, nunca NAEVO), color primario `#0f2bde`, tipografía display Umbra (CDNFonts), body Inter.
- **Product images** — 45 PNGs con fondo blanco, en volumen Docker, las cards usan `bg-white` para matchear.
- **`/home/edit` visual editor** — página WYSIWYG para editar la home sin tocar código. Middleware `admin`. Reutiliza los mismos componentes Vue del home con overlays de edición superpuestos + panel lateral deslizante (400px).

## Project — patrón settings CMS-lite

Para textos hardcodeados en componentes Vue que necesitan ser editables:
1. Agregar la clave al array `PUBLIC_KEYS` en `PublicSettingController`
2. Agregar prop opcional con default vacío al componente (`withDefaults(defineProps<{...}>(), {...})`)
3. En el componente, usar `prop || "texto default hardcodeado"`
4. En `index.vue`, pasar `:section-title="settings.home_X_title"`
5. En `/home/edit`, guardar via `PUT /admin/settings` con array de `{key, value}`

**Claves activas:** `logo_height_mobile/desktop`, `home_products_title/subtitle`, `home_categories_title/subtitle`, `home_quality_title/subtitle/pledge`, `home_newsletter_title/description/success`, `home_rewards_title/intro/cta`, `home_rewards_1/2/3_title/text`, `home_section_order`.

## Project — reordenamiento de secciones

El orden de las secciones reordenables del home (products, categories, quality, newsletter, rewards) se persiste en `settings.home_section_order` como string CSV: `"products,categories,quality,newsletter,rewards"`.

- **Editor:** flechas ↑↓ siempre visibles (no en hover), `@click.stop` para no abrir panel. Swap en array local + `PUT /admin/settings` inmediato.
- **Frontend:** `index.vue` lee `home_section_order` en SSR, renderiza con `<template v-for="section in sectionOrder"><ComponentX v-if="section===x" .../></template>`.
- **Secciones fijas** (no reordenables): AnnouncementBar, Hero, Footer.

## Project — homepage (mayo 2026)

- **Orden por defecto:** products → categories → quality → newsletter → rewards (+ fijas: announcement, hero, footer).
- **QualityBadges dos props** — `badges` + `certifications`, fusiona lo que antes eran dos componentes.
- **WellnessGoals 6-col sin gap** — `gap: 0`, sin `border-top` en los anillos de color. Hover crossfade lifestyle↔producto.
- **Hero trust band** — 5 badges con íconos SVG circulares (GMP, ISO 9001, No GMO, Gluten Free, Vegano). Hardcodeados en `HeroBanner.vue` — distintos a los `cms_trust_badges`.
- **SubscriptionSection y OurStandardsSection** — comentadas en `index.vue` y `edit.vue`, se pueden re-activar cuando estén listas.

## Project — API y data

- **Guest cart session** — el header `X-Session-Id` se envía SIEMPRE, junto con `Bearer token` cuando hay auth.
- **Response patterns de Laravel** — paginator NO hace double-wrap. Image relations son objetos (usar `.image_url`).
- **SSR field mismatches** — historia de múltiples field mismatches corregidos. Lección: curl primero.

## Project — checkout y pagos

- **Checkout single-step** — createOrder (pending) → MercadoPago Brick inline → processPayment → webhook backup.
- **Guest checkout** — `user_id` nullable en `orders`, ownership por `session_id`, confirmación por `guest_token`, auto-vinculación al registrarse.
- **Shipping carriers** — OCA, Andreani, Entregar. Costos simulados (no API real).

## Ver también

- [[naevo|Índice del proyecto]]
- [[contexto|Contexto y decisiones]]
- [[arquitectura|Arquitectura técnica]]
- [[changelog|Changelog]]
