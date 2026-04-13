# Arquitectura — blu-web-v1

> Ver también: [[base-de-conocimiento]] · [[stack]] · [[changelog]]

## Contexto en el monorepo

```
blu/ (monorepo)
├── blu-web-v1/          ← ESTE PROYECTO (Nuxt 3, puerto 3000)
│   ├── Sitio público: /, /nosotros, /hablemos, /servicios/*, /catalogo-merch
│   ├── Admin panel: /cmsadmin/*
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

### Panel admin (`/cmsadmin`)

> Convenciones y guía para agregar secciones en [[base-de-conocimiento#Admin Panel cmsadmin|base de conocimiento → Admin]]

| Ruta | Descripción |
|------|-------------|
| `/cmsadmin/login` | Login standalone |
| `/cmsadmin` | Dashboard |
| `/cmsadmin/contactos` | Mensajes de contacto |
| `/cmsadmin/citas` | Gestión de citas |
| `/cmsadmin/timeslots` | Generación de horarios |
| `/cmsadmin/catalogo` | CRUD del [[#Catálogo de merch\|catálogo de merch]] + upload de imágenes |
| `/cmsadmin/usuarios` | CRUD usuarios |

## Layouts
- `default.vue` — Público: Header + Footer + globalOverlay → usa [[base-de-conocimiento#Fondos de Página|fondos animados]]
- `admin.vue` — Admin: sidebar con nav + logout (item "Catálogo" entre Horarios y Usuarios)

## i18n
- Español (default) e Inglés
- Rutas localizadas: `/servicios/it` ↔ `/services/it`, `/nosotros` ↔ `/about-us`, `/catalogo-merch` ↔ `/merch-catalog`
- Páginas admin excluidas de i18n (`false` en `nuxt.config.ts`)
- Paquete: [[stack#Core|@nuxtjs/i18n 9.5]]

## Auth (admin)
- JWT via `stores/auth.js` ([[stack#Core|Pinia 3.0]])
- Token en localStorage
- `apiFetch()` agrega Bearer automáticamente → [[stack#Backend consumido|endpoints del backend]]
- `middleware/admin.js` protege rutas `/cmsadmin/*`
- Credenciales dev: `sistemas@gmail.com` / `npm8956`

## Catálogo de merch

Feature agregada en [[changelog#2026-04-13 — Catálogo de merch|2026-04-13]]. Galería
pública de productos de merchandising corporativo, sin precios (solo título + fotos
por categoría).

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
pages/cmsadmin/catalogo.vue (admin CRUD con auth)
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
