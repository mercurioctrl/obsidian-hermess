# Stack

## Backend

| Tecnología | Versión | Uso |
|------------|---------|-----|
| PHP | 8.2 (fpm-alpine) | App server |
| PHPMailer | ^6.9 | Envío de emails (SMTP 465 SSL/TLS) |
| PDO | (built-in) | Acceso a base de datos |

## Base de datos

| Tecnología | Versión | Uso |
|------------|---------|-----|
| MySQL | 8.0 | Base de datos principal |

## Infraestructura

| Tecnología | Versión | Uso |
|------------|---------|-----|
| Nginx | alpine | Web server / reverse proxy |
| Docker Compose | 3.8 | Orquestación de servicios |

## Frontend

| Tecnología | Uso |
|------------|-----|
| CSS custom properties | Temas dark/light + templates ROG/ASUS |
| Flatpickr (CDN) | Date picker en formulario |
| Vanilla JS | Form submit, tabs, theme toggle |
| Google Fonts | Orbitron, Rajdhani, Inter, Roboto Condensed |

## SMTP

- Host: `box.asus-sa.com`
- Puerto: 465 (SSL/TLS implícito → `ENCRYPTION_SMTPS`)
- Timeout: 15s obligatorio para evitar workers colgados
- No confundir con puerto 587 (que usa `ENCRYPTION_STARTTLS`)

## Scripts de operación

| Script | Uso |
|--------|-----|
| `start.sh` | Build + up (instala Composer en primer run) |
| `stop.sh` | Down (datos persisten en volumen) |
| `clean.sh` | Reset claims, codes y uploads con password |
| `backup.sh` | Backup de DB + uploads |
| `restore.sh` | Restore desde backup |

## Ver también

- [[Asus/saMiniSiteCodes/saMiniSiteCodes|saMiniSiteCodes]]
- [[Asus/saMiniSiteCodes/arquitectura|Arquitectura]]