# Memoria

Consolidación de la memoria auto-guardada del proyecto (`~/.claude/projects/-var-www-naevo/memory/`). Son patterns, gotchas y decisiones que NO son obvias leyendo el código — cosas que aprendimos del camino.

## Feedback — workflow

Reglas de trabajo aprendidas durante sesiones previas.

- **Nunca adjudicar autoría** — sin Co-Authored-By, sin AI attribution en commits.
- **Rebuild frontend obligatorio** — después de cualquier cambio en Nuxt: `docker compose build --no-cache frontend && docker compose up -d frontend`. SSR requiere rebuild.
- **Backend también necesita rebuild** — tras cambios en Laravel, mismo patrón con `--no-cache backend`.
- **Verificar API antes de crear componentes** — siempre hacer `curl` al endpoint antes de inventar campos en un componente Vue. Los field names deben coincidir con la serialización Eloquent exacta, no asumir.
- **Laravel .env pisa docker-compose env** — `backend/.env` tiene precedencia sobre variables de `docker-compose.yml`. Si algo no funciona, revisar `backend/.env`.
- **Redis port interno vs host** — dentro de containers usar `REDIS_PORT=6379` (interno). El host-mapping (`6382` o `6383`) es solo para conexiones desde el host Mac, no entre containers. El error se manifiesta como `Connection refused` en el log de Laravel durante login/session — pero desde `tinker` Redis responde OK porque usa la conexión directa.
- **Curl API primero en bugs de display** — antes de investigar componentes, storage o nginx, hacer `curl` al endpoint y confirmar qué devuelve. 80% de los bugs de "no muestra" son field mismatches.
- **Revisar auth middleware antes de asumir** — las rutas de carrito NO tienen `auth:sanctum`. Resuelven el user manualmente via `PersonalAccessToken`. No asumir que `$request->user()` funciona sin verificar la ruta.
- **Match route params con controller signature** — el número y orden de `{params}` en la ruta debe coincidir con los argumentos del método del controller.
- **Nuxt component auto-import prefix** — por default `ui/X.vue` registra como `UiX`. Este proyecto usa `pathPrefix: false` para `ui/`, así que registra como `X` directo.
- **Verificar Tailwind classes** — no usar clases no-standard como `w-4.5`. Antes de usar una clase, confirmar que existe.
- **Si un componente no aparece, verificar resolución** — buscar `resolveComponent()` en el build para confirmar que Nuxt lo está resolviendo.
- **Componentes de layout en raíz** — los componentes que se usan en layouts deben vivir en `components/` (raíz), no en subcarpetas. El auto-import por subcarpetas agrega prefijos que rompen los layouts.
- **No hardcodear contenido del CMS** — si algo debería ser editable, actualizar DB + seeder, no inlineear en Vue. Para textos simples usar la tabla `settings` (patrón ya establecido).
- **Primary action field va primero en forms** — el campo principal (search/autocomplete) arriba, los secundarios abajo. Mejora la UX del form.
- **Pivot tables devuelven la join row, no el modelo real** — al iterar `related_products`, el modelo real está anidado (ej. `rp.related_product`). No acceder a campos del producto directamente en el pivot.
- **CMS banner tiene dos campos de imagen** — `image_url` (modo text+image) vs `slider_image_url` (modo slider). Al debuggear, primero chequear qué modo está activo.

## Project — arquitectura y estructura

- **Container names, ports, paths, nginx** — backend=8000, frontend=3000, nginx=80 (host `APP_PORT=8088`), db=3306 (host `DB_PORT=3309`), redis=6379 (host `REDIS_PORT=6382`).
- **Volúmenes nombrados, no bind mounts** — usar `docker compose cp` para copiar archivos. El storage del backend es un volumen persistente.
- **Home usa `layout: false`** — maneja su propia estructura (AnnouncementBar + TheHeader + ... + TheFooter + CartDrawer). Otras páginas usan `default.vue` layout.
- **Branding** — NÆVO (con Æ), color primario `#0f2bde`, tipografía display Umbra (CDNFonts).
- **Product images** — 45 PNGs con fondo blanco, en volumen Docker, las cards del frontend usan `bg-white` para matchear.
- **Workflow de imágenes estáticas** — subir a `images/` en raíz del repo → copiar a `frontend/public/images/` → actualizar DB + seeder si van en CMS.
- **Search system** — SearchModal con live suggestions desde el header + página `/buscar`. Endpoint `/api/products/search`.
- **`/home/edit` visual editor** — página WYSIWYG para editar la home sin tocar código. Protegida con middleware `admin`. Reutiliza los mismos componentes Vue del home con overlays de edición superpuestos.

## Project — patrón settings CMS-lite

Para textos hardcodeados en componentes Vue que necesitan ser editables:
1. Agregar la clave al array `PUBLIC_KEYS` en `PublicSettingController`
2. Agregar prop opcional con default vacío al componente (`withDefaults(defineProps<{...}>(), {...})`)
3. En el componente, usar `prop || 'texto default hardcodeado'`
4. En `index.vue`, pasar `:section-title="settings.home_X_title"`
5. En `/home/edit`, guardar via `PUT /admin/settings` con array de `{key, value}`

Claves activas: `logo_height_mobile`, `logo_height_desktop`, `home_products_title`, `home_products_subtitle`, `home_categories_title`, `home_categories_subtitle`.

## Project — API y data

- **Guest cart session** — el header `X-Session-Id` se envía SIEMPRE, junto con `Bearer token` cuando hay auth. Backend resuelve user manualmente en rutas de cart.
- **Response patterns de Laravel** — paginator NO hace double-wrap (ya viene `data/meta/links`). Image relations son objetos (usar `.image_url`, no string directo).
- **CMS home field mapping** — `/api/cms/home` devuelve un objeto con campos específicos que deben matchear cada componente Vue (hay un doc separado con el mapping completo).
- **SSR field mismatches** — historia de 14 field mismatches del CMS home + 7 de products + 2 de FeaturedProducts que se fueron corrigiendo. Lección: curl primero.

## Project — checkout y pagos

- **Checkout single-step** — createOrder (pending) → MercadoPago Brick inline → processPayment → webhook backup. NO hay flujo multi-paso.
- **Guest checkout** — `user_id` nullable en `orders`, ownership por `session_id`, confirmación por `guest_token`, auto-vinculación al registrarse.
- **Shipping carriers** — OCA, Andreani, Entregar. Logos en DB (`logo_url`), costos simulados (no API real).
- **Google Places Autocomplete** — composable `useGooglePlaces.ts`, restringido a Argentina, requiere `GOOGLE_MAPS_API_KEY` env.

## Project — homepage (mayo 2026)

- **Orden del home**: AnnouncementBar → Header → Hero → FeaturedProducts → ShopByCategory → BestQuality → Newsletter → Rewards → OurStandards → Footer. SubscriptionSection comentada temporalmente.
- **QualityBadges dos props** — `badges` + `certifications`, fusiona lo que antes eran dos componentes.
- **WellnessGoals 6-col sin gap** — `gap: 0`, sin `border-top` en los anillos de color. Hover crossfade lifestyle↔producto.
- **Hero trust band** — 5 badges con íconos SVG circulares (GMP, ISO 9001, No GMO, Gluten Free, Vegano). Hardcodeados en `HeroBanner.vue` — no son los mismos que `cms_trust_badges`.

## Ver también

- [[naevo|Índice del proyecto]]
- [[contexto|Contexto y decisiones]]
- [[arquitectura|Arquitectura técnica]]
- [[changelog|Changelog]]
