# Stack e Infraestructura

## Stack tecnologico

| Capa | Tecnologia | Version |
|------|-----------|---------|
| Frontend | Nuxt 3 + Vue 3 + Tailwind CSS + Pinia | Node 20 |
| Backend | Laravel | 11 |
| Lenguaje backend | PHP | 8.3 |
| [[Base de Datos]] | MySQL | 8 |
| Cache / Queue | Redis | 7 |
| Auth | Laravel Sanctum (Bearer token) | - |
| PDF (presupuestos) | Spatie Browsershot + Chromium headless (Node 20 + Puppeteer en el container) | Browsershot ^4.2 / Chromium 147 |
| PDF (activaciones) | TCPDF + FPDI sobre membretada | - |
| IA | DeepSeek API (deepseek-chat) | - |
| Mail | SMTP (symfony/mailer via Laravel) | - |
| Proxy | Nginx | alpine |
| Containerizacion | Docker Compose | - |

## Docker - Servicios y puertos

| Contenedor | Imagen | Puerto interno | Puerto externo | Notas |
|-----------|--------|----------------|----------------|-------|
| minisaas-db | mysql:8 | 3306 | ${DB_PORT:-3307} | Healthcheck 20 reintentos |
| minisaas-redis | redis:7-alpine | 6379 | - (interno) | Cache y sesiones |
| minisaas-backend | Dockerfile custom | 9000 (FPM) | - (interno) | Laravel 11 |
| minisaas-frontend | Dockerfile custom | 3000 | - (interno) | Nuxt 3 SSR |
| minisaas-nginx | nginx:alpine | 80 | ${APP_PORT:-8823} | Reverse proxy |

**Regla de puertos:** Solo Nginx expone puerto al host. El resto son internos. No agregar `ports:` a otros servicios. Ver [[Errores Comunes#Agregar ports a servicios que no son Nginx]].

## Nginx - Ruteo

```
/api/*     -> backend:8000 (Laravel)
/sanctum/* -> backend:8000
/storage/* -> backend:8000
/*         -> frontend:3000 (Nuxt SSR)
```

## Comandos de deploy

```bash
cd mini-saas

# Levantar
docker compose up -d --build    # con rebuild
docker compose up -d            # sin rebuild

# Detener
docker compose down

# Logs
docker compose logs -f backend
docker compose logs -f frontend

# BACKEND - deploy de cambios PHP sin rebuild (rapido)
docker cp backend/app/Http/Controllers/MiController.php minisaas-backend:/var/www/html/app/Http/Controllers/
docker cp backend/app/Models/MiModelo.php minisaas-backend:/var/www/html/app/Models/
docker cp backend/routes/api.php minisaas-backend:/var/www/html/routes/
docker exec minisaas-backend php artisan optimize:clear

# BACKEND - migraciones nuevas
docker cp backend/database/migrations/XXXX_nueva.php minisaas-backend:/var/www/html/database/migrations/
docker exec minisaas-backend php artisan migrate --force

# FRONTEND - siempre requiere rebuild de imagen
docker compose build --no-cache frontend
docker compose up -d frontend
```

Ver [[Errores Comunes#Rebuild de frontend con cache vieja]] para por que se necesita `--no-cache`.

## Variables de entorno (.env)

```
APP_PORT=8823
DB_PORT=3307
DB_NAME=mini_saas
DB_USER=saas_user
DB_PASSWORD=...
DB_ROOT_PASSWORD=...
SANCTUM_STATEFUL_DOMAINS=localhost
CACHE_STORE=redis
SESSION_DRIVER=redis
NUXT_PUBLIC_API_BASE=http://localhost:8823/api
DEEPSEEK_API_KEY=sk-...

# Mail SMTP (pagos)
MAIL_MAILER=smtp
MAIL_HOST=box.lio.red
MAIL_PORT=465
MAIL_USERNAME=payments@blustudioinc.com
MAIL_PASSWORD=
MAIL_ENCRYPTION=ssl
MAIL_FROM_ADDRESS=payments@blustudioinc.com
MAIL_FROM_NAME="BluStudio Payments"
MAIL_PAYMENTS_BCC=payments@blustudioinc.com
```

> `DEEPSEEK_API_KEY` y `MAIL_PASSWORD` deben estar en el `.env` del container backend. Ver [[Errores Comunes#env no lee variables de entorno del container en PHP-FPM]]. `MAIL_PASSWORD` queda vacía en el repo — cada entorno la completa a mano.

## Volumenes Docker

- `mysql_data` - persistencia de la base de datos
- `redis_data` - persistencia de cache
- `pdf_storage` - PDFs generados en `backend/storage/app/pdfs`
- `uploads_storage` - archivos subidos en `backend/storage/app/public`

## Plantilla PDF membretada

La hoja membretada de Blu (`membretadaBlu.pdf`) se usa como fondo para los PDFs de activaciones. Se almacena en `backend/storage/app/templates/membretada.pdf`.

## Browsershot - renderizado de PDFs de presupuesto

Los PDFs de presupuesto se generan con **Spatie Browsershot + Chromium headless**, no con DomPDF. El motivo es que el botón "PDF" del frontend abre `/preview` como HTML (render del navegador) y se esperaba que el PDF adjuntado al email fuera idéntico. DomPDF no soporta flex, no tiene webfonts y caía a Times serif — el output divergía visiblemente del preview. La solución fue unificar ambos caminos bajo Chrome headless.

### Entry point único

`app/Services/PdfService.php` → `renderPresupuestoPdf(Presupuesto $p): string` devuelve los bytes del PDF. Lo usan:

- `PresupuestoController::pdf()` → endpoint `GET /api/presupuestos/{id}/pdf` (download)
- `PresupuestoInvoiceMail::attachments()` → adjunto del email

Ambos renderizan el **mismo blade**: `resources/views/pdf/presupuesto-preview.blade.php` (el mismo que sirve `/preview` como HTML). No usar `pdf/presupuesto.blade.php` — quedó como legacy de la era DomPDF.

### Configuración de Browsershot

```php
Browsershot::html($html)
    ->setChromePath('/usr/bin/chromium')   // chromium del sistema (no el de puppeteer)
    ->noSandbox()                          // obligatorio si el container corre como root
    ->format('A4')
    ->margins(0, 0, 0, 0)
    ->showBackground()
    ->waitUntilNetworkIdle()
    ->pdf();
```

### Dependencias del container backend (Dockerfile)

- **Chromium:** paquete `chromium` de Debian Trixie + libs compartidas: `libnss3 libatk-bridge2.0-0 libgtk-3-0 libasound2 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libpangocairo-1.0-0 libpango-1.0-0 libcairo2 libxshmfence1`
- **Fuentes:** `fonts-liberation fonts-dejavu-core fonts-noto-color-emoji`
- **Node 20:** instalado desde `deb.nodesource.com/setup_20.x`
- **Puppeteer global:** `npm install -g puppeteer` con env vars para que NO baje su propio Chromium:
  - `PUPPETEER_SKIP_DOWNLOAD=true`
  - `PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true`
  - `PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium`

Rebuild pesado: ~300MB extras en la imagen, varios minutos de build. Corre headless sin GUI en servers Linux sin modificaciones.

### Advisories de Composer (Browsershot PKSA)

`spatie/browsershot ^4.2` tiene 6 advisories activos (`PKSA-j9hz-k29x-6s58`, `PKSA-kq82-8x3t-s3fs`, `PKSA-8m7x-943y-brpz`, `PKSA-318x-z311-x7rh`, `PKSA-y3ty-b1bg-gxtm`, `PKSA-5jt2-w99c-cs4s`) que bloquean el install en Composer 2.8+. La mitigación es no exponer los métodos vulnerables a input de usuario (acá Browsershot solo recibe HTML generado server-side — no hay user input). Workaround en `composer.json`:

```json
"config": {
    "audit": {
        "abandoned": "ignore",
        "ignore": ["PKSA-j9hz-k29x-6s58", "PKSA-kq82-8x3t-s3fs", "PKSA-8m7x-943y-brpz", "PKSA-318x-z311-x7rh", "PKSA-y3ty-b1bg-gxtm", "PKSA-5jt2-w99c-cs4s"]
    }
}
```

Y el Dockerfile corre `composer update --no-dev --optimize-autoloader --no-scripts --no-audit`. Ver [[Errores Comunes#Browsershot bloqueado por security advisories PKSA]].

### Verificación en runtime

```bash
docker exec minisaas-backend chromium --version    # Chromium 147.x...
docker exec minisaas-backend node --version        # v20.x
docker exec minisaas-backend ls /usr/lib/node_modules/puppeteer  # existe
```

Si el PDF falla al generarse, chequear primero estos tres puntos.

## Mail SMTP

El proyecto envía mails transaccionales vía SMTP de BluStudio. Por ahora solo invoices de presupuestos (`POST /api/presupuestos/{id}/enviar-invoice`), con BCC automático a `payments@blustudioinc.com`.

### Configuración

| Opción | Valor |
|--------|-------|
| Host | `box.lio.red` |
| Puerto SMTP | `465` |
| Encriptación | SSL/TLS |
| Username / From | `payments@blustudioinc.com` |
| BCC automático | `payments@blustudioinc.com` (via `MAIL_PAYMENTS_BCC`) |
| Puerto IMAP | 993 SSL (no usado por la app — solo referencia) |

### `config/mail.php` creado a mano

Laravel 11 en este repo **no trae** `config/mail.php` en el skeleton (solo `app`, `auth`, `cache`, `cors`, `database`, `sanctum`, `services`, `session`). Hubo que crearlo — sin ese archivo el Mail facade no funciona aunque estén las env vars, porque Laravel solo lee los `.php` que existen en `config/`. Ver [[Errores Comunes#Laravel 11 sin config mail php por default]].

### Patrón de Mailable con PDF adjunto

`app/Mail/PresupuestoInvoiceMail.php` es la referencia canónica: delega la generación del PDF al `PdfService` (Browsershot + Chromium) para no duplicar lógica.

```php
public function attachments(): array
{
    $pdf = app(PdfService::class)->renderPresupuestoPdf($this->presupuesto);

    return [
        Attachment::fromData(fn () => $pdf, "invoice-{$this->presupuesto->numero}.pdf")
            ->withMime('application/pdf'),
    ];
}
```

- **PDF in-memory:** `renderPresupuestoPdf()` devuelve el binario como string, no toca filesystem ni volumen Docker
- **BCC en el `Envelope()`:** Leído de `config('mail.payments_bcc')` con fallback a env. El controller no necesita conocer el BCC
- **Un único entry point:** Tanto `GET /api/presupuestos/{id}/pdf` (download) como el adjunto del email pasan por `PdfService::renderPresupuestoPdf()`. Así el output es el mismo en los dos caminos. Ver [[#Browsershot - renderizado de PDFs de presupuesto]]

### Futuro: múltiples transportes

Cuando aparezcan credenciales de otras cuentas (no-pagos), agregar un nuevo mailer en `config/mail.php` (`mailers.notifications`, etc.) en lugar de pisar el SMTP de pagos. Cada Mailable puede elegir transporte con `->mailer('notifications')`.

Ver [[Backend - API#Presupuestos]] para el endpoint `enviar-invoice` y [[memoria#Mail SMTP y envío de invoices]] para el contexto de la decisión.

## Entrypoint del backend

El backend usa `docker-entrypoint.sh` como ENTRYPOINT. Garantiza:
1. Crear directorios de storage necesarios
2. Asignar permisos 775
3. Limpiar cache de Laravel

Ver [[Errores Comunes#Please provide a valid cache path tras rebuild del backend]].

## Acceso por defecto

- URL: `http://localhost:8823`
- Admin: `admin@empresa.com` / `admin123`

---

## Ver tambien

- [[Base de Datos]] - Esquema completo de la DB
- [[Backend - API]] - Rutas y controllers
- [[Frontend]] - Estructura del frontend
- [[Errores Comunes]] - Problemas frecuentes con Docker y deploy
