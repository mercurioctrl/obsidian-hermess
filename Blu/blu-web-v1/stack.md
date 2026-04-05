# Stack Técnico — blu-web-v1

> Ver también: [[arquitectura]] · [[base-de-conocimiento]]

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
> Admin consume estos endpoints via `apiFetch()` → [[base-de-conocimiento#Admin Panel cmsadmin|panel admin]]

- Laravel 10 en `localhost:8060`
- Auth: Sanctum (Bearer token)
- Endpoints: `/api/contact`, `/api/calendar/timeslots`, `/api/appointment`, `/api/vCard`, `/api/login`, `/api/backOffice/*`

## Colores de servicios

> Uso en componentes: [[base-de-conocimiento#Colores de Servicios|flujo del color de acento]]
> Páginas que los usan: [[arquitectura#Sitio público|mapa de servicios]]

- IT: `#00D985` (verde)
- Marketing: `#FF00D0` (magenta)
- BI: `#9c44ff` (violeta)
- Recruiting: `#00CFCE` (cyan)
- Azul principal: `#0474f4`
