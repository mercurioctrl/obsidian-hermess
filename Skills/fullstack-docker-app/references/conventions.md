# Convenciones y Patrones

> Parte del skill [[SKILL|fullstack-docker-app]]. Ver también [[architecture]].

## Backend (Laravel)

### env() vs config()

**NUNCA usar `env()` directamente en controllers o services.** PHP-FPM no hereda variables de entorno del container.

```php
// MAL
$key = env('API_KEY');

// BIEN — registrar en config/services.php, luego usar config()
$key = config('services.mi_servicio.api_key');
```

### Rutas específicas antes de apiResource

```php
// BIEN
Route::get('gastos/categorias', [GastoController::class, 'categorias']);
Route::apiResource('gastos', GastoController::class);
```

### Enums casteados

```php
// BIEN
if ($usuario->rol === RolUsuario::ADMIN) { ... }
```

### API Resources y wrapper data:

Los endpoints envuelven respuesta en `{ "data": {...} }`.
Frontend: `const res = await api.get(...); modelo.value = res?.data ?? res`

## Frontend (Nuxt 3)

### useApi

```typescript
const { data } = await api.get('/endpoint');
const { data } = await api.post('/endpoint', { campo: valor });
await api.delete('/endpoint', { data: { campo: valor } });
```

### Componentes UI

Con `pathPrefix: false`, los componentes en `components/ui/` se usan directamente:

```vue
<FormField />   <!-- NO <UiFormField /> -->
<Modal />       <!-- NO <UiModal /> -->
```

### Modal siempre con v-model

```vue
<Modal v-model="showModal">...</Modal>
```

### Iconos con prefijo lucide:

```vue
<Icon name="lucide:search" />
```

## Docker

### DB_HOST es el nombre del servicio

En [[backend-env.example]]: `DB_HOST=db`, `REDIS_HOST=redis` (DNS Docker).
Ver [[docker-compose.yml]] para la definición de servicios.

### Deploy rápido backend

```bash
docker cp backend/archivo.php container-backend:/var/www/html/path/
docker exec container-backend php artisan optimize:clear
```

No requiere rebuild. Ver [[architecture]] para explicación.

### Deploy frontend (siempre rebuild)

```bash
docker compose build --no-cache frontend
docker compose up -d frontend
docker restart container-nginx
```

Requiere rebuild porque Nuxt compila a `.output/` en build time. Ver [[frontend.Dockerfile]].

## General

- Idioma del proyecto: español (código, variables, commits)
- `.env` nunca se commitea → template en [[env.example]]
- Secretos generados por [[start.sh]] con `openssl rand`
- Infraestructura definida en [[docker-compose.yml]]
