# Arquitectura

## Servicios Docker

3 contenedores orquestados con Docker Compose:

| Servicio | Imagen | Rol |
|----------|--------|-----|
| `php` | PHP 8.2-fpm-alpine | App server, monta todo `./src` → `/var/www` |
| `nginx` | nginx:alpine | Web server, solo monta `./src/public` y `./src/uploads` |
| `db` | mysql:8.0 | Base de datos, volumen persistente `db_data` |

**Gotcha importante:** Nginx NO monta todo `./src` — solo `public/` y `uploads/`. Cualquier ruta nueva necesita volumen explícito en `docker-compose.yml` + location en `default.conf`.

## Request flow

- `GET /` → `index.php` — Página pública con 3 tabs (Solicitud, Instrucciones, Soporte)
- `POST /api/claim.php` → Valida datos + inserta en `claims` (status=pending). Rechaza con 403 si `PROMO_CLOSED=true`.
- `POST /api/ticket.php` → Ticket de soporte con video obligatorio → tabla `tickets` + emails
- `GET /admin/` → Login → Dashboard, Claims, Codes, Tickets
- Admin "Enviar Código" → `send_code.php` → transacción con `SELECT FOR UPDATE` (race-condition safe) → marca code used + claim delivered → envía email

## Estructura de archivos clave

```
src/
├── includes/
│   ├── db.php          # PDO singleton
│   ├── auth.php        # Sesión + ensureAdminExists()
│   └── mailer.php      # PHPMailer wrapper (SMTP 465, timeout 15s)
├── public/
│   ├── index.php       # Página pública (3 tabs)
│   ├── api/
│   │   ├── claim.php   # Endpoint solicitudes
│   │   └── ticket.php  # Endpoint tickets soporte
│   ├── admin/
│   │   ├── index.php       # Login
│   │   ├── dashboard.php   # Panel principal
│   │   ├── claims.php      # Gestión de solicitudes
│   │   ├── codes.php       # Gestión de códigos
│   │   ├── tickets.php     # Gestión de tickets
│   │   └── send_code.php   # Envío de código por email
│   └── assets/
│       ├── css/style.css   # Todo el CSS (variables, templates, temas)
│       └── js/main.js      # JS unificado
└── uploads/                # Archivos subidos (facturas + videos)
```

## Base de datos

4 tablas en MySQL 8 (`re_requiem`):

- **claims** — Solicitudes de canje (serial, fecha compra, factura, tienda, nombre, email, status pending/delivered, invoice_file)
- **codes** — Códigos de activación (code_value, is_used, claim_id)
- **admins** — Credenciales admin (sincronizadas desde env vars en cada request)
- **tickets** — Tickets de soporte (name, code, email, comment, video_file, status open/closed)

Migraciones en caliente: `claim.php` y `ticket.php` hacen `ALTER TABLE` / `CREATE TABLE IF NOT EXISTS` al inicio.

## Decisiones de diseño

- **No framework:** PHP puro con PDO. Proyecto simple, no justifica Laravel/Symfony.
- **Dual template/theme:** ROG (dark, default) + ASUS Corporate (light). Controlado por `data-template` y `data-theme` en `<html>`.
- **PROMO_CLOSED env var:** Toggle para cerrar el formulario sin tocar código. Solo cambia la env var y se recrea el container PHP.
- **ensureAdminExists():** Credenciales admin siempre sincronizadas desde `.env` — no requiere migración para cambiar password.

## Ver también

- [[Asus/saMiniSiteCodes/saMiniSiteCodes|saMiniSiteCodes]]
- [[Asus/saMiniSiteCodes/stack|Stack]]
- [[Asus/saMiniSiteCodes/contexto|Contexto]]