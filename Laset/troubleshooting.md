# Troubleshooting

Ver también: [[Laset]] · [[operaciones]] · [[arquitectura]]
Versión completa en el repo: `/var/www/laset/docs/troubleshooting.md`.

## Back
- **500 `Adaptive Server is unavailable (172.31.10.208)`** → DB del backup es de otra red (VPC AWS),
  sin ruta. Usar `db-nb-massql-dev.blu.net.ar,4444` (user `cmercurio`) en los `.env`.
- **500 Laravel `valid cache path` / `vendor/autoload.php not found`** → falta `vendor/` y/o `storage/`
  (ambos gitignoreados). Ver [[operaciones]].
- **composer: "affected by security advisories"** → `--no-security-blocking`.
- **composer: `ext-gd`/`ext-zip` (cobros)** → `--ignore-platform-reqs`.
- **`Unable to read environment file`** → `.env` en 600, `chmod 644`.
- **`all predefined address pools have been fully subnetted`** → usar `laset-net` compartida; no red por app; no `prune`.
- **`container name already in use` / puerto ocupado** → falta sufijo `-laset` / puerto 81xx-39xx.
- **`docker compose up --build` falla en `pecl install sqlsrv`** → no buildear; usar imagen `*-laset` (`image:`).

## Dominio único / SSO

### Entrar a una app desloguea de TODAS
Ese back valida el permiso leyéndolo del **payload del token**, pero el token lo emitió otra app y
cada back mete su propia forma de usuario. Falta el campo → 401 → `auth-next` borra el token
compartido → se cae la sesión de todo el ERP.
**Fix:** el middleware relee el usuario de la base por `UserId` (`getByToken()` / `getById()`).

### La app se ve bien pero no responde a nada / vuelve al login sola
Los assets dan 404 y la app **no hidrata** (el SSR igual pinta el HTML, por eso "parece" andar).
Causa: `build.publicPath` absoluto. Nuxt 2 le prepende `router.base` → monta en
`/pedidos/pedidos/_nuxt/`. **Fix:** `publicPath: '_nuxt/'`.

### 401 `Signature verification failed` entre backs
Ese back firma con otra clave. Todos usan `md5(JWT_SIGNATURE_KEY)` HS256. Comparar sin exponer el
secreto: `grep -hE '^JWT_SIGNATURE_KEY=' <back>/app/.env | cut -d= -f2- | md5sum | cut -c1-8`.

### ms-metadata rechaza los tokens de los backs PHP
PyJWT exige el parámetro `audience` cuando el token trae claim `aud`, y los PHP ponen ahí un sha1
de IP+User-Agent+hostname. **Fix:** `jwt.decode(..., options={"verify_aud": False})`.

### El navegador bloquea las llamadas a un back Phinx (CORS), pero `curl` anda
`Cors.php` está, pero los warnings de PHP 8 se imprimen **antes** de los headers y PHP ya no puede
enviarlos. **Fix:** `display_errors` apagado en `public/index.php` (escape `DEBUG_OUTPUT=1`).
Se nota porque la respuesta sale como `text/html` con los warnings delante del JSON.

### 500 `could not be opened in append mode: chmod()`
El dir `logs/` del back es del usuario del host y Apache corre como `www-data`.
**Fix:** `chgrp -R 33 <back>/app/logs && chmod -R g+w` (+ `g+s`).

### 500 `SSL Provider: certificate verify failed: self-signed certificate`
El contenedor trae **ODBC Driver 18**, que cifra y valida el certificado; el del SQL Server es
autofirmado. (Expedición trae el 17 y por eso no falla.)
**Fix:** `Encrypt = 1; TrustServerCertificate = 1;` en el DSN.

## Front
- **`npm install` falla en `canvas`/node-pre-gyp** (comprobante-pdf) → `--ignore-scripts`.
- **build falla `ERR_OSSL_EVP_UNSUPPORTED`** → `NODE_OPTIONS=--openssl-legacy-provider`.
- **`pm2 start: Script not found nuxt.js`** → install no dejó `nuxt`, reinstalar con `--ignore-scripts`.
- **`ERESOLVE`** → `--legacy-peer-deps`.
- **Host sin RAM al levantar fronts** → bajar `instances` a `2` (no `'max'`).
