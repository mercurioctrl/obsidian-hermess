# Módulos

Mapa rápido de los 13 módulos documentados en `naevo/docs/modules/`. Cada uno tiene su archivo con detalles de controllers, modelos y lógica no-obvia.

| Módulo | Propósito | Claves |
|---|---|---|
| **auth** | Login, registro, tokens Sanctum | Cookie `auth_token`, auto-vinculación de orders guest al registrarse |
| **blog** | Posts, categorías, comentarios | Author es string libre (no FK a users) |
| **cart-checkout** | Carrito + flujo de checkout | Guest session via `X-Session-Id`, resolución manual del user |
| **checkout** | Single-step con MercadoPago Bricks | createOrder (pending) → Brick → processPayment → webhook backup |
| **cms** | Contenido del home editable | Todo el home viene de `/api/cms/home`. Campos duales en banners: `image_url` vs `slider_image_url` |
| **infrastructure** | Docker, Nginx, volumes, env vars | REDIS_PORT interno 6379, APP_PORT host 8088 |
| **loyalty** | Programa de puntos | Puntos se acreditan al `delivery`, no al purchase. Bonus por review aprobada. Solo users auth |
| **newsletter** | Suscripciones al newsletter | Email simple, sin doble opt-in |
| **orders** | Estados y transiciones | `pending → confirmed → preparing → shipped → delivered` (+ cancel/refund) |
| **products** | Catálogo, variants, reviews | Reviews moderadas. Stock decrementa al crear orden. `is_active` para ocultar (no soft delete) |
| **quiz** | Cuestionario de bienestar | Suma pesos de `quiz_option_product_rules`, retorna top 3-5 |
| **reviews** | Moderación de reseñas | `pending → approved/rejected`. Al aprobar recalcula promedio del producto |
| **subscriptions** | Suscripciones mensuales | Cron en container `naevo-scheduler` genera órdenes según `frequency_days` |

## API pública (resumen)

- `GET /api/products`, `/api/products/search`, `/api/products/{slug}`
- `GET /api/categories`
- `GET /api/cms/home`
- `GET /api/quiz`, `POST /api/quiz/submit`
- `GET /api/blog`, `/api/blog/{slug}`
- `POST /api/auth/register`, `/api/auth/login`, `/api/auth/logout`, `GET /api/auth/me`
- `GET/POST /api/cart/*`
- `POST /api/checkout/create`, `/api/checkout/process-payment`
- `GET /api/orders/guest/{orderNumber}` (public con guest_token)
- `GET /api/shipping-methods`
- `POST /api/webhooks/mercadopago`
- `POST /api/reviews`
- `GET /api/loyalty` (auth)
- `POST /api/newsletter`

## API admin

Prefijo `/api/admin/*`, todas con middleware `auth:sanctum` + check `role=admin`. 18 controllers.

## Ver también

- [[naevo|Índice]]
- [[arquitectura|Arquitectura]]
- [[contexto|Reglas de negocio]]
