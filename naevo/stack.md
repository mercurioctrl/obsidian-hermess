# Stack

## Frontend

| Tecnología | Versión | Uso |
|---|---|---|
| **Nuxt 3** | SSR | Framework principal, páginas + admin panel |
| **Vue 3** | Composition API | Componentes |
| **Pinia** | - | State management (`stores/auth.ts`, `stores/cart.ts`) |
| **Tailwind CSS** | - | Estilos utility-first |
| **TypeScript** | - | Tipado en `.vue` y composables |

**Composables clave:**
- `useApi.ts` — wrapper con SSR base URL, auth token, guest session via `X-Session-Id`, `upload()` para FormData
- `useMercadoPago.ts` — carga SDK de MP y renderiza Payment Brick
- `useGooglePlaces.ts` — autocomplete de direcciones (Argentina), requiere `GOOGLE_MAPS_API_KEY`
- `useToast.ts` — notificaciones toast

**Layouts:**
- `default.vue` — AnnouncementBar + TheHeader + slot + TheFooter + CartDrawer
- `auth.vue` — Logo + formulario (login/registro)
- `admin.vue` — AdminSidebar + AdminHeader + slot

El home usa `definePageMeta({ layout: false })` y maneja su propia estructura.

## Backend

| Tecnología | Versión | Uso |
|---|---|---|
| **Laravel** | 11 | API REST |
| **PHP** | 8.3 | Runtime |
| **Sanctum** | - | Auth con tokens (cookie `auth_token`) |
| **MySQL** | 8 | Base de datos |
| **Redis** | 7 | Cache, sessions, queues |
| **MercadoPago SDK PHP** | - | Integración Bricks + webhooks |

**Estructura:**
- 39 modelos Eloquent
- 45 migraciones
- 16 seeders (incluye admin, 6 productos, 5 wellness goals, testimonials, blog posts, quiz completo, 3 shipping carriers)
- 15 controllers públicos + 18 controllers admin
- Scheduler corriendo en container separado (generación de órdenes de suscripción)

## Infraestructura (Docker Compose)

6 servicios en `naevo/docker-compose.yml`:

| Servicio | Imagen/Build | Puerto interno | Puerto host (via `.env`) |
|---|---|---|---|
| `naevo-db` | mysql:8 | 3306 | `DB_PORT=3309` |
| `naevo-redis` | redis:7 | 6379 | `REDIS_PORT=6383` |
| `naevo-backend` | Laravel build | 8000 | - |
| `naevo-scheduler` | Laravel build (cron) | - | - |
| `naevo-frontend` | Nuxt build | 3000 | - |
| `naevo-nginx` | nginx:alpine | 80 | `APP_PORT=8088` |

Nginx rutea `/api/*` → backend:8000 y `/` → frontend:3000.

**Volúmenes nombrados** (no bind mounts) — usar `docker compose cp` para copiar archivos.

## Servicios externos

- **MercadoPago** — Payment Brick + webhook en `/api/webhooks/mercadopago`
- **Google Places API** — autocomplete de direcciones (AR)
- **Shipping carriers** — OCA, Andreani, Entregar (costos simulados, no hay integración real todavía)

## Comandos

```bash
cd naevo && ./start.sh                                                # Build + start
cd naevo && ./stop.sh                                                 # Stop
cd naevo && ./restore.sh                                              # Restaurar backup (interactivo)

docker compose -f naevo/docker-compose.yml logs -f frontend           # Logs frontend
docker compose -f naevo/docker-compose.yml logs -f backend            # Logs backend
docker compose -f naevo/docker-compose.yml exec backend php artisan migrate --seed
docker compose -f naevo/docker-compose.yml exec backend php artisan tinker

# Rebuild frontend (obligatorio tras cambios por SSR):
docker compose -f naevo/docker-compose.yml build --no-cache frontend && \
  docker compose -f naevo/docker-compose.yml up -d frontend
```

## Ver también

- [[naevo|Índice]]
- [[arquitectura|Arquitectura]]
- [[modulos|Módulos backend]]
