# Changelog

## 2026-08-27

- **Inicio del proyecto**: scaffolding Nuxt 3 + Tailwind (PostCSS nativo), estética AORUS.
- **Proxy + agrupador** contra BluPartPicker: trae items Gigabyte de los 7 resellers, agrupa por `oracular_sku`, caché en memoria (TTL 30 min). API key oculta en el server.
- **API interna**: `/api/products` (filtros/orden/paginación), `/api/products/:id` (ficha), `/api/facets`.
- **UI**: home (hero + categorías + destacados), catálogo con filtros/orden/paginación, ficha con tabla de vendedores + link a su web.
- **Entorno**: instalado Node 20 portable (Nuxt 3.17 requiere ≥20.11); removido `@nuxtjs/tailwindcss` por error de `import.meta` en postcss.
- **Fix nombres**: `cleanName()` colapsa palabras/bigramas repetidos de las fuentes.
- **Imágenes**: panel claro + `mix-blend-multiply` para eliminar fondos blancos de las fotos de resellers.
- **Branding**: logo oficial GIGABYTE (SVG máscara) en header/footer + favicons; `CategoryIcon.vue` con iconos de línea por categoría.
- **Tema claro/oscuro**: tokens de color con CSS vars, `ThemeToggle`, estado en `useState`+cookie (SSR-aware). Fix: `useCookie` suelto no sincronizaba → `useState`.
- **Fix filtros**: parámetros `undefined` como string rompían el filtrado → query limpio en cliente + server defensivo.
- **Git**: publicado en `git@github.com:BluIncStudio/giga-partpicker.git` (rama `main`, sin firma de Claude).
- **Docs**: README, CLAUDE.md y carpeta `docs/` (arquitectura, api-partpicker, design-system, deploy).
- **Normalización de categorías**: `normalizeCategoria()` unifica PLACA/PLACA DE VIDEO/TARJETA → `PLACA DE VIDEO` y WATER/WATER COOLER → `WATER COOLER` (12 → 9 categorías).
- **Filtro outlet**: se excluyen las ofertas cuyo nombre contenga "outlet" antes de agrupar (336 → 330 productos).

Archivos principales: `server/utils/partpicker.ts`, `server/utils/config.ts`, `server/api/`, `components/`, `composables/useTheme.ts`, `assets/css/main.css`, `tailwind.config.ts`.

## Ver también

- [[gigabyte-aterrizaje/gigabyte-aterrizaje|gigabyte-aterrizaje]] · [[gigabyte-aterrizaje/contexto|contexto]]
