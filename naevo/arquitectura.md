# Arquitectura

E-commerce headless: Nuxt 3 SSR en el frontend + Laravel 11 en el backend, conectados via Nginx como reverse proxy. Admin panel vive dentro del frontend Nuxt (no es una SPA aparte).

## Estructura de carpetas

```
naevo/
  docker-compose.yml          # 6 servicios
  start.sh / stop.sh          # Arranque completo
  backup.sh / restore.sh      # Backup interactivo de DB + uploads
  sync-from-prod.sh           # Pull data desde prod

  frontend/                   # Nuxt 3 SSR
    pages/                    # Storefront + admin/
    components/
      home/                   # 10 componentes del homepage
      ui/                     # DataTable, FormField, Modal, StatusBadge, Toast
      admin/                  # AdminHeader, AdminSidebar
      (root)                  # TheHeader, TheFooter, AnnouncementBar, CartDrawer, SearchModal
    layouts/                  # default, auth, admin
    stores/                   # auth.ts, cart.ts (Pinia)
    composables/              # useApi.ts, useMercadoPago.ts, useGooglePlaces.ts, useToast.ts

  backend/                    # Laravel 11
    app/Http/Controllers/Api/        # 15 controllers públicos
    app/Http/Controllers/Api/Admin/  # 18 controllers admin
    app/Models/                      # 39 modelos Eloquent
    database/migrations/             # 45 migraciones
    database/seeders/                # 16 seeders
    routes/api.php                   # Todas las rutas API

  nginx/default.conf          # /api → backend:8000, / → frontend:3000
  docs/                       # architecture.md, schema.md, modules/
```

## Patrones de datos

- **API REST** — sin GraphQL, convencional CRUD en `/api/*`.
- **SSR con hidratación** — el home y páginas estáticas se renderizan en servidor (via `useAsyncData` con `useApi().get()`). Requiere `docker build --no-cache frontend` después de cada cambio.
- **Guest session** — el header `X-Session-Id` se envía siempre (sin login) junto con `Bearer token` cuando hay auth. El backend resuelve user/session manualmente en rutas que no tienen `auth:sanctum`.
- **Auth por cookie** — token Sanctum en cookie `auth_token` (no localStorage), compatible con SSR.
- **Home 100% CMS-driven** — todo el contenido del home viene de `/api/cms/home`. Nada hardcodeado excepto estructura de componentes.

## Módulos backend (13)

Un archivo `.md` por módulo en `naevo/docs/modules/`:
auth, blog, cart-checkout, checkout, cms, infrastructure, loyalty, newsletter, orders, products, quiz, reviews, subscriptions.

Ver [[modulos|Mapa de módulos]] para detalle rápido.

## Reglas de negocio clave

- **Stock** → se decrementa al crear orden (estado `pending`). Producto pasa a `out_of_stock` cuando llega a 0.
- **Orders** → flujo `pending → confirmed → preparing → shipped → delivered` (+ cancel/refund).
- **Checkout single-step** → crear orden → MercadoPago Brick → `processPayment` → webhook backup. Soporta guest (email + dirección inline) y auth (dirección guardada).
- **Delivery** → `shipping` (address + shipping method) o `pickup` (sin costo).
- **Loyalty** → puntos se acreditan al `delivery`, no al purchase. Bonus por review aprobada. Solo para users auth (guests no acumulan).
- **Guest checkout** → `user_id` nullable en orders, ownership por `session_id`, confirmación por `guest_token`, auto-vinculación al registrarse.
- **Reviews** → moderadas (`pending → approved/rejected`). Al aprobar, recalcular promedio del producto.
- **Quiz** → suma pesos de `quiz_option_product_rules`, retorna top 3-5 en orden descendente.
- **Cupones** → validar: activo, rango fechas, max usos, monto mínimo, aplicabilidad.
- **Suscripciones** → cron genera órdenes automáticamente según `frequency_days`.

## Decisiones ya tomadas

1. **No hay soft deletes** — se usa `is_active` para ocultar, o se borra directo.
2. **Categorías flat** — sin `parent_id`, sin jerarquía.
3. **Addresses referenciadas, no copiadas** — orders tienen FK con `nullOnDelete`.
4. **Pagos via MercadoPago Brick** — `mercadopago_payment_id` y `mercadopago_preference_id` en orders.
5. **Blog author es string libre** — no hay FK a users.

## Orden actual del home (abril 2026)

Tras la reestructuración de abril 2026:

1. AnnouncementBar
2. TheHeader (nav: Inicio, Productos, Ciencia, Blog, Profesionales)
3. HeroSlider o HeroBanner (según `hero_display_mode`)
4. **FeaturedProducts** (movido arriba)
5. WellnessGoals (grid 6-col con hover crossfade lifestyle↔producto)
6. QualityBadges (unificado con certifications)
7. SubscriptionSection
8. QuizSection
9. TestimonialsSection
10. RewardsSection
11. NewsletterSection
12. TheFooter

`ScienceIngredients` y `BlogPreview` ya no se renderizan en el home — Science vive en `/ciencia`, el blog preview se eliminó completamente.

## Ver también

- [[naevo|Índice]]
- [[stack|Stack y dependencias]]
- [[modulos|Módulos]]
- [[contexto|Reglas de negocio y TODOs]]
- [[memoria|Memoria auto-guardada]]
