---
tipo: auditoria-seguridad
proyecto: blu-web-v1 + sitio-api-rest-v1-laravel
dominio: blustudioinc.com / api.blustudioinc.com
fecha: 2026-09-19
autor: Hermes + Claude
estado: aplicado-pendiente-de-deploy
---

# 🔒 Auditoría de seguridad — blustudioinc.com (2026-09-19)

> Documento de trabajo **para Claude Code**. Lista lo que hay que resolver en el
> front ([[blu-web-v1]]) y en la API Laravel (`sitio-api-rest-v1-laravel`).
> **Regla de oro: no romper nada de lo que hoy funciona.** Cada tarea indica qué
> tocar, qué **NO** tocar y cómo verificar que no se rompió nada.

---

## ⚠️ Antes de empezar — leer esto

1. **El checkout local diverge de producción.** Durante la auditoría se detectó que
   el código en `/var/www/blu/sitio-api-rest-v1-laravel` **no coincide** con lo
   deployado:
   - El middleware `client.api.key` **no existe en local** pero en prod **sí corre**
     (los endpoints `/partner/*` devuelven 401 sin API key en vivo).
   - `.env` local tiene `APP_DEBUG=true` / `APP_ENV=local`, pero **prod tiene debug OFF**.
   
   👉 **Primer paso obligatorio:** sincronizar / traer la rama que está realmente en
   producción y **re-validar cada hallazgo contra el código deployado** antes de editar.
   No apliques cambios a ciegas sobre el checkout local.

2. **Trabajar en rama aparte** (`fix/seguridad-2026-09`), no sobre main/producción.

3. **Tests antes y después:** correr `php vendor/bin/phpunit` antes de tocar nada para
   tener baseline, y de nuevo después de cada tarea. Si un test que pasaba empieza a
   fallar → revisar, no forzar.

4. **Deploy:** el backend se deploya con `./start.sh`. El front corre en PM2 puerto 3008.

---

## 🔴 PRIORIDAD ALTA — resolver primero

### TAREA 1 — Escalada de privilegios en UpdateUser (Broken Access Control)

- **Archivo:** `app/Src/BackOffice/User/Update/UpdateUserRequest.php`
- **Problema:** `authorize()` permite el rol `staff` además de `admin`, y `role_id`
  solo se valida como `exists:roles,id`. Un usuario **`staff` puede hacer
  `PATCH /backOffice/user/{suPropioId}` con `role_id=1` y auto-promoverse a admin**,
  o cambiar el rol de cualquier otro usuario.

```php
// ACTUAL (vulnerable)
public function authorize(): bool
{
    return in_array($this->user()->role, ['admin', 'staff']);
}
```

- **Fix propuesto:**
  1. Restringir la modificación de `role_id` **solo a `admin`**. Opciones:
     - Que `authorize()` para editar `role_id` sea solo `admin`, o
     - Remover `role_id` de las reglas si el que edita no es admin (regla condicional).
  2. Prohibir que un usuario **cambie su propio rol** (comparar `$this->route('id')`
     contra `$this->user()->id`).
  3. Impedir asignar un rol de mayor privilegio que el del que edita.
- **Qué NO tocar:** el flujo normal de edición de perfil (nombre, teléfono, etc.) para
  `staff` debe seguir funcionando — solo bloquear el campo `role_id`. No cambiar
  `UpdateUserService` ni la firma del endpoint.
- **Verificación:**
  - Como `staff`: PATCH con `role_id` → debe dar 403 (o ignorar el campo).
  - Como `staff`: PATCH de datos normales (nombre) → sigue funcionando (200).
  - Como `admin`: PATCH con `role_id` a otro usuario → sigue funcionando.

---

## 🟡 PRIORIDAD MEDIA — esta semana

### TAREA 2 — Rate limiting en /login (anti brute-force)

- **Archivo:** `routes/api.php` (línea del `Route::post('/login', ...)`).
- **Problema:** `/login` solo hereda el throttle global `throttle:api` (~60/min). Sin
  lockout → fuerza bruta viable.
- **Fix propuesto:** `Route::post('/login', Login::class)->middleware('throttle:5,1');`
  o un `RateLimiter` por `email + IP` con bloqueo temporal.
- **Qué NO tocar:** no bajar el throttle global de la API (rompería otros endpoints).
  Aplicar el límite estricto **solo a login**.
- **Verificación:** 6+ intentos fallidos seguidos → HTTP 429. Login normal (1 intento
  correcto) → sigue funcionando.

### TAREA 3 — Eliminar DatabaseConnectionController (debug peligroso)

- **Archivo:** `app/Http/Controllers/DatabaseConnectionController.php`
- **Problema:** expone config de DB, muestra de usuarios, info de red, stacktraces y
  corre `shell_exec` (ping/nc/ip addr). **Hoy no está ruteado** (no explotable), pero
  es un riesgo latente crítico.
- **Fix propuesto:** borrar el archivo. Antes de borrar, `grep -rn "DatabaseConnection"`
  para confirmar que **nada** lo referencia (rutas, tests, comandos).
- **Qué NO tocar:** solo confirmar que no está en uso. Si por algún motivo se usa para
  un healthcheck legítimo, reemplazar por un endpoint mínimo que devuelva solo `{status: ok}`
  sin ningún dato sensible ni `shell_exec`.
- **Verificación:** app arranca, tests pasan, no hay referencias colgando.

### TAREA 4 — CORS: quitar el wildcard

- **Archivo:** `config/cors.php`
- **Problema:** `'allowed_origins' => ['*']` sobre `api/*`. (Mitigado por
  `supports_credentials => false` + auth por Bearer, pero sigue siendo mala práctica.)
- **Fix propuesto:**
```php
'allowed_origins' => [
    'https://blustudioinc.com',
    'https://www.blustudioinc.com',
    // agregar los dominios de landings de partners que consumen /partner/*
],
```
- **Qué NO tocar:** ⚠️ **cuidado con los endpoints `/partner/*`** — los usan landings de
  clientes desde otros dominios. Antes de restringir, listar TODOS los orígenes de
  partners legítimos y agregarlos, o dejar `/partner/*` con una política CORS aparte.
  Romper esto tira abajo los formularios de contacto de las landings de clientes.
- **Verificación:** front propio sigue llamando a la API OK; probar que una landing de
  partner conocida sigue pudiendo enviar el formulario.

### TAREA 5 — Security headers (front + API)

- **Dónde:** preferentemente **Cloudflare Transform Rules** (afecta ambos dominios sin
  tocar código), o middleware en Nuxt/Laravel.
- **Problema:** faltan todos: HSTS, CSP, X-Frame-Options, X-Content-Type-Options,
  Referrer-Policy, Permissions-Policy.
- **Fix propuesto (orden de prioridad):**
  1. `X-Frame-Options: DENY` (o `SAMEORIGIN`) — anti-clickjacking.
  2. `Strict-Transport-Security: max-age=31536000; includeSubDomains`.
  3. `X-Content-Type-Options: nosniff`.
  4. `Referrer-Policy: strict-origin-when-cross-origin`.
  5. CSP: armar con cuidado y **probar en `Content-Security-Policy-Report-Only` primero**
     (una CSP mal armada rompe el sitio — Unicorn Studio/WebGL, GTM, fuentes, etc.).
- **Qué NO tocar:** no meter CSP en modo enforce de una sin testear — puede romper los
  fondos WebGL (Unicorn Studio), Google Tag Manager y assets. Empezar en report-only.
- **Verificación:** el sitio carga igual (hero WebGL, vCard, formularios), y los headers
  aparecen en la respuesta.

### TAREA 6 — Higiene de .env / secretos

- **Problema:** el `.env` de dev en disco tiene `APP_DEBUG=true` y 7 líneas de secretos.
- **Fix propuesto:**
  1. Confirmar que prod tiene `APP_ENV=production` + `APP_DEBUG=false` (hoy está OK).
  2. Asegurar que el `.env` **nunca** se deploya (ya está en `.gitignore`, verificar).
  3. Confirmar que ningún secreto quedó versionado en git history.
- **Qué NO tocar:** no cambiar el `.env` de prod. Solo verificación + garantizar que el
  de dev no sube.

---

## 🟢 PRIORIDAD BAJA — próximo ciclo

### TAREA 7 — Info leak en ControlAccessMiddleware
- **Archivo:** `app/Http/Middleware/ControlAccessMiddleware.php`
- **Problema:** en el `catch` devuelve `$e->getMessage()` crudo al cliente.
- **Fix:** devolver mensaje genérico (`['error' => 'Unauthorized']`), loguear el detalle
  del lado del server.

### TAREA 8 — Comparación de token timing-safe
- **Archivo:** `app/Models/Appointment.php` (líneas ~214 y ~226).
- **Problema:** compara `cancel_token` con `===`.
- **Fix:** `hash_equals($this->cancel_token, $token)`. Impacto bajo (el path real usa
  `where()` en DB), pero es buena práctica.
- **Qué NO tocar:** la generación del token (`Str::random(32)`) ya es correcta, dejarla.

### TAREA 9 — Ocultar header x-powered-by: Nuxt
- **Dónde:** config de Nuxt/Nitro (front).
- **Fix:** remover el header `x-powered-by`.

### TAREA 10 — Tokens Sanctum sin expiración
- **Problema:** `createToken('auth_token')` sin TTL → tokens de larga vida.
- **Fix:** definir expiración/abilities en config de Sanctum (evaluar impacto en el front
  que guarda el JWT en localStorage — no forzar logout masivo sin avisar).

### TAREA 11 — Rutas de Telescope alcanzables en prod
- **Problema:** `/telescope` responde 500 (no 404) en prod → rutas registradas.
- **Fix:** deshabilitar el registro de Telescope en producción (gate `viewTelescope` o
  no cargar el ServiceProvider según `APP_ENV`).

---

## ✅ Lo que YA está bien — NO tocar

Confirmado correcto durante la auditoría. **No modificar estas cosas "de paso":**

- **`cancel_token`** usa `Str::random(32)` → sin IDOR en cancelación de citas.
- **Login sin enumeración de usuarios** (mensaje genérico "Invalid credentials" +
  `Hash::check`).
- **Upload de CV** valida el mime **real** vía `getMimeType()` + límite de 10 MB → no es
  vector de RCE. No relajar esta validación.
- **Mass assignment controlado**: los controllers usan `$request->validated()`, no
  `request->all()`. Mantener este patrón en cualquier código nuevo.
- **Sin SQLi**: no hay queries raw con input de usuario.
- **Prod endurecido**: `APP_DEBUG=false`, sin `.git`/`.env` expuestos, `/api/user`
  protegido (401), sin CORS con `supports_credentials`.

---

## 📋 Orden sugerido de ejecución

1. Sincronizar rama de producción y re-validar (⚠️ paso obligatorio).
2. Baseline de tests (`phpunit`).
3. TAREA 1 (privesc) → deploy → verificar.
4. TAREAS 2, 3 → deploy → verificar.
5. TAREA 4 (CORS, con cuidado por partners) → verificar landings.
6. TAREA 5 (headers, CSP en report-only) → verificar sitio.
7. TAREA 6 (verificación de secretos).
8. TAREAS 7–11 en el próximo ciclo.

Después de cada bloque: `phpunit` verde + smoke test manual del front (login, agendar
cita, cancelar cita, formulario de contacto, formulario de partner).

---

---

## 📌 Estado de ejecución (2026-09-19)

Ramas: `fix/seguridad-2026-09` en ambos repos. **Hecho, falta deployar.**

| Tarea | Estado | Dónde |
|---|---|---|
| 1 — Privesc UpdateUser | ✅ | `UpdateUserRequest` + `CreateUserRequest` |
| 2 — Rate limit /login | ✅ | `RouteServiceProvider` + `routes/api.php` |
| 3 — DatabaseConnectionController | ✅ borrado | — |
| 4 — CORS | ✅ | `config/cors.php` + `AllowPartnerCors` |
| 5 — Security headers | ✅ (sin CSP) | `nuxt.config.ts > routeRules` |
| 6 — Higiene de .env | ✅ verificado | — |
| 7 — Info leak ControlAccess | ✅ | `ControlAccessMiddleware` |
| 8 — hash_equals | ✅ | `Appointment` |
| 9 — x-powered-by | ✅ | `server/plugins/hide-powered-by.ts` |
| 10 — TTL de tokens | ✅ 7 días | `config/sanctum.php` + `stores/auth.js` |
| 11 — Telescope en prod | ✅ | `composer.json` + `config/app.php` + `AppServiceProvider` |

### Decisiones tomadas

- **TAREA 1 — se amplió a `CreateUserRequest`.** Bloquear solo `role_id` en el update
  dejaba el bypass obvio: un `staff` podía crear un usuario admin y loguearse con él.
  Ahora asignar rol (`role_id` / `roleId`) es exclusivo de admin en ambos endpoints, y
  además nadie puede cambiar su propio rol.
- **TAREA 4 — política partida.** `config/cors.php` queda con lista blanca
  (blustudioinc.com, www, localhost:3000/3008) y el middleware global `AllowPartnerCors`
  reabre el wildcard **solo** para `api/partner/*`. Así no hubo que enumerar los dominios
  de las landings de clientes y ninguna se rompe. Sobrescribible con `CORS_ALLOWED_ORIGINS`.
- **TAREA 5 — sin CSP.** Se aplicaron X-Frame-Options (`SAMEORIGIN`, no `DENY`, para no
  romper los iframes internos de `/propuestas`), nosniff, Referrer-Policy, HSTS y
  Permissions-Policy. La CSP queda pendiente: hay que armarla y probarla en Report-Only.
- **TAREA 10 — 401 manejado en el front.** `apiFetch()` no manejaba el 401, así que con
  tokens vencidos el panel quedaba roto. Ahora limpia la sesión y redirige al login.
  ⚠️ Al deployar, todos los usuarios del panel con token de más de 7 días se desloguean
  una vez.

### ⚠️ Pendiente de deploy

Nada de esto está en producción todavía. Backend: `./start.sh` (corre `composer install`,
necesario para que `dont-discover` de Telescope tome efecto). Front: `npm run build` +
restart de PM2.

### 🔴 Hallazgo nuevo — fuera de la auditoría original

`docker-compose.yml` (versionado en el repo) tiene las passwords de MySQL en claro
(`npm8956` / `npm8956_root`) y publica **MySQL en `0.0.0.0:3308`** y **phpMyAdmin en
`0.0.0.0:8080`**. Si el server de producción tiene esos puertos abiertos hacia internet,
la base es accesible con una password que está en el repositorio.

No se tocó (decisión del usuario: verificar y reportar). Verificado en la máquina de dev:
los binds son a `0.0.0.0` (confirmado con `ss -ltn`). **Falta verificar en el server de
producción** si el firewall los está tapando. Si no: atar a `127.0.0.1`, rotar las
credenciales y sacarlas del repo.

### Verificaciones corridas

- `phpunit`: 2/2 OK antes y después (baseline y final).
- `/login`: intentos 1-5 → 401, 6+ → 429. Otro email en paralelo → 401 (el keying por
  email+IP funciona, no bloquea a toda la oficina).
- CORS: preflight de `/partner/*` desde dominio externo → `Access-Control-Allow-Origin: *`;
  `/contact` y `/login` desde origen ajeno → sin allow-origin; desde blustudioinc.com y
  localhost:3000 → permitidos.
- Telescope: 44 rutas en local, 0 con `APP_ENV=production`. La app arranca en ambos.
- Front: build OK, las 11 páginas principales responden 200 con los 5 headers y sin
  `x-powered-by`. Screenshots de home y `/servicios/marketing` idénticas. El diff del
  front no toca ningún `.vue`, `.scss` ni `.css`.

Relacionado: [[blu-web-v1]] · [[arquitectura]] · [[stack]] · [[changelog]]
