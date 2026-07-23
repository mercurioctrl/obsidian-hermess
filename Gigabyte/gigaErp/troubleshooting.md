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

## 8. PhpSpreadsheet no instalado en el container

**Síntoma:** subir un `.xlsx` a cualquier importador (mercadería o catálogo) tira:
```
Class "PhpOffice\PhpSpreadsheet\IOFactory" not found
```

**Causa:** la imagen del backend es vieja. `maatwebsite/excel` (que trae PhpSpreadsheet) está en `composer.json` del host pero **nunca corrió `composer install`** en el container → `vendor/phpoffice` y `vendor/maatwebsite` no existen. Además no hay binario `composer` dentro del container.

**Fix de raíz:** reconstruir la imagen del backend (instala las deps del composer.json):
```bash
docker compose build backend && docker compose up -d backend
docker restart gigaerp-nginx
```

**Workaround vigente:** el importador de catálogo (`ImportacionCatalogoController`) parsea **CSV de forma nativa** (`fgetcsv`) y solo usa PhpSpreadsheet para xlsx → con CSV anda sin rebuild. El importador de mercadería (`ImportacionMercaderiaController`) sí depende de PhpSpreadsheet siempre.

## 9. `$request->validate()` descarta claves de un array anidado

**Síntoma:** se mapean varias columnas (`mapping.bu_code`, `mapping.ean`, ...) pero al backend solo llega la única que tiene regla explícita (`mapping.item_no`); el resto queda null.

**Causa:** `$request->validate(['mapping' => 'array', 'mapping.item_no' => 'required|integer'])` devuelve **solo las claves anidadas que tienen regla**. Las demás se descartan del set validado.

**Fix:** agregar un comodín que valide (y por ende devuelva) todas las claves:
```php
'mapping'         => 'required|array',
'mapping.item_no' => 'required|integer|min:0',
'mapping.*'       => 'nullable|integer|min:0',
```

## 10. Rebuild limpio del backend falla (composer create-project)

**Síntoma:** `docker compose build backend` (o `--no-cache`) revienta en la etapa `vendor`:
```
composer create-project laravel/laravel:^11.0 . --no-interaction --quiet
Your requirements could not be resolved to an installable set of packages.
```

**Causa:** el `backend/Dockerfile` **reconstruye Laravel desde cero** en cada build vía `composer create-project laravel/laravel:^11.0`. El skeleton `^11.0` fue evolucionando y sus dependencias ya no resuelven contra la imagen `composer:2` actual. No depende del código propio; es fragilidad del Dockerfile.

**Consecuencia:** no se puede regenerar la imagen del backend. Los cambios de backend se despliegan **en caliente**:
```bash
docker cp backend/app/... gigaerp-backend:/var/www/html/app/...
# (si hace falta un ini nuevo, escribirlo en /usr/local/etc/php/conf.d/ dentro del container)
docker restart gigaerp-backend    # el restart PRESERVA el writable layer; un recreate/compose up NO
docker exec gigaerp-backend php artisan config:cache   # o cae a sqlite (gotcha #2)
```
⚠️ Un `docker compose up --build` / `down && up` **descarta** los cambios cp'ados (vuelve a la imagen vieja).

**Fix de raíz (pendiente):** en el Dockerfile, pinear una versión exacta de `laravel/laravel` conocida-buena o agregar `--ignore-platform-reqs` al `create-project` (como ya se hace en el `composer require` de abajo). El feature de backup ([[changelog#2026-07-02 — Backup/restore completo en ZIP (datos + archivos)|backup ZIP]]) quedó desplegado en caliente por esto.

## 11. Flysystem S3 rompe copy/move por GetObjectAcl

**Síntoma:** con el disco S3 del módulo [[modulos/contenido|Contenido]], renombrar/mover una carpeta o archivo tira:
```
League\Flysystem\UnableToMoveFile: Unable to copy file ...
  → UnableToRetrieveMetadata: Unable to retrieve the visibility ...
  → S3Exception: Error executing "GetObjectAcl" ... AccessDenied (s3:GetObjectAcl)
```

**Causa:** al copiar, Flysystem intenta **preservar la visibilidad** del objeto origen y para eso llama a `GetObjectAcl`. Con una policy IAM least-privilege (sin permisos de ACL) devuelve 403, y `move` (que es copy+delete) revienta.

**Fix (aplicado):** decirle al disco que **no gestione ACLs por objeto** — correcto para bucket privado servido con URLs firmadas, y portable aunque el bucket tenga ACLs deshabilitadas (Object Ownership = bucket owner enforced). En `config/filesystems.php`, disco `contenido`:
```php
'visibility' => 'private',
'retain_visibility' => false,   // evita el GetObjectAcl en copy/move
```
NO agregar permisos de ACL a la policy — la solución es no depender de ellos.

## 12. Instalar una dependencia composer sin composer en el container

**Síntoma:** hace falta un paquete nuevo (ej. `league/flysystem-aws-s3-v3`) pero `docker exec ... composer` da `composer: not found` y el rebuild limpio está roto (gotcha #10).

**Fix (deploy en caliente):** bajar `composer.phar` dentro del container con el propio PHP y usarlo:
```bash
docker exec gigaerp-backend sh -c 'cd /var/www/html && \
  [ -f composer.phar ] || (php -r "copy(\"https://getcomposer.org/installer\",\"composer-setup.php\");" \
    && php composer-setup.php --quiet && rm -f composer-setup.php); \
  php composer.phar require league/flysystem-aws-s3-v3:^3.0 --no-interaction'
```
⚠️ Sobrevive a `docker restart` (writable layer) pero NO a un recreate/`compose up`. Para el fix de raíz, la dependencia ya se agregó al build del Dockerfile (`b832208`).

⚠️ **No** copiar el `composer.json` del container al repo (ni viceversa): el container es un skeleton `laravel/laravel` **divergido** del `composer.json` del repo (`gigabyte/gigaerp`). Editar la dependencia en el repo a mano; instalar en el container con `composer.phar require`.

## 13. Carácter no-ASCII en header HTTP se ve mal (Ã)

**Síntoma:** el header `X-Res` del thumbnail de [[modulos/contenido|Contenido]] traía la resolución como `2880×600`, pero en la UI se veía **`2880Ã600 px`**.

**Causa:** los **headers HTTP son ASCII/latin-1**. El `×` (U+00D7, multibyte UTF-8: `0xC3 0x97`) se transmite como esos bytes y el navegador (`fetch().headers.get`) los decodifica como latin-1 → `Ã` + un control char.

**Fix:** en el header usar solo **ASCII** (`2880x600`, con `x` letra) y formatear a `×` en el cliente al mostrar. Regla general: nunca meter caracteres no-ASCII en un header; usarlos solo en el body/HTML.

## 14. Editar un archivo bind-mounteado (un solo archivo) no se refleja en el container

**Síntoma:** se edita un archivo montado como bind mount de **un solo archivo** (ej. `./nginx/default.conf.template`) pero el container sigue viendo la versión vieja; `docker cp` para pisarlo falla con `device or resource busy`.

**Causa:** Docker bindea el **inode** del archivo host al crear el container. Los editores que guardan de forma atómica (escriben temp + rename) crean un **inode nuevo** → el mount sigue apuntando al viejo. Además no se puede `docker cp` sobre un path que es bind mount.

**Fix:**
- **Definitivo:** recrear el container (`docker compose up -d <svc>`) → re-bindea el inode actual. En prod esto alcanza (el deploy recrea).
- **En caliente (sin recrear):** copiar el archivo a un path NO montado del container y regenerar/usar desde ahí. Ej. nginx con template: `docker cp tpl gigaerp-nginx:/tmp/x && docker exec gigaerp-nginx sh -c 'envsubst "\${CONTENT_DOMAIN}" < /tmp/x > /etc/nginx/conf.d/default.conf' && nginx -s reload`.
- Alternativa: montar el **directorio** en vez del archivo (los cambios de archivos dentro sí se ven).

## 15. Modelo con enum casteado revienta si la columna tiene default en DB pero no en `$attributes`

**Síntoma:** crear un registro sin pasar un campo que tiene default en la DB (ej. `Tarea` sin `estado`) guarda bien la fila, pero el objeto devuelto rompe en el Resource con `Attempt to read property "value" on null` (`$this->estado->value`).

**Causa:** el default vive en la migración (DB), no en el modelo. Eloquent no lee el default de la DB al construir el objeto en memoria, así que el atributo queda `null`; el cast a enum sobre `null` no falla al hidratar, pero acceder a `->value` sí.

**Fix:** espejar los defaults de la DB en `protected $attributes` del modelo.

```php
protected $attributes = [
    'estado'    => 'POR_HACER',
    'prioridad' => 'MEDIA',
];
```

Introducido en `4af7a34` (módulo [[modulos/contenido|Contenido]], commit que además tocó tareas).


## Ver también

- [[arquitectura]] — patrones de controllers/rutas/resources
- [[modulos/contenido]] — disco S3, URLs firmadas, deploy en caliente (gotchas 10-14)
- [[modulos/invoice-preview]] — donde aparece la trampa html2canvas/SVG
- [[modulos/productos]] — importador de catálogo (gotchas 8 y 9)
- [[changelog]] — cuando se identificó cada uno

