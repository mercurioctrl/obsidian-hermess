# Troubleshooting — gigaErp

Catálogo de trampas recurrentes con causa y fix. Mirar acá ANTES de improvisar.

## 1. `migrate` falla con "Table personal_access_tokens already exists"

**Síntoma:**
```
SQLSTATE[42S01]: Base table or view already exists: 1050 Table 'personal_access_tokens' already exists
```

**Causa:** el `docker-entrypoint.sh` del backend corre `php artisan vendor:publish` para Sanctum **en cada arranque**, generando un archivo nuevo `database/migrations/{timestamp}_create_personal_access_tokens_table.php`. Como la tabla ya existe (volumen persistido), `migrate` revienta.

**Fix temporal:** borrar la migración duplicada antes de migrar.
```bash
docker exec gigaerp-backend sh -c 'rm -f database/migrations/*_create_personal_access_tokens_table.php'
docker exec gigaerp-backend php artisan migrate --force
```

**Fix de raíz (pendiente):** el entrypoint debería chequear si la tabla ya existe antes de republicar (o usar `vendor:publish --force=false`).

## 2. Backend devuelve 500 con `Connection: sqlite`

**Síntoma:** después de `php artisan optimize:clear`, cualquier request al backend tira:
```
SQLSTATE[HY000]: General error: 1 no such table: ... (Connection: sqlite, SQL: ...)
```

**Causa:** Laravel 11 + PHP-FPM **no lee `getenv()` por defecto**. El `env('DB_CONNECTION')` solo funciona vía config cache (que fue limpiado). Sin cache, el default cae a sqlite.

**Fix:** re-cachear config inmediatamente después de cualquier `optimize:clear`.
```bash
docker exec gigaerp-backend php artisan config:cache
```

## 3. Nginx 502 después de rebuild

**Síntoma:** `/api/*` devuelve `502 Bad Gateway` después de `docker compose up --build` o restart del backend/frontend.

**Causa:** nginx resuelve la IP del upstream `backend:9000` o `frontend:3000` **al iniciar** y la cachea. Si recreás el container, la IP cambia pero nginx sigue apuntando a la vieja.

**Fix:**
```bash
docker restart gigaerp-nginx
```

Hacelo SIEMPRE después de rebuild de cualquier container app.

## 4. Logo recortado en el PDF de invoice

**Síntoma:** en la preview HTML el logo AORUS se ve perfecto, pero al "Descargar PDF" el logo aparece recortado / con solo el ala / vacío.

**Causa:** `frontend/public/logos/aorus_logo_black.svg` tiene `viewBox="519 657 1819 455"` (no empieza en 0,0). **html2canvas** (que usa html2pdf.js) **no respeta el offset del viewBox**, captura la región (0,0)→(1819,455) donde no hay nada.

**Fix aplicado (commit `001f8c8`):**
1. Generar PNG del logo con playwright/chromium (script en `/tmp/svg2png.mjs`).
2. Embeber el PNG como **data URI base64** en el blade:
```php
$logoData = 'data:image/png;base64,' . base64_encode(file_get_contents(public_path('logos/aorus_logo_black.png')));
```
3. `<img src="{{ $logoData }}">` en header y footer.

PNG vive en `backend/public/logos/aorus_logo_black.png` (commiteado).

## 5. Asset nuevo en `frontend/public/` no se sirve

**Síntoma:** archivos copiados a `frontend/public/` o vía `docker cp` a `.output/public/` retornan HTML del SPA, no el asset.

**Causa:** Nitro (runtime de Nuxt 3) tiene un **manifest de assets generado en build time**. Archivos agregados después no están en el manifest → catch-all del SPA los intercepta.

**Fix:** rebuild del frontend (`docker compose build --no-cache frontend`). Alternativa rápida: embeber el asset en el backend (data URI o servirlo por una ruta `/api/...`).

## 6. Puerto 3308 ocupado al levantar la DB

**Síntoma:**
```
Error response from daemon: failed to set up container networking: ...
Bind for 0.0.0.0:3308 failed: port is already allocated
```

**Causa:** hay otro container `mysql` corriendo en la máquina ocupando 3308.

**Fix:** cambiar `DB_PORT` en `.env` a `3310` (o cualquier libre). Solo afecta acceso externo — el backend conecta interno por `db:3306`.

## 7. ValidationException devuelve 500 (no 422)

**Síntoma:** validaciones de form fallan con HTTP 500 en lugar de 422. El body sí incluye el `message` correcto.

**Causa:** el exception handler global de la app (pre-existente, no de mi código) renderiza `ValidationException` sin setear el status code, defaultea a 500.

**Workaround:** la UX no se rompe porque el frontend lee `e.message` (que sí está). Si querés arreglar de raíz, mirar el handler en `bootstrap/app.php`.

## Ver también

- [[arquitectura]] — patrones de controllers/rutas/resources
- [[modulos/invoice-preview]] — donde aparece la trampa html2canvas/SVG
- [[changelog]] — cuando se identificó cada uno
