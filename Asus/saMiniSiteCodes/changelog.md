# Changelog

## 2026-04-15

- feat: Agregado toggle `PROMO_CLOSED` en env var para cerrar el formulario de solicitudes
  - `index.php` muestra panel "Promoción finalizada" cuando `PROMO_CLOSED=true`
  - `api/claim.php` retorna 403 si la promo está cerrada
  - Tabs de Instrucciones y Soporte siguen funcionando

## 2026-04-04

- feat: Sistema de tickets de soporte con video obligatorio
  - Endpoint `api/ticket.php` — upload de video (MP4/WebM/MOV, máx 55MB)
  - Admin `admin/tickets.php` — lista, filtros, cerrar/reabrir, ver video
  - Emails: notificación a soporte + confirmación al usuario
- feat: Navegación por tabs (Solicitud, Instrucciones, Soporte)
- feat: Página de instrucciones de canje en Steam con capturas

## 2026-03-17

- feat: Comprobante de compra obligatorio (upload de factura JPG/PNG/WEBP/PDF)
- feat: Scripts de backup y restore (`backup.sh`, `restore.sh`)

## 2026-03-11

- fix: `clean.sh` — uso correcto de docker-compose y flag -e para SQL
- feat: `clean.sh` — reset de claims, codes y uploads con confirmación por password
- fix: Texto de email — mención de plataforma STEAM
- fix: Reducción de padding vertical en header
- fix: Forzar template ROG — eliminar `rog-template` de localStorage
- feat: Cache-busting con `filemtime` en CSS y JS
- feat: File upload de comprobante, logos ROG, sistema dual-template/theme, mejoras admin

## 2026-03-10

- fix: Login — eliminado ícono biohazard y estilos obsoletos
- feat: Commit inicial — mini site de canje de códigos ASUS Team

## Ver también

- [[Asus/saMiniSiteCodes/saMiniSiteCodes|saMiniSiteCodes]]
- [[Asus/saMiniSiteCodes/arquitectura|Arquitectura]]