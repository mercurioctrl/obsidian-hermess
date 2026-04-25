# Memoria

Consolidación de la memoria auto-guardada del proyecto (`~/.claude/projects/-Users-hermess-www-naevo-web/memory/`). Son patterns, gotchas y decisiones que NO son obvias leyendo el código — cosas que aprendimos del camino.

## Feedback — workflow

Reglas de trabajo aprendidas durante sesiones previas.

- **Nunca adjudicar autoría** — sin Co-Authored-By, sin AI attribution en commits.
- **Rebuild frontend obligatorio** — después de cualquier cambio en Nuxt: `docker compose build --no-cache frontend && docker compose up -d frontend`. SSR requiere rebuild.
- **Backend también necesita rebuild** — tras cambios en Laravel, mismo patrón con `--no-cache backend`.
- **Verificar API antes de crear componentes** — siempre hacer `curl` al endpoint antes de inventar campos en un componente Vue. Los field names deben coincidir con la serialización Eloquent exacta, no asumir.
- **Laravel .env pisa docker-compose env** — `backend/.env` tiene precedencia sobre variables de `docker-compose.yml`. Si algo no funciona, revisar `backend/.env`.
- **Redis port interno vs host** — dentro de containers usar `REDIS_PORT=6379` (interno). El host-mapping (`REDIS_PORT=6383`) es solo para conexiones desde la Mac, no entre containers.
- **Curl API primero en bugs de display** — antes de investigar componentes, storage o nginx, hacer `curl` al endpoint y confirmar qué devuelve. 80% de los bugs de "no muestra" son field mismatches.
- **Revisar auth middleware antes de asumir** — las rutas de carrito NO tienen `auth:sanctum`. Resuelven el user manualmente via `PersonalAccessToken`. No asumir que `$request->user()` funciona sin verificar la ruta.
- **Match route params con controller signature** — el número y orden de `{params}` en la ruta debe coincidir con los argumentos del método del controller.
- **Nuxt component auto-import prefix** — por default `ui/X.vue` registra como `UiX`. Este proyecto usa `pathPrefix: false` para `ui/`, así que registra como `X` directo.
- **Verificar Tailwind classes** — no usar clases no-standard como `w-4.5`. Antes de usar una clase, confirmar que existe.
- **Si un componente no aparece, verificar resolución** — buscar `resolveComponent()` en el build para confirmar que Nuxt lo está resolviendo.
- **Componentes de layout en raíz** — los componentes que se usan en layouts deben vivir en `components/` (raíz), no en subcarpetas. El auto-import por subcarpetas agrega prefijos que rompen los layouts.
- **No hardcodear contenido del CMS** — si algo debería ser editable, actualizar DB + seeder, no inlineear en Vue.
- **Primary action field va primero en forms** — el campo principal (search/autocomplete) arriba, los secundarios abajo. Mejora la UX del form.
- **Pivot tables devuelven la join row, no el modelo real** — al iterar `related_products`, el modelo real está anidado (ej. `rp.related_product`). No acceder a campos del producto directamente en el pivot.
- **CMS banner tiene dos campos de imagen** — `image_url` (modo text+image) vs `slider_image_url` (modo slider). Al debuggear, primero chequear qué modo está activo.

## Project — arquitectura y estructura

- **Container names, ports, paths, nginx** — backend=8000, frontend=3000, nginx=80 (host `APP_PORT=8088`), db=3306 (host `DB_PORT=3309`), redis=6379 (host `REDIS_PORT=6383`).
- **Volúmenes nombrados, no bind mounts** — usar `docker compose cp` para copiar archivos. El storage del backend es un volumen persistente.
- **Home usa `layout: false`** — maneja su propia estructura (AnnouncementBar + TheHeader + ... + TheFooter + CartDrawer). Otras páginas usan `default.vue` layout.
- **Branding** — color primario `#0f2bde`, logo en `frontend/public/logo.png`.
- **Product images** — 45 PNGs con fondo blanco, en volumen Docker, las cards del frontend usan `bg-white` para matchear.
- **Workflow de imágenes estáticas** — subir a `images/` en raíz del repo → copiar a `frontend/public/images/` → actualizar DB + seeder si van en CMS.
- **Search system** — SearchModal con live suggestions desde el header + página `/buscar`. Endpoint `/api/products/search`.

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

## Project — customizations UI

- **Featured products slider** — slider horizontal, 8 productos (featured + random fill), sin librería de carousel.
- **Product detail shipping & payments** — sección de shipping (API) + logos de medios de pago (SVGs inline) abajo de los badges.

## Project — homepage (abril 2026)

- **Nuevo orden del home** — ver [[arquitectura#orden-actual-del-home-abril-2026]].
- **QualityBadges dos props** — `badges` + `certifications`, fusiona lo que antes eran dos componentes.
- **WellnessGoals 6-col con hover crossfade** — ver [[project_wellness_goals_hover|memoria técnica]] y [[contexto|contexto de la decisión]].
- **Nav 5 links** — Inicio, Productos, Ciencia, Blog, Profesionales. Hardcoded en `TheHeader.vue`, no viene del CMS. Al agregar un link nuevo, verificar que la página exista Y agregar el slug a `reservedSlugs` en `pages/[slug].vue`.
- **Páginas `/ciencia` y `/profesionales`** — ambas usan layout default. `/profesionales` tiene form con TODO de endpoint inexistente.

## Project — bug fixes históricos

- **Quiz** — 6 bugs fixeados, expandido de 3→6 preguntas. Field name mismatches principalmente.
- **Blog listing** — response double-wrapped, endpoint de categorías públicas faltante, field de imagen equivocado.

## Reference — scripts y external

- **restore.sh** — interactivo, pide número de backup + password del `.env` + "si". Ejecutar con prefijo `!` en Claude (no funciona con pipe/heredoc).
- **backup.sh** — genera `backups/backup_YYYYMMDD_HHMMSS.tar.gz` con DB + uploads.
- **sync-from-prod.sh** — script custom del usuario (no tracked en git) para pull desde prod.


## Project — templates & preview switcher (abril 2026)

- **10 templates Nuxt live** bajo `pages/templates/<slug>.vue` — una página por DS con CSS scoped, consumen CMS via `useTemplateData()`. Ver [[templates-preview]] y [[project_templates_gallery]].
- **tpl-* live routing** — `load()` del switcher `/preview/` rutea `tpl-*` a `/templates/<slug>` y el resto a mirrors estáticos. Ver [[project_preview_tpl_routing]].
- **Blu-NN naming** — variantes se presentan al cliente como `blu-NN Fantasía`, label-only, nunca tocar values/slugs. Próxima: blu-29. Ver [[feedback_blu_naming_convention]].
- **Panel Ajustes size-only** — color pickers hidden (no borrados), `applyToIframe` sólo inyecta font/logo. Colores respetan original del template. Ver [[feedback_preview_size_only_tools]].
- **Docker disk cleanup** — build fallaba con 'no space left on device'. Orden: `docker builder prune -af` → `image prune -f` → `system prune -af`. **NUNCA** `--volumes` (mata MySQL). Ver [[feedback_docker_disk_cleanup]].
- **Logo con filtro mono** — templates con header/footer oscuros usan `filter: brightness(0) invert(1)` (carbon, shadcn footer), los de aesthetic minimal usan `brightness(0)` (apple-hig, shadcn header), el resto full-color.

## Ver también

- [[naevo|Índice]]
- [[arquitectura|Arquitectura]]
- [[contexto|Reglas de negocio y TODOs]]
- [[changelog|Changelog]]
