# Arquitectura — blu-web-v1

> Ver también: [[base-de-conocimiento]] · [[stack]]

## Contexto en el monorepo

```
blu/ (monorepo)
├── blu-web-v1/          ← ESTE PROYECTO (Nuxt 3, puerto 3000)
│   ├── Sitio público: /, /nosotros, /hablemos, /servicios/*
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
| `/servicios/marketing` | `services/marketing.vue` | [[base-de-conocimiento#2 Cards Flotantes Marketing|Cards flotantes]] |
| `/servicios/bi` | `services/bi.vue` | [[base-de-conocimiento#3 Scroll Horizontal BI|Scroll horizontal]] |
| `/servicios/recruiting` | `services/recruiting.vue` | [[base-de-conocimiento#4 Acordeón Expandible Recruiting|Acordeón]] + [[base-de-conocimiento#JobBoard Búsquedas activas de Recruiting|JobBoard]] |
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
| `/cmsadmin/usuarios` | CRUD usuarios |

## Layouts
- `default.vue` — Público: Header + Footer + globalOverlay → usa [[base-de-conocimiento#Fondos de Página|fondos animados]]
- `admin.vue` — Admin: sidebar con nav + logout

## i18n
- Español (default) e Inglés
- Rutas localizadas: `/servicios/it` ↔ `/services/it`, `/nosotros` ↔ `/about-us`
- Páginas admin excluidas de i18n (`false` en `nuxt.config.ts`)
- Paquete: [[stack#Core|@nuxtjs/i18n 9.5]]

## Auth (admin)
- JWT via `stores/auth.js` ([[stack#Core|Pinia 3.0]])
- Token en localStorage
- `apiFetch()` agrega Bearer automáticamente → [[stack#Backend consumido|endpoints del backend]]
- `middleware/admin.js` protege rutas `/cmsadmin/*`
- Credenciales dev: `sistemas@gmail.com` / `npm8956`
