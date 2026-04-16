# Stack Técnico — blu-web-v1

> Ver también: [[arquitectura]] · [[base-de-conocimiento]] · [[changelog]]

## Core
- **Framework:** Nuxt 3.16 + Vue 3.5 → [[arquitectura#Contexto en el monorepo|contexto monorepo]]
- **Estilos:** SCSS (sass 1.89) + Nuxt UI 3.3 → [[base-de-conocimiento#Patrones y Convenciones|patrones CSS]]
- **i18n:** @nuxtjs/i18n 9.5 (español default + inglés) → [[arquitectura#i18n|config i18n]]
- **State:** Pinia 3.0 → [[arquitectura#Auth admin|auth store]]
- **Router:** Vue Router 4.5

## Dependencias principales

> Uso de GSAP y Lottie documentado en [[base-de-conocimiento#Optimizaciones de Rendimiento|rendimiento y animaciones]]

| Paquete | Uso |
|---------|-----|
| gsap 3.12 | [[base-de-conocimiento#Animaciones CSS Performantes|Animaciones]] + ScrollTrigger |
| lottie-web 5.13 | Animaciones Lottie |
| @nuxt/image 1.10 | Optimización de imágenes |
| @nuxt/icon 1.12 | Iconos |
| @nuxt/fonts 0.11 | Fuentes |
| @nuxt/scripts 0.11 | Scripts externos |
| @nuxtjs/color-mode 3.5 | Tema claro/oscuro |
| @nuxtjs/sitemap 7.6 | Sitemap SEO |
| nuxt-gtag 4.0 | Google Analytics 4 |
| vee-validate 4.15 | Validación de formularios |
| vue-recaptcha-v3 2.0 | reCAPTCHA v3 (formulario [[arquitectura#Sitio público|/hablemos]]) |
| hamburgers 1.2 | Menú hamburguesa CSS |

## Dev
- ESLint 9 + eslint-plugin-vue 10
- Tabs, semicolons

## Backend consumido

> Estructura del backend en [[arquitectura#Contexto en el monorepo|monorepo]]
> Admin consume estos endpoints via `apiFetch()` → [[base-de-conocimiento#Admin Panel staffpanel|panel admin]]

- Laravel 10 en `localhost:8060` (container `blu-api-laravel`, branch `gamma`)
- Auth: Sanctum (Bearer token)
- **IMPORTANTE:** `APP_URL=http://localhost:8060` en el `.env` del container
  (ver [[arquitectura#Trampa del APP_URL|trampa del APP_URL]])

### Endpoints públicos
- `POST /api/contact` — formulario de contacto (con reCAPTCHA v3)
- `POST /api/job-application` — postulación desde [[base-de-conocimiento#JobBoard Búsquedas activas de Recruiting|JobBoard]]
- `POST /api/appointment` — agendar cita
- `GET /api/calendar/timeslots` — horarios disponibles
- `GET /api/catalog/products` — [[arquitectura#Catálogo de merch|catálogo de merch]] (acepta `?category=X` y `?include_inactive=1`)
- `GET /api/vCard?email=` — vCard dinámica
- `POST /api/login` — login admin

### Endpoints protegidos (`/api/backOffice/*`)
- `user`, `client`, `service` — CRUD de usuarios, clientes, servicios
- `contact`, `appointment` — lectura y gestión
- `time-slot/generate`, `time-slot/generate/weekly`, `time-slot/{id}` — generación y borrado de horarios
- `catalog/products` — CRUD productos del [[arquitectura#Catálogo de merch|catálogo]]
- `catalog/products/{id}/images` — upload múltiple (multipart `images[]`, mimes jpg/jpeg/png/webp, max 8MB)
- `catalog/images/{imageId}` — delete imagen (promueve siguiente portada si era cover)
- `catalog/images/{imageId}/cover` — set cover

## Colores de servicios

> Uso en componentes: [[base-de-conocimiento#Colores de Servicios|flujo del color de acento]]
> Páginas que los usan: [[arquitectura#Sitio público|mapa de servicios]]

- IT: `#00D985` (verde)
- Marketing: `#FF00D0` (magenta) — también se usa en el [[arquitectura#Catálogo de merch|catálogo de merch]]
- BI: `#9c44ff` (violeta)
- Recruiting: `#00CFCE` (cyan)
- Azul principal: `#0474f4`
