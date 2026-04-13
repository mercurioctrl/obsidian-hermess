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
| PDF (presupuestos) | barryvdh/laravel-dompdf | - |
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

`app/Mail/PresupuestoInvoiceMail.php` es la referencia canónica para cualquier futuro Mailable que adjunte PDFs generados con DomPDF:

```php
public function attachments(): array
{
    $pdf = Pdf::loadView('pdf.presupuesto', [...])->setPaper('a4');

    return [
        Attachment::fromData(fn () => $pdf->output(), "invoice-{$numero}.pdf")
            ->withMime('application/pdf'),
    ];
}
```

- **PDF in-memory:** `$pdf->output()` devuelve el binario como string, no toca filesystem ni volumen Docker
- **BCC en el `Envelope()`:** Leído de `config('mail.payments_bcc')` con fallback a env. El controller no necesita conocer el BCC
- **No reutilizar `PdfService`:** `PdfService->generarPresupuesto()` devuelve un `Response` (download), no un string, así que el Mailable duplica la carga de la view con `Pdf::loadView(...)`

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
