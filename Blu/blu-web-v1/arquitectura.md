# Arquitectura — blu-web-v1

> Ver también: [[base-de-conocimiento]] · [[stack]] · [[changelog]]

## Contexto en el monorepo

```
blu/ (monorepo)
├── blu-web-v1/          ← ESTE PROYECTO (Nuxt 3, puerto 3000)
│   ├── Sitio público: /, /nosotros, /hablemos, /servicios/*, /catalogo-merch
│   ├── Admin panel: /staffpanel/*
│   └── consume API de ↓
├── sitio-api-rest-v1-laravel/  (Laravel 10, puerto 8060)
│   └── MySQL 8.0 + Redis
├── bluMiniErp/          (ERP interno, puerto 8823)
└── adata/landing/       (HTML estático)
```

## Páginas principales

### Sitio público

> Componentes de cada página en [[base-de-conocimiento#Estructura de Archivos Importantes|base de conocimiento → Estructura]]
> Layouts de servicios en [[base-de-conocimiento#Layouts de Servicios|base de conocimiento → Layouts]]

| Ruta | Archivo | Descripción |
|------|---------|-------------|
| `/` | `index.vue` | Landing ([[base-de-conocimiento#Hero Section LandingHeroSectionvue|Hero]] + Servicios + Goals) |
| `/nosotros` | `aboutUs.vue` | Hero, manifiesto, ritmo, unidades de negocio, clientes |
| `/hablemos` | `letsTalk.vue` | Tab 0: formulario contacto, Tab 1: calendario citas |
| `/servicios/it` | `services/it.vue` | [[base-de-conocimiento#1 Timeline Vertical IT|Timeline vertical]] |
| `/servicios/marketing` | `services/marketing.vue` | [[base-de-conocimiento#2 Cards Flotantes Marketing|Cards flotantes]] + CTA a [[#Catálogo de merch\|catálogo]] |
| `/servicios/bi` | `services/bi.vue` | [[base-de-conocimiento#3 Scroll Horizontal BI|Scroll horizontal]] |
| `/servicios/recruiting` | `services/recruiting.vue` | [[base-de-conocimiento#4 Acordeón Expandible Recruiting|Acordeón]] + [[base-de-conocimiento#JobBoard Búsquedas activas de Recruiting|JobBoard]] |
| `/catalogo-merch` | `catalogoMerch.vue` | Galería pública del [[#Catálogo de merch\|catálogo de merch]], filtros por categoría + búsqueda + lightbox |
| `/[email]` | `[email].vue` | vCard dinámica |

### Panel admin (`/staffpanel`)

> Convenciones y guía para agregar secciones en [[base-de-conocimiento#Admin Panel staffpanel|base de conocimiento → Admin]]

| Ruta | Descripción |
|------|-------------|
| `/staffpanel/login` | Login standalone |
| `/staffpanel` | Dashboard |
| `/staffpanel/contactos` | Mensajes de contacto |
| `/staffpanel/citas` | Gestión de citas |
| `/staffpanel/timeslots` | Generación de horarios |
| `/staffpanel/catalogo` | CRUD del [[#Catálogo de merch\|catálogo de merch]] + upload de imágenes |
| `/staffpanel/usuarios` | CRUD usuarios |

## Layouts
- `default.vue` — Público: Header + Footer + globalOverlay → usa [[base-de-conocimiento#Fondos de Página|fondos animados]]
- `admin.vue` — Admin: sidebar con nav + logout (item "Catálogo" entre Horarios y Usuarios)

## i18n
- Español (default) e Inglés
- Rutas localizadas: `/servicios/it` ↔ `/services/it`, `/nosotros` ↔ `/about-us`, `/catalogo-merch` ↔ `/merch-catalog`
- Páginas admin excluidas de i18n (`false` en `nuxt.config.ts`)
- Paquete: [[stack#Core|@nuxtjs/i18n 9.5]]

## Auth y permisos (admin)

- JWT via `stores/auth.js` ([[stack#Core|Pinia 3.0]])
- Token en localStorage
- `apiFetch()` agrega Bearer automáticamente → [[stack#Backend consumido|endpoints del backend]]
- `middleware/admin.js` protege rutas `/staffpanel/*` (auth + permisos por sección)
- Credenciales dev: `sistemas@gmail.com` / `npm8956`

### Sistema de permisos por sección

Cada usuario tiene `permissions` (JSON array) en la tabla `users` del backend.
Admin role siempre tiene todos los permisos (bypass en el getter).

| Componente | Archivo | Función |
|-----------|---------|--------|
| Getter | `stores/auth.js` → `hasPermission(section)` | Admin=true siempre, otros chequean array |
| Middleware | `middleware/admin.js` → mapa `ROUTE_SECTION` | Redirige a dashboard si no tiene permiso |
| Sidebar | `layouts/admin.vue` → `v-if` en cada nav item | Oculta secciones sin permiso |
| Gestión | `pages/staffpanel/usuarios.vue` → array `SECTIONS` | Checkboxes para asignar permisos |
| Backend | `UpdateUserRequest` + `CreateUserRequest` | Valida códigos con `in:` |

**Códigos válidos:** `contactos`, `citas`, `timeslots`, `catalogo`, `reclutamiento`, `usuarios`

Al agregar nueva sección: registrar el código en los 5 archivos listados arriba.
Ver [[changelog#2026-04-15 — Sistema de permisos por sección  fixes admin panel|changelog]] y [[memoria#Sistema de permisos admin 2026-04-15|memoria]].

### HTML nativo en admin (NO Nuxt UI)

Los componentes Nuxt UI (`UInput`, `UButton`, `UFormField`) renderizan mal en el
admin porque el sitio tiene dark mode global. Usar HTML nativo con estilos scoped.
`<UIcon>` y `<UModal>` sí funcionan. Ver [[memoria#HTML nativo en admin|detalle]].

### Data flow

```
CSV + images/{sku}/      ← import local (host)
       ↓
docker cp → blu-api-laravel:/tmp/...
       ↓
php artisan catalog:import
       ↓
MySQL: products + product_images     +     storage/app/public/catalog/{sku}/*
       ↓                                           ↓
GET /api/catalog/products      ←    imágenes servidas por Apache en
       ↓                              http://localhost:8060/storage/...
pages/catalogoMerch.vue (front)
pages/staffpanel/catalogo.vue (admin CRUD con auth)
```

### Modelo de datos (backend)

| Tabla | Columnas relevantes |
|-------|---------------------|
| `products` | `sku` (unique), `category`, `title`, `description`, `active`, `sort_order` |
| `product_images` | `product_id` (cascade), `path`, `sort_order`, `is_cover` |

Al borrar un producto, las imágenes se eliminan del storage antes del `delete()`.
Al borrar la imagen portada, la siguiente por `sort_order` se promueve automáticamente.

### Endpoints consumidos

Ver detalles en [[stack#Backend consumido|stack → backend]]. Resumen:

- Público: `GET /api/catalog/products?category=X&include_inactive=0`
- Admin (Bearer): CRUD `products` + endpoints de `images` (upload múltiple, delete, set cover)

### Trampa del APP_URL

Las URLs de imagen se generan con `Storage::url()` que usa `APP_URL` del `.env`
del backend. Por default viene como `http://localhost` — hay que setear
`http://localhost:8060` en dev o el dominio real en producción para que las
imágenes se carguen desde el front.

### Pipeline de normalización de imágenes

Toda imagen que entra al catálogo (via [[base-de-conocimiento#Admin Panel staffpanel|admin panel]]
o via `catalog:import`) se pasa por `App\Src\BackOffice\Catalog\Image\NormalizeImage`
(GD puro, sin dependencias composer extra). Objetivo: que todas las cards queden con
el mismo marco visual aunque las fotos originales tengan fondos, sombras, transparencias
o aspect ratios distintos.

**Pasos del pipeline:**

1. **Detectar tipo real por contenido** (`getimagesize`), no por extensión — clientes
   suben PNGs con extensión `.jpg` (export Mac "Copia de X")
2. **Flatten sobre canvas blanco** — maneja PNGs con transparencia
3. **Whiten background** — todo pixel con RGB ≥ 230 se snapea a blanco puro, eliminando
   sombras suaves y gradientes que bloqueaban el crop
4. **imagecropauto** con `IMG_CROP_THRESHOLD=0.5` contra blanco — recorta márgenes
5. **Canvas cuadrado** con 8% de padding (`contentSize = max(cw, ch); canvasSize = contentSize * 1.16`)
6. **Save atómico** — escribe a `.tmp` y `rename()` sobre el original (si falla, queda intacto)

Hay comando artisan `catalog:normalize-images [--sku=X | --product=ID]` idempotente
para reprocesar lo existente (683 imágenes ~2 min en el container).

**Estilos del front** para que el fondo blanco se perciba como "marco":
`pages/catalogoMerch.vue` → cards, modal y thumbs usan `background: #fff` con
`padding` en el `<img>` (12px card, 20px modal, 4px thumb).

**Filtro adicional**: el `computed` del front oculta productos con `active=false`
o sin imágenes, además del filtro del backend.

Ver gotchas en [[changelog#2026-04-13 — Normalización de imágenes del catálogo|changelog]].

## SEO y archivos de descubrimiento

El sitio vive en el **dominio canónico `blustudioinc.com`**. La razón social legal
es "BLU STUDIO GROUP LLC" pero `blustudiogroup.com` **no** es el dominio — es una
trampa recurrente que costó un commit de corrección (`5b87943` el 2026-04-15). Si
aparece `blustudiogroup.com` en el código, es un bug. Ver [[memoria#Dominio canónico blustudioinccom|memoria → dominio canónico]].

### Lugares donde el dominio vive hardcodeado

| Archivo | Líneas |
|---------|--------|
| `nuxt.config.ts` | `site.url` (para `@nuxtjs/sitemap`) + `runtimeConfig.public.siteUrl` |
| `public/robots.txt` | línea `Sitemap:` |
| `public/llms.txt` | URLs de servicios + contacto + idiomas |
| `public/.well-known/security.txt` | `Contact:` + `Canonical:` |

### Archivos de descubrimiento

Ubicación: `public/` → servidos como estáticos en la raíz del dominio.

| Archivo | Propósito | Fuente |
|---------|-----------|--------|
| `/sitemap.xml` | Indexación de buscadores | **Generado automáticamente** por `@nuxtjs/sitemap` en build, incluye todas las rutas de Nuxt con variantes i18n. No se commitea. |
| `/robots.txt` | Permisos de crawlers | Estático. Referencia el sitemap. Permite explícitamente GPTBot, ClaudeBot, Google-Extended, PerplexityBot, YouBot. |
| `/llms.txt` | Descripción estructurada para LLMs | Estático. Formato [llms.txt](https://llmstxt.org/): servicios, contacto, idiomas. |
| `/.well-known/security.txt` | Contacto de seguridad | Estático. Expira 2027-03-23, reemplazar antes. |
| `/bimi/logo.svg` | Logo para BIMI (Brand Indicators for Message Identification) | Estático. Perfil **SVG Tiny 1.2 Portable/Secure** obligatorio. |

### Checklist del perfil BIMI

Todo SVG que vaya a `/bimi/logo.svg` debe cumplir:

- `baseProfile="tiny-ps"` + `version="1.2"` en el root `<svg>`
- Elemento `<title>` presente
- `viewBox` cuadrado arrancando en `0 0` (ej. `0 0 500 500`)
- **Sin** `x`/`y` en el root
- **Sin** `<script>`, `<animate*>`, `<foreignObject>`, `<image>`, `<filter>`, `xlink:`, refs externas (`href=`)
- Tamaño < 32 KB

Se validan todos con un solo `grep -cE`:
```bash
grep -cE "<script|<animate|<foreignObject|<image |xlink:|<a |<use |href=|filter=|<filter" public/bimi/logo.svg
# Debe devolver 0
```

Un SVG "normal" (Illustrator export, Figma export) **no cumple** estas restricciones
— hay que ajustarlo a mano o rechazarlo.
